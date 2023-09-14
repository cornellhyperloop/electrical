import React, { Component } from "react";
import "../App.css";

export default class Navbar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      page: 0,
    };
  }

  setStateAndRunCallback = (val) => {
    this.setState(val, () => {
      this.props.toCallBack(this.state);
    });
  };

  render() {
    return (
      <div className="Navbar">
        <nav class="">
          <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex items-center justify-between h-28">
              <div class="flex items-center">
                <div class="flex-shrink-0">
                  <img
                    class="h-20 w-96"
                    src="./img/logotextthin.png"
                    alt="Workflow"
                  />
                </div>
                <div class="hidden md:block">
                  <div class="ml-10 flex items-baseline space-x-3">
                    <button
                      class="text-gray-300 hover:bg-gray-700 hover:text-white px-2 py-2 rounded-md text-lg font-medium"
                      onClick={() => this.setStateAndRunCallback({ page: 0 })}
                      type="button"
                    >
                      Home
                    </button>
                    <button
                      class="text-gray-300 hover:bg-gray-700 hover:text-white px-2 py-2 rounded-md text-lg font-medium"
                      onClick={() => this.setStateAndRunCallback({ page: 1 })}
                      type="button"
                    >
                      About
                    </button>
                    <button
                      class="text-gray-300 hover:bg-gray-700 hover:text-white px-2 py-2 rounded-md text-lg font-medium"
                      onClick={() => this.setStateAndRunCallback({ page: 2 })}
                      type="button"
                    >
                      Computing Systems
                    </button>
                    <button
                      class="text-gray-300 hover:bg-gray-700 hover:text-white px-2 py-2 rounded-md text-lg font-medium"
                      onClick={() => this.setStateAndRunCallback({ page: 3 })}
                      type="button"
                    >
                      GUI
                    </button>
                    <button
                      class="text-gray-300 hover:bg-gray-700 hover:text-white px-2 py-2 rounded-md text-lg font-medium"
                      onClick={() => this.setStateAndRunCallback({ page: 4 })}
                      type="button"
                    >
                      Power Systems
                    </button>
                    <div class="dropdown">
                      <button
                        type="button"
                        class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-lg font-medium"
                      >
                        Previous Projects
                        <svg
                          class="-mr-1 ml-1 h-5 w-5 inline-block"
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 20 20"
                          fill="currentColor"
                          aria-hidden="true"
                        >
                          <path
                            fill-rule="evenodd"
                            d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z"
                            clip-rule="evenodd"
                          />
                        </svg>
                      </button>
                      <nav>
                        <ul>
                          <li>
                            <button
                              className="bg-gray-800 hover:bg-gray-700 text-gray-300 block px-4 py-2 text-sm min-w-full"
                              onClick={() =>
                                this.setStateAndRunCallback({ page: 5 })
                              }
                            >
                              Communications SP '21
                            </button>
                          </li>
                          <li>
                            <button
                              className="bg-gray-800 hover:bg-gray-700 text-gray-300 block px-4 py-2 text-sm min-w-full"
                              onClick={() =>
                                this.setStateAndRunCallback({ page: 6 })
                              }
                            >
                              Power Systems SP '21
                            </button>
                          </li>
                          <li>
                            <button
                              className="bg-gra-800 hover:bg-gray-700 text-gray-300 block px-4 py-2 text-sm min-w-full"
                              onClick={() =>
                                this.setStateAndRunCallback({ page: 7 })
                              }
                            >
                              Sensors SP '21
                            </button>
                          </li>
                        </ul>
                      </nav>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </nav>
      </div>
    );
  }
}
