let word = prompt("enter one simbol").toLowerCase()

if (word.length !== 1) {
    alert("please enter one simbol")

} else if (word === "a" || word === "e" || word === "i" || word === "o" || word === "u") {
    alert("number is vowel")

} else {
    alert("number is consontant")
}