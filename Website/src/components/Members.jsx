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
  var leads = [{ name: "Cameron Robinson", imageurl: "CameronRobinson.jpg", title: "Team Manager", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Robert Fleming", imageurl: "robertfleming.jpg", title: "Electrical Lead", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Ellie Perlitz", imageurl: "ElliePerlitz.jpg", title: "Business Lead", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Nikita Dolgopolov", imageurl: "banana.jpeg", title: "Mechanical Lead", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Courtney Kraft", imageurl: "CourtneyKraft.jpg", title: "Mechanical Advisor", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Mark Edwards", imageurl: "markedwards.jpg", title: "Magnetic Levitation Lead", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Jack Crespo", imageurl: "profilephoto.png", title: "Lead Systems Engineer", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Joshua Coombs", imageurl: "profilephoto.png", title: "Braking Lead", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Ashna Gupta", imageurl: "profilephoto.png", title: "Structures Lead", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
  { name: "Vanshaj Jain", imageurl: "vanshajjain.jpg", title: "GUI Lead", rurl: "https://www.linkedin.com/in/vanshaj24/" },
  { name: "Berk Gokmen", imageurl: "profilephoto.png", title: "Power Systems Lead", rurl: "https://www.linkedin.com/in/berk-gokmen/" },
  { name: "Ridhit Bhura", imageurl: "profilephoto.png", title: "Computing Systems Lead", rurl: "https://www.linkedin.com/in/ridhit/" },
  { name: "Stephen Chien", imageurl: "profilephoto.png", title: "Web Lead", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" }]

  var gui = ["Kelvin Wang", "Ryan Mao", "Devika Krishna", "Patrick Choo", "Mihika Jain", "Stephen Chien", "Cooper Proctor", "Aislinn Ennis", "Benson Yee"]
  var computing = ["Anoushka Kabra", "Ashley Heckman", "David Lilienfeld", "Yaqi Gao", "Levi Zeng", "Shefali Awasthi", "Zarif Karim", "Neera Kapoor", "Aiman Mobhani"]
  var powersystems = ["Schuyler Seyram", "Steven Wei Chen", "Lalo Esparza", "Rares-Stefan Busca", "Kirti Bagepalli", "Max Trager", "Jenna Kafrawi"]

 
  var gui = ["Kelvin Wang", "Ryan Mao", "Devika Krishna", "Patrick Choo", "Mihika Jain", "Cooper Proctor", "Aislinn Ennis", "Benson Yee"]
  var computing = ["Anoushka Kabra", "Ashley Heckman", "David Lilienfeld", "Yaqi Gao", "Levi Zeng", "Shefali Awasthi", "Zarif Karim", "Neera Kapoor", "Aiman Mobhani"]
  var powersystems = ["Schuyler Seyram", "Berk Gokmen", "Steven Wei Chen", "Lalo Esparza", "Rares-Stefan Busca", "Kirti Bagepalli", "Max Trager", "Jenna Kafrawi"]

  var magnetic = ["Nikita Dolgopolov", "Rushil Choudary", "Verena Gonzalez"]
  var braking = ["Yueming Liu", "Sal Ciminello", "Moez Amini", "Michelle Yu", "Madison Schaaff", "Siddhant Ahuja"]
  var structures = ["David Ovetsky", "Harsh Maskara", "Allison Liao", "Jack Meyer", "Riya Guttigoli", "Daniel Akinwale"]
  var business = ["Tyler Angelica", "Jonathan Chen", "Luke Shao", "Elizabeth Song", "Aidan Shor", "Ryan Graziano", "Jason Ng", "Vasu Patel", "John Goepfert"]


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


          </div>          <div className=" mx-auto flex justify-between text-center pb-4 md:pb-4">
            <h2 className="h2 my-4 text-3xl font-semibold">Electrical</h2>
            <div>


            </div>

          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            {gui.map((item) => {
              return <Member src={"profilephoto.png"} title={"User Interfaces"} subtitle={item} />;
            })}
            {powersystems.map((item) => {
              return <Member src={"profilephoto.png"} title={"Power Systems"} subtitle={item} />;
            })}
            {computing.map((item) => {
              return <Member src={"profilephoto.png"} title={"Computing Systems"} subtitle={item} />;
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
              return <Member src={"profilephoto.png"} title={"Business"} subtitle={item} />;
            })}


          </div>
          <div className=" mx-auto flex justify-between text-center pb-4 md:pb-4">
            <h2 className="h2 my-4 text-3xl font-semibold">Mechanical</h2>
            <div>

            </div>

          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            {magnetic.map((item) => {
              return <Member src={"profilephoto.png"} title={"Magnetic"} subtitle={item} />;
            })}
            {braking.map((item) => {
              return <Member src={"profilephoto.png"} title={"Braking"} subtitle={item} />;
            })}
            {structures.map((item) => {
              return <Member src={"profilephoto.png"} title={"Structures"} subtitle={item} />;
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