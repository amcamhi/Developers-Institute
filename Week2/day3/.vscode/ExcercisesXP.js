//Excercise1

// let colors = ["blue", "green", "black", "red"]
// for(i=0;i<colors.length;i++){
//     console.log("my #1 choice is",colors[i])
// }
// for(let favorite in colors){
//     console.log("my #"+(Number(favorite)+1)+" choice is", colors[favorite])
// }

//Excercise 2
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// names.sort();
// for(let person of names){
//     console.log(person.substring(0,1));
//     }

//Excercise 3

// do(number = Number(prompt("write a number")));
// while(number<10);

//Excercise 4
// let people = ["Greg", "Mary", "Devon", "James"];

// for(i=0;i<people.length;i++){
//     console.log(people[i]);
// }
// people.shift();
// people.splice(2,1,"Jason");
// people.push("Andres");

// // **do(console.log(people))
// // while()
// let copy = people.slice(1,3);
//  console.log(copy);

//  console.log(people.indexOf("Mary"))
//  console.log(people.indexOf("Foo"))

//  let last = people[(people.length)-1]

// //Excercise 5
// let age = [20,5,12,43,98,55];
// for(i=0;i<age.length;i++){
    
// }
    
// }

//ExcerciseXP GOLD
const GUEST_LIST = {
    Randy: "Germany",
    Karla: "France",
    Wendy: "Japan",
    Norman: "England",
    Sam: "Argentina"
  }

  let studentName = prompt("What is your name?");
  let country = GUEST_LIST.studentName

  switch(studentName){
      case "Randy": console.log("Hi! I´m "+studentName+" and I´m from "+  country)
      break;
      case "Karla": console.log("Hi! I´m "+studentName+" and I´m from " + country)
      break;
      case "Wendy": console.log("Hi! I´m "+studentName+" and I´m from " + country)
      break;
      case "Norman": console.log("Hi! I´m "+studentName+" and I´m from " + country)
      break;
      case "Sam": console.log("Hi! I´m "+studentName+" and I´m from " + country)
      break;
      default: console.log("sorry, you are not on the list")
  }