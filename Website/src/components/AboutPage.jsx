import React, { Component } from 'react';
import '../App.css';
import * as d3 from 'd3';
import Modal from './info.jsx';

export default class AboutPage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            pageData: "test"
        }
    }

    componentDidMount() {
        fetch("./data/about.json").then(
            (result) => result.json()).then(
                (data) => this.setState({ pageData: data })
            )
    }

    componentDidUpdate() {
        this.renderVelocityGraph();
    }

    renderVelocityGraph() {
        let height = 500;
        let width = 500;
        let barWidth = 30;
        let colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00", "#ffff33", "#a65628", "#f781bf", "#999999"];

        let svg = d3.select('.velocityGraph')
            .append('svg')
            .attr('height', height)
            .attr('width', width)
        let margin = { top: 10, right: 10, bottom: 30, left: 50 };
        let chartWidth = width - margin.left - margin.right;
        let chartHeight = height - margin.top - margin.bottom;
        let annotations = svg.append('g')
            .attr('id', 'annotations')
        let chartArea = svg.append('g')
            .attr('id', 'chart-area')
            .attr('transform', `translate(${margin.left}, ${margin.top})`)

        let sprints = ["Sprint #1", "Sprint #2"];
        let workExtent = [0, 20];

        // Values order: Computing Systems, Power Systems, UI
        let data = [
            {
                sprint: "Sprint #1",
                values: [1, 4, 16]
            },
            {
                sprint: "Sprint #2",
                values: [5, 16, 19]
            }
        ]

        let xScale = d3.scaleBand().domain(sprints).range([0, chartWidth]).padding(0.05);
        let yScale = d3.scaleLinear().domain(workExtent).range([chartHeight, 0]);

        let xAxis = d3.axisBottom().scale(xScale);
        let xAxisG = annotations.append('g')
            .attr('class', 'x axis')
            .attr('transform', `translate(${margin.left}, ${chartHeight + margin.top + 10})`)
            .call(xAxis)

        let yAxis = d3.axisLeft(yScale);
        // let yGridlines = d3.axisLeft(yScale)
        //                    .tickSize(-chartWidth - 10)
        //                    .tickFormat('')

        annotations.append('g')
            .attr('class', 'y axis')
            .attr('transform', `translate(${margin.left - 10}, ${margin.top})`)
            .call(yAxis)
        // annotations.append('g')
        //            .attr('class', 'y gridlines')
        //            .attr('transform', `translate(${margin.left - 10}, ${margin.top})`)
        //            .call(yGridlines)

        let rects = chartArea.selectAll('rect.bar')
            .data(data)
            .join(
                enter => {
                    let bandwidth = xScale.bandwidth();
                    let barWidth = xScale.bandwidth() / (2 * sprints.length);

                    enter.append('rect')
                        .attr('class', 'bar')
                        .attr('fill', colors[0])
                        .attr('x', d => xScale(d.sprint) + bandwidth / 2 - (barWidth * 1.5))
                        .attr('y', d => yScale(d.values[0]))
                        .attr('width', barWidth)
                        .attr('height', d => chartHeight + margin.top - 10 - yScale(d.values[0]))

                    enter.append('rect')
                        .attr('class', 'bar')
                        .attr('fill', colors[1])
                        .attr('x', d => xScale(d.sprint) + bandwidth / 2 - (barWidth * 0.5))
                        .attr('y', d => yScale(d.values[1]))
                        .attr('width', barWidth)
                        .attr('height', d => chartHeight + margin.top - 10 - yScale(d.values[1]))

                    enter.append('rect')
                        .attr('class', 'bar')
                        .attr('fill', colors[2])
                        .attr('x', d => xScale(d.sprint) + bandwidth / 2 + (barWidth * 0.5))
                        .attr('y', d => yScale(d.values[2]))
                        .attr('width', barWidth)
                        .attr('height', d => chartHeight + margin.top - 10 - yScale(d.values[2]))
                }
            )



        console.log(rects);

        // let xScale = d3.scaleBand().domain(sprints).range([0, width]);
        // svg.append('g')
        //     .attr('transform', 'translate(30,' + height/1.2 + ')')
        //     .call(d3.axisBottom(xScale).tickSize(0));

        // let yScale = d3.scaleLinear().domain([0, 20]).range([height/1.2-10, 0]);
        // svg.append('g')
        //     .attr("transform", "translate(30, 10)")
        //     .call(d3.axisLeft(yScale))

        // // Computing Systems
        // svg.append('rect')
        //     .attr('x', 110)
        //     .attr('y', yScale(1)+10)
        //     .attr('height', height - yScale(1) - 93)
        //     .attr('width', barWidth)
        //     .style('fill', colors[0])

        // // Power Systems
        // svg.append('rect')
        //     .attr('x', 140)
        //     .attr('y', yScale(4)+10)
        //     .attr('height', height - yScale(4) - 93)
        //     .attr('width', barWidth)
        //     .style('fill', colors[1])

        // // UI
        // svg.append('rect')
        //     .attr('x', 170)
        //     .attr('y', yScale(16)+10)
        //     .attr('height', height - yScale(16) - 93)
        //     .attr('width', barWidth)
        //     .style('fill', colors[2])

        // // Legend
        // svg.append('rect')
        //     .attr('x', width - 190)
        //     .attr('y', 10)
        //     .attr('height', 20)
        //     .attr('width', 20)
        //     .style('fill', colors[0])

        // svg.append('rect')
        //     .attr('x', width - 190)
        //     .attr('y', 35)
        //     .attr('height', 20)
        //     .attr('width', 20)
        //     .style('fill', colors[1])

        // svg.append('rect')
        //     .attr('x', width - 190)
        //     .attr('y', 60)
        //     .attr('height', 20)
        //     .attr('width', 20)
        //     .style('fill', colors[2])

        // svg.append('text')
        //     .attr('x', width - 160)
        //     .attr('y', 20)
        //     .attr('dominant-baseline', 'middle')
        //     .attr('font-size', '18px')
        //     .text('Computing Systems')

        // svg.append('text')
        //     .attr('x', width - 160)
        //     .attr('y', 45)
        //     .attr('dominant-baseline', 'middle')
        //     .attr('font-size', '18px')
        //     .text('Power Systems')

        // svg.append('text')
        //     .attr('x', width - 160)
        //     .attr('y', 70)
        //     .attr('dominant-baseline', 'middle')
        //     .attr('font-size', '18px')
        //     .text('UI')
    }
    state = {
        show: false
      };
      showModal = e => {
        this.setState({
          show: !this.state.show
        });
      };

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
                                <article>
                                    <div class="flex flex-col bg-white m-auto p-auto">
                                        <h1 class="flex py-5 lg:px-20 md:px-10 px-5 lg:mx-40 md:mx-20 mx-5 font-bold text-4xl text-gray-800">Members</h1>
                                        <div class="flex overflow-x-scroll pb-10 hide-scroll-bar">
                                            <div class="flex flex-nowrap lg:ml-40 md:ml-20 ml-10 ">
                                                <div class="inline-block px-3">
                                                    <div class="w-64 h-64 max-w-xs overflow-hidden rounded-lg shadow-md bg-white hover:shadow-xl transition-shadow duration-300 ease-in-out">
                                                        <Modal onClose={this.showModal} show={this.state.show} />
                                                    </div>
                                                    <h2 class="text-1xl py-4 font-bold text-gray-900">Person1</h2>
                                                </div>
                                                <div class="inline-block px-3">
                                                    <div class="w-64 h-64 max-w-xs overflow-hidden rounded-lg shadow-md bg-white hover:shadow-xl transition-shadow duration-300 ease-in-out">
                                                        <img src="./img/sample.jpg" />
                                                    </div>
                                                    <h2 class="text-1xl py-4 font-bold text-gray-900">Person2</h2>
                                                </div>
                                                <div class="inline-block px-3">
                                                    <div class="w-64 h-64 max-w-xs overflow-hidden rounded-lg shadow-md bg-white hover:shadow-xl transition-shadow duration-300 ease-in-out">
                                                        <img src="./img/sample.jpg" />
                                                    </div>
                                                    <h2 class="text-1xl py-4 font-bold text-gray-900">Person3</h2>
                                                </div>
                                                <div class="inline-block px-3">
                                                    <div class="w-64 h-64 max-w-xs overflow-hidden rounded-lg shadow-md bg-white hover:shadow-xl transition-shadow duration-300 ease-in-out"></div>
                                                    <h2 class="text-1xl py-4 font-bold text-gray-900">Person4</h2>
                                                </div>
                                                <div class="inline-block px-3">
                                                    <div class="w-64 h-64 max-w-xs overflow-hidden rounded-lg shadow-md bg-white hover:shadow-xl transition-shadow duration-300 ease-in-out"></div>
                                                    <h2 class="text-1xl py-4 font-bold text-gray-900">Person5</h2>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </article>
                                <h2 class="text-2xl py-4 font-bold text-gray-900">Electrical Team Overview</h2>
                                <p>{pageData.overviewText}</p>
                                <h2 class="text-2xl py-4 font-bold text-gray-900">Current Team Members</h2>
                                <img src="./img/Team.png" alt="Team Members" />
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
                                <img src="./img/AgileWorkshop.png" alt="Agile Workshop" />

                                <h2 class="text-2xl py-4 font-bold text-gray-900">Work Sessions</h2>
                                <p>{pageData.workSessionsText}</p>
                                <img class="px-48 py-4 h-96" src="./img/ELL.jpeg" alt="ELL" />

                                <h2 class="text-2xl py-4 font-bold text-gray-900">Velocity</h2>
                                <p class="pb-4">{pageData.velocityText}</p>
                                <div class="velocityGraph"></div>
                                <div>
                                </div>
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
