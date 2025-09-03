import React from 'react';
import Header from '@/components/header/Header';
import Footer from '@/components/footer/Footer';

export default function Pricing() {
  const plans = [
    {
      name: 'Free',
      price: '$0',
      period: 'forever',
      features: [
        'Track up to 5 subscriptions',
        'Basic renewal alerts',
        'Email support',
        'Community access',
      ],
      cta: 'Get Started',
      popular: false,
    },
    {
      name: 'Pro',
      price: '$4.99',
      period: 'per month',
      features: [
        'Unlimited subscriptions',
        'Advanced analytics',
        'Priority renewal alerts',
        'Usage tracking',
        'Priority email support',
        'Export data',
      ],
      cta: 'Try Free for 14 Days',
      popular: true,
    },
    {
      name: 'Business',
      price: '$9.99',
      period: 'per month',
      features: [
        'Everything in Pro',
        'Team collaboration (up to 5 users)',
        'Custom categories',
        'Advanced reporting',
        'Dedicated account manager',
        'Phone support',
      ],
      cta: 'Try Free for 14 Days',
      popular: false,
    },
  ];

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow container mx-auto px-4 py-8">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Simple, Transparent Pricing
          </h1>
          <p className="text-xl text-gray-600 max-w-2xl mx-auto">
            Choose the plan that works best for you. All plans include a 14-day free trial.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          {plans.map((plan, index) => (
            <div
              key={index}
              className={`rounded-lg shadow-lg overflow-hidden ${
                plan.popular ? 'ring-2 ring-blue-500 relative' : 'border border-gray-200'
              }`}
            >
              {plan.popular && (
                <div className="bg-blue-500 text-white text-sm font-semibold text-center py-1">
                  MOST POPULAR
                </div>
              )}
              <div className="p-6">
                <h3 className="text-2xl font-bold text-gray-900 mb-2">{plan.name}</h3>
                <div className="mb-4">
                  <span className="text-4xl font-bold text-gray-900">{plan.price}</span>
                  <span className="text-gray-600">/{plan.period}</span>
                </div>
                <ul className="mb-6 space-y-3">
                  {plan.features.map((feature, featureIndex) => (
                    <li key={featureIndex} className="flex items-center">
                      <svg
                        className="h-5 w-5 text-green-500 mr-2"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          d="M5 13l4 4L19 7"
                        ></path>
                      </svg>
                      <span className="text-gray-600">{feature}</span>
                    </li>
                  ))}
                </ul>
                <button
                  className={`w-full py-2 px-4 rounded-md font-medium ${
                    plan.popular
                      ? 'bg-blue-600 text-white hover:bg-blue-700'
                      : 'bg-gray-100 text-gray-900 hover:bg-gray-200'
                  }`}
                >
                  {plan.cta}
                </button>
              </div>
            </div>
          ))}
        </div>

        <div className="mt-12 text-center">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Frequently Asked Questions</h2>
          <div className="max-w-3xl mx-auto text-left space-y-4">
            <div className="border-b border-gray-200 pb-4">
              <h3 className="text-lg font-semibold text-gray-900">Can I change plans later?</h3>
              <p className="text-gray-600">
                Yes, you can upgrade or downgrade your plan at any time. Your billing will be prorated
                accordingly.
              </p>
            </div>
            <div className="border-b border-gray-200 pb-4">
              <h3 className="text-lg font-semibold text-gray-900">What payment methods do you accept?</h3>
              <p className="text-gray-600">
                We accept all major credit cards including Visa, Mastercard, and American Express.
              </p>
            </div>
            <div className="border-b border-gray-200 pb-4">
              <h3 className="text-lg font-semibold text-gray-900">Do you offer discounts for students or non-profits?</h3>
              <p className="text-gray-600">
                Yes, we offer special pricing for students and non-profit organizations. Please contact
                our support team for more information.
              </p>
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}