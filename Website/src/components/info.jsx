import React from "react";
import '../App.css';

export default class Modal extends React.Component {
  state = { isOpen: false };

  handleShowDialog = () => {
    this.setState({ isOpen: !this.state.isOpen });
    console.log('clicked');
  };

  render() {
    return (
      <div>
        <img
          className="portrait"
          src="./img/sample.jpg"
          onClick={this.handleShowDialog}
          alt="member"
        />
        {this.state.isOpen && (
          <dialog
            className="member-info"
            open
            onClick={this.handleShowDialog}>
            <div>
            <div class ="max-w-sm rounded overflow-hidden shadow-lg">
            <div class ="px-1 py-1">
            <div class ="font-bold text-xl mb-2">Mountain</div>
            <p class ="text-gray-700 text-base">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit.Voluptatibus quia, nulla!Maiores et perferendis eaque, exercitationem praesentium nihil.
            </p>
            </div>
            <div class ="px-6 pt-4 pb-2">
            <span class ="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#photography</span>
            <span class ="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#travel</span>
            <span class ="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#winter</span>
            </div>
            </div>
            </div>
          </dialog>
        )}
      </div>
    );
  }
}