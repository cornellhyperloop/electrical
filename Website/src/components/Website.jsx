import React, { Component } from 'react';
import Navbar from './Navbar';
import HomePage from './HomePage';
import AboutPage from './AboutPage';
import PowerSystems from './PowerSystems';
import CommunicationsSP21 from './CommunicationsSP21';
import PowerSystemsSP21 from './PowerSystemsSP21';
import SensorsSP21 from './SensorsSP21';
import '../App.css';

export default class Website extends Component {
    constructor(props) {
        super(props);
        this.state =  {
            page: 0
        }
    }

    render() {
        return (
            <div className="Website">
                <Navbar toCallBack={(childState) => this.setState({page: childState.page})}/>
                <HomePage display={this.state.page} />
                <AboutPage display={this.state.page} />
                <PowerSystems display={this.state.page} />
                <CommunicationsSP21 display={this.state.page} />
                <PowerSystemsSP21 display={this.state.page} />
                <SensorsSP21 display={this.state.page} />
            </div>
        )
    }
}