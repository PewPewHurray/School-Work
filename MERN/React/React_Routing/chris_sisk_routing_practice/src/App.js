import './App.css';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import Text from './components/Text';
import Welcome from './components/Welcome';

function App() {
  return (
    <BrowserRouter>
      <div className="App">
        <Routes>
          <Route path="/home" element={<Welcome />} />
          <Route path="/:text" element={<Text />} />
          <Route path="/:text/:fontColor/:bgColor" element={<Text />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
