let num = Number(prompt("enter number"))

if (num % 3 === 0 && num % 5 === 0) {
    alert("Divisible by both")

} else if (num % 3 === 0){
    alert("Divisible by 3 only")

} else if (num % 5 === 0){
    alert("Divisible by 5 only")

} else{
    alert("Not divisible by either")
}
