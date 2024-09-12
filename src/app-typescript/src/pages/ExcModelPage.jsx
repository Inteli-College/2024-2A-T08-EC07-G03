import React, { useState } from 'react';
import Header from '../components/Header';
const ExcModelPage = () => {
    const [isPopupVisible, setPopupVisible] = useState(false);
    const handleOpenPopup = () => {
        setPopupVisible(true);
    };
    const handleClosePopup = () => {
        setPopupVisible(false);
    };
    return (<div className="min-h-screen bg-gradient-to-b from-[#333641] to-[#282A32] text-white p-8">
      <Header />
      <div className="flex flex-col items-center justify-center">
      <h1 className="text-3xl font-light mb-6">Modelo Executado:</h1>

      <div className="w-full max-w-2xl h-64 bg-gray-200 rounded-lg flex items-center justify-center text-black text-2xl mb-8">
        Gráficos e Métricas
      </div>

      <div className="w-full max-w-2xl mb-4">
        <label className="block text-gray-400 mb-2">Resultado Atual:</label>
        <div className="w-full bg-gray-300 h-10 rounded-lg flex justify-center items-center">
          <span className="text-black">XXXXXX</span>
        </div>
      </div>

      <div className="w-full max-w-2xl mb-4">
        <label className="block text-gray-400 mb-2">Modelo Anterior:</label>
        <div className="w-full bg-gray-300 h-10 rounded-lg flex justify-center items-center">
          <span className="text-black">XXXXXX</span>
        </div>
      </div>

    
     
    </div>
    </div>);
};
export default ExcModelPage;
