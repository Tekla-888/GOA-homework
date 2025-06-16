let num1 = Number(prompt("enter first number"))

let num2 = Number(prompt("enter second number"))

let num3 = Number(prompt("enter third number"))

if (num1 === num2 && num2 === num3){
    alert("every number is equal")

} else if (num1 >= num2 && num1 >= num3) {
    alert("first number is the largest")

} else if (num2 >= num1 && num2 >= num3) {
    alert("second number is the largest")

} else {
    alert("third number is the largest")
}

