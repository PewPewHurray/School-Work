import {useState} from "react";
import StyledTab from "./StyledTab";
import StyledTabText from "./StyledTabText";

const Tabs  = (props) => {
    const {displayContent, setDisplayContent} = props;
    const tabsArray = [
        {header: "Tab 1", content: "Tab 1 content is showing here.", bgColor: "white", textColor: "black"},
        {header: "Tab 2", content: "Tab 2 content is showing here.", bgColor: "white", textColor: "black"},
        {header: "Tab 3", content: "Tab 3 content is showing here.", bgColor: "white", textColor: "black"}
    ];
    const [allTabs, setAllTabs] = useState(tabsArray);

    const handleTabClick = (e) => {
        setAllTabs(allTabs.map((tab, index) => {
            if(index == e.target.id){
                setDisplayContent(tab.content);
                tab.bgColor = "black";
                tab.textColor = "white";
            }
            else {
                tab.bgColor = "white";
                tab.textColor = "black";
            };
            return tab;
        }));
    }

    return (
        <div>
            {allTabs.map((tab, index) =>
                <StyledTab key={index} bgColor={tab.bgColor}>
                    <StyledTabText id={index} onClick={(e) => handleTabClick(e)} textColor={tab.textColor}>{tab.header}</StyledTabText>
                </StyledTab>)}
        </div>
    );
}

export default Tabs;