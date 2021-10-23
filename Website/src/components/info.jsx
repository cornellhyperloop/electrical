import React from "react";
//import "./modal.css";

// export default class Modal extends React.Component {
//   onClose = e => {
//     this.props.onClose && this.props.onClose(e);
//   };
//   state = {
//     show: false
//   };
//   showModal = e => {
//     this.setState({
//       show: true
//     });
//   };
//   render() {
//     if (!this.props.show) {
//       return null;
//     }
//     return (
//       <div class="modal" id="modal">
//         <h2>Modal Window</h2>
//         <div class="content">{this.props.children}</div>
//         <div class="actions">
//           <button class="toggle-button" onClick={this.onClose}>
//             close
//           </button>
//         </div>
//       </div>
//     );
//   }
// }
export default class Modal extends React.Component {
  state = { isOpen: false };

  handleShowDialog = () => {
    this.setState({ isOpen: !this.state.isOpen });
    console.log('cliked');
  };

  render() {
    return (
      <div>
        <img
          className="small"
          src="./img/sample.jpg"
          onClick={this.handleShowDialog}
          alt="no image"
        />
        {this.state.isOpen && (
          <dialog
            className="dialog"
            style={{ position: 'absolute' }}
            open
            onClick={this.handleShowDialog}>
            <div class ="p-10">
            <div class ="max-w-sm rounded overflow-hidden shadow-lg">
              <img class ="w-full" src="./img/sample.jpg" alt="Mountain"> </img>
            <div class ="px-6 py-4">
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