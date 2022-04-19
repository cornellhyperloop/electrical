import React from "react";
import "../App.css";

export default class Modal extends React.Component {
  constructor(props) {
    super(props);
    this.member = props.member;
  }
  state = { isOpen: false };

  handleShowDialog = () => {
    this.setState({ isOpen: !this.state.isOpen });
    console.log("clicked");
  };

  state = {
    show: false,
  };

  showModal = (e) => {
    this.setState({
      show: !this.state.show,
    });
  };

  render() {
    if (this.member === undefined) return <div></div>;
    else
      return (
        <div className="portrait-container">
          <img
            className="portrait"
            src={this.member.image}
            onClick={this.handleShowDialog}
            alt="member"
          />
          {this.state.isOpen && (
            <dialog
              className="member-info"
              open
              onClick={this.handleShowDialog}
            >
              <div class="h-full rounded overflow-hidden shadow-lg flex flex-1 flex-col justify-between">
                <div className="flex flex-1 flex-col justify-between">
                  <div class="px-1 py-1">
                    <div class="font-bold text-xl mb-2 px-2 pt-1">
                      {this.member.name}, {this.member.year}
                    </div>
                    <div class="font-bold text-sm mb-2 px-2 pt-1">
                      {this.member.major}
                    </div>
                    <p class="text-gray-700 text-base px-2">
                      {this.member.funfact}
                    </p>
                  </div>
                  <div class="px-3 pt-4 pb-2">
                    <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                      <a href={this.member.github}>Github</a>
                    </span>
                    <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
                      <a href={this.member.linkedin}>LinkedIn</a>
                    </span>
                  </div>
                </div>
              </div>
            </dialog>
          )}
        </div>
      );
  }
}
