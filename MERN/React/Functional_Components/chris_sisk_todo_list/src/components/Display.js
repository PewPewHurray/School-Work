const Display = (props) => {
    const {todoArray, setTodoArray} = props;

    const handleDelete = (e, selectedTask) => {
        setTodoArray(todoArray.filter((item, index) => index !== selectedTask));
    }

    const handleCheckboxChange = (e, selectedTask) => {
        setTodoArray(todoArray.map((item, index) => {
            if(index === selectedTask){
                const currentItem = {...item, selected: !item.selected};
                return currentItem;
            }
            return item;
        }));
    }
    
    return (
        <ul>
        {todoArray.map((item, index) => {
            const todoClasses = [];

            if (item.selected){
                todoClasses.push(...todoClasses, "checked")
            }

            return (
                <li key={index} className={todoClasses.join(" ")}>{item.task}
                    <input className="checkbox" type="checkbox" checked={item.selected} onChange={(e) => handleCheckboxChange(e, index)} />
                    <input className="delete" type="button" value="Delete" onClick={(e) => handleDelete(e, index)} />
                </li>
            )
        })}
        </ul>
    );
}

export default Display;