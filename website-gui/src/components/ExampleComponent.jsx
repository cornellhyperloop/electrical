import React, { Component } from 'react';
import '../App.css';

export default class ExampleComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            test: 1
        }
    }

    componentDidMount() {
        console.log('Mounted!');
        console.log("PROPS: ", this.props);
    }

    componentDidUpdate() {
        console.log('Updated!');
        console.log("PROPS: ", this.props);
    }

    render() {
        return (
            <div className="Example-Component">
                <h1>Example Component</h1>
            </div>
        )
    }
}