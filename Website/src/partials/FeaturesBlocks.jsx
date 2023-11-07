import React from 'react';
import Business from '../img/IMG_0078.JPG';
import Mechanical from '../img/mechanical.jpg';
import Electrical from '../img/img3.jpg';

import { Link} from 'react-router-dom'

function FeaturesBlocks() {

  const scrollToTopAndNavigate = (event, contentPath) => {
    event.preventDefault(); // Prevent the default behavior of links
    window.scrollTo({ top: 0, behavior: 'smooth' }); // Scroll to the top
    setTimeout(() => {
      window.location.href = contentPath; // Navigate after scrolling
    }, 500); // Adjust the delay as needed
  };
  
  return (
    <section className="relative">
      {/* Section background (needs .relative class on parent and next sibling elements) */}
      <div className="absolute inset-0 bottom-1/2 md:mt-4 lg:mt-0 bg-gray-200 pointer-events-none" aria-hidden="true"></div>

      <div className="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20">
          {/* Section header */}
          <div className="mx-auto flex justify-between text-center pb-8 md:pb-8">
            <h2 className="h2 mb-4 text-xl font-semibold">Our Teams</h2>
            <div>
              <a className="h2 mb-4 text-xl text-red-700 font-semibold hover:underline" href="https://forms.gle/55mEu3RbK8n9cHxf9">Apply Now</a>
            </div>
          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto grid gap-6 md:grid-cols-2 lg:grid-cols-3 items-start md:max-w-2xl lg:max-w-none">
            {/* 1st item */}
            <Link to="/mechanical" onClick={(e) => scrollToTopAndNavigate(e, '/mechanical')} className="hover:opacity-90 relative flex flex-col items-center p-6 bg-white rounded shadow-xl">
              <img className="w-full rounded-md object-cover h-64" src={Mechanical} alt="Mechanical Team" />
              <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">Mechanical</h4>
            </Link>
            <Link to="/business" onClick={(e) => scrollToTopAndNavigate(e, '/business')} className="hover:opacity-90 relative h-full flex flex-col items-center p-6 bg-white rounded shadow-xl">
              <img className="h-64 w-full object-cover rounded-md" src={Business} alt="Business Team" />
              <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">Business</h4>
            </Link>
            <Link to="/electrical" onClick={(e) => scrollToTopAndNavigate(e, '/electrical')} className="hover:opacity-90 relative flex h-full flex-col items-center p-6 bg-white rounded shadow-xl">
              <img className="h-64 w-full rounded-md object-cover" src={Electrical} alt="Electrical Team" />
              <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">Electrical</h4>
            </Link>
          </div>
        </div>
      </div>
    </section>
  );
}

export default FeaturesBlocks;
