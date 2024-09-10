import React, { useState } from 'react';
import Header from '../components/Header';
import MetricDisplay from '../components/MetricDisplay';
import ModelSelector from '../components/ModelSelector';

const TrainedModelPage: React.FC = () => {
  const [model, setModel] = useState('current');
  const currentMetrics = ['Accuracy: 95%', 'Loss: 5%'];
  const previousMetrics = ['Accuracy: 90%', 'Loss: 10%'];

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <Header />
      <h1 className="text-3xl font-bold text-center mt-8">Modelo Treinado: Gráficos e Métricas</h1>
      <div className="container mx-auto p-4">
        <MetricDisplay title="Modelo Atual:" metrics={model === 'current' ? currentMetrics : previousMetrics} />
        <MetricDisplay title="Modelo Anterior:" metrics={model === 'previous' ? previousMetrics : currentMetrics} />
        <ModelSelector onSelect={(selected) => setModel(selected)} />
      </div>
    </div>
  );
};

export default TrainedModelPage;
