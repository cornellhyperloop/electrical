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
          <div className=" mx-auto flex justify-between text-center pb-8 md:pb-8">
            <h2 className="h2 mb-2 text-2xl font-bold">Mechanical</h2>
            <div>

              
              </div>

          </div>
 <div className="md:grid md:grid-cols-12 md:gap-6">

            {/* Content */}
            <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-7 lg:col-span-6 md:mt-6 pb-20" data-aos="fade-right">
              <div className="md:pr-4 bg-gray-50 p-3 rounded-sm lg:pr-12 xl:pr-16 mb-8">
                <h3 className="h3 mb-3 font-bold">The Goal</h3>
                <p className="text-xl text-gray-600">Every few centuries, something comes along that revolutionizes the world - something that, once integrated with society, leaves us wondering how we had lived without it. The examples are plenty: fire, the wheel, the ship, the train, the car, the plane. Now we find ourselves on the brink of another such innovation: the Hyperloop. Cornell Hyperloop seeks to spearhead the revolution in transportation technology.</p>
              </div>
              {/* Tabs buttons */}
              
            </div>

            {/* Tabs items */}
            <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-5 lg:col-span-6 mb-8 md:mb-0 md:order-1" >
 <div className="md:pr-4 lg:pr-12 xl:pr-16 bg-gray-50 p-3 rounded-sm  mb-8">
                <h3 className="h3 mb-3 font-bold">The Goal</h3>
                <p className="text-xl text-gray-600">Every few centuries, something comes along that revolutionizes the world - something that, once integrated with society, leaves us wondering how we had lived without it. The examples are plenty: fire, the wheel, the ship, the train, the car, the plane. Now we find ourselves on the brink of another such innovation: the Hyperloop. Cornell Hyperloop seeks to spearhead the revolution in transportation technology.</p>
              </div>            </div >

          </div >
          {/* Items */}
          

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
          
          <div className="flex flex-wrap justify-center">
  <h1 className="mx-auto w-full md:w-1/2 text-4xl md:text-5xl font-extrabold leading-tighter tracking-tighter mb-4 py-2 px-4" data-aos="zoom-y-out">
    Help Support the Future of Transportation
  </h1>
</div>

      
          <div className=' w-screen flex justify-center'>
                        <button className="hover:opacity-90 hover:bg-red-400 absolute  top-full mb-20 flex items-center transform -translate-y-1/2 bg-red-400 rounded-md font-medium group p-4 shadow-lg" onClick={(e) => { e.preventDefault();   const section = document.querySelector( '#goals' );
  section.scrollIntoView( { behavior: 'smooth', block: 'start' } );
 }} aria-controls="modal">
               
                <span className="mx-2 text-white">Donate now!</span>
            </button>
            </div>


        </div>

      </div>
    </section>
  );
}
export default Donate;