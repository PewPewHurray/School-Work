const tossCoin = () => {
    return Math.random() > 0.5 ? "heads" : "tails";
}
const fiveHeads = new Promise((resolve, reject) => {
    let heads = 0;
    let attempts = 0;
    let maxAttempts = 100;
    while (attempts <= 100 && heads < 5){
        attempts++;
        const result = tossCoin();
        console.log(result)
        if(result === "heads"){
            heads++;
        } else {
            heads = 0;
        }
    }
    if (attempts <= maxAttempts){
        resolve(`It took ${attempts} attempts to get 5 heads in a row.`);
    } else {
        reject("After 100 attempts did not get 5 heads in a row.");
    }
});


fiveHeads
    .then( res => console.log(res))
    .catch ( err => console.log(err));
console.log("End of all the code");