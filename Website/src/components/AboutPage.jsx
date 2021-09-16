import React, { Component } from 'react';
import '../App.css';

export default class AboutPage extends Component {
    render() {
        if (this.props.display === 1) {
            return (
                <div className="HomePage">
                    <header class="bg-white shadow">
                        <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
                            <h1 class="text-3xl font-bold text-gray-900">Meet the Team!</h1>
                        </div>
                    </header>
                    <main>
                        <div class="max-w-3xl mx-auto py-6 sm:px-6 lg:px-8">
                            <div class="px-4 py-6 sm:px-0">
                                <h2 class="text-2xl py-4 font-bold text-gray-900">Electrical Team Overview</h2>
                                <p>
                                    The Electrical Team contains two subteams: Hardware and Software. 
                                    This semester, hardware and software worked closely on three major projects: 
                                    Computing Systems, GUI, and Power Systems. Each project's description and 
                                    semester accomplishments can be found on its individual page.
                                </p>
                                <h2 class="text-2xl py-4 font-bold text-gray-900">Current Team Members</h2>
                                <img src="https://hyperloop.cornell.edu/electrical/img/Team.png" alt="Team Members" />
                                <h2 class="text-2xl pt-4 font-bold text-gray-900">Leadership</h2>
                                <ul class="list-disc px-5 py-4">
                                    <li>Tim Tran: Electrical Lead</li>
                                    <li>Ronin Sharma: Hardware Lead</li>
                                    <li>Michael Guan: Software Lead</li>
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
                                <p class="py-4">
                                    This semester we held three workshops based on members' interests. The three workshops 
                                    were about Github, Arduino, and Agile. The image below depicts members learning about 
                                    the Scrum methodology during the Agile Workshop.
                                </p>
                                <img src="https://hyperloop.cornell.edu/electrical/img/AgileWorkshop.png" alt="Agile Workshop" />

                                <h2 class="text-2xl py-4 font-bold text-gray-900">Work Sessions</h2>
                                <p>
                                    With the limited time provided to us by the University, team members meet up in the ELL 
                                    to build towards a more sustainable mode of transportation.
                                </p>
                                <img class="px-48 py-4 h-96" src="https://hyperloop.cornell.edu/electrical/img/ELL.jpg" alt="ELL" />
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
