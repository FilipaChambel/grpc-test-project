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

                if receiver in active_connections:
                    await active_connections[receiver].send_json({"type": "new_message", "sender": username, "content": content})
    except WebSocketDisconnect:
        print(f"{username} disconnected")
        del active_connections[username]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)