const tossCoin = () => {
    return Math.random() > 0.5 ? "heads" : "tails";
}
const fiveHeads = new Promise((resolve, reject) => {
    let heads = 0;
    let attempts = 0;
    while (attempts <= 100 && heads < 5){
        attempts++;
        const result = tossCoin();
        if(result === "heads"){
            heads++;
        } else {
            heads = 0;
        }
        if (heads === 5){
            resolve(`It took ${attempts} attempts to get 5 heads in a row.`);
        } else if (attempts === 100) {
            reject("After 100 attempts did not get 5 heads in a row.");
        }
    }
});


fiveHeads
    .then( res => console.log(res))
    .catch ( err => console.log(err));
console.log("End of all the code");