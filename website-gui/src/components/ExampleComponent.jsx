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
    }

    componentDidUpdate() {
        console.log('Updated!');
    }

    render() {
        return (
            <div className="Example-Component">
                <h1>Example Component</h1>
            </div>
        )
    }
}