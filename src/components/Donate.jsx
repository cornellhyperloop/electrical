import React, {useState} from 'react';
import HeroImage from '../img/team.jpeg';

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

function Donate() {
  return (
    <div className="flex flex-col min-h-screen overflow-hidden justify-center items-center sm:px-4">

      {/*  Site header */}
      <Header/>
      {/*  Page content */}
      <main className="flex-grow">

        {/*  Page sections */}
        <HeroMembers />
        <FeaturesBlocks />
        <Sponsors/>
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
s
      <div className="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20">

          {/* Section header */}
            <h2 className="h2 mb-2 text-4xl md:text-5xl w-full text-center font-bold pb-20">Choose your package</h2>
          <h2 className="h2 mb-2 text-xl w-full text-center  pb-20">Ready to donate? We have multiple tier packages available</h2>
            <div className='flex justify-center'>
                        <a href="https://givingday.cornell.edu/campaigns/cu-hyperloop" className="hover:opacity-90 hover:bg-red-400   top-full mb-20 flex items-center bg-red-400 rounded-md font-medium  p-4 shadow-lg"  aria-controls="modal">
               
                <span className="mx-2 text-white">Donate now!</span>
            </a>
          </div>
                    <h2 className="h2 mb-2 text-xl w-full text-center  pb-20">Questions? Feel free to <a className='underline cursor-pointer hover:opacity-60' href="mailto:cornellhyperloop@gmail.com">email us</a> </h2>

          {/* Items */}
          

        </div>
      </div>
    </section>
  );
}

function Sponsors() {
    var teammembers=[{name:"john doe",imageurl:"mechanical.png",title:"lead"}]
  return (
    <section className="relative bg-gray-50">

      {/* Section background (needs .relative class on parent and next sibling elements) */}
      <div className="absolute inset-0 bottom-1/2 md:mt-4 lg:mt-0  pointer-events-none" aria-hidden="true"></div>
s
      <div className="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20">

          {/* Section header */}
            <h2 className="h2 mb-2 text-4xl md:text-5xl w-full text-center font-bold pb-20">Thanks to our sponsors</h2>


<div className=" mx-auto flex flex-wrap flex-row gap-6 w-3/4 items-center justify-center  lg:max-w-none">
      <img className="h-36 object-cover w-36 rounded-md contain" src={require("../img/headshots/3erp.png").default}></img>


          
          </div>
          {/* Items */}
          

        </div>
      </div>
    </section>
  );
}

function Member({ src, title, subtitle }) {
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
    <section className="relative h-screen w-screen bg-red" >

      {/* Illustration behind hero content */}
     
      <img className="h-screen absolute  mx-auto  w-full  opacity-40 object-cover" src={HeroImage} alt="Hero" />
      <div className="absolute w-screen z-100 mx-auto px-4 sm:px-6 bg-red50">

        {/* Hero content */}
        <div className="pt-32 pb-12 md:pt-36 md:pb-20">

          {/* Section header */}
          
          {/* Hero image */}
          <div>
            <div className=" z-100 absolute flex justify-center mb-8 h-full" data-aos="zoom-y-out" data-aos-delay="450">
              <div className="flex flex-col justify-center ">
                
                <svg className="absolute inset-0 max-w-full mx-auto md:max-w-none h-auto" width="768" height="432" viewBox="0 0 768 432" xmlns="http://www.w3.org/2000/svg" xmlnsXlink="http://www.w3.org/1999/xlink">
                 
                </svg>
              </div>
             
            </div>

         

          </div>
          
          <div className="flex w-screen flex-wrap justify-center">
  <h1 className="mx-auto w-full md:w-1/2 text-4xl md:text-5xl font-extrabold text-center leading-tighter tracking-tighter mb-4 py-2" data-aos="zoom-y-out">
    Help Support the Future of Transportation
  </h1>
</div>

      
          <div className=' w-screen flex justify-center'>
                        <a href="https://givingday.cornell.edu/campaigns/cu-hyperloop" className="hover:opacity-90 hover:bg-red-400 absolute  top-full mb-20 flex items-center transform -translate-y-1/2 bg-red-400 rounded-md font-medium group p-4 shadow-lg"  aria-controls="modal">
               
                <span className="mx-2 text-white">Donate now!</span>
            </a>
            </div>


        </div>

      </div>
    </section>
  );
}
export default Donate;