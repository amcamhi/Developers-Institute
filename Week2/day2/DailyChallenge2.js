// let string = "this tomato is not that bad"
// let not = string.indexOf("not")
// let bad = string.indexOf("bad")

// console.log(not)
// console.log(bad)

// if(not<bad){
//     console.log(string.substring(0,not)+"good")
// } else {
// console.log(string)
// }

//Excercise GOLDXP

// let userPrompt = prompt("please write a word:")
// let noVow = userPrompt.replace(/[aeiouAEIOU]/g,"")
// console.log(noVow);


// Excercise2
// let language = prompt("which language do you speak? ");

// if(language=="French"){
//     console.log("Bonjour")
// } else if(language =="English"){
//     console.log("hello")
// } else if(language =="Hebrew"){
//     console.log("Shalom")
// } else{
//     console.log(":)")
// }

// let language = prompt("what language do you speak?")
// switch(language){
//     case "French":
//     console.log("Bonjour!");
//     break;
//     case "Hebrew":
//         console.log("Shalom!");
//         break;
//     case "English":
//         console.log("Hello");
//         break;
//     default:
//         console.log(":)")
// }
// Excercise 3
// let grade = Number(prompt("whats your grade?"));
// console.log(grade)
// if( grade>=90){
//     console.log("A")
// } 
// else if (80<=grade){
//     console.log("B")
// }
// else if (70<=grade){
//         console.log("C")
//     }
// else{
//     console.log("D")
// }

// Exercise 4

// let zipCode =prompt("what´s your zipcode?")
// let spaces = (zipCode.split(" ").length-1);
// let zip = Number(zipCode)

// if(spaces>0){
//     console.log("must not contain spaces")
// }
// else if(typeof zip!== "number"){
//     console.log("must contain only numbers");
// }
// else if(zipCode>99999 || zipCode<10000){
//     console.log("must not be greater than 5 digits in lenght");
// }

// else {console.log("Good!")}
