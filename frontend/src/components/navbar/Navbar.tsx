import React from 'react';
import Link from 'next/link';

const Navbar = () => {
  return (
    <nav>
      <ul className="flex space-x-6">
        <li>
          <Link href="/" className="text-gray-600 hover:text-blue-600 transition-colors">
            Home
          </Link>
        </li>
        <li>
          <Link href="/features" className="text-gray-600 hover:text-blue-600 transition-colors">
            Features
          </Link>
        </li>
        <li>
          <Link href="/pricing" className="text-gray-600 hover:text-blue-600 transition-colors">
            Pricing
          </Link>
        </li>
        <li>
          <Link href="/about" className="text-gray-600 hover:text-blue-600 transition-colors">
            About
          </Link>
        </li>
        <li>
          <Link href="/contact" className="text-gray-600 hover:text-blue-600 transition-colors">
            Contact
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;