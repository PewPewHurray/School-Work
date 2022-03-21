import './App.css';
import { useState } from 'react'; 
import Tabs from './components/Tabs';
import Results from './components/Results';

function App() {
  const [displayContent, setDisplayContent] = useState("");
  return (
    <div className="App">
      <Tabs setDisplayContent={setDisplayContent} displayContent={displayContent}/>
      <Results displayContent={displayContent}/>
    </div>
  );
}

export default App;
