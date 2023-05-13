import logo from './logo.svg';
import Website from './components/Website';
import './App.css';
import HomePage from './components/HomePage';
import Members from './components/Members';
import Team from './components/Team';
import Apply from './components/Apply';

import { Route,Routes,BrowserRouter} from 'react-router-dom';
import Donate from './components/Donate';


function App() {

  return (
    <div className="App" class="p-0 items-center justify-center">
          <Routes>
        <Route exact path="/" element={  <HomePage/>}  >
        
          </Route>
          <Route exact path="/members" element={<Members/>}/>
          <Route exact path="/team" element={<Team/>}/>
          <Route  exact path="/apply" element={<Apply/>}/>
          <Route exact path="/donate" element={<Donate/>}/>

          </Routes>

      </div>
  );
}

export default App;
