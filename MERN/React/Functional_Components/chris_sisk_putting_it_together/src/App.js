import './App.css';
import Person from "./components/Person"

function App() {
  return (
    <div className="App">
      <Person firstName={"Chris"} lastName={"Sisk"} age={32} hairColor={"Brown"}/>
      <Person firstName={"John"} lastName={"Smith"} age={35} hairColor={"Black"}/>
      <Person firstName={"Jane"} lastName={"Doe"} age={29} hairColor={"Red"}/>
      <Person firstName={"Billy"} lastName={"Bob"} age={70} hairColor={"Gray"}/>
    </div>
  );
}

export default App;
