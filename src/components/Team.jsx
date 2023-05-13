import React, {useState} from 'react';
import HeroImage from '../img/logo_symbol.png';

import Header from '../partials/Header';
import FeaturesHome from '../partials/Features';
import Testimonials from '../partials/Testmonials';
import Newsletter from '../partials/Newsletter';
import Footer from '../partials/Footer';
import Banner from '../partials/Banner';
import Challenge from '../partials/Challenge';
import Business from '../img/business.png';
import Mechanical from '../img/mechanical.png';
import Electrical from '../img/electrical.png';

function Team() {
  return (
    <div className="flex flex-col min-h-screen overflow-hidden">

      {/*  Site header */}
      <Header/>
      {/*  Page content */}
      <main className="flex-grow">

        {/*  Page sections */}
        <HeroMembers />
        {FeaturesBlocks()}
      </main>
      <Banner />
      
      {/*  Site footer */}

    </div>
  );
}

function FeaturesBlocks() {
    var teammembers=[{name:"john doe",imageurl:"mechanical.png",title:"lead"},{name:"john doe",imageurl:"mechanical.png",title:"lead"}]
  return (
    <section className="relative">

      {/* Section background (needs .relative class on parent and next sibling elements) */}
      <div className="absolute inset-0 bottom-1/2 md:mt-4 lg:mt-0  pointer-events-none" aria-hidden="true"></div>

      <div className="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20" id="mechanical">

          {/* Section header */}
          <div className=" mx-auto flex justify-between text-center pb-8 md:pb-8" >
            <h2 className="h2 mb-2 text-2xl font-bold" >Mechanical</h2>
            <div>

              
              </div>

          </div>
 <div className="md:grid md:grid-cols-12 md:gap-6">

            {/* Content */}
            <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-7 lg:col-span-6" data-aos="fade-right">
              <div className="md:pr-4 bg-gray-50 p-3 rounded-sm lg:pr-12 xl:pr-16 ">
                <h3 className="h3 mb-4 font-light text-3xl">Subteams</h3>
                <h3 className="h3 my-1 font-light text-xl">Magnetics</h3>
                <h3 className="h3 my-1 ">The magnetics team works on our propulsion and levitation systems.</h3>
                <h3 className="h3 mt-8 mb-1 font-light text-xl">Structures</h3>
                <h3 className="h3 my-1 ">The structures team focuses on the pod's cooling and systems integration and chassis design.</h3>
                <h3 className="h3 mt-8 mb-1 font-light text-xl">Braking</h3>
                <h3 className="h3 my-1 ">The braking team specializes within the mechanical and magnetic braking systems.</h3>
              </div>
              {/* Tabs buttons */}
              
            </div>

            {/* Tabs items */}
            <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-5 lg:col-span-6  md:mb-0 md:order-1" >
 <div className="md:pr-4 lg:pr-12 xl:pr-16 bg-gray-50 p-3 rounded-sm ">
                <h3 className="h3 my-1 font-light text-xl">Description</h3>
                <h3 className="h3 my-1 ">The mechanical team is responsible for developing all mechanical subsystems on the pod, including the chassis, suspension, propulsion system, brakes, and levitation.</h3>
                              <h3 className="h3 mt-8 mb-1 font-light text-xl">Tools & Tech</h3>
                <h3 className="h3 my-1 ">The pod designs employ a variety of manufacturing techniques, inluding traditional machining, welding, CNC, 3D printing, and carbon fiber composite structures.</h3>

              </div>            </div >

          </div >

         <div className="pt-20 mx-auto flex justify-between text-center pb-4" id="electrical">
            <h2 className="h2 mb-2 text-2xl font-bold">Electrical</h2>
            <div>

              
              </div>

          </div>
 <div className="md:grid md:grid-cols-12 md:gap-6">

            {/* Content */}
            <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-7 lg:col-span-6 md:mt-6 pb-20" data-aos="fade-right">
              <div className="md:pr-4 bg-gray-50 p-3 rounded-sm lg:pr-12 xl:pr-16 mb-8">
                <h3 className="h3 mb-4 font-light text-3xl">Subteams</h3>
                <h3 className="h3 my-1 font-light text-xl">Power Systems</h3>
                <h3 className="h3 my-1 ">The Power Systems team is in charge of all the electrical components.</h3>
                <h3 className="h3 mt-8 mb-1 font-light text-xl">Computing Systems</h3>
                <h3 className="h3 my-1 ">The Computing Systems team is in charge of all the embedded software.</h3>
                <h3 className="h3 mt-8 mb-1 font-light text-xl">GUI</h3>
                <h3 className="h3 my-1 ">The GUI team is in charge of the GUI and the website.</h3>
              </div>
              {/* Tabs buttons */}
              
            </div>

            {/* Tabs items */}
            <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-5 lg:col-span-6 mb-8 md:mb-0 md:order-1" >
 <div className="md:pr-4 lg:pr-12 xl:pr-16 bg-gray-50 p-3 rounded-sm  mb-8">
                <h3 className="h3 my-1 font-light text-xl">Description</h3>
                <h3 className="h3 my-1 ">The main goal of the team is to construct and maintain the electrical system. This includes the batteries, motors, and sensors. We are also in charge of developing software that enables the pod to be fully autonomous. Lastly, we maintain an electrical website to showcase the team. The team is currently building a battery pack, as well as set up several sensor sets along with the internal pod network.</h3>
                              <h3 className="h3 mt-8 mb-1 font-light text-xl">Tools & Tech</h3>
                <h3 className="h3 my-1 ">The team uses a variety of tools, since we are involved in both the hardware and software. On the hardware side, there's KiCAD and physical benches to develop the circuits. On the software side, we use Python to develop our embedded systems, as well as a networking protocol called ZCM.</h3>

              </div>            </div >

          </div >
          {/* Items */}
          

        </div>
           <div className=" mx-auto flex justify-center w-full text-center pb-8 md:pb-8" id="business">
            <h2 className="h2 mb-2 text-2xl font-bold">Business</h2>
            <div>

              
              </div>

          </div>
 <div className="flex flex-row items-center">

            {/* Content */}
           
            {/* Tabs items */}
            <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-5 lg:col-span-6 mb-8 md:mb-0 md:order-1" >
 <div className="md:pr-4 lg:pr-12 xl:pr-16 bg-gray-50 p-3 rounded-sm  mb-8">
                <h3 className="h3 my-1 font-light text-xl">Description</h3>
                <h3 className="h3 my-1 ">The main goal of the business team is to support all of Hyperloop's business-related initiatives. This includes budgeting, organization, sponsorship outreach, social media, and marketing - including our website!</h3>
                              <h3 className="h3 mt-8 mb-1 font-light text-xl">Tools & Tech</h3>
                <h3 className="h3 my-1 ">The business team uses Adobe Creative Cloud to produce marketing materials for social media sites such as Instagram, Twitter, and LinkedIn. We also use Excel for budgeting spreadsheets.</h3>

            </div>            </div >
          
          </div >
          {/* Items */}
          

        
      </div>
    </section>
  );
}
function Member({ src,title,subtitle }) {
  return (
    <div className="relative flex flex-col items-center mx-4 bg-white rounded ">
      <img className="h-44 w-44 rounded-md" src={require("../img/"+src).default}></img>

      <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">{title}</h4>
      <h4 className="text-lg font-normal leading-snug tracking-tight mb-1 mt-1 self-start">{subtitle}</h4>

    </div>
  );
}
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
            <h1 className="text-5xl md:text-6xl font-extrabold leading-tighter tracking-tighter mb-4" data-aos="zoom-y-out">Our Teams</h1>
            
          </div>


        </div>

      </div>
    </section>
  );
}
export default Team;