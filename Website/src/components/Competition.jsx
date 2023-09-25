import React from "react";
import Header from "../partials/Header";
import Newsletter from "../partials/Newsletter";
import Footer from "../partials/Footer";
import "../Timeline.css";
import OldTeam from "../img/oldteam.png";


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
            <p className="text-gray-600">
              Cornell Daily Sun wrote an article about Cornell Hyperloop's recent achievements in competitions. You can read the full article by clicking the link below:
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
          </div>
        </section>
      </main>

      {/* Site footer */}
      <Footer />
    </div>
  );
}

export default CompetitionPage;
