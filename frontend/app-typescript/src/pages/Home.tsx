import React, { useState } from 'react';
import Button from '../components/Button';
import Navbar from '../components/Navbar';
import { useNavigate } from 'react-router-dom';
import Popup from '../components/Popup'; 

const Home: React.FC = () => {
    const navigate = useNavigate();
    const [isPopupVisible, setIsPopupVisible] = useState(false);

    const handleTrainClick = () => {
        setIsPopupVisible(true);  
    };

    const handleClosePopup = () => {
        setIsPopupVisible(false);  
    };

    const handleConfirm = () => {
        setIsPopupVisible(false);  
        navigate('/training');  // Redireciona para a página TrainingPage
    };

    return (
        <div className="min-h-screen flex flex-col bg-gradient-to-r from-gray-900 to-gray-800">
            {/* Navbar */}
            <Navbar>
                <a href="/">Home</a>
            </Navbar>

            {/* Conteúdo Principal Centralizado */}
            <div className="flex-1 flex items-center justify-center bg-gradient-to-r from-gray-900 to-gray-800">
                <div className="flex flex-col items-center space-y-8">

                    {/* Logo e Título */}
                    <div className="flex flex-col items-center space-y-4">
                        <img src="../../src/assets/logo.png" alt="Käfer logo" />
                    </div>

                    {/* Botões */}
                    <div className="mt-8 flex space-x-4">
                        <Button label="Executar" />
                        <Button label="Treinar" onClick={handleTrainClick} />
                    </div>

                    {/* Footer */}
                    <footer className="text-gray-400 text-sm">
                        Arquivos suportados: (.csv)
                    </footer>
                </div>
            </div>

            {/* Popup Modal */}
            <Popup
                isVisible={isPopupVisible}
                onClose={handleClosePopup}
                onConfirm={handleConfirm}  // Passa a função handleConfirm
            />
        </div>
    );
};

export default Home;
