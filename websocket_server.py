import grpc
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict
from protos import chat_pb2, chat_pb2_grpc

app = FastAPI()
grpc_channel = grpc.insecure_channel("localhost:50051")
grpc_stub = chat_pb2_grpc.ChatServiceStub(grpc_channel)

active_connections: Dict[str, WebSocket] = {}

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await websocket.accept()
    active_connections[username] = websocket
    print(f"{username} connected via WebSocket")

    #Start a background task for gRPC message streaming
   # asyncio.create_task(stream_messages_to_websocket(username, websocket))
    
    try:
        while True:
            data = await websocket.receive_json()
            action = data.get("action")

            if action == "login":
                password = data.get("password")
                response = grpc_stub.Login(chat_pb2.LoginRequest(username=username, password=password))
                if response.success:
                    await websocket.send_json({"type": "login_success", "message": "Login successful"})
                else: 
                    await websocket.send_json({"type": "error", "message": "Invalid credentials"})
            elif action == "send_message":
                receiver = data["receiver"]
                content = data["content"]
                grpc_stub.SendPrivateMessage(chat_pb2.PrivateMessageRequest(sender=username, receiver=receiver, content=content))

                # If the receiver is connected, send the message immediately
                if receiver in active_connections:
                    await active_connections[receiver].send_json({"type": "new_message", "sender": username, "content": content})
    except WebSocketDisconnect:
        print(f"{username} disconnected")
        del active_connections[username]

# async def stream_messages_to_websocket(username:str, websocket: WebSocket):
#     """Continuously listen for messages from gRPC and forward to the WebSocket client."""
#     request = chat_pb2.StreamRequest(username=username)

#     def grpc_stream():
#         """Blocking gRPC streaming function that listens for messages."""
#         try:
#             for message in grpc_stub.StreamMessages(request):
#                 if username in active_connections:
#                     asyncio.run(send_message_to_websocket(username, message))
#         except grpc.RpcError as e:
#             print(f"gRPC Streaming Error for {username}: {e}")

#     #Run the blocking gRPC call in a separate thread
#     asyncio.create_task(asyncio.to_thread(grpc_stream))

# async def send_message_to_websocket(username: str, message):
#     """Helper function to send messages to WebSocket clients."""
#     if username in active_connections:
#         websocket = active_connections[username]
#         await websocket.send_json({"type": "new_message", "sender": message.sender, "content": message.content})

if __name__ == "__main__":
    import uvicorn
    print(f"Websocket Server running on port 8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)