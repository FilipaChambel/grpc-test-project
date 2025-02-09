import grpc
from protos import chat_pb2, chat_pb2_grpc
import threading

SERVER_ADDRESS = "localhost:50051"

class ChatClient:
    def __init__(self, username, password):
        self.username = username
        self.token = None
        self.channel = grpc.insecure_channel(SERVER_ADDRESS)
        self.stub = chat_pb2_grpc.ChatServiceStub(self.channel)

        #Login user
        self.login(password)

    def login(self, password):
        request = chat_pb2.LoginRequest(username=self.username, password=password)
        response = self.stub.Login(request)
        if response.success:
            self.token = response.token
            print(f"Logged in as {self.username}")
            self.update_presence(True)
        else:
            print(f"Login failed:", response.message)
            exit(1)

    def logout(self):
        if self.token:
            request = chat_pb2.LogoutRequest(token=self.token)
            response = self.stub.Logout(request)
            if response.success:
                print("Logged out successfully.")
            else:
                print("Logout failed.")
        
    def send_private_message(self, receiver, message):
        request = chat_pb2.PrivateMessageRequest(sender=self.username, receiver=receiver, content=message)
        response = self.stub.SendPrivateMessage(request)
        print(f"{response.message}")
    
    def send_group_message(self, group_id, message):
        request = chat_pb2.GroupMessageRequest(sender=self.username, group_id=group_id, content=message)
        response = self.stub.SendGroupMessage(request)
        print(f"{response.message}")

    def stream_messages(self):
        request = chat_pb2.StreamRequest(username=self.username)
        try:
            for message in self.stub.StreamMessages(request):
                print(f"\n {message.sender}: {message.content} (Timestamp: {message.timestamp})\n", end="")
        except grpc.RpcError as e:
            print("Error in streaming:", e)
    
    def get_online_users(self):
        response = self.stub.GetOnlineUsers(chat_pb2.Empty())
        print("Online users:", ", ".join(response.users))
    
    def update_presence(self, is_online):
        request = chat_pb2.PresenceRequest(username =self.username, is_online=is_online)
        self.stub.UpdatePresence(request)
    
    def start_chat(self):
        threading.Thread(target=self.stream_messages, daemon=True).start()

        while True:
            command = input("> ")
            if command == "/exit":
                self.logout()
                break
            elif command == "/users":
                self.get_online_users()
            elif command.startswith("@"):
                parts = command.split(" ", 1)
                if len(parts) < 2:
                    print("Usage: @username message")
                    continue
                receiver, message = parts
                self.send_private_message(receiver[1:], message)
            elif command.startswith("#"):
                parts = command.split(" ", 1)
                if len(parts) < 2:
                    print("Usage: #group_id message")
                    continue
                group_id, message = parts
                self.send_group_message(group_id[1:], message)

            else:
                print("Invalid command! Use @usernameto send DM, #gpoup to send groupmsg, /users to list online users, /exit to quit.")

if __name__ == "__main__":
    username = input("Enter your username: ")
    password = input("Enter your password:")

    client = ChatClient(username, password)
    client.start_chat()