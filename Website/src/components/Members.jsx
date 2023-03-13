import React from 'react';

import Header from '../partials/Header';
import HeroMembers from '../partials/HeroMembers';
import FeaturesHome from '../partials/Features';
import Testimonials from '../partials/Testmonials';
import Newsletter from '../partials/Newsletter';
import Footer from '../partials/Footer';
import Banner from '../partials/Banner';
import Challenge from '../partials/Challenge';
import Business from '../img/business.png';
import Mechanical from '../img/mechanical.png';
import Electrical from '../img/electrical.png';

function Members() {
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
    var teammembers=[{name:"john doe",imageurl:"mechanical.png",title:"lead"}]
  return (
    <section className="relative">

      {/* Section background (needs .relative class on parent and next sibling elements) */}
      <div className="absolute inset-0 bottom-1/2 md:mt-4 lg:mt-0  pointer-events-none" aria-hidden="true"></div>

      <div className="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20">

          {/* Section header */}
          <div className=" mx-auto flex justify-between text-center pb-8 md:pb-8">
            <h2 className="h2 mb-4 text-xl font-semibold">Our teams</h2>
            <div>

              
              </div>

          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            { teammembers.map((item) => {
              return <Member src={item.imageurl} title={item.title} subtitle={item.name} />;
              }) }
            
          
          </div>

        </div>
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

export default Members;