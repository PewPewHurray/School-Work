import StyledContentBox from './StyledContentBox';

const Results = (props) => {
    const {displayContent} = props;
    return (
        <StyledContentBox>
            <h3>{displayContent}</h3>
        </StyledContentBox>
    );
}

export default Results;