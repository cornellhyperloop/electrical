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
                        <div class="max-w-3xl mx-auto py-6 sm:px-6 lg:px-8">
                            <div class="px-4 py-6 sm:px-0">
                                <h2 class="text-2xl py-4 font-bold text-gray-900">Communications SP '21</h2>
                                <p class="py-2">
                                    <b>David Wolfers:</b> {pageData.DavidWolfersText}
                                </p>
                                <p class="py-2">
                                    <b>Nandita Kathiresan:</b> {pageData.NanditaKathiresanText}
                                </p>
                                <p class="py-2">
                                    <b>Anoushka Kabra:</b> {pageData.AnoushkaKabraText}
                                </p>
                                <h2 class="text-1xl py-4 font-bold text-gray-900">Odroid</h2>
                                    {pageData.OdroidText}
                                <h2 class="text-1xl py-4 font-bold text-gray-900">ZCM</h2>
                                <p>
                                    {pageData.ZCMText}
                                </p>

                                <h2 class="text-1xl py-4 font-bold text-gray-900">Hyperloop GUI</h2>
                                <p>
                                    {pageData.GUIText}
                                </p>
                                <h2 class="text-1xl py-4 font-bold text-gray-900">Next Steps</h2>
                                <p>
                                    {pageData.NextText}
                                </p>
                                <br></br>
                                <a href="https://magazine.odroid.com/wp-content/uploads/odroid-c2-user-manual.pdf">Odroid C2 Manual</a>
                                <br>
                                </br>
                                <br></br>
                                <a href="http://zerocm.github.io/zcm/">ZCM</a>
                                <br></br> <br></br>
                                <a href="https://doc.qt.io/qtforpython/">PyQT Documentation</a>
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
