// Var, let, const ---
// var: function scoped (much wider) - available anywhere within the function
    // Can reclare var as often as possible -- easy to overwrite variables
    // Can log a var variable before we create it

// let and const and block scoped: available anywhere within the block
    // const is the same as let, but you can't change the value (can't reassign it)
    // can change the properties of an object
    // Use const if you don't want to modify a variable later

console.log(a1);

var a1 = 1;

if (true) {
    var b1 = 4;
    let b2 = 5;
    const b3 = 6;

    console.log(b1);
    console.log(b2);
    console.log(b3);
}

console.log(b1);
// console.log(b2);
// console.log(b3);

var b1 = 7;
let b2 = 8;
// let b2 = 8;
const b3 = 9;
// const b3 = 9;

b1 = 10;
b2 = 11;
// b3 = 12;

const obj = {
    name: 'Tim',
    age: 21
}

obj.name = 'Chris';
// obj = {}

// Regular functions and arrow functions ---

function basicPrintHello() {
    console.log('Hello');
}

let printHello = () => { 
    console.log('Hello');
}

let print = ( a ) => {
    console.log(a);
}

// Modify HTML/CSS code ---
let e1 = document.querySelector('.text');
let e2 = document.querySelector('#input-field');
let button = document.querySelector('#button')
// let element = document.querySelector('div.class1)

e1.textContent = '';


let updateText = () => {
    e1.textContent = e2.value;
}

//button.addEventListener('click', printHello);
//button.addEventListener('click', updateText);
button.addEventListener('click', () => {
    e1.textContent = e2.value;
    e1.style.color = 'red';
    e2.style.color = 'blue';
});

// Asynchronous Javascript: async/await, Promises



// Miscellaneous: == vs. ===, array/object destructuring, array methods, ES6

if (4 == '4') {
    console.log('4 is 4')
}