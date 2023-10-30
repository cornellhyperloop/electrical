import React, { useState } from "react";
import HeroImage from "../img/logo_symbol.png";

import Header from "../partials/Header";
import FeaturesHome from "../partials/Features";
import Testimonials from "../partials/Testmonials";
import Newsletter from "../partials/Newsletter";
import Footer from "../partials/Footer";
import Banner from "../partials/Banner";
import Challenge from "../partials/Challenge";
import Business from "../img/business.png";
import Mechanical from "../img/mechanical.png";
import Electrical from "../img/electrical.png";

function Mechanical2() {
  return (
    <div className="flex flex-col min-h-screen overflow-hidden">
      {/*  Site header */}
      <Header />
      {/*  Page content */}
      <main className="flex-grow">
        {/*  Page sections */}
        {FeaturesBlocks()}
      </main>
      <Banner />

      {/*  Site footer */}
    </div>
  );
}

function FeaturesBlocks() {

  return (
    <section className="relative">
      {/* Section background (needs .relative class on parent and next sibling elements) */}
      <div
        className="absolute inset-0 bottom-1/2 md:mt-4 lg:mt-0  pointer-events-none"
        aria-hidden="true"
      ></div>

    


      <div className="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20" id="mechanical">

          {/* Section header */}
          <div className=" mx-auto flex justify-between text-center pb-8 md:pb-8">
            <h2 className="h3 mb-2 text-4xl font-bold text-red-700 font-semibold"> Mechanical Subteams</h2>
            <div></div>
          </div>



          <div className="mt-4"></div>
            {/* Tabs items */}
            <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-5 lg:col-span-6  md:mb-0 md:order-1">
              <div className="md:pr-4 lg:pr-12 xl:pr-16 bg-gray-50 p-3 rounded-sm ">
                <h3 className="h3 my-1 font-light text-xl text-red-700 font-semibold">Description</h3>
                <h3 className="h3 my-1 ">
                  The mechanical team is responsible for developing all
                  mechanical subsystems on the pod, including the chassis,
                  suspension, propulsion system, brakes, and fuselage.
                </h3>
                <h3 className="text-red-700 font-semibold h3 mt-8 mb-1 font-light text-xl">
                  Tools & Tech
                </h3>
                <h3 className="h3 my-1 ">
                  The pod designs employ a variety of manufacturing techniques,
                  including traditional machining, welding, CNC, 3D printing, and
                  carbon fiber composite structures.
                </h3>
              </div>{" "}
            </div>

            <div className="mt-4"></div>

          <div className="md:grid md:grid-cols-12 md:gap-6">
            {/* Content */}
            <div
              className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-7 lg:col-span-6"
              data-aos="fade-right"
            >
              <div className="md:pr-4  bg-gray-50 p-3 rounded-sm lg:pr-12 xl:pr-16 ">
                <h3 className="h3 my-1 font-light text-xl text-red-700 font-semibold">Structures</h3>
                <h3 className="h3 my-1 ">
                The Structures subteam is an interdisciplinary team open to taking on problems as they apply to the overall architecture of the pod, 
                from the chassis and shell to the cooling system and more. 
                This means revamping the whole chassis, the pod's skeleton, iteration to iteration,
                 which requires careful planning of the many subsystems and their placement. 
                 On top of that we must come up with new designs for the aeroshell to optimize both space and aerodynamics 
                 while fitting nicely with the pod, and we are currently still in the process of creating a tried and tested process
                  for the manufacture of a carbon-fiber shell of such a scale. 
                 
                </h3>
              </div>


              {/* Tabs buttons */}
            </div>

            <div
              className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-7 lg:col-span-6"
              data-aos="fade-right"
            >
              <div className="md:pr-4 bg-gray-50 p-3 rounded-sm lg:pr-12 xl:pr-16 ">
                <h3 className="h3 my-1 font-light text-xl text-red-700 font-semibold">Suspension</h3>
                <h3 className="h3 my-1 ">
                The magnetics subteam is in charge of the levitation, propulsion, and guidance systems of the pod. 
                 Our levitation system uses custom-made electromagnets that induce eddy currents in the track for levitation,
                  and our propulsion system relies on a linear induction motor to create a moving magnetic pole to attract
                   and repel the track as the pod travels. Our guidance system allows for control in the horizontal, 
                   roll, and yaw directions, and this year also allows for control in the vertical and pitch directions.
                    The magnetics team is very research-focused and brings together a lot of
                     novel technologies in order to make our pods' ambitious goals a reality.
                </h3>

              </div>


              {/* Tabs buttons */}
            </div>


            <div
              className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-7 lg:col-span-6"
              data-aos="fade-right"
            >
              <div className="md:pr-4 bg-gray-50 p-3 rounded-sm lg:pr-12 xl:pr-16  ">
                <h3 className="h3 my-1 font-light text-xl text-red-700 font-semibold">Cooling </h3>
                <h3 className="h3 my-1 ">
                The cooling subteam is currently working on developing a robust 
                  but simple cooling architecture for our batteries and BMS.
                   Future problems will include continued iteration of the chassis and shell, 
                   but also the expansion of our cooling system from just the batteries to other parts of the pod that will need it 
                   ,currently under the jurisdiction of other subteams but likely to be united under one cooling subsystem owned by structures.
                    In short, the structures subteam is a particularly multifaceted subteam here on Cornell Hyperloop, 
                    and a great team for learning the general architecture of the pod before delving into specifics. 

                </h3>

              </div>


              {/* Tabs buttons */}
            </div>

            <div
              className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-7 lg:col-span-6"
              data-aos="fade-right"
            >
              <div className="md:pr-4 bg-gray-50 p-3 rounded-sm lg:pr-12 xl:pr-16 ">

                <h3 className="h3 my-1 font-light text-xl text-red-700 font-semibold">Braking</h3>
                <h3 className="h3 my-1 ">
                  The braking subteam is responsible for the design, construction, and testing of two braking systems:
                   magnetic braking and pneumatic braking. 
                   Magnetic brakes employ electromagnets to generate eddy currents in the track,
                    creating resistance against the pod's motion.
                     The braking force increases with speed, making it effective at decelerating the pod from high velocities.
                      Pneumatic brakes utilize compressed air and pneumatic cylinders to activate frictional brake pads,
                       which make contact with the track and bring the pod to a complete halt. 
                       The braking team is actively engaged in researching and experimenting with various design possibilities, 
                       while also collaborating closely with other subteams to develop and test our electromagnets and pneumatic actuation systems.
                   Our collective efforts are dedicated to turning the highperloop concept into a reality.
                </h3>
              </div>


              {/* Tabs buttons */}
            </div>
          
          </div>


          {/* Items */}
        </div>
   
        {/* Items */}
      </div>
    </section>
  );
}
function Member({ src, title, subtitle }) {
  return (
    <div className="relative flex flex-col items-center mx-4 bg-white rounded ">
      <img
        className="h-44 w-44 rounded-md"
        src={require("../img/" + src).default}
      ></img>

      <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">
        {title}
      </h4>
      <h4 className="text-lg font-normal leading-snug tracking-tight mb-1 mt-1 self-start">
        {subtitle}
      </h4>
    </div>
  );
}
function HeroMembers(myRef) {
  const [videoModalOpen, setVideoModalOpen] = useState(false);

  return (
    <section className="relative max-h-screen">
      {/* Illustration behind hero content */}
      <div
        className="absolute left-1/2 transform -translate-x-1/2 bottom-0 pointer-events-none"
        aria-hidden="true"
      >
        <svg
          width="1360"
          height="578"
          viewBox="0 0 1360 578"
          xmlns="http://www.w3.org/2000/svg"
        >
          <defs>
            <linearGradient
              x1="50%"
              y1="0%"
              x2="50%"
              y2="100%"
              id="illustration-01"
            >
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
            <div
              className="relative flex justify-center mb-8 h-full"
              data-aos="zoom-y-out"
              data-aos-delay="450"
            >
              <div className="flex flex-col justify-center ">
                <div className=" w-screen items-center justify-center">
                  <img
                    className="mx-auto w-1/4 h-full"
                    src={HeroImage}
                    alt="Hero"
                  />
                </div>
                <svg
                  className="absolute inset-0 max-w-full mx-auto md:max-w-none h-auto"
                  width="768"
                  height="432"
                  viewBox="0 0 768 432"
                  xmlns="http://www.w3.org/2000/svg"
                  xmlnsXlink="http://www.w3.org/1999/xlink"
                ></svg>
              </div>
            </div>
          </div>
          <div className="text-center pb-12 md:pb-0">
            <h1
              className="text-5xl md:text-6xl font-extrabold mb-4"
              data-aos="zoom-y-out"
            >
              Mechanical
            </h1>
          </div>
        </div>
      </div>
    </section>
  );
}
export default Mechanical2;
