import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import HeroImage from '../img/logo_symbol.png';

function Header() {

  const [top, setTop] = useState(true);

  // detect whether user has scrolled the page down by 10px 
  useEffect(() => {
    const scrollHandler = () => {
      window.pageYOffset > 10 ? setTop(false) : setTop(true)
    };
    window.addEventListener('scroll', scrollHandler);
    return () => window.removeEventListener('scroll', scrollHandler);
  }, [top]);  

  return (
    <header className={`fixed w-full z-30 md:bg-opacity-90 transition duration-300 ease-in-out bg-gray-800`}>
      <div className="mx-20 sm:px-6 ">
        <div className="flex items-center justify-between h-16 md:h-20">

          {/* Site branding */}
          <div className="flex-shrink-0 mr-4">
            {/* Logo */}
            <div to="/" className="block" aria-label="Cruip">
           

            </div>
          </div>
          <img className="h-16 w-16" src={HeroImage}></img>
          {/* Site navigation */}
          <nav className="flex flex-grow justify-end">
            
            <p className="text-xl font-semilight text-white mr-4 ">MEMBERS</p>
            <p className="text-xl font-semilight text-white mr-4 ">TEAMS</p>
            <p className="text-xl font-semilight text-white mr-4">SPONSORS</p>
            <p className="text-xl font-semilight text-white mr-4">APPLY</p>


          </nav>

        </div>
      </div>
    </header>
  );
}

export default Header;