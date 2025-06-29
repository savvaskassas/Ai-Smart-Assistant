import * as React from 'react';
import { Box, Typography, Paper } from '@mui/material';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { StaticDatePicker } from '@mui/x-date-pickers/StaticDatePicker';

const Calendar = ({ events }) => {
  const [selectedDate, setSelectedDate] = React.useState(new Date());

  const eventDates = events
    .map(ev => ev.start?.date || ev.start?.dateTime)
    .filter(Boolean)
    .map(dateStr => new Date(dateStr).toDateString());

  return (
    <Box sx={{ mt: 4, maxWidth: 400, mx: 'auto' }}>
      <Paper elevation={2} sx={{ p: 2, borderRadius: 3, background: '#f5f7fa' }}>
        <LocalizationProvider dateAdapter={AdapterDateFns}>
          <StaticDatePicker
            displayStaticWrapperAs="desktop"
            value={selectedDate}
            onChange={setSelectedDate}
            slots={{ actionBar: () => null }}
            renderDay={(day, _value, DayComponentProps) => {
              const isEvent = eventDates.includes(day.toDateString());
              return (
                <div style={{ position: 'relative' }}>
                  <span style={{
                    background: isEvent ? '#1976d2' : undefined,
                    color: isEvent ? 'white' : undefined,
                    borderRadius: '50%',
                    padding: '0.3em',
                    display: 'inline-block',
                    width: 32,
                    height: 32,
                    textAlign: 'center',
                    lineHeight: '32px',
                  }}>
                    {day.getDate()}
                  </span>
                </div>
              );
            }}
          />
        </LocalizationProvider>
        <Box sx={{ mt: 2 }}>
          <Typography variant="subtitle1" fontWeight={600} color="primary">Events:</Typography>
          {events.filter(ev => {
            const date = ev.start?.date || ev.start?.dateTime;
            return date && new Date(date).toDateString() === selectedDate.toDateString();
          }).map((ev, i) => (
            <Typography key={i} variant="body2" sx={{ mb: 0.5 }}>
              {ev.summary} ({ev.start?.date || ev.start?.dateTime})
            </Typography>
          ))}
          {events.filter(ev => {
            const date = ev.start?.date || ev.start?.dateTime;
            return date && new Date(date).toDateString() === selectedDate.toDateString();
          }).length === 0 && (
            <Typography variant="body2" color="text.secondary">No events for this day.</Typography>
          )}
        </Box>
      </Paper>
    </Box>
  );
};

export default Calendar;
