import React, { useState } from 'react';
import { Box, TextField, Button, Paper, Typography } from '@mui/material';

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;
    setMessages([...messages, { sender: 'user', text: input }]);
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:8080/chat/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      });
      const data = await response.json();
      setMessages(msgs => [...msgs, { sender: 'assistant', text: data.response }]);
    } catch (e) {
      setMessages(msgs => [...msgs, { sender: 'assistant', text: 'Connection error with backend.' }]);
    }
    setInput('');
    setLoading(false);
  };

  return (
    <Box sx={{ maxWidth: 500, mx: 'auto', mt: 4 }}>
      <Paper sx={{ p: 2, minHeight: 300 }}>
        {messages.map((msg, i) => (
          <Typography key={i} sx={{ color: msg.sender === 'user' ? 'blue' : 'green' }}>
            <b>{msg.sender === 'user' ? 'You' : 'Assistant'}:</b> {msg.text}
          </Typography>
        ))}
      </Paper>
      <Box sx={{ display: 'flex', mt: 2 }}>
        <TextField
          fullWidth
          variant="outlined"
          placeholder="Type your message..."
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && sendMessage()}
          disabled={loading}
        />
        <Button onClick={sendMessage} variant="contained" sx={{ ml: 1 }} disabled={loading}>
          Send
        </Button>
      </Box>
    </Box>
  );
};

export default Chatbot;
