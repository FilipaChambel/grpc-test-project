import { useState, useEffect } from 'react'

import './App.css'

export default function App() {
  const [socket, setSocket] = useState(null);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loggedIn, setLoggedIn] = useState(false);
  const [receiver, setReceiver] = useState("");
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    if(socket){
      socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        if(data.type === "login_success"){
          setLoggedIn(true);
        } else if(data.type === "new_message"){
          setMessages((prev) => [...prev, `${data.sender}: ${data.content}`]);
        }
      }
    }
  },[socket]);

  const handleLogin = () => {
    const ws = new WebSocket(`ws://localhost:8000/ws/${username}`);
    ws.onopen = () => {
      ws.send(JSON.stringify({action: "login", password}));
    };
    setSocket(ws);
  };

  const sendMessage = () => {
    if(socket && receiver && message){
      socket.send(JSON.stringify({action: "send_message", receiver, content: message}))
      setMessage((prev) => [...prev, `You: ${message}`]);
      setMessage("");
    }
  }
  
  return (
    <div style={{textAlign: "center", padding: "20px"}}>
      {!loggedIn ? (
        <div>
          <h2>Login</h2>
          <input placeholder='Username' onChange={(e)=> setUsername(e.target.value)}/>
          <input type='password' placeholder='Password' onChange={(e)=> setPassword(e.target.value)}/>
          <button onClick={handleLogin}>Login</button>
        </div>
      ): (
        <div>
          <h2>Chat as {username}</h2>
          <input placeholder='Receiver' onChange={(e)=> setReceiver(e.target.value)}/>
          <input placeholder='Message' value={message} onChange={(e)=> setMessage(e.target.value)}/>
          <button onClick={sendMessage}>Send</button>
          <div>
            <h3>Messages</h3>
            {messages.map((msg, index) => (
              <p key={index}>{msg}</p>
            ))}
          </div>
        </div>
      )}
      
    </div>
  )
}

