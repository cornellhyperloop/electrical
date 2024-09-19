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

  const [videoHeight, setVideoHeight] = useState(390);
  const [videoWidth, setVideoWidth] = useState('100%');

  useEffect(() => {
    heightFix()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [tab])
  const onPlayerReady = (event) => {
    // access to player in all event handlers via event.target
  }

  const opts = {
    height: videoHeight,
    width: videoWidth,
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
                <h3 className="h3 mb-3 font-bold text-red-700 tracking-wide uppercase">Competition</h3>
                <p className="text-xl text-black-600 leading-relaxed">To achieve our goal, the Cornell Hyperloop Project Team will participate in the SpaceX Hyperloop Challenge.
                  This is a call to all who are able to design and build a pod to test on their track in Hawthorne, California each summer.
                  Our team will rise to this challenge with
                  <span className="font-bold text-red-700"> relentless determination and exacting precision.</span>
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