// FIZZBUZZ!
// Write a function that checks each number from 1 to 25 and prints "Fizz" for each number that is evenly divisible by 3, 
// "Buzz" for each number that is evenly divisible by 5, and "FizzBuzz" for each 
// number that is evenly divisible by both 3 and 5.


function fizzBuzz(){
    // YOUR CODE HERE
    for (var i = 1; i <= 25; i++){
        // if (i % 3 === 0){
        //     console.log(i, "Fizz");
        //     if (i % 5 === 0){
        //         console.log(i, "Buzz");
        //         console.log(i, "FizzBuzz");
        //     }
        // }

        // else if (i % 5 === 0){
        //     console.log(i, "Buzz");
        // }
        
        if (i % 3 === 0 && i % 5 === 0){
            console.log("FizzBuzz");
        }
        else if (i % 3 === 0){
            console.log("Fizz");
        }
        else if (i % 5 === 0){
            console.log("Buzz");
        }
    }
}


// TEST
fizzBuzz();