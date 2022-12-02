import React from 'react';
import Business from '../img/business.png';
import Mechanical from '../img/mechanical.png';
import Electrical from '../img/electrical.png';

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
            <h2 className="h2 mb-4 text-xl font-semibold">Our teams</h2>
            <div>

              <h2 className=" h2 mb-4 text-xl text-red-500 font-semibold">Apply Now ></h2>
              
              </div>

          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto grid gap-6 md:grid-cols-2 lg:grid-cols-3 items-start md:max-w-2xl lg:max-w-none">

            {/* 1st item */}
            <div className="relative flex flex-col items-center p-6 bg-white rounded shadow-xl">
                        <img className="h-full w-full rounded-md" src={Mechanical}></img>

              <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">Mechanical</h4>
            </div>
            <div className="relative flex h-full flex-col items-center p-6 bg-white rounded shadow-xl">
                        <img className="h-full w-full rounded-md" src={Electrical}></img>

              <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">Electrical</h4>
            </div>
            <div className="relative h-full flex flex-col items-center p-6 bg-white rounded shadow-xl">
                        <img className="h-full w-full rounded-md" src={Business}></img>

              <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">Business</h4>
            </div>

            

          </div>

        </div>
      </div>
    </section>
  );
}

export default FeaturesBlocks;