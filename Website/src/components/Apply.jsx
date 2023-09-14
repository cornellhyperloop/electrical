import React, { useState, useEffect } from "react";
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
import "../Timeline.css";
import OldTeam from "../img/oldteam.png";

function Apply() {
  return (
    <div className="flex flex-col min-h-screen overflow-hidden">
      {/*  Site header */}
      <Header />
      {/*  Page content */}
      <main className="flex-grow flex-shrink-0">
        {/*  Page sections */}
        <HeroMembers />
        <Timeline />
        <WhoWeLookFor />
      </main>
      <Banner />
      <FeaturesBlocks />
      {/*  Site footer */}
    </div>
  );
}

function HeroMembers() {
  const [videoModalOpen, setVideoModalOpen] = useState(false);

  return (
    <section className="relative max-h-screen">
      {/* Illustration behind hero content */}
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        {/* Hero content */}
        <div className="pt-32 pb-12 md:pt-36 md:pb-2">
          {/* Section header */}
          <div className="flex flex-col md:flex-row justify-center items-center">
            <h1 className="text-4xl md:text-6xl font-extrabold tracking-tight text-gray-900">
              Join Cornell <span className="text-red-700"> Hyperloop </span>
            </h1>
          </div>
          {/* Hero image */}
          <div className="flex justify-center pt-6">
            <img src={HeroImage} alt="Hero Image" className="w-64" />
          </div>

          <div className="text-center pb-12 md:pb-0 z-100">
            <h2 className="text-2xl md:text-4xl font-extrabold tracking-tight text-gray-900 pt-8">
              Build the Future of Transportation
            </h2>
            <p className="text-xl md:text-2xl leading-relaxed tracking-wide text-gray-600 pt-6">
              Cornell Hyperloop is an engineering project team dedicated to
              contributing to the development of Hyperloop technology. We are
              always looking for talented and ambitious students to join us and
              help build the future of transportation. Our team is open to
              students from all majors and backgrounds.
            </p>
          </div>
        </div>
      </div>
      <div
        className="absolute left-1/2 transform z-0 -translate-x-1/2 bottom-0 pointer-events-none"
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
              z="0"
              y1="0%"
              x2="50%"
              y2="100%"
              id="illustration-01"
            >
              <stop stopColor="#FFF" offset="0%" />
              <stop stopColor="#EAEAEA" offset="72.402%" />
              <stop stopColor="#DFDFDF" offset="100%" />
            </linearGradient>
          </defs>
          <g fill="url(#illustration-01)" fillRule="evenodd">
            <cirlce cx="1000" cy="200" r="128" />
            <cirlce cx="431" cy="443" r="128" />
          </g>
        </svg>
      </div>
    </section>
  );
}

function Timeline() {
  return (
    <div>
      <div className="timeline-bar"></div>
      <div className="timeline-container">
        <div className="timeline-bar"></div>
        <div className="timeline">
          <div className="timeline-item">
            <div className="timeline-date">August 20th</div>
            <div className="timeline-content">
              <h3 className="timeline-title">Project Team Announcement</h3>
              <p className="timeline-description">
                Openings will be announced for each one of our subteams
                recruiting.
              </p>
            </div>
          </div>
          <div className="timeline-item">
            <div className="timeline-date">August 21st - September 21st</div>
            <div className="timeline-content">
              <h3 className="timeline-title">Application Period</h3>
              <p className="timeline-description">
                Applications will be accepted during this time period.
              </p>
            </div>
          </div>
          <div className="timeline-item">
            <div className="timeline-date">September 21st-27th</div>
            <div className="timeline-content">
              <h3 className="timeline-title">Interviews</h3>
              <p className="timeline-description">
                Selected candidates will be invited for an interview.
              </p>
            </div>
          </div>
          <div className="timeline-item">
            <div className="timeline-date">Sept 28th-30th</div>
            <div className="timeline-content">
              <h3 className="timeline-title">Selection</h3>
              <p className="timeline-description">
                Selected candidates will be notified of their selection.
              </p>
            </div>
          </div>
        </div>
      </div>
      <div className="text-center pb-12 z-100 ">
        <a
          href="/team#mechanical"
          className="bg-red-700 text-white font-bold py-4 px-8 rounded-full mt-12 inline-block"
          style={{ boxShadow: "inset 0px 0px 10px 3px rgba(255,0,0,0.7)" }}
        >
          Apply Now
        </a>
      </div>
    </div>
  );
}

function WhoWeLookFor() {
  return (
    <div className="flex flex-col md:flex-row justify-center items-center md:gap-8">
      <img
        src={OldTeam}
        alt="Old Team"
        className="w-1/2 md:pr-4 md:pl-8 md:mt-0 mt-8"
        style={{ padding: "2rem" }}
      />
      <div className="md:pl-16">
        <h1 className="text-4xl font-bold mb-4">Who We Look For</h1>
        <p className="text-lg leading-relaxed mb-8" style={{ padding: "2rem" }}>
          Cornell Hyperloop has a position for everyone. We are broken down into
          three teams, including a total of seven “sub-teams,” each focusing on
          a specific component of our work. Each team recruits undergraduate
          students of all years from any major that can demonstrate the skills
          needed to succeed on that team.
        </p>
      </div>
    </div>
  );
}

function FeaturesBlocks() {
  return (
    <section className="relative">
      {/* Section background (needs .relative class on parent and next sibling elements) */}
      <div
        className="absolute inset-0 bottom-1/2 md:mt-4 lg:mt-0 bg-gray-200 pointer-events-none"
        aria-hidden="true"
      ></div>
      s
      <div className="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20">
          {/* Section header */}
          <div className=" mx-auto flex justify-between text-center pb-8 md:pb-8">
            <h2 className="h2 mb-4 text-xl font-semibold">Our Teams</h2>
            <div>
              <a className=" h2 mb-4 text-xl text-red-700 font-semibold">
                {" "}
                Learn More about Our Teams!{" "}
              </a>
            </div>
          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto grid gap-6 md:grid-cols-2 lg:grid-cols-3 items-start md:max-w-2xl lg:max-w-none">
            {/* 1st item */}
            <a
              href="/team#mechanical"
              className="hover:opacity-90 relative flex flex-col items-center p-6 bg-white rounded shadow-xl"
            >
              <img
                className=" w-full rounded-md object-cover h-64"
                src={Mechanical}
              ></img>

              <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">
                Mechanical
              </h4>
            </a>

            <a
              href="/team#business"
              className=" hover:opacity-90  relative h-full flex flex-col items-center p-6 bg-white rounded shadow-xl"
            >
              <img
                className="h-64 w-full object-cover rounded-md"
                src={Business}
              ></img>

              <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">
                Business
              </h4>
            </a>
            <a
              href="/team#electrical"
              className="hover:opacity-90  relative flex h-full flex-col items-center p-6 bg-white rounded shadow-xl"
            >
              <img
                className="h-64 w-full rounded-md object-cover"
                src={Electrical}
              ></img>

              <h4 className="text-xl font-bold leading-snug tracking-tight mb-1 mt-4 self-start">
                Electrical
              </h4>
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}

export default Apply;
