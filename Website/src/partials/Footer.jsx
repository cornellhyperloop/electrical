import React from "react";

function Footer() {
  return (
    <footer className="text-black py-6">
      <div className="container mx-auto px-4">
        {/* Your footer content here */}
        Cornell Hyperloop &copy; {new Date().getFullYear()} 
      </div>
    </footer>
  );
}

export default Footer;