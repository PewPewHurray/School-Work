import styled from "styled-components";

const StyledTab = styled.div`
    border: 1px solid gray;
    background: ${props => props.bgColor};
    width: 180px;
    height: 50px;
    display: inline-block;
    padding-top: 10px;
    margin: 20px 5px 10px;
    `;

export default StyledTab;