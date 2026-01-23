import React from 'react';
import { Box, IconButton, Tooltip } from '@mui/material';
import Brightness4Icon from '@mui/icons-material/Brightness4';
import Brightness7Icon from '@mui/icons-material/Brightness7';
import { useColorMode } from './ThemeContext';
import Chatbot from './components/Chatbot';

function App() {
  const { mode, toggleColorMode } = useColorMode();

  return (
    <Box sx={{ minHeight: '100vh', position: 'relative' }}>
      {/* Theme toggle button in top-right corner */}
      <Box sx={{ position: 'fixed', top: 16, right: 16, zIndex: 1000 }}>
        <Tooltip title={`Switch to ${mode === 'light' ? 'dark' : 'light'} mode`}>
          <IconButton 
            onClick={toggleColorMode} 
            color="inherit"
            sx={{ 
              bgcolor: 'background.paper', 
              boxShadow: 2,
              '&:hover': { bgcolor: 'action.hover' }
            }}
          >
            {mode === 'dark' ? <Brightness7Icon /> : <Brightness4Icon />}
          </IconButton>
        </Tooltip>
      </Box>
      
      <Box sx={{ py: 2 }}>
        <Chatbot />
      </Box>
    </Box>
  );
}

export default App;
