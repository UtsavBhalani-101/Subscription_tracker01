'use client';

import React from 'react';
import Link from 'next/link';
import Header from '../components/header/Header';
import Footer from '../components/footer/Footer';
import Login from '../components/auth/Login';

export default function LoginPage() {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow container mx-auto px-4 py-8 flex items-center justify-center">
        <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
          <Login />
          <div className="mt-6 text-center">
            <Link href="/forgot-password" className="text-sm text-blue-600 hover:text-blue-500">
              Forgot your password?
            </Link>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}