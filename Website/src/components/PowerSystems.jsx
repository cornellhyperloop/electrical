import React, { Component } from 'react';
import '../App.css';

export default class PowerSystems extends Component {
    constructor(props) {
        super(props);
        this.state = {
            pageData: "test"
        }
    }

    componentDidMount() {
        fetch("./data/PowerSystems.json").then(
            (result) => result.json()).then(
                (data) => this.setState({ pageData: data })
            )
    }

    render() {
        if (this.props.display === 4) {
            let pageData = this.state.pageData;
            return (
                <div className="PowerSystems">
                    <header class="bg-white shadow">
                        <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
                            <h1 class="text-3xl font-bold text-gray-900">{pageData.header}</h1>
                        </div>
                    </header>
                    <main>
                        <div class="max-w-3xl mx-auto py-6 sm:px-6 lg:px-8">
                            <div class="px-4 py-6 sm:px-0">
                                <h2 class="text-2xl py-4 font-bold text-gray-900">The Power Systems Team</h2>
                                <p class="py-2">
                                    <b>Robert Fleming:</b> {pageData.robertFlemingText}
                                </p>
                                <p class="py-2">
                                    <b>Max Garval:</b> {pageData.maxGarvalText}
                                </p>
                                <p class="py-2">
                                    {pageData.powerSystemsTeamText}
                                </p>
                                <img class="py-3" src="./img/Max_and_Tim_working.png" alt="Power Systems Team" />
                                <h2 class="text-1xl py-4 font-bold text-gray-900">Sensors</h2>
                                <p>
                                    {pageData.sensorsText}
                                </p>
                                <img class="py-3" src="./img/Arduino_diagram.png" alt="Arduino Diagram" />

                                <h2 class="text-1xl py-4 font-bold text-gray-900">Braking</h2>
                                <p>
                                    {pageData.brakingText}
                                </p>
                                <img class="py-3 px-48 h-96" src="./img/Relay_circuit.jpeg" alt="Relay Circuit" />

                                <h2 class="text-1xl py-4 font-bold text-gray-900">Motors</h2>
                                <p>
                                    {pageData.motorsText}
                                </p>

                            </div>
                        </div>
                    </main>
                </div>
            )
        } else {
            return <div className="PowerSystems"></div>
        }

    }
}
