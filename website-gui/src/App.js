import logo from './logo.svg';
import ExampleComponent from './components/ExampleComponent';
import Navbar from './components/Navbar';
import './App.css';

function App() {

  return (
    <div className="App" class="p-6 items-center justify-center">
      <Navbar toCallBack={(childState) => console.log(childState)}/>
      <ExampleComponent />
    </div>
  );
}

export default App;
