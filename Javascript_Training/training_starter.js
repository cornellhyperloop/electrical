// Var, let, const ---









    
// Regular functions and arrow functions ---












// Modify HTML/CSS code ---















// Asynchronous Javascript: Promises, Async/Await ---

// Promises
let promise = new Promise((resolve, reject) => {
    let count = 0;
    let max = 9999;
    while (count < max) count += 1;

    if (count == max) {
        resolve('Correct');
    } else {
        reject('Incorrect')
    }
})

// Add code here


console.log('After Promise')

// Async/Await - cleaner form of Promises (don't need to chain .then)



// Miscellaneous: : == vs. ===, array/object destructuring, array methods ---


