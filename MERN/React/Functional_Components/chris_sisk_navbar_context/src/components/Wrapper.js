import MyContext from "../context/MyContext";
import {useState} from "react";

const Wrapper = (props)  => {
    const [name, setName] = useState("");

    return (
        <MyContext.Provider value={{name, setName}}>
            {props.children}
        </MyContext.Provider>
    )
}

export default Wrapper;