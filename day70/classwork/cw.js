// function userLoopI() {
//     let num = Number(prompt("Enter number:"))

//     let num1 = Number(prompt("Enter number:"))

   

//     for (let i = num; i <= num1; i++ ) {
//         alert(i)
//     }
// } 
// window.onload = userLoopI;



function changeElements() {
    let input = document.getElementById("t").value
    alert(input)

    let button = document.getElementById("b")
    button.style.backgroundColor = "black"
    button.style.color = "white"


    let head = document.getElementById("h")
    head.style.textAlign = "center"

    document.body.style.backgroundColor = "green"
    
    


}

window.onload = changeElements;
