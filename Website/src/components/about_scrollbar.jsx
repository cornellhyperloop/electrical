import React, { Component } from "react";
import "../App.css";
import Modal from "./modal.jsx";

export default class AboutScrollbar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      header: props.team,
      teamData: props.teamData,
    };
  }

  render() {
    let header = this.state.header;
    let teamData = this.state.teamData;
    if (teamData === undefined) return <div></div>;
    else
      return (
        <article class="mt-8">
          <div class="flex flex-col bg-white m-auto p-auto">
            <h1 class="flex py-5 px-5 mx-0 font-bold text-4xl text-gray-800">
              {header}
            </h1>
            <div class="flex overflow-x-scroll pb-10" id="no-scrollbar">
              <div class="flex flex-nowrap ml-0 ">
                {teamData.map((person) => (
                  <div class="inline-block px-3">
                    <Modal member={person} />
                    <h2 class="text-1xl py-4 font-bold text-gray-900">
                      {person.name}
                    </h2>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </article>
      );
  }
}
