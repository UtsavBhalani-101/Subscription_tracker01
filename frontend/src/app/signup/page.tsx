'use client';

import React from 'react';
import Link from 'next/link';
import Header from '../components/header/Header';
import Footer from '../components/footer/Footer';
import Signup from '../components/auth/Signup';

export default function SignupPage() {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow container mx-auto px-4 py-8 flex items-center justify-center">
        <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
          <Signup />
          <div className="mt-6 text-center">
            <span className="text-sm text-gray-600">Already have an account? </span>
            <Link href="/login" className="text-sm font-medium text-blue-600 hover:text-blue-500">
              Sign in
            </Link>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}