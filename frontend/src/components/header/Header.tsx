import React from 'react';
import Navbar from '../navbar/Navbar';

const Header = () => {
  return (
    <header className="bg-white shadow-md">
      <div className="container mx-auto px-4 py-4">
        <div className="flex justify-between items-center">
          <div className="text-2xl font-bold text-blue-600">SubTrack</div>
          <Navbar />
        </div>
      </div>
    </header>
  );
};

export default Header;