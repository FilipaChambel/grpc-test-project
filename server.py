import grpc
from protos import chat_pb2, chat_pb2_grpc 
from concurrent import futures
import threading
import time

# In-memory storage
users = {"alice": "password123", "bob": "password456"} # username -> password
active_users = {} #username -> (token, stream)
message_queues = {} # List of chat messages

class ChatService(chat_pb2_grpc.ChatServiceServicer):
    def Login(self, request, context):
        username = request.username
        password = request.password

        if username in users and users[username] == password:
            token = f"token_{username}"
            active_users[username] = token
            if username not in message_queues:
                message_queues[username] = []
            return chat_pb2.LoginResponse(token=token, success=True, message="Login successful")
        else:
            return chat_pb2.LoginResponse(token="", success=False, message="Invalid credentails")
        
    def Logout(self, request, context):
        token = request.token
        user = self.get_user_from_token(token)
        if user:
            del active_users[user]
            return chat_pb2.LogoutResponse(success=True)
        return chat_pb2.LogoutResponse(success=False)
    
    def SendPrivateMessage(self, request, context):
        sender = request.sender
        receiver = request.receiver
        content = request.content

        if receiver not in active_users:
            return chat_pb2.MessageResponse(success=False, message="User not online")
        
        message_queues[receiver].append(chat_pb2.ChatMessage(sender=sender, content=content, timestamp=str(time.time())))

        return chat_pb2.MessageResponse(success=True, message="Message sent")
    
    def SendGroupMessage(self, request, context):
        sender = request.sender
        group_id = request.group_id
        content = request.content

        for user in active_users:
            if user != sender:
                if active_users[user][1]:
                    active_users[user][1].write(chat_pb2.ChatMessage(sender=sender, content=content, timestamp=str(time.time())))
        
        return chat_pb2.MessageResponse(success=True, message="Group message sent")
    
    def StreamMessages(self, request, context):
        username = request.username
        if username not in active_users:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "User not logged in")
        
        def message_stream():
            while True:
                time.sleep(1)
                if username in message_queues and message_queues[username]:
                        # Yield all queued messages
                        while message_queues[username]:
                            yield message_queues[username].pop(0)
    
    def GetOnlineUsers(self, request, context):
        return chat_pb2.OnlineUsersResponse(users=list(active_users.keys()))
    
    def UpdatePresence(self, request, context):
        username = request.username
        is_online = request.is_online

        if is_online:
            active_users[username] = (f"token_{username}", None)
        else:
            active_users.pop(username, None)
        
        return chat_pb2.PresenceResponse(success=True)
    
    def get_user_from_token(self, token):
        for user, (stored_token, _) in active_users.items():
            if stored_token == token:
                return user
        return None
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Chat server started on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    #Add test users
    users["alice"] = "password123"
    users["bob"] = "password456"

    serve()