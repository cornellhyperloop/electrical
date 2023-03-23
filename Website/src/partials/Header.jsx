import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import HeroImage from '../img/logo_symbol.png';

function Header() {

  const [top, setTop] = useState(true);
  const [url, setUrl] = useState("");
  // detect whether user has scrolled the page down by 10px 
  useEffect(() => {
    const scrollHandler = () => {
      window.pageYOffset > 10 ? setTop(false) : setTop(true)
    };
    setUrl(window.location.href);
    window.addEventListener('scroll', scrollHandler);
    return () => window.removeEventListener('scroll', scrollHandler);
  }, [top]);  

  return (
    <header className={`fixed w-full z-30 md:bg-opacity-90 bg-white bg-opacity-10 transition duration-300 ease-in-out`}>
      <div className="mx-20 sm:px-6 ">
        <div className="flex items-center justify-between h-16 md:h-18">

          {/* Site branding */}
          <div className="flex-shrink-0 mr-4">
            {/* Logo */}
            <div to="/" className="block" aria-label="Cruip">
           

            </div>
          </div>
          <a className="hover:opacity-60" href="/"><img className="h-16 w-16" src={HeroImage}></img></a>
          {/* Site navigation */}
          <nav className="flex flex-grow justify-end">
            
            <a className={url.includes("members") ? "text-xl font-semibold text-gray-800 mr-4 hover:underline" : "text-xl font-semilight text-gray-800 mr-4 hover:underline" } href="/members">Members</a>
            <a className={url.includes("team") ? "text-xl font-semibold text-gray-800 mr-4 hover:underline" : "text-xl font-semilight text-gray-800 mr-4 hover:underline" }  href="/team">Team</a>
            <a className={url.includes("donate") ? "text-xl font-semibold text-gray-800 mr-4 hover:underline" : "text-xl font-semilight text-gray-800 mr-4 hover:underline" }  href="/donate">Donate</a>
            <a className={url.includes("apply") ? "text-xl font-semibold text-gray-800 mr-4 hover:underline" : "text-xl font-semilight text-gray-800 mr-4 hover:underline" }  href="/apply">Apply</a>


          </nav>

        </div>
      </div>
    </header>
  );
}

export default Header;