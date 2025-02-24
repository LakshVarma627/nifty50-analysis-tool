# Nifty50 Analysis Tool

## Overview

The Nifty50 Analysis Tool is a comprehensive platform designed to provide real-time analysis and insights into the Nifty50 stock market index. The tool offers various features including candlestick charts, technical indicators, AI-driven trading signals, and market news updates. It aims to assist traders and investors in making informed decisions by leveraging advanced technologies and data analysis.

## Technology Stack

### Frontend
- **React**: A JavaScript library for building user interfaces.
- **Vite**: A build tool that provides a fast development environment.
- **ApexCharts**: A modern charting library for visualizing data.
- **Axios**: A promise-based HTTP client for making API requests.
- **Zustand**: A small, fast, and scalable state-management solution.
- **Sass**: A CSS preprocessor for writing more maintainable styles.

### Backend
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **TensorFlow**: An open-source machine learning framework for building and training models.
- **WolframAlpha**: An API for accessing computational knowledge and data.
- **PostgreSQL**: A powerful, open-source relational database system.
- **Django**: A high-level Python web framework for building robust web applications.

## Folder Structure

### Root Directory
- `frontend/`: Contains the frontend codebase.
- `nifty50-analysis-tool/`: Contains the core analysis and backend services.

### Frontend Directory
- `.env`: Environment variables for the frontend application.
- `package.json`: Lists dependencies and scripts for the frontend.
- `public/`: Contains static assets like the `index.html` file.
- `src/`: Contains the source code for the frontend application.
  - `components/`: Reusable UI components.
    - `alerts/`: Components related to alert functionality.
    - `charts/`: Components for rendering different types of charts.
    - `news/`: Components for displaying market news.
  - `contexts/`: Context providers for managing global state.
  - `hooks/`: Custom hooks for data fetching and WebSocket connections.
  - `pages/`: Different pages of the application.
    - `Auth/`: Authentication-related pages like Login and Signup.
    - `Dashboard/`: Main dashboard page with various widgets.
  - `services/`: API service functions for data fetching.
  - `utils/`: Utility functions for calculations and data processing.
  - `main.jsx`: Entry point for the React application.
  - `App.jsx`: Main application component with routing.

### Backend Directory
- `quantum-core/`: Core algorithms and models for analysis.
  - `algo_frameworks/`: Contains algorithm scripts.
    - `quantlib_scripts/`: Scripts for financial calculations.
    - `tensorflow_models/`: TensorFlow models for predictions.
  - `wolfram/`: Integration with WolframAlpha API.
    - `api_integrator.py`: API integration script.
    - `symbolic_engine/`: Wolfram Language scripts for financial analysis.
- `singularity-backend/`: Backend services and APIs.
  - `cyborg_services/`: Services for TensorFlow and Wolfram integration.
    - `tensorflow_services/`: TensorFlow model training and prediction.
    - `wolfram_proxy/`: Proxy services for WolframAlpha API.
  - `hyperdrive/`: API routing and endpoints.
    - `wolfram_router.py`: API router for WolframAlpha queries.
  - `neo_models/`: Database models and caching.
    - `mongo_quant.py`: MongoDB integration for data storage.
    - `wolfram_cache.py`: Caching for WolframAlpha queries.
- `starlight-frontend/`: Additional frontend components for advanced features.
  - `src/`: Source code for the additional frontend.
    - `neuro-components/`: Components for TensorFlow and Wolfram integration.
      - `TensorDisplay/`: Components for displaying TensorFlow predictions.
      - `WolframCell/`: Components for WolframAlpha queries.
    - `pages/`: Pages for advanced analysis.
      - `QuantumAnalysis/`: Page for quantum analysis using WolframAlpha.
    - `quantum-hooks/`: Custom hooks for WolframAlpha integration.

## Getting Started

### Prerequisites
- Node.js and npm installed
- Python and pip installed
- PostgreSQL database setup

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LakshVarma627/nifty50-analysis-tool.git
   cd nifty50-analysis-tool
   ```

2. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

3. Install backend dependencies:
   ```bash
   cd ../nifty50-analysis-tool
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the `frontend` directory with the necessary environment variables.
   - Create a `.env` file in the `nifty50-analysis-tool` directory with the necessary environment variables.

### Running the Application

1. Start the frontend development server:
   ```bash
   cd frontend
   npm run dev
   ```

2. Start the backend server:
   ```bash
   cd ../nifty50-analysis-tool 
   uvicorn main:app --reload
   ```

3. Open your browser and navigate to `http://localhost:3000` to access the application.

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Special thanks to the contributors and the open-source community for their valuable support and resources.
