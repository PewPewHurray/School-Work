function changeName(id){
    var element = document.querySelector(id);
    element.innerText = "Hermione Granger"
}

function removeRequest(id1, id2, id3){
    var element1 = document.querySelector(id1);
    var element2 = document.querySelector(id2);
    var element3 = document.querySelector(id3);
    element1.remove();
    element2.innerHTML--;
    element3.innerHTML++;
}