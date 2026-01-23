import React from 'react';
import { Box, Typography, Paper, Grid, Card, CardContent, useTheme } from '@mui/material';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';
import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import EventNoteIcon from '@mui/icons-material/EventNote';

const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042', '#8884D8', '#82CA9D'];

const ProductivityChart = ({ insights }) => {
  const theme = useTheme();
  const isDark = theme.palette.mode === 'dark';

  if (!insights) {
    return null;
  }

  // Prepare data for hourly chart
  const hourlyData = Object.entries(insights.minutes_per_hour || {})
    .filter(([_, minutes]) => minutes > 0)
    .map(([hour, minutes]) => ({
      hour,
      minutes: Math.round(minutes),
      hours: (minutes / 60).toFixed(1)
    }))
    .sort((a, b) => a.hour.localeCompare(b.hour));

  // Prepare data for pie chart
  const totalScheduled = insights.total_minutes || 0;
  const workDayMinutes = 8 * 60; // 8 hour work day
  const freeTime = Math.max(0, workDayMinutes - totalScheduled);
  
  const pieData = [
    { name: 'Scheduled Time', value: totalScheduled, color: '#0088FE' },
    { name: 'Free Time', value: freeTime, color: '#00C49F' }
  ];

  return (
    <Box sx={{ mt: 3 }}>
      <Typography variant="h5" fontWeight={700} mb={3} color="primary">
        📊 Productivity Analytics Dashboard
      </Typography>

      {/* Summary Cards */}
      <Grid container spacing={2} mb={3}>
        <Grid item xs={12} sm={4}>
          <Card elevation={2} sx={{ background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)', color: 'white' }}>
            <CardContent>
              <Box display="flex" alignItems="center" mb={1}>
                <EventNoteIcon sx={{ mr: 1 }} />
                <Typography variant="h6">Total Events</Typography>
              </Box>
              <Typography variant="h3" fontWeight={700}>
                {insights.total_events || 0}
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        
        <Grid item xs={12} sm={4}>
          <Card elevation={2} sx={{ background: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)', color: 'white' }}>
            <CardContent>
              <Box display="flex" alignItems="center" mb={1}>
                <AccessTimeIcon sx={{ mr: 1 }} />
                <Typography variant="h6">Total Time</Typography>
              </Box>
              <Typography variant="h3" fontWeight={700}>
                {Math.round((insights.total_minutes || 0) / 60)}h {Math.round((insights.total_minutes || 0) % 60)}m
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        
        <Grid item xs={12} sm={4}>
          <Card elevation={2} sx={{ background: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)', color: 'white' }}>
            <CardContent>
              <Box display="flex" alignItems="center" mb={1}>
                <TrendingUpIcon sx={{ mr: 1 }} />
                <Typography variant="h6">Peak Hour</Typography>
              </Box>
              <Typography variant="h3" fontWeight={700}>
                {insights.most_productive_hour || 'N/A'}
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Charts */}
      <Grid container spacing={3}>
        <Grid item xs={12} md={8}>
          <Paper elevation={3} sx={{ p: 3, borderRadius: 2 }}>
            <Typography variant="h6" fontWeight={600} mb={2} color="primary">
              ⏰ Hourly Activity Distribution
            </Typography>
            {hourlyData.length > 0 ? (
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={hourlyData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="hour" />
                  <YAxis label={{ value: 'Minutes', angle: -90, position: 'insideLeft' }} />
                  <Tooltip 
                    formatter={(value) => `${value} minutes (${(value / 60).toFixed(1)}h)`}
                    contentStyle={{ 
                      background: isDark ? '#1e1e1e' : '#fff', 
                      border: `1px solid ${isDark ? '#555' : '#ccc'}`, 
                      borderRadius: 5,
                      color: isDark ? '#fff' : '#000'
                    }}
                  />
                  <Legend />
                  <Bar dataKey="minutes" fill={isDark ? '#90caf9' : '#1976d2'} name="Scheduled Minutes" />
                </BarChart>
              </ResponsiveContainer>
            ) : (
              <Typography variant="body2" color="text.secondary" align="center" py={5}>
                No hourly data available for today
              </Typography>
            )}
          </Paper>
        </Grid>

        <Grid item xs={12} md={4}>
          <Paper elevation={3} sx={{ p: 3, borderRadius: 2 }}>
            <Typography variant="h6" fontWeight={600} mb={2} color="primary">
              📈 Time Allocation
            </Typography>
            {totalScheduled > 0 ? (
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                  <Pie
                    data={pieData}
                    cx="50%"
                    cy="50%"
                    labelLine={false}
                    label={({ name, percent }) => `${name}: ${(percent * 100).toFixed(0)}%`}
                    outerRadius={80}
                    fill="#8884d8"
                    dataKey="value"
                  >
                    {pieData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip 
                    formatter={(value) => `${Math.round(value)} minutes`}
                    contentStyle={{ 
                      background: isDark ? '#1e1e1e' : '#fff', 
                      border: `1px solid ${isDark ? '#555' : '#ccc'}`, 
                      borderRadius: 5,
                      color: isDark ? '#fff' : '#000'
                    }}
                  />
                </PieChart>
              </ResponsiveContainer>
            ) : (
              <Typography variant="body2" color="text.secondary" align="center" py={5}>
                No time allocation data available
              </Typography>
            )}
            <Box mt={2}>
              <Typography variant="body2" color="text.secondary">
                <strong>Scheduled:</strong> {Math.round(totalScheduled)} min ({(totalScheduled / 60).toFixed(1)}h)
              </Typography>
              <Typography variant="body2" color="text.secondary">
                <strong>Free Time:</strong> {Math.round(freeTime)} min ({(freeTime / 60).toFixed(1)}h)
              </Typography>
            </Box>
          </Paper>
        </Grid>
      </Grid>

      {/* Additional Insights */}
      <Paper elevation={2} sx={{ p: 3, mt: 3, borderRadius: 2, bgcolor: 'background.paper' }}>
        <Typography variant="h6" fontWeight={600} mb={2} color="primary">
          💡 Key Insights
        </Typography>
        <Grid container spacing={2}>
          <Grid item xs={12} sm={6}>
            <Typography variant="body2" color="text.secondary">
              📅 <strong>Total Events Today:</strong> {insights.total_events || 0} events
            </Typography>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Typography variant="body2" color="text.secondary">
              ⏱️ <strong>Average Event Duration:</strong> {insights.total_events ? Math.round((insights.total_minutes || 0) / insights.total_events) : 0} minutes
            </Typography>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Typography variant="body2" color="text.secondary">
              🎯 <strong>Most Productive Hour:</strong> {insights.most_productive_hour || 'Not enough data'}
            </Typography>
          </Grid>
          <Grid item xs={12} sm={6}>
            <Typography variant="body2" color="text.secondary">
              📊 <strong>Schedule Utilization:</strong> {((totalScheduled / workDayMinutes) * 100).toFixed(0)}% of 8-hour workday
            </Typography>
          </Grid>
        </Grid>
      </Paper>
    </Box>
  );
};

export default ProductivityChart;
