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
import powershot1 from "../img/MechanicalTeamImgs/image.png";
import powershot2 from "../img/MechanicalTeamImgs/smartppl.png";


function Buisness2() {
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
            <h2 className="h3 mb-2 text-4xl font-bold text-red-700 font-semibold"> Business Subteams</h2>
            <div></div>
          </div>



          <div className="mt-4"></div>
          {/* Tabs items */}
          <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-5 lg:col-span-6  md:mb-0 md:order-1">
            <div className="md:pr-4 lg:pr-12 xl:pr-16 bg-gray-50 p-3 rounded-sm ">
              <h3 className="h3 my-1 font-light text-xl text-red-700 font-semibold">Description</h3>
              <h3 className="h3 my-1 ">
                The business subteam is in charge of Marketing, Operations, and Development.
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
                <h3 className="h3 my-1 font-light text-xl text-red-700 font-semibold">Operations Team</h3>
                <h3 className="h3 my-1 ">
                  The operations subteam handles all of Cornell Hyperloop's finances.
                  Operations closely monitors income and spending while also performing monthly account verifications for audits.
                  Operations is also responsible for competition planning,
                  and is currently working on facilitating this summer's Hyperloop Global Conference in Canada.


                </h3>
              </div>


              {/* Tabs buttons */}
            </div>

            <div
              className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-7 lg:col-span-6"
              data-aos="fade-right"
            >
              <div className="md:pr-4 bg-gray-50 p-3 rounded-sm lg:pr-12 xl:pr-16 ">
                <h3 className="h3 my-1 font-light text-xl text-red-700 font-semibold">Development Team</h3>
                <h3 className="h3 my-1 ">
                  The development subteam fuels all of Cornell Hyperloop's outreach,
                  sponsorship acquisition, and fundraising. Development's recent projects include creating an updated sponsorship packet,
                  facilitating crowdfunding, and maintaining connections with our extensive network of alumni.
                </h3>

              </div>


              {/* Tabs buttons */}
            </div>


            {/* Tabs buttons */}


            <div
              className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-7 lg:col-span-6"
              data-aos="fade-right"
            >
              <div className="md:pr-4 bg-gray-50 p-3 rounded-sm lg:pr-12 xl:pr-16 ">

                <h3 className="h3 my-1 font-light text-xl text-red-700 font-semibold">Marketing</h3>
                <h3 className="h3 my-1 ">
                  The marketing subteam is the artistic soul of Cornell Hyperloop.
                  Marketing designs a wide variety of visuals for the team,
                  ranging from professional logos to creative concept art.
                  Marketing is also responsible for creating every semester's new team merchandise,
                  as well as maintaining of Cornell Hyperloop's social media accounts.

                </h3>
              </div>


              {/* Tabs buttons */}
            </div>

          </div>


          {/* Items */}
        </div>

        {/* Items */}
      </div>

      <section className="py-16">
        <div className="container mx-auto px-4">
          <h2 className="text-2xl font-semibold mb-4">Photo Gallery</h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {/* Add your gallery images here */}
            <div className="rounded-lg p-4 bg-white">
              <video controls autoplay loop muted playsInline>
                <source src="videos/crowdfunding.mp4" type="video/mp4"></source>
              </video>
            </div>
            <div className="rounded-lg p-4 bg-white">
              <img
                src={powershot2}
                alt="Gallery Image 3"
                className="w-full h-auto"  // You can adjust these values
                style={{ width: '100%', height: 'auto' }} // You can also use inline CSS
              />
            </div>
            {/* Add more images as needed */}
          </div>
        </div>
      </section>
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
export default Buisness2;
