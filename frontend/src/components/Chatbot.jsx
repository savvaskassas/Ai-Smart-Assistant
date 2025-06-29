import React, { useState } from 'react';
import { Box, TextField, Button, Paper, Typography } from '@mui/material';
import Calendar from './Calendar';

const Chatbot = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [calendarEvents, setCalendarEvents] = useState([]);

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
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && sendMessage()}
          disabled={loading}
        />
        <Button onClick={sendMessage} disabled={loading} sx={{ ml: 1 }} variant="contained">
          Send
        </Button>
        <Button onClick={fetchCalendarEvents} disabled={loading} sx={{ ml: 1 }} variant="outlined">
          Calendar Events
        </Button>
        <Button onClick={fetchDayPlan} disabled={loading} sx={{ ml: 1 }} variant="outlined">
          Day Plan
        </Button>
        <Button onClick={fetchProductivityInsights} disabled={loading} sx={{ ml: 1 }} variant="outlined">
          Productivity Insights
        </Button>
      </Box>
      {calendarEvents.length > 0 && <Calendar events={calendarEvents} />}
    </Box>
  );
};

export default Chatbot;
