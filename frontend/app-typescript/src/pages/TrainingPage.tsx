import React from 'react';
import Header from '../components/Header';
import { useNavigate } from 'react-router-dom';


const Title: React.FC = () => {
  return (
    <h1 className="text-4xl font-light text-white text-center mt-16 font-sans">
      Dados de Treinamento:
    </h1>
  );
};

const FileUpload: React.FC = () => {
  return (
    <div className="font-sans flex flex-col items-center justify-center border-2 border-dashed bg-gradient-to-b from-[#333641] to-[#2D3039] h-64 w-full max-w-lg mx-auto mt-10 bg-gray-800 rounded-lg">
      <label className="cursor-pointer">
        <div className="flex flex-col items-center space-y-2">
          <svg width="150" height="150" viewBox="0 0 150 150" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="40" y="70" width="70" height="40" rx="5" stroke="#888888" stroke-width="6" />
          <circle cx="95" cy="90" r="4" fill="#888888" />
          <path d="M75 30 L75 80" stroke="#888888" stroke-width="6" stroke-linecap="round" />
          <path d="M60 45 L75 30 L90 45" stroke="#888888" stroke-width="6" stroke-linecap="round" />
          </svg>
          <p className="text-white">Adicione seu .csv para treinar o modelo</p>
        </div>
        <input type="file" accept=".csv" className="hidden" />
      </label>
    </div>
  );
};

const KNRInput: React.FC = () => {
  return (
    <div className="flex flex-col items-center mt-6">
      <input 
        type="text"
        placeholder="Digite seu KNR"
        className="w-full max-w-lg px-4 py-2 border border-gray-500 rounded-lg bg-transparent text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white font-light"
      />
    </div>
  );
};

const ConfirmButton: React.FC = () => {
  const navigate = useNavigate();

  const handleTrainClick = () => {
      navigate('/progress');
  };
  return (
    <div className="flex justify-center mt-6">
      <button onClick={handleTrainClick} className="px-8 py-2 bg-white text-gray-900 rounded-lg hover:bg-gray-200 transition duration-200">
        Confirmar
      </button>
    </div>
  );
};


const TrainingPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-b from-[#333641] to-[#282A32] font-sans">
      <Header />
      <Title />
      <FileUpload />
      <KNRInput />
      <ConfirmButton />
    </div>
  );
};



export default TrainingPage;
