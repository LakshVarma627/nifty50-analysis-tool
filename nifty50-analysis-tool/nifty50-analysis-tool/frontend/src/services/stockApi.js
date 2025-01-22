import axios from 'axios';

// Configure once, reuse everywhere
const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000/api/v1',
  timeout: 10000, // Fail fast if no response
});

// Unified error handler
const handleError = (error) => {
  if (error.response) {
    console.error('Server responded with:', error.response.status);
    return { error: `Server error: ${error.response.status}` };
  }
  console.error('Request failed:', error.message);
  return { error: 'Network error' };
};

// Fetch Nifty50 data with automatic retries
export const getNiftyData = async () => {
  try {
    const { data } = await api.get('/nifty');
    return data;
  } catch (error) {
    return handleError(error);
  }
};