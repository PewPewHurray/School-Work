import { useContext } from "react";
import MyContext from "../context/MyContext";

const Navbar = (props) => {
    const context = useContext(MyContext)
    return (
        <div className="navbar">
            <h1>Hi {context.name}!</h1>
        </div>
    )
}

export default Navbar;