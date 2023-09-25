import React from "react";
import Header from "../partials/Header";
import Footer from "../partials/Footer";
import "../Timeline.css";
import OldTeam from "../img/oldteam.png";
import fun from "../img/fun.jpg";
import teamchc from "../img/team_CHC.jpg";
import powershot1 from "../img/power-shot1.png";
import powershot2 from "../img/power-shot2.png";

function CompetitionPage() {
  return (
    <div className="flex flex-col min-h-screen overflow-hidden justify-center items-center sm:px-4">
      {/* Site header */}
      <Header />

      {/* Page content */}
      <main className="flex-grow">
        {/* Competition article section */}
        <section className="py-16 bg-gray-100">
          <div className="container mx-auto px-4">
            <h1 className="text-3xl font-semibold mb-8">
              Cornell Hyperloop in the News
            </h1>
            <p className="text-black-600">
              Cornell Daily Sun wrote an article about Cornell Hyperloop's
              recent achievements in competitions. You can read the full article
              by clicking the link below:
            </p>
            <p className="mt-4">
              <a
                href="https://cornellsun.com/2023/08/29/project-teams-spend-the-summer-excelling-in-competitions-traveling-globally/"
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-500 hover:underline"
              >
                Read the article
              </a>
            </p>
            <p className="mt-4">
              We plan to attend more competitions in the near future. Stay in
              touch on our{" "}
              <a
                href="https://www.instagram.com/cornellhyperloop/"
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-500 hover:underline"
              >
                Instagram
              </a>
              .
            </p>
          </div>
        </section>

        <section className="py-16">
          <div className="container mx-auto px-4">
            <h2 className="text-2xl font-semibold mb-4">Photo Gallery</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
              {/* Add your gallery images here */}
              <div className="rounded-lg p-4 bg-white">
                <img
                  src={fun}
                  alt="Gallery Image 1"
                  className="w-full h-full"
                />
              </div>
              <div className="rounded-lg p-4 bg-white">
                <img
                  src={teamchc}
                  alt="Gallery Image 2"
                  className="w-full h-auto"
                />
              </div>
              <div className="rounded-lg p-4 bg-white">
                <img
                  src={powershot1}
                  alt="Gallery Image 3"
                  className="w-full h-auto"
                />
              </div>
              <div className="rounded-lg p-4 bg-white">
                <img
                  src={powershot2}
                  alt="Gallery Image 3"
                  className="w-full h-auto"
                />
              </div>
              {/* Add more images as needed */}
            </div>
          </div>
        </section>
      </main>

      {/* Site footer */}
      <Footer />
    </div>
  );
}

export default CompetitionPage;
