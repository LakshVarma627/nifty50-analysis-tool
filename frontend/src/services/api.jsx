export const fetchStockData = async () => {
  const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/stock-data`);
  return response.json();
};

export const fetchNews = async () => {
  const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/news`);
  return response.json();
};