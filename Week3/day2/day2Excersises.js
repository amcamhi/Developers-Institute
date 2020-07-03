// // // Excercise 1 GOLD

// // let div = document.getElementById("root");
// // let li = document.createElement("li");
// // let ul = document.createElement("ul");
// // let input = document.createElement("input")
// // input.setAttribute("placeholder","enter items")

// // let liText = document.createTextNode("sentence");
// // let button = document.createElement("button");
// // button.className = "boton";
// // button.innerText = "ENTER"
// // button.addEventListener("click", function(){
// //         if(input.value.length > 0){
// //         let li = document.createElement("li");
// //         li.appendChild(document.createTextNode(input.value));
// //         ul.appendChild(li);
// //         input.value = ""}
// // })


// // // input.addEventListener("keypress",)



// // li.appendChild(liText);
// // ul.appendChild(li);

// // div.appendChild(button);
// // div.appendChild(input);
// // div.appendChild(ul);

// //Excercises XP 

// // 1

// let elementsInArticle = document.querySelector("article").children;
// for (element of elementsInArticle){
//         element.className = "para_article"
// }
// console.log(elementsInArticle)
// let lastParagraph = document.querySelectorAll("p")[3];
// lastParagraph.remove()

// document.getElementsByTagName("h2")[0].addEventListener("click", remove);
// function remove(){
//         this.remove()
// }

// let h1 = document.getElementsByTagName("h1")[0];
// h1.style.fontSize= Math.floor(Math.random()*101)+"px"

// document.querySelector("p").addEventListener("click",hide);
// function hide(){
//         this.style.display = "none"
// }
// // document.querySelectorAll("p")[1].addEventListener("click", fadeout);
// // function fadeout(){
// //         this.fadeOut(2000)
// // }  THIS DIDNT WORK, CHECK WITH JONATHAN.




// // EXCERCISE 2 

// function getBold_items(){
//         let bold_items = document.getElementsByTagName("strong");
//         return bold_items
// }
// let getBold = getBold_items()

// function highlight(){
// for(item of getBold){
//         item.style.color = "blue"
// }
// }
// function return_normal(){
//         for (item of getBold){
//                 item.style.color = "black"
//         }
// }

// for(item of getBold){
//         item.addEventListener("mouseover", highlight);
//         item.addEventListener("mouseout", return_normal);

// }


// Excercise 3
function getSphereVolume(){
        let radius = document.getElementById("radius").value
        let vol = 4/3*Math.PI*Math.pow(radius,3);
        
        return vol
}
let button = document.getElementsByTagName("button")[0];
button.addEventListener("click",getSphereVolume);

volume.setAttribute("value",getSphereVolume(radius.value))
