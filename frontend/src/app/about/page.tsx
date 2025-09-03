import React from 'react';
import Header from '@/components/header/Header';
import Footer from '@/components/footer/Footer';

export default function About() {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow container mx-auto px-4 py-8">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            About SubTrack
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            We help you take control of your subscriptions and save money.
          </p>
        </div>

        <div className="max-w-3xl mx-auto">
          <div className="bg-white rounded-lg shadow-md p-6 mb-8">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">Our Mission</h2>
            <p className="text-gray-600 mb-4">
              At SubTrack, we believe that managing subscriptions should be simple and stress-free. 
              Our mission is to help individuals and businesses take control of their recurring expenses 
              by providing an intuitive platform that makes tracking, analyzing, and optimizing 
              subscriptions effortless.
            </p>
            <p className="text-gray-600">
              We understand how easy it is to lose track of multiple subscriptions, leading to 
              unnecessary expenses. That's why we've built a solution that not only helps you keep 
              track of what you're paying for but also provides insights to help you save money.
            </p>
          </div>

          <div className="bg-white rounded-lg shadow-md p-6 mb-8">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">Our Story</h2>
            <p className="text-gray-600 mb-4">
              SubTrack was founded in 2023 by a team of financial enthusiasts who were frustrated 
              with the lack of transparency in subscription management. We realized that many people 
              were unknowingly overspending on subscriptions they had forgotten about or weren't 
              using effectively.
            </p>
            <p className="text-gray-600">
              What started as a personal project to solve our own subscription management problems 
              quickly evolved into a full-fledged solution that we believed could help others as well. 
              Today, SubTrack is used by thousands of users worldwide to regain control over their 
              recurring expenses.
            </p>
          </div>

          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-2xl font-bold text-gray-900 mb-4">Our Values</h2>
            <ul className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <li className="flex items-start">
                <div className="bg-blue-100 rounded-full p-2 mr-3">
                  <svg className="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                  </svg>
                </div>
                <span className="text-gray-600">Transparency in pricing and features</span>
              </li>
              <li className="flex items-start">
                <div className="bg-blue-100 rounded-full p-2 mr-3">
                  <svg className="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
                  </svg>
                </div>
                <span className="text-gray-600">Security and privacy of user data</span>
              </li>
              <li className="flex items-start">
                <div className="bg-blue-100 rounded-full p-2 mr-3">
                  <svg className="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
                  </svg>
                </div>
                <span className="text-gray-600">User-centric design and experience</span>
              </li>
              <li className="flex items-start">
                <div className="bg-blue-100 rounded-full p-2 mr-3">
                  <svg className="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                  </svg>
                </div>
                <span className="text-gray-600">Continuous innovation and improvement</span>
              </li>
            </ul>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}