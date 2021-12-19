function acceptCookies(id){
    var element = document.querySelector(id);
    element.remove();
}

var temp = "°C";

function selectTemp(element, day1High, day1Low, day2High, day2Low, day3High, day3Low, day4High, day4Low){
    var h1 = document.querySelector(day1High);
    var l1 = document.querySelector(day1Low);
    var h2 = document.querySelector(day2High);
    var l2 = document.querySelector(day2Low);
    var h3 = document.querySelector(day3High);
    var l3 = document.querySelector(day3Low);
    var h4 = document.querySelector(day4High);
    var l4 = document.querySelector(day4Low);

    if (temp == "°C"){
        temp = element.value;
        h1.innerText = Math.round(h1.innerText * 1.8 + 32);
        l1.innerText = Math.round(l1.innerText * 1.8 + 32);
        h2.innerText = Math.round(h2.innerText * 1.8 + 32);
        l2.innerText = Math.round(l2.innerText * 1.8 + 32);
        h3.innerText = Math.round(h3.innerText * 1.8 + 32);
        l3.innerText = Math.round(l3.innerText * 1.8 + 32);
        h4.innerText = Math.round(h4.innerText * 1.8 + 32);
        l4.innerText = Math.round(l4.innerText * 1.8 + 32);
    }
    
    else{
        temp = element.value;
        h1.innerText = Math.round((h1.innerText-32)/1.8);
        l1.innerText = Math.round((l1.innerText-32)/1.8);
        h2.innerText = Math.round((h2.innerText-32)/1.8);
        l2.innerText = Math.round((l2.innerText-32)/1.8);
        h3.innerText = Math.round((h3.innerText-32)/1.8);
        l3.innerText = Math.round((l3.innerText-32)/1.8);
        h4.innerText = Math.round((h4.innerText-32)/1.8);
        l4.innerText = Math.round((l4.innerText-32)/1.8);
    }
}