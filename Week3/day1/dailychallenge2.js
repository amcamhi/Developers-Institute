let planets  = ["Earth", "Mars", "Venus", "Jupiter", "Saturn"];

let div1 = document.createElement("div");
let div2 = document.createElement("div");
let div3 = document.createElement("div");
let div4 = document.createElement("div");
let div5 = document.createElement("div");

div1.className = "planet blue";
div2.className = "planet red" ;
div3.className = "planet green";
div4.className = "planet orange";
div5.className = "planet purple";

let div1Text = document.createTextNode(planets[0]);
let div2Text = document.createTextNode(planets[1]);
let div3Text = document.createTextNode(planets[2]);
let div4Text = document.createTextNode(planets[3]);
let div5Text = document.createTextNode(planets[4]);

div1.appendChild(div1Text);
div2.appendChild(div2Text);
div3.appendChild(div3Text);
div4.appendChild(div4Text);
div5.appendChild(div5Text);

div1.setAttribute("style","background-color:blue");
div2.setAttribute("style","background-color:red");
div3.setAttribute("style","background-color:green");
div4.setAttribute("style","background-color:yellow");
div5.setAttribute("style","background-color:purple");


console.log(div1)
let body = document.querySelector("body");
document.body.appendChild(div1)
document.body.appendChild(div2)
document.body.appendChild(div3)
document.body.appendChild(div4)
document.body.appendChild(div5)

//MISSING THE BONUS

