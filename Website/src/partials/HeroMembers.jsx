import React, { useState } from 'react';
import Modal from '../utils/Modal';

import HeroImage from '../img/logo_symbol.png';

function HeroMembers(myRef) {

  const [videoModalOpen, setVideoModalOpen] = useState(false);

  return (
    <section className="relative max-h-screen" >

      {/* Illustration behind hero content */}
      <div className="absolute left-1/2 transform -translate-x-1/2 bottom-0 pointer-events-none" aria-hidden="true">
        <svg width="1360" height="578" viewBox="0 0 1360 578" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient x1="50%" y1="0%" x2="50%" y2="100%" id="illustration-01">
              <stop stopColor="#FFF" offset="0%" />
              <stop stopColor="#EAEAEA" offset="77.402%" />
              <stop stopColor="#DFDFDF" offset="100%" />
            </linearGradient>
          </defs>
          <g fill="url(#illustration-01)" fillRule="evenodd">
            <circle cx="1232" cy="128" r="128" />
            <circle cx="155" cy="443" r="64" />
          </g>
        </svg>
      </div>

      <div className="max-w-6xl mx-auto px-4 sm:px-6">

        {/* Hero content */}
        <div className="pt-32 pb-12 md:pt-36 md:pb-20">

          {/* Section header */}
          
          {/* Hero image */}
          <div>
            <div className="relative flex justify-center mb-8 h-full" data-aos="zoom-y-out" data-aos-delay="450">
              <div className="flex flex-col justify-center ">
                <div className=' w-screen items-center justify-center'>
                  <img className="mx-auto w-1/4 h-full" src={HeroImage} alt="Hero" />
                  </div>
                <svg className="absolute inset-0 max-w-full mx-auto md:max-w-none h-auto" width="768" height="432" viewBox="0 0 768 432" xmlns="http://www.w3.org/2000/svg" xmlnsXlink="http://www.w3.org/1999/xlink">
                 
                </svg>
              </div>
             
            </div>

         

          </div>
          <div className="text-center pb-12 md:pb-0">
            <h1 className="text-5xl md:text-6xl font-extrabold leading-tighter tracking-tighter mb-4" data-aos="zoom-y-out">Our Members</h1>
            
          </div>


        </div>

      </div>
    </section>
  );
}

export default HeroMembers;