import React, { useState, useRef, useEffect } from 'react';
import Transition from '../utils/Transition';
import YouTube, { YouTubeProps } from 'react-youtube';

import FeaturesBg from '../img/features-bg.png';
import FeaturesElement from '../img/features-element.png';

function Features() {

  const [tab, setTab] = useState(1);

  const tabs = useRef(null);

  const heightFix = () => {
    if (tabs.current.children[tab]) {
      tabs.current.style.height = tabs.current.children[tab - 1].offsetHeight + 'px'
    }
  }

  useEffect(() => {
    heightFix()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [tab])
  const onPlayerReady = (event) => {
    // access to player in all event handlers via event.target
  }

  const opts = {
    height: '390',
    width: '640',
    playerVars: {
      // https://developers.google.com/youtube/player_parameters
      autoplay: 0,
    },
  };
  return (
    <section className="relative" id="goals">

      {/* Section background (needs .relative class on parent and next sibling elements) */}
      <div className="absolute inset-0 bg-gray-100 pointer-events-none mb-16" aria-hidden="true"></div>
      <div className="absolute left-0 right-0 m-auto w-px p-px h-20 bg-gray-200 transform -translate-y-1/2"></div>

      <div className="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div className="pt-12 md:pt-20">

         
          {/* Section content */}
          <div className="md:grid md:grid-cols-12 md:gap-6">

            {/* Content */}
            <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-7 lg:col-span-6 md:mt-6 pb-20" data-aos="fade-right">
              <div className="md:pr-4 lg:pr-12 xl:pr-16 mb-8">
                <h3 className="h3 mb-3 font-bold">The Goal</h3>
                <p className="text-xl text-gray-600">Every few centuries, something comes along that revolutionizes the world - something that, once integrated with society, leaves us wondering how we had lived without it. The examples are plenty: fire, the wheel, the ship, the train, the car, the plane. Now we find ourselves on the brink of another such innovation: the Hyperloop. Cornell Hyperloop seeks to spearhead the revolution in transportation technology.</p>
              </div>
              {/* Tabs buttons */}
              
            </div>

            {/* Tabs items */}
            <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-5 lg:col-span-6 mb-8 md:mb-0 md:order-1" data-aos="zoom-y-out" ref={tabs}>
            <YouTube videoId="S5fOWB6SNqs" opts={opts} onReady={onPlayerReady} />
            </div >

          </div >

        </div >
      </div >
    </section >
  );
}

export default Features;