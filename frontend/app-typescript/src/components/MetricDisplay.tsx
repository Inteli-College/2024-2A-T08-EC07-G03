import React from 'react';

interface MetricDisplayProps {
  title: string;
  metrics: string[];
}

const MetricDisplay: React.FC<MetricDisplayProps> = ({ title, metrics }) => {
  return (
    <div className="bg-white p-4 rounded-lg shadow">
      <h3 className="font-bold text-lg mb-2">{title}</h3>
      <div className="space-y-1">
        {metrics.map((metric, index) => (
          <div key={index} className="grid grid-cols-2">
            <p className="text-gray-700">{metric.split(':')[0]}</p>
            <p className="text-right text-gray-600">{metric.split(':')[1]}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MetricDisplay;
