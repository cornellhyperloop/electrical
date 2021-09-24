import React, { Component } from 'react';
import '../App.css';
import * as d3 from 'd3';

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
        
        this.renderVelocityGraph();
    }
    
    renderVelocityGraph() {
        let height = 500;
        let width = 500;
        let barWidth = 30;
        let colors = ["#e41a1c","#377eb8","#4daf4a","#984ea3","#ff7f00","#ffff33","#a65628","#f781bf","#999999"];

        let svg = d3.select('.velocityGraph')
                    .append('svg')
                    .attr('height', height)
                    .attr('width', width)
                    //.style('border', '1px solid black')
        
        let sprints = ["Sprint #1", "Sprint #2"];
        let xScale = d3.scaleBand().domain(sprints).range([0, width]);
        svg.append('g')
            .attr('transform', 'translate(30,' + height/1.2 + ')')
            .call(d3.axisBottom(xScale).tickSize(0));

        let yScale = d3.scaleLinear().domain([0, 20]).range([height/1.2-10, 0]);
        svg.append('g')
            .attr("transform", "translate(30, 10)")
            .call(d3.axisLeft(yScale))
        
        // Computing Systems
        svg.append('rect')
            .attr('x', 110)
            .attr('y', yScale(1)+10)
            .attr('height', height - yScale(1) - 93)
            .attr('width', barWidth)
            .style('fill', colors[0])
        
        // Power Systems
        svg.append('rect')
            .attr('x', 140)
            .attr('y', yScale(4)+10)
            .attr('height', height - yScale(4) - 93)
            .attr('width', barWidth)
            .style('fill', colors[1])
        
        // UI
        svg.append('rect')
            .attr('x', 170)
            .attr('y', yScale(16)+10)
            .attr('height', height - yScale(16) - 93)
            .attr('width', barWidth)
            .style('fill', colors[2])
        
        // Legend
        svg.append('rect')
            .attr('x', width - 190)
            .attr('y', 10)
            .attr('height', 20)
            .attr('width', 20)
            .style('fill', colors[0])
        
        svg.append('rect')
            .attr('x', width - 190)
            .attr('y', 35)
            .attr('height', 20)
            .attr('width', 20)
            .style('fill', colors[1])
        
        svg.append('rect')
            .attr('x', width - 190)
            .attr('y', 60)
            .attr('height', 20)
            .attr('width', 20)
            .style('fill', colors[2])
        
        svg.append('text')
            .attr('x', width - 160)
            .attr('y', 20)
            .attr('dominant-baseline', 'middle')
            .attr('font-size', '18px')
            .text('Computing Systems')
        
        svg.append('text')
            .attr('x', width - 160)
            .attr('y', 45)
            .attr('dominant-baseline', 'middle')
            .attr('font-size', '18px')
            .text('Power Systems')
        
        svg.append('text')
            .attr('x', width - 160)
            .attr('y', 70)
            .attr('dominant-baseline', 'middle')
            .attr('font-size', '18px')
            .text('UI')
    }

    render() {
        if (this.props.display === 1) {
            let pageData = this.state.pageData;
            return (
                <div className="AboutPage">
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
                                <p class="pb-4">{pageData.velocityText}</p>
                                <div class="velocityGraph"></div>
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
