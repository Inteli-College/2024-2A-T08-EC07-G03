import React, { useState } from 'react';
import Header from '../components/Header';
import FileUpload_Resultados from '../components/FileUpload_Resultados';
import FileUpload_Status from '../components/FileUpload_Status';
import FileUpload_Falhas from '../components/FileUpload_Falhas';
import { useNavigate } from 'react-router-dom';

const Title = () => {
    return (<h1 className="text-6xl font-light text-white text-center mt-8 mb-24 font-sans">
      Dados de Treinamento:
    </h1>);
};

const ConfirmButton = ({ resultados, falhas, status }) => {
    const navigate = useNavigate();

    const handleTrainClick = async () => {
        const formData = new FormData();
        
        // Adicionando os arquivos de resultados ao FormData
        resultados.forEach((file) => {
            formData.append("resultados", file);
        });

        // Adicionando os arquivos de falhas ao FormData
        falhas.forEach((file) => {
            formData.append("falhas", file);
        });

        // Adicionando os arquivos de status ao FormData
        status.forEach((file) => {
            formData.append("status", file);
        });

        formData.append("save_new_model", "true");

        try {
            const response = await fetch('http://127.0.0.1:8000/api/model/retrain', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                const data = await response.json();
                console.log(data);
                navigate('/progress'); // Navegar para a página de progresso após o sucesso
            } else {
                const errorData = await response.json();
                console.error('Erro:', errorData.detail);
            }
        } catch (error) {
            console.error('Erro ao enviar os arquivos:', error);
        }
    };

    return (
        <div className="flex justify-center mt-6">
            <button onClick={handleTrainClick} className="px-12 py-1 mt-8 bg-white text-gray-900 rounded-lg hover:bg-gray-200 transition duration-200">
                Confirmar
            </button>
        </div>
    );
};

const TrainingPage = () => {
    // Estados para armazenar os arquivos
    const [resultados, setResultados] = useState([]);
    const [falhas, setFalhas] = useState([]);
    const [status, setStatus] = useState([]);

    return (
        <div className="min-h-screen bg-gradient-to-b from-[#333641] to-[#282A32] font-sans">
            <Header />
            <Title />
            <div className="flex justify-center gap-4 mt-8">
                <FileUpload_Resultados setFiles={setResultados} />
                <FileUpload_Status setFiles={setStatus} />
                <FileUpload_Falhas setFiles={setFalhas} />
            </div>
            <ConfirmButton resultados={resultados} falhas={falhas} status={status} />
        </div>
    );
};

export default TrainingPage;
