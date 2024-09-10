import React from 'react';
import { Link } from 'react-router-dom';

const Header: React.FC = () => {
  return (
    <header className="flex items-center space-x-4 p-4">
      <Link to="/" className="text-gray-400 hover:text-white">Home</Link>
      <span className="text-gray-400">{'>'}</span>
      <span className="text-white">Pagina atual</span>
    </header>
  );
};

export default Header;