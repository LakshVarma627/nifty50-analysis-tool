import CandlestickChart from '../../components/charts/CandlestickChart';
import TechnicalIndicators from '../../components/charts/TechnicalIndicators';
import RecommendationEngine from './RecommendationEngine';
import AlertForm from '../../components/alerts/AlertForm';
import NewsCard from '../../components/news/NewsCard';

export default function Dashboard() {
  return (
    <div className="dashboard">
      <div className="main-content">
        <CandlestickChart />
        <TechnicalIndicators />
        <RecommendationEngine />
      </div>
      <div className="sidebar">
        <AlertForm />
        <NewsCard />
      </div>
    </div>
  );
}