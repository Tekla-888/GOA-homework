// 1. Create an empty object
let emptyObject = {};

// 2. Create an object with your name, age, and city
let person = {
  name: "Alex",
  age: 30,
  city: "New York"
};

// 3. Access the value of a property in an object
console.log(person.name);

// 4. Add a new property to an existing object
person.country = "USA";

// 5. Create a nested object (an object inside another object)
let user = {
  username: "alex_dev",
  details: {
    age: 30,
    city: "New York"
  }
};

// 6. Change the value of an existing property in an object
person.age = 31;

// 7. Check if two numbers are both greater than 10
let a = 15;
let b = 20;
console.log(a > 10 && b > 10):

// 8. Check if at least one of two conditions is true
let x = 5;
let y = 12;
console.log(x > 10 || y > 10); 

// 9. Use the NOT operator to invert a boolean value
let isAvailable = false;
console.log(!isAvailable);

// 10. Combine multiple logical operations in a single expression
let num1 = 15;
let num2 = 5;
let num3 = 20;
console.log(num1 > 10 && (num2 < 10 || num3 === 20));

// 11. Convert a number to a string using String()
let num = 123;
let numAsString = String(num);
console.log(typeof numAsString);

// 12. Convert a boolean value to a string using String()
let boolVal = true;
let boolAsString = String(boolVal);
console.log(typeof boolAsString):

// 13. Convert a string containing a number to a number using Number()
let str = "456";
let convertedNum = Number(str);
console.log(typeof convertedNum);

// 14. Use Number() to convert a boolean to a number
console.log(Number(true));
console.log(Number(false));

// 15. Check what happens when you use Number() on a non-numeric string
let invalidStr = "hello";
let result = Number(invalidStr);
console.log(result);
console.log(typeof result);