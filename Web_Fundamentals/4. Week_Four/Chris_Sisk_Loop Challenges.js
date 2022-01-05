//Challenge 1
console.log("Chllenge 1");
for(var i = 1; i <= 20; i++){
    if(i % 2 === 1){
        console.log(i);
    }
}

console.log("")

//Challenge 2
console.log("Challenge 2");
for(var i = 100; i >= 0; i--){
    if(i % 2 === 0){
        console.log(i);
    }
}

console.log("");

//Challenge 3
console.log("Challenge 3");
var arr = [4, 2.5, 1, -0.5, -2, -3.5];
for(var i = 0; i < arr.length; i++){
    var x = 0;
    x = arr[i];
    console.log(x);
}

console.log("");

//Challenge 4
console.log("Challenge 4");
var sum = 0;
var i4 = 1;
while(i4 <= 100){
    sum += i4;
    i4++
}
console.log(sum);

console.log("");

//Challenge 5
console.log("Challenge 5");
var product = 1;
var i5 = 1;
while(i5 <= 12){
    product *= i5;
    i5++
}
console.log(product);