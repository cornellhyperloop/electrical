import React, { useState } from "react";
import HeroImage from "../img/logo_symbol.png";

import Header from "../partials/Header";
import HeroHome from "../partials/HeroHome";
import FeaturesHome from "../partials/Features";
import FeaturesBlocks from "../partials/FeaturesBlocks";
import Testimonials from "../partials/Testmonials";
import Newsletter from "../partials/Newsletter";
import Footer from "../partials/Footer";
import Banner from "../partials/Banner";
import Challenge from "../partials/Challenge";

function HomePage() {
  return (
    <div className="flex flex-col min-h-screen overflow-hidden">
      {/*  Site header */}
      <Header />
      {/*  Page content */}
      <main className="flex-grow">
        {/*  Page sections */}
        <HeroHome />
        <FeaturesHome />
        <Challenge />
        <FeaturesBlocks />
      </main>
      <Banner />

      {/*  Site footer */}
    </div>
  );
}

export default HomePage;
