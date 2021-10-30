// Var, let, const ---

// let y;
// const z = 5;

// if (true) {
//     // var x = 5;
//     y = 6;
//     z = 7;

//     // console.log(x);
// //     console.log("within if", y);
// //     console.log("within if", z);
// // }

// console.log(x);
// console.log(y);
// console.log(z);



// x = 5; print(x)

// let x = {
//     field1: 1,
//     field2: 'Tim'
// }

// console.log(x);
// console.log(x.field1);
// console.log(x['field2'])

    
// Regular functions and arrow functions ---

// function printHello() {
//     console.log('hello');
// }

// let printHello = () => {
//     console.log('hello')
// }

// let add1 = x => x + 1;
// let add2Num = (x, y) => x + y;

// printHello()

// function obj(obj)








// Modify HTML/CSS code ---

let element = document.querySelector('.text');
console.log(element)

element.textContent = 'new text';

let button = document.querySelector('#button')
console.log(button)

let inputField = document.querySelector('#input-field')
console.log(inputField)

button.addEventListener('click', () => {
    element.textContent = inputField.value;
    element.style.color = 'red';
})




// Miscellaneous: == vs. ===, array/object destructuring, array methods ---
if (4 == 'x04') {
    console.log(0x04)
}

if (4 === '4') {
    console.log(0x04)
}

let x = [1, 2, 3];

let [y, ...z] = x

console.log(y)
console.log(z)

let a = [...x, ...x]
console.log(a);


let c = 1;
let d = "hello";
console.log(`asdfa ${c} sdfasdf`)

// "string {x}".format(x)







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



