import logo from './logo.svg';
import Website from './components/Website';
import './App.css';
import HomePage from './components/HomePage';
import Members from './components/Members';
import Team from './components/Team';
import Apply from './components/Apply';
import Mechanical2 from './components/Mechanical2'
import Electrical from './components/Electrical'
import Business from './components/Business'
import { Route, Routes, BrowserRouter } from 'react-router-dom';
import Donate from './components/Donate';
import CompetitionPage from './components/Competition';


function App() {

  return (
    <div className="App" class="p-0 items-center justify-center">
      <Routes>

 
        <Route path="/competition" element={<CompetitionPage />} />
        <Route path="/mechanical" element={<Mechanical2 />} />
        <Route path="/electrical" element={<Electrical />} />
        <Route path="/business" element={<Business />} />

        <Route path="/members" element={<Members />} />
        <Route path="/team" element={<Team />} />
        <Route path="/apply" element={<Apply />} />
        <Route path="/donate" element={<Donate />} />


        <Route path="/" element={<HomePage />}  >

</Route>



      </Routes>

    </div>
  );
}

export default App;
