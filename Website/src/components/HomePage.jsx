import React, { Component } from 'react';
import '../App.css';

export default class HomePage extends Component {
    render() {
        if (this.props.display === 0) {
            return (
                <div className="HomePage">
                    <header class="bg-white shadow">
                        <div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
                            <h1 class="text-3xl font-bold text-gray-900">Welcome to the Electrical Team Website!</h1>
                        </div>
                    </header>
                    <main>
                        <div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
                            <div class="px-4 py-6 sm:px-0">
                                <div class="border-4 border-dashed border-gray-200 rounded-lg h-96">
                                    <h1 class="text-blue-400 font-extrabold">Cornell Hyperloop</h1>
                                    <p class="tracking-widest">The electrical team is the best team.</p>
                                </div>
                            </div>
                        </div>
                    </main>
                </div>
            )
        } else {
            return <div className="HomePage"></div>
        }

    }
}
