import React, { useState, useRef, useEffect } from 'react';
import { Box, TextField, Button, Paper, Typography, Stack, Avatar, CircularProgress, Tooltip } from '@mui/material';
import Calendar from './Calendar';
import PersonIcon from '@mui/icons-material/Person';
import SmartToyIcon from '@mui/icons-material/SmartToy';

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [calendarEvents, setCalendarEvents] = useState([]);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

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

  const fetchCalendarEvents = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:8080/calendar/events');
      const data = await response.json();
      console.log('Calendar events response:', data);
      setCalendarEvents(data.events || []);
      setMessages(msgs => [
        ...msgs,
        { sender: 'assistant', text: 'Calendar events loaded!' }
      ]);
    } catch (e) {
      setMessages(msgs => [...msgs, { sender: 'assistant', text: 'Error fetching calendar events.' }]);
    }
    setLoading(false);
  };

  const fetchDayPlan = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:8080/day-plan');
      const data = await response.json();
      setMessages(msgs => [
        ...msgs,
        { sender: 'assistant', text: 'Day plan:\n' + data.day_plan.join('\n') }
      ]);
    } catch (e) {
      setMessages(msgs => [...msgs, { sender: 'assistant', text: 'Error fetching day plan.' }]);
    }
    setLoading(false);
  };

  const fetchProductivityInsights = async () => {
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:8080/productivity-insights');
      const data = await response.json();
      const insights = data.insights;
      setMessages(msgs => [
        ...msgs,
        { sender: 'assistant', text: `Productivity Insights:\nTotal events: ${insights.total_events}\nTotal minutes: ${insights.total_minutes}\nMost productive hour: ${insights.most_productive_hour}\nMinutes per hour: ${JSON.stringify(insights.minutes_per_hour, null, 2)}` }
      ]);
    } catch (e) {
      setMessages(msgs => [...msgs, { sender: 'assistant', text: 'Error fetching productivity insights.' }]);
    }
    setLoading(false);
  };

  return (
    <Box sx={{ maxWidth: { xs: '100%', sm: 600 }, mx: 'auto', mt: { xs: 2, sm: 6 }, p: { xs: 1, sm: 2 } }}>
      <Typography variant="h4" align="center" fontWeight={700} mb={2} color="primary" sx={{ fontSize: { xs: '1.5rem', sm: '2.125rem' } }}>
        AI Smart Assistant
      </Typography>
      <Paper elevation={3} sx={{ p: { xs: 1.5, sm: 3 }, minHeight: 250, background: '#f9f9f9', borderRadius: 3 }}>
        <Stack spacing={2}>
          {messages.map((msg, i) => (
            <Box key={i} sx={{ display: 'flex', flexDirection: msg.sender === 'user' ? 'row-reverse' : 'row', alignItems: 'flex-end' }}>
              <Avatar sx={{ bgcolor: msg.sender === 'user' ? 'primary.main' : 'secondary.main', ml: msg.sender === 'user' ? 2 : 0, mr: msg.sender === 'assistant' ? 2 : 0, width: { xs: 32, sm: 40 }, height: { xs: 32, sm: 40 } }}>
                {msg.sender === 'user' ? <PersonIcon fontSize="small" /> : <SmartToyIcon fontSize="small" />}
              </Avatar>
              <Box sx={{
                bgcolor: msg.sender === 'user' ? 'primary.light' : 'secondary.light',
                color: '#222',
                px: 2, py: 1, borderRadius: 2, maxWidth: { xs: '85%', sm: '70%' },
                boxShadow: 1,
                whiteSpace: 'pre-line',
                fontSize: { xs: '0.95rem', sm: '1rem' },
              }}>
                <Typography variant="body1" fontWeight={msg.sender === 'user' ? 600 : 500}>
                  {msg.text}
                </Typography>
              </Box>
            </Box>
          ))}
          <div ref={messagesEndRef} />
        </Stack>
      </Paper>
      {loading && (
        <Box sx={{ display: 'flex', justifyContent: 'center', my: 2 }}>
          <CircularProgress size={32} color="primary" />
        </Box>
      )}
      <Stack direction={{ xs: 'column', sm: 'row' }} spacing={2} mt={2}>
        <TextField
          fullWidth
          variant="outlined"
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && sendMessage()}
          disabled={loading}
          placeholder="Type your message..."
          sx={{ bgcolor: 'white', borderRadius: 2 }}
        />
        <Tooltip title="Send your message">
          <span>
            <Button onClick={sendMessage} disabled={loading} variant="contained" size="large" sx={{ minWidth: { xs: '100%', sm: 100 } }}>
              Send
            </Button>
          </span>
        </Tooltip>
      </Stack>
      <Stack direction={{ xs: 'column', sm: 'row' }} spacing={2} mt={2} justifyContent="center">
        <Tooltip title="Load your Google Calendar events">
          <span>
            <Button onClick={fetchCalendarEvents} disabled={loading} variant="outlined" sx={{ minWidth: { xs: '100%', sm: 160 } }}>
              Calendar Events
            </Button>
          </span>
        </Tooltip>
        <Tooltip title="Get your personalized day plan">
          <span>
            <Button onClick={fetchDayPlan} disabled={loading} variant="outlined" sx={{ minWidth: { xs: '100%', sm: 160 } }}>
              Day Plan
            </Button>
          </span>
        </Tooltip>
        <Tooltip title="See productivity analytics">
          <span>
            <Button onClick={fetchProductivityInsights} disabled={loading} variant="outlined" sx={{ minWidth: { xs: '100%', sm: 180 } }}>
              Productivity Insights
            </Button>
          </span>
        </Tooltip>
      </Stack>
      {calendarEvents.length > 0 && <Calendar events={calendarEvents} />}
    </Box>
  );
};

export default Chatbot;
