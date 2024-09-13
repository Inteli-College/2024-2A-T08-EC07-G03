import React from 'react';
import Header from '../components/Header';
import FileUpload from '../components/FileUpload';
import { useNavigate } from 'react-router-dom';


const Title: React.FC = () => {
  return (
    <h1 className="text-4xl font-light text-white text-center mt-16 font-sans">
      Dados para Análise:
    </h1>
  );
};

const KNRInput: React.FC = () => {
  return (
    <div className="flex flex-col items-center mt-6">
      <input 
        type="text"
        placeholder="Digite seu KNR"
        className="w-full max-w-lg px-4 py-2 border border-gray-500 rounded-lg bg-transparent text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-white font-light"
        id='krn_input'
      />
    </div>
  );
};

const ConfirmButton: React.FC = () => {
  const navigate = useNavigate();

  const handleTrainClick = async () => {

      try{
        const knr = (document.getElementById('krn_input') as HTMLInputElement).value;
        console.log(knr);

        const response = await fetch('http://localhost:8000/api/model/predict', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({knr})
        });

        if (response.ok) {
          navigate('/excProgress');
        } else {
          throw new Error('Erro ao enviar o KNR');
        }
      } catch (error) {
        console.log("Erro na requisição de predição", error);
      }
  };
  return (
    <div className="flex justify-center mt-6">
      <button onClick={handleTrainClick} className="px-8 py-2 bg-white text-gray-900 rounded-lg hover:bg-gray-200 transition duration-200">
        Confirmar
      </button>
    </div>
  );
};

const ExcPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-gradient-to-b from-[#333641] to-[#282A32] font-sans">
      <Header />
      <Title />
      <FileUpload />
      <p className="text-white text-center mt-6">ou</p>
      <KNRInput />
      <ConfirmButton />
    </div>
  );
};

export default ExcPage;