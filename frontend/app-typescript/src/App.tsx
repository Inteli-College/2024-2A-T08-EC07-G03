import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import TrainingPage from './pages/TrainingPage';  
import TrainingProgressPage from './pages/TrainingProgressPage';
import TrainedModelPage from './pages/TrainedModelPage';



function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/training" element={<TrainingPage />} />
        <Route path="/progress" element={<TrainingProgressPage />} />
        <Route path="/trained" element={<TrainedModelPage />} />
      </Routes>
    </Router>
  );
}

export default App;