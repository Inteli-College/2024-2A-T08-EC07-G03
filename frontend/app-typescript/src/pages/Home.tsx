import React from 'react';
import Button from '../components/Button';
import Navbar from '../components/Navbar';
import { useNavigate } from 'react-router-dom';


const App: React.FC = () => {

    const navigate = useNavigate();

    const handleTrainClick = () => {
        navigate('/training');
    };

    return (
        <div className="min-h-screen flex flex-col">
            {/* Navbar */}
            <Navbar>
                <a href="/">Home</a>
            </Navbar>

            {/* Conteúdo Principal Centralizado */}
            <div className="flex-1 flex items-center justify-center bg-gradient-to-r from-gray-900 to-gray-800">
                <div className="flex flex-col items-center space-y-8">

                    {/* Logo e Título */}
                    <div className="flex flex-col items-center space-y-4">
                        <img src="/assets/logo.png" alt="Käfer logo" className="h-24 w-24" />
                        <h1 className="text-white text-4xl font-light">Käfer</h1>
                    </div>

                    {/* Botões */}
                    <div className="mt-8 flex space-x-4">
                        <Button label="Executar" />
                        <button onClick={handleTrainClick}>Treinar</button>
                        </div>

                    {/* Footer */}
                    <footer className="text-gray-400 text-sm">
                        Arquivos suportados: (.csv)
                    </footer>
                </div>
            </div>
        </div>
    );
};

export default App;
