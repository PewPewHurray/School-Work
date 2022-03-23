import './App.css';
import Display from './components/Display';
import Todo from './components/Todo';
import {useState, useEffect} from "react";

function App() {
  const [todoArray, setTodoArray] = useState(() => {
    const saved = localStorage.getItem("todoArray");
    const initialValue = JSON.parse(saved);
    return initialValue || [];
  });

  useEffect(() => {
    localStorage.setItem("todoArray", JSON.stringify(todoArray));
  }, [todoArray]);

  return (
    <div className="App">
      <Todo todoArray={todoArray} setTodoArray={setTodoArray}>
        <Display todoArray={todoArray} setTodoArray={setTodoArray} />
      </Todo>
    </div>
  );
}

export default App;
