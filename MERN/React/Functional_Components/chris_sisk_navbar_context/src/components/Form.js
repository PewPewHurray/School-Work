import { useContext } from "react";
import MyContext from "../context/MyContext";

const Form = (props) => {
    const context = useContext(MyContext);

    return (
        <div>
            <label className="name">
                Your Name:
                <input type="text" className="nameInput" onChange={(e) => context.setName(e.target.value)} value={context.name} />
            </label>
        </div>
    )
}

export default Form;