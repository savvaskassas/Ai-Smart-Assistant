import * as React from 'react';
import { Box, Typography } from '@mui/material';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns';
import { StaticDatePicker } from '@mui/x-date-pickers/StaticDatePicker';

const Calendar = ({ events }) => {
  const [selectedDate, setSelectedDate] = React.useState(new Date());

  // Εξάγουμε τις ημερομηνίες των events
  const eventDates = events
    .map(ev => ev.start?.date || ev.start?.dateTime)
    .filter(Boolean)
    .map(dateStr => new Date(dateStr).toDateString());

  return (
    <Box sx={{ mt: 2 }}>
      <LocalizationProvider dateAdapter={AdapterDateFns}>
        <StaticDatePicker
          displayStaticWrapperAs="desktop"
          value={selectedDate}
          onChange={setSelectedDate}
          slots={{ actionBar: () => null }} // Αφαιρεί τα CANCEL/OK
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
        <Typography variant="subtitle1">Events:</Typography>
        {events.filter(ev => {
          const date = ev.start?.date || ev.start?.dateTime;
          return date && new Date(date).toDateString() === selectedDate.toDateString();
        }).map((ev, i) => (
          <Typography key={i} variant="body2">
            {ev.summary} ({ev.start?.date || ev.start?.dateTime})
          </Typography>
        ))}
      </Box>
    </Box>
  );
};

export default Calendar;
