import { useEffect, useState } from 'react';
import { fetchNews } from '../../services/api';

export default function NewsCard() {
  const [news, setNews] = useState([]);

  useEffect(() => {
    fetchNews().then(data => setNews(data));
  }, []);

  return (
    <div className="news-card">
      <h3>Market News</h3>
      {news.map((item, index) => (
        <div key={index} className="news-item">
          <h4>{item.title}</h4>
          <p>{item.summary}</p>
        </div>
      ))}
    </div>
  );
}