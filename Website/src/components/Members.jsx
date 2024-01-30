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

  var faculty = [{ name: "Rick Geddes", imageurl: "GeddesRick.jpg", title: "Faculty Co-Advisor", rurl: "https://www.linkedin.com/in/rick-geddes-5134475/" },
  { name: "Zhiting Tian", imageurl: "TianZhiting.jpg", title: "Faculty Co-Advisor", rurl: "https://www.linkedin.com/in/zhiting-tian-3103179/" }]
  var leads = [
    { name: "Vanshaj Jain", imageurl: "vanshajjain.jpg", title: "Electrical Lead", rurl: "https://www.linkedin.com/in/vanshaj24/" },
  { name: "Jonathan Chen", imageurl: "jonathanchen.jpg", title: "Business Lead", rurl: "https://www.linkedin.com/in/jonathan-chen-377a261b6/" },
  { name: "Nikita Dolgopolov", imageurl: "nikitadolgopolov.jpg", title: "Mechanical Lead", rurl: "https://www.linkedin.com/in/nikita-dolgopolov/" },
  { name: "David Ovetsky", imageurl: "davidovetsky.jpg", title: "Structures Lead", rurl: "https://www.linkedin.com/in/david-ovetsky/" },
  { name: "Mark Edwards", imageurl: "markedwards.jpg", title: "Magnetics Lead", rurl: "https://www.linkedin.com/in/markvedwards02/" },
  { name: "Moez Amini", imageurl: "moezamini.jpg", title: "Braking Lead", rurl: "https://www.linkedin.com/in/moezamini/" },
  { name: "Daniel Akinwale", imageurl: "danielakinwale.jpg", title: "Composites Lead", rurl: "https://www.linkedin.com/in/daniel-akinwale-894297202/" },
  { name: "Sal Ciminello", imageurl: "salciminello.jpg", title: "Prototyping Lead", rurl: "https://www.linkedin.com/in/sal-ciminello-863471255/" },
  { name: "Berk Gokmen", imageurl: "berkgokmen.jpg", title: "Power Systems Lead", rurl: "https://www.linkedin.com/in/berk-gokmen/" },
  { name: "David Lilienfeld", imageurl: "davidlilienfeld.jpg", title: "Computing Systems Lead", rurl: "https://www.linkedin.com/in/david-lilienfeld-aa7162133/" },
  { name: "Aislinn Ennis", imageurl: "AislinnEnnis.jpg", title: "UI Lead", rurl: "https://www.linkedin.com/in/aislinn-ennis/" },
  { name: "John Goepfert", imageurl: "johngoepfort.jpg", title: "Operations Lead", rurl: "https://www.linkedin.com/in/john-goepfert/" },
  { name: "Vasu Patel", imageurl: "vasupatel.jpg", title: "Business Dev Lead", rurl: "https://www.linkedin.com/in/patelv1/" },
  { name: "Luke Shao", imageurl: "banana.jpeg", title: "Marketing Lead", rurl: "https://www.linkedin.com/in/luke-shao/" },
  { name: "Stephen Chien", imageurl: "apple.jpeg", title: "Web Lead", rurl: "https://www.linkedin.com/in/stephenlchien/" },



]

  var gui = [
    { name: "Devika Krishna", imageurl: "devikakrishna.png", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Patrick Choo", imageurl: "banana.jpeg",  rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Aislinn Ennis", imageurl: "aislinnennis.jpg",  rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Brandon Lerit", imageurl: "brandonlerit.jpg",  rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Max Farma", imageurl: "maxfarma.jpg",  rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },

  ]

  var powersystems = [
    { name: "Schuyler Seyram", imageurl: "devikakrishna.png", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Steven Wei Chen", imageurl: "banana.jpeg",  rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Lalo Esparza", imageurl: "aislinnennis.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Max Trager", imageurl: "brandonlerit.jpg",  rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Jenna Kafrawi", imageurl: "maxfarma.jpg",  rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Ivan Huang", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Xueqing Tsang", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" }
  ]


  var computing = [
    { name: "Anoushka Kabra", imageurl: "devikakrishna.png", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Ashley Heckman", imageurl: "banana.jpeg",  rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name:"David Lilienfeld", imageurl: "aislinnennis.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Yaqi Gao", imageurl: "brandonlerit.jpg",  rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Levi Zeng", imageurl: "maxfarma.jpg",  rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Shefali Awasthi", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Zarif Karim", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Neera Kapoor", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name:"Aiman Mobhani", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" }
  ]


  var magnetic = [

    { name: "Nikita Dolgopolov", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Rushil Choudary", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Verena Gonzalez", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },

  ]


  var braking = [

    { name: "Nikita Dolgopolov", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Rushil Choudary", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Verena Gonzalez", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },

  ]


  var structures = [

    { name: "Nikita Dolgopolov", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Rushil Choudary", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Verena Gonzalez", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },

  ]

  var business = [

    { name: "Tyler Angelica", imageurl: "zarifkarim.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Jonathan Chen", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Luke Shao", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Elizabeth Song", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Aidan Shor", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Ryan Graziano", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Jason Ng", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Vasu Patel", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "John Goepfort", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" }


  ]



  return (
    <section className="relative">

      {/* Section background (needs .relative class on parent and next sibling elements) */}
      <div className="absolute inset-0 bottom-1/2 md:mt-4 lg:mt-0  pointer-events-none" aria-hidden="true"></div>

      <div className="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div className="py-12 md:py-20">

          {/* Section header */}
          <div className=" mx-auto flex justify-between text-center pb-4 md:pb-4">
            <h2 className="h2 mb-4 text-3xl font-semibold">Faculty</h2>


          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            {faculty.map((item) => {
              return <Member src={item.imageurl} title={item.title} subtitle={item.name} rurl={item.rurl} />;
            })}


          </div>
          <div className=" mx-auto flex justify-between text-center pt-4 pb-4 md:pb-4">
            <h2 className="h2 mb-4 text-3xl font-semibold">Leads</h2>


          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            {leads.map((item) => {
              return <Member src={item.imageurl} title={item.title} subtitle={item.name} rurl={item.rurl} />;
            })}


          </div>        
            <div className=" mx-auto flex justify-between text-center pb-4 md:pb-4">
            <h2 className="h2 my-4 text-3xl font-semibold">Electrical</h2>

          </div>
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            {gui.map((item) => {
              return <Member src={item.imageurl} title={"User Interfaces"} subtitle={item.name} rurl={item.rurl} />;
            })}
            </div>

            <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            {powersystems.map((item) => {
              return <Member src={item.imageurl} title={"Power Systems"} subtitle={item.name} rurl={item.rurl} />;
            })}
            </div>


            <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            {computing.map((item) => {
              return <Member src={item.imageurl} title={"Computing Systems"} subtitle={item.name} rurl={item.rurl} />;
            })}
            </div>

          </div>

          <div className=" mx-auto flex justify-between text-center pb-4 md:pb-4">
            <h2 className="h2 my-4 text-3xl font-semibold">Mechanical</h2>
            <div>

            </div>

          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
          
            {magnetic.map((item) => {
              return <Member src={item.imageurl} title={"Magnetic"} subtitle={item.name} rurl={item.rurl} />;
            })}
        
            {braking.map((item) => {
              return <Member src={item.imageurl} title={"Braking"} subtitle={item.name} rurl={item.rurl} />;
            })}
            {structures.map((item) => {
              return <Member src={item.imageurl} title={"Structures"} subtitle={item.name} rurl={item.rurl} />;
            })}


          </div>

          <div className=" mx-auto flex justify-between text-center pb-4 md:pb-4">
            <h2 className="h2 my-4 text-3xl font-semibold">Business</h2>
            <div>


            </div>

          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
          {business.map((item) => {
              return <Member src={item.imageurl} title={"Business"} subtitle={item.name} rurl={item.rurl} />;
            })}


          </div>




        </div>
      </div>
    </section>
  );
}

function Member({ src, title, subtitle, rurl }) {
  return (
    <div className="relative flex flex-col items-center mx-4 my-4 bg-white p-4 shadow-md transition transform hover:scale-105 hover:shadow-xl">
      <div className="relative w-48 h-48 overflow-hidden">
        <a href={rurl} >
          <img
            className="object-cover w-full h-full"
            src={"/img/headshots/" + src}
          /></a>
      </div>
      <h4 className="text-xl font-bold mt-3 text-center">{title}</h4>
      <h4 className="text-lg text-center text-gray-600">{subtitle}</h4>
    </div>
  );
}


export default Members;