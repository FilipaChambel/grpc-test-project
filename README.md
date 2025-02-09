# grpc-test-project
# Install gRPC and Protocol buffers
pip3 install grpcio-tools protobuf

python3 -m grpc_tools.protoc -I protos --python_out=./protos --grpc_python_out=./protos protos/chat.proto

pip install fastapi uvicorn grpcio grpcio-tools protobuf websockets
npx create-vite@latest grpc-chat --template react
cd grpc-chat
npm install
npm install websocket


# Run the application
1. Run the backend gRPC server:
    `python3 server.py`
2. Run the backend websocker server:
    `websocket_server.py`
3. Run the frontend client - Vite React JS:
    `npm run dev`