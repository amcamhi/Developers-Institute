let button = document.querySelector("button");

function changeColor(){
  button.style.color = "red"
}

function alert(){
  alert("ALERT!!!!")
}

function fontSize(){
  button.style.fontSize = "40px";
}

function background(){
  button.style.backgroundColor = "lime";
}

function fontFamily(){
  button.style.fontFamily = "Bangers"
}

button.addEventListener("click",changeColor)
button.addEventListener("mouseover",background)
button.addEventListener("mousedown",fontSize)
button.addEventListener("mouseleave", fontFamily)
button.addEventListener("mouseover", alert)
