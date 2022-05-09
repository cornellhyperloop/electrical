import React, { Component } from 'react';
import '../App.css';

export default class CommunicationsSP21 extends Component {
    constructor(props) {
        super(props);
        this.state = {
            pageData: "test"
        }
    }

    /* need to change this */
    componentDidMount() {
        fetch("./data/CommunicationsSP21.json").then(
            (result) => result.json()).then(
                (data) => this.setState({ pageData: data })
            )
    }

    render() {
        if (this.props.display === 5) {
            let pageData = this.state.pageData;
            return (
                <div className="CommunicationsSP21">
                    <header class="bg-white shadow">
                        <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
                            <h1 class="text-3xl font-bold text-gray-900">{pageData.header}</h1>
                        </div>
                    </header>
                    <main>
                        <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
                            <div class="px-4 py-6 sm:px-0">
                                <h2 class="text-2xl py-4 font-bold text-gray-900">Team Members and Their Works</h2>
                                <div style={{display:'flex', overflowX: 'scroll'}}>
                                    <div class="image-cap-container">
                                        <img src={pageData.Members.a.image} alt="Power Systems Team"/>
                                        <div class="image-caption">
                                            <p><b>{pageData.Members.a.name}</b> {pageData.Members.a.text}</p>
                                        </div>
                                    </div>
                                    <div class="image-cap-container">
                                        <img src={pageData.Members.b.image} alt="Power Systems Team" />
                                        <div class="image-caption">
                                            <p><b>{pageData.Members.b.name}</b> {pageData.Members.b.text}</p>
                                        </div>
                                    </div>
                                    <div class="image-cap-container">
                                        <img src={pageData.Members.c.image} alt="Power Systems Team" />
                                        <div class="image-caption">
                                            <p><b>{pageData.Members.c.name}</b> {pageData.Members.c.text}</p>
                                        </div>
                                    </div>
                                    <div class="image-cap-container">
                                        <img src={pageData.Members.d.image} alt="Power Systems Team" />
                                        <div class="image-caption">
                                            <p><b>{pageData.Members.d.name}</b> {pageData.Members.d.text}</p>
                                        </div>
                                    </div>
                                    <div class="image-cap-container">
                                        <img src={pageData.Members.e.image} alt="Power Systems Team" />
                                        <div class="image-caption">
                                            <p><b>{pageData.Members.e.name}</b> {pageData.Members.e.text}</p>
                                        </div>
                                    </div>
                                </div>

                                <br></br>
                                <br></br>
                            <h2 class="text-2xl py-4 font-bold text-gray-900">Projects from this Semester</h2>
                                <div class='projectcols'>
                                    <h2 class="text-1xl py-4 font-bold text-gray-900">{pageData.Projects.a.name}</h2>
                                        <p>{pageData.Projects.a.text}</p><br></br>
                                        <button class="button">
                                            <span><a href={pageData.Projects.a.link}>{pageData.Projects.a.linkText}</a></span>
                                        </button>
                                        <h2 class="text-1xl py-4 font-bold text-gray-900">{pageData.Projects.b.name}</h2>
                                        <p>{pageData.Projects.b.text}</p><br></br>
                                        <button class="button">
                                            <span><a href={pageData.Projects.b.link}>{pageData.Projects.b.linkText}</a></span>
                                        </button>
                                        <h2 class="text-1xl py-4 font-bold text-gray-900">{pageData.Projects.c.name}</h2>
                                        <p>{pageData.Projects.c.text}</p><br></br>
                                        <button class="button">
                                            <span><a href={pageData.Projects.c.link}>{pageData.Projects.c.linkText}</a></span>
                                        </button>
                                </div>

                                <h2 class="text-2xl py-4 font-bold text-gray-900">Next Steps</h2>
                                <p>{pageData.NextText}</p>
                                <br></br>
                            </div>
                        </div>
                    </main>
                </div>
            )
        } else {
            return <div className="CommunicationsSP21"></div>
        }

    }
}
