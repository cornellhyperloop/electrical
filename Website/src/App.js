import logo from './logo.svg';
import Website from './components/Website';
import './App.css';
import HomePage from './components/HomePage';
import Members from './components/Members';
import Team from './components/Team';
import Apply from './components/Apply';

import { Route,Routes,BrowserRouter} from 'react-router-dom';
import Donate from './components/Donate';
import CompetitionPage from './components/Competition';


function App() {

  return (
    <div className="App" class="p-0 items-center justify-center">
          <Routes>
        <Route path="/" element={  <HomePage/>}  >
        
          </Route>
          <Route  path="/members" element={<Members/>}/>
          <Route  path="/team" element={<Team/>}/>
          <Route  path="/apply" element={<Apply/>}/>
          <Route  path="/donate" element={<Donate/>}/>
          <Route  path="/competition" element={<CompetitionPage/>}/>
          

          </Routes>

      </div>
  );
}

export default App;
