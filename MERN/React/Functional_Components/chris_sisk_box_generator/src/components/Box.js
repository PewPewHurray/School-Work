import {useState} from "react";
import styles from "./Box.module.css";
const Box = (props) => {
    const [color, setColor] = useState("");;
    const [colorError, setColorError] = useState("Required");
    const [boxList, setBoxList] = useState([]);
    const [heightAndWidth, setHeightAndWidth] = useState("");
    const [heightAndWidthError, setHeightAndWidthError] = useState("Required");

    const handleColorChange = (e) => {
        setColor(e.target.value);
        if(e.target.value.length < 1){
            setColorError("Required");
        } else {
            setColorError("");
        }
    }

    const handleHeightAndWidthChange = (e) => {
        setHeightAndWidth(e.target.value);
        if(e.target.value == null){
            setHeightAndWidthError("Required")
        } else {
            setHeightAndWidthError("")
        }
    }

    const createBox = (e) => {
        e.preventDefault();
        const heightAndWidthInPX = heightAndWidth + "px";
        const boxObj = {"boxColor":color,"boxHeightandWidth":heightAndWidthInPX};
        setBoxList(() => [...boxList, boxObj]);
        setColor("");
        setHeightAndWidth("");
    }
    return (
        <div>
            {/* <h1>{JSON.stringify(color)}</h1>
            <h1>{JSON.stringify(heightAndWidth)}</h1>
            <h1>{JSON.stringify(boxList)}</h1> */}
            <div>
                <form onSubmit={createBox}>
                    <label>Color:</label>
                    <input id="color" type="text" value={color} onChange={(e) => handleColorChange(e)}/>
                    {colorError ? <p className={styles.error}>{colorError}</p>:null}
                    <label>Height and Width:</label>
                    <input id="heightandwidth" type="number" value={heightAndWidth} onChange={(e) => handleHeightAndWidthChange(e)} />
                    {heightAndWidthError ? <p className={styles.error}>{heightAndWidthError}</p>:null}
                    {colorError ? <input type="submit" value="Add" disabled /> : heightAndWidthError ? <input type="submit" value="Add" disabled /> : <input type="submit" value="Add"/>}
                </form>
            </div>
            <div>
                {boxList.map((box, index) =>
                    <div key={index} className={styles.box} style={{backgroundColor: box.boxColor, height: box.boxHeightandWidth, width: box.boxHeightandWidth}}></div>
                )}
            </div>
        </div>
    );
}

export default Box