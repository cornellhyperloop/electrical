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
    { name: "Mark Edwards", imageurl: "mark_edwards_2.jpg", title: "Magnetics Lead", rurl: "https://www.linkedin.com/in/markvedwards02/" },
    { name: "Moez Amini", imageurl: "moezamini.jpg", title: "Braking Lead", rurl: "https://www.linkedin.com/in/moezamini/" },
    { name: "Daniel Akinwale", imageurl: "danielakinwale.jpg", title: "Composites Lead", rurl: "https://www.linkedin.com/in/daniel-akinwale-894297202/" },
    { name: "Sal Ciminello", imageurl: "salciminello.jpg", title: "Prototyping Lead", rurl: "https://www.linkedin.com/in/sal-ciminello-863471255/" },
    { name: "Berk Gokmen", imageurl: "berkgokmen.jpg", title: "Power Systems Lead", rurl: "https://www.linkedin.com/in/berk-gokmen/" },
    { name: "David Lilienfeld", imageurl: "davidlilienfeld.jpg", title: "Computing Systems Lead", rurl: "https://www.linkedin.com/in/david-lilienfeld-aa7162133/" },
    { name: "Aislinn Ennis", imageurl: "AislinnEnnis.jpg", title: "UI Lead", rurl: "https://www.linkedin.com/in/aislinn-ennis/" },
    { name: "John Goepfert", imageurl: "johngoepfort.jpg", title: "Operations Lead", rurl: "https://www.linkedin.com/in/john-goepfert/" },
    { name: "Vasu Patel", imageurl: "vasupatel.jpg", title: "Business Dev Lead", rurl: "https://www.linkedin.com/in/patelv1/" },
    { name: "Luke Shao", imageurl: "profilephoto.png", title: "Marketing Lead", rurl: "https://www.linkedin.com/in/luke-shao/" },
    { name: "Stephen Chien", imageurl: "profilephoto.png", title: "Web Lead", rurl: "https://www.linkedin.com/in/stephenlchien/" },


  ]
  var advisors = [
    { name: "Mahika Goel", imageurl: "MahikaGoel.jpg", title: "Mechanical Advisor", rurl: "https://www.linkedin.com/in/mahika-goel-2bbb201a5/" },
    { name: "Jack Crespo", imageurl: "JackCrespo.jpg", title: "Mechanical Advisor", rurl: "https://www.linkedin.com/in/jack-crespo/" },
    { name: "Ellie Perlitz", imageurl: "ElliePerlitz.jpg", title: "Business Advisor", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Jack Rebillard", imageurl: "profilephoto.png", title: "Business Advisor", rurl: "https://www.linkedin.com/in/jack-rebillard/" },
    { name: "Tyler Angelica", imageurl: "profilephoto.png", title: "Business Advisor", rurl: "https://www.linkedin.com/in/tylerangelica/" },
  ]




  var gui = [
    { name: "Devika Krishna", imageurl: "devikakrishna.png", rurl: "https://www.linkedin.com/in/devika-krishna-9a60711b2/" },
    { name: "Brandon Lerit", imageurl: "brandonlerit.jpg", rurl: "https://www.linkedin.com/in/brandonlerit/" },
    { name: "Max Farma", imageurl: "maxfarma.jpg", rurl: "https://www.linkedin.com/in/maximilian-farma-529420289/" },
  ]

  var powersystems = [
    { name: "Kirti Bagepalli", imageurl: "kirtibagepalli.jpg", rurl: "https://www.linkedin.com/in/kirti-bagepalli/" },
    { name: "Steven Wei Chen", imageurl: "profilephoto.png", rurl: "https://www.linkedin.com/in/steven-chen-bb4798286/" },
    { name: "Lalo Esparza", imageurl: "laloesparza.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Max Trager", imageurl: "maxtrager.jpg", rurl: "https://www.linkedin.com/in/max-trager-679652183/" },
    { name: "Jenna Kafrawi", imageurl: "profilephoto.png", rurl: "https://www.linkedin.com/in/jenna-kafrawi/" },
  ]


  var computing = [
    { name: "Ashley Heckman", imageurl: "ashley_heckman.jpg", rurl: "https://www.linkedin.com/in/ashley-heckman-6b3848224/" },
    { name: "Yaqi Gao", imageurl: "yaqigao.jpg", rurl: "https://www.linkedin.com/in/yaqi-gao/" },
    { name: "Levi Zeng", imageurl: "levizeng.jpg", rurl: "https://www.linkedin.com/in/levi-zeng-529b37255/" },
    { name: "Shefali Awasthi", imageurl: "shefaliawasthi.jpg", rurl: "https://www.linkedin.com/in/shefali-awasthi-46a14a1aa/" },
    { name: "Zarif Karim", imageurl: "zarifkarim.jpg", rurl: "https://www.linkedin.com/in/zkarim28/" },
    { name: "Neera Kapoor", imageurl: "profilephoto.png", rurl: "https://www.linkedin.com/in/neera-kapoor-7a673327b/" },
    { name: "Aiman Mobhani", imageurl: "aimanmobhani.jpg", rurl: "https://www.linkedin.com/in/aiman-mobhani-19247720a/" },
    {
      name: "Rares-Stefan Busca", imageurl: "profilephoto.png", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/",
    }, { name: "Jake Ludgin", imageurl: "jakeludgin.jpg", rurl: "https://www.linkedin.com/in/jake-ludgin-059287252/" },
  ]


  var magnetics = [

    { name: "Sal Ciminello", imageurl: "salciminello.jpg", rurl: "https://www.linkedin.com/in/sal-ciminello-863471255/" },
    { name: "Riya Guttigoli", imageurl: "riyaguttigoli.jpg", rurl: "https://www.linkedin.com/in/riya-guttigoli-39a979196/" },
    { name: "Verena Gonzalez", imageurl: "verenagonzalez.jpg", rurl: "https://www.linkedin.com/in/verena-gonzalez-a7a62024a/" },
    { name: "Marcel Latasa", imageurl: "marcellatasa.jpg", rurl: "https://www.linkedin.com/in/marcel-latasa-a633ba219/" },
    { name: "Aarian Mepani", imageurl: "profilephoto.png", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Anubhav Nigam", imageurl: "anubhavnigam.jpg", rurl: "https://www.linkedin.com/in/anubhav-nigam/" },

  ]


  var braking = [

    { name: "Siddhant Ahuja", imageurl: "profilephoto.png", rurl: "https://www.linkedin.com/in/siddhant-ahuja-43988a207/" },
    { name: "Madison Schaaff", imageurl: "madisonshaaff.jpg", rurl: "https://www.linkedin.com/in/madison-schaaff-5bb075274/" },
    { name: "Olaa Ahmed", imageurl: "olaaahmed.jpg", rurl: "https://www.linkedin.com/in/olaa-ahmed-075751285/" },
    { name: "Shreya Anand", imageurl: "profilephoto.png", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },

  ]


  var structures = [

    { name: "Harshvardhan Maskara", imageurl: "profilephoto.png", rurl: "https://www.linkedin.com/in/harshvardhan-maskara-998107147/?originalSubdomain=in" },
    { name: "Daniel Akinwale", imageurl: "danielakinwale.jpg", rurl: "https://www.linkedin.com/in/daniel-akinwale-894297202/" },
    { name: "Tokunbo Oshinowo", imageurl: "tokunbooshinowo.jpg", rurl: "https://www.linkedin.com/in/tokunbo-oshinowo/" },
    { name: "Qing Yi Chen", imageurl: "profilephoto.png", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },

  ]

  var business = [

    { name: "Tyler Angelica", imageurl: "profilephoto.png", rurl: "https://www.linkedin.com/in/tylerangelica/" },
    { name: "Jonathan Chen", imageurl: "jonathanchen.jpg", rurl: "https://www.linkedin.com/in/jonathan-chen-377a261b6/" },
    { name: "Luke Shao", imageurl: "profilephoto.png", rurl: "https://www.linkedin.com/in/luke-shao/" },
    { name: "Elizabeth Song", imageurl: "elizabethsong.jpg", rurl: "https://www.linkedin.com/in/elizabethyurisong/" },
    { name: "Ryan Graziano", imageurl: "ryangraziano.jpeg", rurl: "https://www.linkedin.com/in/ryangraziano/" },
    { name: "Jason Ng", imageurl: "IMG_4355.jpg", rurl: "https://www.linkedin.com/company/cornell-hyperloop/mycompany/" },
    { name: "Vasu Patel", imageurl: "vasupatel.jpg", rurl: "https://www.linkedin.com/in/patelv1/" },
    { name: "John Goepfert", imageurl: "johngoepfort.jpg", rurl: "https://www.linkedin.com/in/john-goepfert/" }


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

          <div className=" mx-auto flex justify-between text-center pt-4 pb-4 md:pb-4">
            <h2 className="h2 mb-4 text-3xl font-semibold">Advisors </h2>

          </div>

          <div className="max-w-sm mx-auto flex flex-wrap flex-row gap-6  items-start md:max-w-2xl lg:max-w-none">
            {advisors.map((item) => {
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
              return <Member src={item.imageurl} title={"Magnetics"} subtitle={item.name} rurl={item.rurl} />;
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