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

  // show or hide the menu based on screen size
  const [showMenu, setShowMenu] = useState(false);
  const [showMenuItems, setShowMenuItems] = useState(false);


  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth < 768) { // show menu on screens less than 768px wide (mobile and tablet)
        setShowMenu(true);
      } else {
        setShowMenu(false);
      }
    };

    handleResize(); // call handleResize on initial render
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return (
    <header className={`w-full z-30 md:bg-opacity-90 bg-white bg-opacity-10 transition duration-300 ease-in-out`}>
      <div className="mx-auto sm:px-6 text-center">
        <div className="flex items-center justify-between h-16 md:h-18">

          {/* Site branding */}
          <div className="flex-shrink-0 mr-4">
            {/* Logo */}
            <a className="hover:opacity-60" href="/">
              <img className="h-10 max-w-none sm:h-16 mx-auto " src={HeroImage} alt="Logo"></img>
            </a>
          </div>

          {/* Site navigation */}
          {/* Render the hamburger menu on small screens */}
          {showMenu && (
        
          // create a hamburger menu that links to team, members, donate, and apply, and closes when clicked
          <div className="sm:hidden">
            <button onClick={() => setShowMenu(!showMenu)} className="inline-flex items-center justify-center p-2 rounded-md text-black-300 hover:text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" aria-controls="mobile-menu" aria-expanded="false">
              <span className="sr-only">Open main menu</span>
          
              {/* Menu open: "block", Menu closed: "hidden" */}
              <svg className={`${showMenu ? 'block' : 'hidden'} h-6 w-6`} xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
          )}


          {/* Render the full menu on large screens */}
          {!showMenu && (
          <div className={`sm:flex sm:items-center sm:ml-6`}>
            <div className="flex space-x-4">
              <Link to="/team" className="text-black-300 hover:bg-red-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Team</Link>
              <Link to="/members" className="text-black-300 hover:bg-red-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Members</Link>
              <Link to="/donate" className="text-black-300 hover:bg-red-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Donate</Link>
              <Link to="/apply" className="text-black-300 hover:bg-red-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Apply</Link>
              <Link to="/competition" className="text-black-300 hover:bg-red-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">News</Link>
            </div>
          </div>)}
        </div>
      </div>
    </header>
  );
}

export default Header;
