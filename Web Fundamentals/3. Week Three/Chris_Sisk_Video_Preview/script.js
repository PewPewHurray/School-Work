console.log("page loaded...");

function mouseOver(element){
    element.play();
    element.muted=true;
}

function mouseLeave(element){
    element.pause();
}