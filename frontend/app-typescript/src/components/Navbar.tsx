import React from 'react';

interface NavbarProps {
  children: React.ReactNode;
}

const Navbar: React.FC<NavbarProps> = ({ children }) => {
  return (
    <nav className="text-white text-lg">
      {children}
    </nav>
  );
};

export default Navbar;
