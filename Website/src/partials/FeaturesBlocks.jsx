import React from 'react';
import Business from '../img/IMG_0078.JPG';
import Mechanical from '../img/mechanical.jpg';
import Electrical from '../img/img3.jpg';

function FeaturesBlocks() {
  return (
    <section className="relative">

      {/* Section background (needs .relative class on parent and next sibling elements) */}
      <div className="absolute inset-0 bottom-1/2 md:mt-4 lg:mt-0 bg-gray-200 pointer-events-none" aria-hidden="true"></div>
s
      <div className="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20">

          {/* Section header */}
          <div className=" mx-auto flex justify-between text-center pb-8 md:pb-8">
            <h2 className="h2 mb-4 text-xl font-semibold">Our Teams</h2>
            <div>

              <a className=" h2 mb-4 text-xl text-red-700 font-semibold hover:underline" href="/apply">Apply Now </a>
              
              </div>

          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto grid gap-6 md:grid-cols-2 lg:grid-cols-3 items-start md:max-w-2xl lg:max-w-none">

            {/* 1st item */}
            <a href="/team#mechanical" className="hover:opacity-90 relative flex flex-col items-center p-6 bg-white rounded shadow-xl">
                        <img className=" w-full rounded-md object-cover h-64" src={Mechanical}></img>

              <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">Mechanical</h4>
            </a>
            
          <a href="/team#business" className=" hover:opacity-90  relative h-full flex flex-col items-center p-6 bg-white rounded shadow-xl">
                        <img className="h-64 w-full object-cover rounded-md" src={Business}></img>

              <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">Business</h4>
            </a>
          <a href="/team#electrical" className="hover:opacity-90  relative flex h-full flex-col items-center p-6 bg-white rounded shadow-xl">
                        <img className="h-64 w-full rounded-md object-cover" src={Electrical}></img>

              <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">Electrical</h4>
            </a>
            

          </div>

        </div>
      </div>
    </section>
  );
}

export default FeaturesBlocks;