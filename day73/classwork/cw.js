// function elements(){

//     let div = document.getElementById("d")

//     let button = document.createElement("button")
  
//     button.textContent = "click"

//     div.appendChild(button)
// }


// window.onload = elements



function e (){
    let div = document.getElementById("d2")

    let p = document.getElementById("p")

    let button = document.getElementById("bo")

    if (button) {
        div.removeChild(button)
    }


    let i = document.createElement("i")

    i.textContent = "hello world!"

    div.replaceChild(i,p)

}

window.onload = e

