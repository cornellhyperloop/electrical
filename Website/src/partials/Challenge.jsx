import React, { useState, useRef, useEffect } from 'react';
import Transition from '../utils/Transition';
import YouTube, { YouTubeProps } from 'react-youtube';

import FeaturesBg from '../img/features-bg.png';
import FeaturesElement from '../img/features-element.png';

function Challenge() {

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
    <section className="relative">

      {/* Section background (needs .relative class on parent and next sibling elements) */}
      <div className="absolute inset-0 pointer-events-none mb-16" aria-hidden="true"></div>

      <div className="relative max-w-6xl mx-auto px-4 sm:px-6">
        <div className="pt-12 md:pt-20">

         
          {/* Section content */}
          <div className="md:grid  md:grid-cols-12 md:gap-20">

            {/* Content */}
                                    <YouTube className="md:col-span-7" videoId="0d7ttUMODt0" opts={opts} onReady={onPlayerReady} />

            <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-5 lg:col-span-5 md:mt-6 " data-aos="fade-right">
              <div className="md:pr-4 lg:pr-12 xl:pr-16 mb-8">
                <h3 className="h3 mb-3 font-bold">Competition</h3>
                <p className="text-xl text-gray-600">In order to accomplish our goal, Cornell Hyperloop will participate in the SpaceX Hyperloop Challenge. With the goal of dramatically shortening transit times over long distances, SpaceX has proposed a challenge to all who are able: to design and build a pod to test on their track in Hawthorne, California each summer. At Cornell Hyperloop, we will answer this call with determination and exacting precision.
</p>
              </div>
              {/* Tabs buttons */}
              
            </div>


            {/* Tabs items */}
            <div className="max-w-xl md:max-w-none md:w-full mx-auto md:col-span-5 lg:col-span-6 mb-8 md:mb-0 md:order-1" data-aos="zoom-y-out" ref={tabs}>
            </div >

          </div >

        </div >
      </div >
    </section >
  );
}

export default Challenge;