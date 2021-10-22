import React, { Component } from 'react';
import '../App.css';

export default class Navbar extends Component {
    constructor(props) {
        super(props);
        this.state = {
            page: 0
        }
    }

    setStateAndRunCallback = (val) => {
        this.setState(val, () => {
            this.props.toCallBack(this.state);
        });
    }

    render () {
        return (
            <div className="Navbar">
                <nav class="bg-gray-800">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="flex items-center justify-between h-28">
                        <div class="flex items-center">
                        <div class="flex-shrink-0">
                            <img class="h-20 w-96" src="./img/logotextthin.png" alt="Workflow" />
                        </div>
                        <div class="hidden md:block">
                            <div class="ml-10 flex items-baseline space-x-3">
                                <button class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-lg font-medium" onClick={() => this.setStateAndRunCallback({page: 0})} type="button">Home</button>
                                <button class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-lg font-medium" onClick={() => this.setStateAndRunCallback({page: 1})} type="button">About</button>
                                <button class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-lg font-medium" onClick={() => this.setStateAndRunCallback({page: 2})} type="button">Computing Systems</button>
                                <button class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-lg font-medium" onClick={() => this.setStateAndRunCallback({page: 3})} type="button">GUI</button>
                                <button class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-lg font-medium" onClick={() => this.setStateAndRunCallback({page: 4})} type="button">Power Systems</button>
                                <button class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-lg font-medium" onClick={() => this.setStateAndRunCallback({page: 5})} type="button">Previous Projects</button>
                            </div>
                        </div>
                        </div>
                    </div>
                    </div>
                </nav>
            </div>
        )
    }
}
