import React from 'react';

interface ModelSelectorProps {
  onSelect: (model: 'current' | 'previous') => void;
}

const ModelSelector: React.FC<ModelSelectorProps> = ({ onSelect }) => {
  return (
    <div className="flex justify-center gap-4 mt-4">
      <button onClick={() => onSelect('current')} className="px-4 py-2 rounded bg-gray-700 text-white">Atual</button>
      <button onClick={() => onSelect('previous')} className="px-4 py-2 rounded bg-gray-700 text-white">Anterior</button>
    </div>
  );
};

export default ModelSelector;
