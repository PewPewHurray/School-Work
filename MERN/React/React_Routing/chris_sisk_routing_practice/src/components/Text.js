import { useParams } from "react-router-dom";

const Text = (props) => {
    const {text, fontColor, bgColor} = useParams();

    return (
        <div>
            {isNaN(text)
                ?<h2 style={{color: fontColor, backgroundColor: bgColor}}>The word is: {text}</h2>
                :<h2>The number is: {text}</h2>}
        </div>
    );
}

export default Text;