import {useState} from "react";

const Todo = (props) => {
    const {todoArray, setTodoArray} = props;
    
    const [todoItem, setTodoItem] = useState("");
    const [todoItemError, setTodoItemError] = useState("Required");

    const handleTodoItemChange = (e) => {
        setTodoItem(e.target.value);
        if (e.target.value.length < 1){
            setTodoItemError("Required");
        } else {
            setTodoItemError("");
        };
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        setTodoArray(() => [...todoArray, {task: todoItem, selected: false}]);
        setTodoItem("");
        setTodoItemError("Required")
    };

    return (
        <div className="tododiv">
            <form onSubmit={(e) => handleSubmit(e)}>
                {todoItemError?<p className="error">{todoItemError}</p>:null}
                <input type="text" onChange={(e) => handleTodoItemChange(e)} value={todoItem} />
                {todoItemError?
                    <input type="submit" value="Add" disabled/>:
                    <input type="submit" value="Add" />}
            </form>
            {props.children}
        </div>
    );
};

export default Todo;