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
  var faculty=[{name:"Rick Geddes",imageurl:"GeddesRick.jpg",title:"Faculty Co-Advisor"},{name:"Zhiting Tian",imageurl:"TianZhiting.jpg",title:"Faculty Co-Advisor"}]
  var leads = [{ name: "Cameron Robinson", imageurl: "CameronRobinson.jpg", title: "Team Manager" }, { name: "David Wolfers", imageurl: "DavidWolfers.jpg", title: "Electrical Lead" }, { name: "Ellie Perlitz", imageurl: "ElliePerlitz.jpg", title: "Business Lead" }, { name: "Mahika Goel", imageurl: "profilephoto.png", title: "Mechanical Lead" }, { name: "Courtney Kraft", imageurl: "CourtneyKraft.jpg", title: "Mechanical Advisor" }, { name: "Mark Edwards", imageurl: "profilephoto.png", title: "Magnetic Levitation Lead" }, { name: "Jack Crespo", imageurl: "profilephoto.png", title: "Lead Systems Engineer"},{name:"Joshua Coombs",imageurl:"profilephoto.png",title:"Braking Lead"},{name:"Ashna Gupta",imageurl:"profilephoto.png",title:"Structures Lead"},{name:"Vanshaj Jain",imageurl:"vanshajjain.jpg",title:"GUI Lead"},{name:"Robert Fleming",imageurl:"profilephoto.png",title:"Power Systems Lead"},{name:"Ridhit Bhura",imageurl:"profilephoto.png",title:"Computing Systems Lead"},{name:"Devan Flores",imageurl:"profilephoto.png",title:"Web Lead"}]
  var gui=["Kelvin Wang","Ryan Mao" ,"Christina Unkenholz","Devika Krishna","Patrick Choo","Mihika Jain","Stephen Chien","Cooper Proctor","Aislinn Ennis", "Benson Yee"]
  var computing=["Anoushka Kabra","Ashley Heckman","David Lilienfeld","Yaqi Gao","Levi Zeng","Shefali Awasthi","Zarif Karim", "Neera Kapoor", "Aiman Mobhani"]
  var powersystems=["Schuyler Seyram", "Berk Gokmen" , "Steven Wei Chen", "Lalo Esparza", "Rares-Stefan Busca","Kirti Bagepalli", "Max Trager", "Jenna Kafrawi"]
  var magnetic = ["Nikita Dolgopolov", "Rushil Choudary", "Verena Gonzalez"]
  var braking = ["Yueming Liu","Sal Ciminello","Moez Amini","Michelle Yu","Madison Schaaff","Siddhant Ahuja"]
  var structures = ["David Ovetsky","Harsh Maskara","Allison Liao", "Jack Meyer","Riya Guttigoli", "Daniel Akinwale"]
  var business = [ "Tyler Angelica", "Jonathan Chen", "Luke Shao", "Elizabeth Song", "Aidan Shor", "Ryan Graziano", "Jason Ng", "Vasu Patel", "John Goepfert"]


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
            { faculty.map((item) => {
              return <Member src={item.imageurl} title={item.title} subtitle={item.name} />;
              }) }
            
          
          </div>
          <div className=" mx-auto flex justify-between text-center pt-4 pb-4 md:pb-4">
            <h2 className="h2 mb-4 text-3xl font-semibold">Leads</h2>
            <div>

              
              </div>

          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            { leads.map((item) => {
              return <Member src={item.imageurl} title={item.title} subtitle={item.name} />;
              }) }
            
          
          </div>          <div className=" mx-auto flex justify-between text-center pb-4 md:pb-4">
            <h2 className="h2 my-4 text-3xl font-semibold">Electrical</h2>
            <div>

              
              </div>

          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            { gui.map((item) => {
              return <Member src={"profilephoto.png"} title={"User Interfaces"} subtitle={item} />;
              }) }
              { powersystems.map((item) => {
              return <Member src={"profilephoto.png"} title={"Power Systems"} subtitle={item} />;
              })}
              { computing.map((item) => {
              return <Member src={"profilephoto.png"} title={"Computing Systems"} subtitle={item} />;
              }) }
          
          </div>
           <div className=" mx-auto flex justify-between text-center pb-4 md:pb-4">
            <h2 className="h2 my-4 text-3xl font-semibold">Business</h2>
            <div>

              
              </div>

          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            { business.map((item) => {
              return <Member src={"profilephoto.png"} title={"Business"} subtitle={item} />;
              }) }
             
          
          </div>    
          <div className=" mx-auto flex justify-between text-center pb-4 md:pb-4">
            <h2 className="h2 my-4 text-3xl font-semibold">Mechanical</h2>
            <div>

              
              </div>

          </div>

          {/* Items */}
          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            { magnetic.map((item) => {
              return <Member src={"profilephoto.png"} title={"Magnetic"} subtitle={item} />;
              }) }
              { braking.map((item) => {
              return <Member src={"profilephoto.png"} title={"Braking"} subtitle={item} />;
              })}
              { structures.map((item) => {
              return <Member src={"profilephoto.png"} title={"Structures"} subtitle={item} />;
              }) }
          
          </div>    
        </div>
      </div>
    </section>
  );
}
function Member({ src,title,subtitle }) {
  return (
    <div className="relative flex flex-col items-center mr-4 bg-white rounded ">
      <img className="h-36 object-cover w-36 rounded-md contain" src={require("../img/headshots/"+src).default}></img>

      <h4 className="text-xl font-bold w-36 leading-snug tracking-tight mb-1 mt-4 self-start">{title}</h4>
      <h4 className="text-lg font-normal object-contain leading-snug tracking-tight mb-1 mt-1 self-start">{subtitle}</h4>

    </div>
  );
}

export default Members;