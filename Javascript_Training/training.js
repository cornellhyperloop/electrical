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
// let element = document.querySelector('div.class1')

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



// Miscellaneous: == vs. ===, array/object destructuring, array methods

if (4 == '4') {
    console.log('4 is 4')
}

if (4 === '4') {
    console.log('4 is also 4')
}

let d0 = [1, 2, 3, 4, 5];
let [d1, d2, ...d3] = d0;
console.log(d1);
console.log(d2);
console.log(d3);

let [d4, , d5, d6] = d0;
console.log(d4);
console.log(d5);
console.log(d6);

let d7 = [...d0, ...d0];
console.log(d7);


let obj1 = {
    field1: 1,
    field2: 2,
    field3: 3
}

let { field1: newVar, ...others } = obj1
//console.log(field1);
console.log(newVar);
console.log(others);

let obj2 = {
    field2: 5
}

let obj3 = { ...obj1, ...obj2 };


// Requires knowledge of the field names or some other methods to get the fields
// function printUser(obj) {
// 	console.log('Field1 is ${obj.field1}. Field2 is ${obj.field2}.')
// }

function printUser({ f1, f2 }) {
	console.log(`Field1 is ${f1}. Field2 is ${f2}.`)
}
printUser(obj3)

let arr = [
    { field1: 1, field2: 2},
    { field1: 10, field2: 20},
    { field1: 5, field2: 1}
]

// Filter array
let filterArr = arr.filter( (obj) => {
    return obj.field1 > 1
})
console.log(filterArr);

// Array to array
let mapArr = arr.map( (obj) => {
    return obj.field2
})
console.log(mapArr)

arr.forEach( (obj, index) => {
    console.log(index);
    console.log(obj.field1);
})


