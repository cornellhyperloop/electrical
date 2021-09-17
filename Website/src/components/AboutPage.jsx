import React, { Component } from 'react';
import '../App.css';

export default class AboutPage extends Component {
    constructor(props) {
        super(props);
        this.state =  {
            pageData: "test"
        }
    }
    componentDidMount() {
        fetch("./data/about.json").then(
            (result) => result.json()).then(
            (data) => this.setState({pageData: data}))
    }

    render() {
        if (this.props.display === 1) {
            let pageData = this.state.pageData;
            return (
                <div className="HomePage">
                    <header class="bg-white shadow">
                        <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
                            <h1 class="text-3xl font-bold text-gray-900">{pageData.header}</h1>
                        </div>
                    </header>
                    <main>
                        <div class="max-w-3xl mx-auto py-6 sm:px-6 lg:px-8">
                            <div class="px-4 py-6 sm:px-0">
                                <h2 class="text-2xl py-4 font-bold text-gray-900">Electrical Team Overview</h2>
                                <p>{pageData.overviewText}</p>
                                <h2 class="text-2xl py-4 font-bold text-gray-900">Current Team Members</h2>
                                <img src="https://hyperloop.cornell.edu/electrical/img/Team.png" alt="Team Members" />
                                <h2 class="text-2xl pt-4 font-bold text-gray-900">Leadership</h2>
                                <ul class="list-disc px-5 py-4">
                                    <li>{pageData.electricalLead}: Electrical Lead</li>
                                    <li>{pageData.hardwareLead}: Hardware Lead</li>
                                    <li>{pageData.softwareLead}: Software Lead</li>
                                </ul>

                                <h2 class="text-2xl font-bold text-gray-900">Computing Systems</h2>
                                <ul class="list-disc px-5 py-4">
                                    <li>Michael Guan</li>
                                    <li>David Wolfers</li>
                                    <li>Nandita Kathiresan</li>
                                </ul>

                                <h2 class="text-2xl font-bold text-gray-900">GUI</h2>
                                <ul class="list-disc px-5 py-4">
                                    <li>Ronin Sharma</li>
                                </ul>

                                <h2 class="text-2xl font-bold text-gray-900">Power Systems</h2>
                                <ul class="list-disc px-5 py-4">
                                    <li>Tim Tran</li>
                                    <li>Robert Fleming</li>
                                    <li>Max Garval</li>
                                </ul>

                                <h2 class="text-2xl font-bold text-gray-900">Workshops</h2>
                                <p class="py-4">{pageData.workshopsText}</p>
                                <img src="https://hyperloop.cornell.edu/electrical/img/AgileWorkshop.png" alt="Agile Workshop" />

                                <h2 class="text-2xl py-4 font-bold text-gray-900">Work Sessions</h2>
                                <p>{pageData.workSessionsText}</p>
                                <img class="px-48 py-4 h-96" src="https://hyperloop.cornell.edu/electrical/img/ELL.jpg" alt="ELL" />

                                <h2 class="text-2xl py-4 font-bold text-gray-900">Velocity</h2>
                                <p>{pageData.velocityText}</p>
                            </div>
                        </div>
                    </main>
                </div>
            )
        } else {
            return <div className="AboutPage"></div>
        }

    }
}
