//Excercise1

// let colors = ["blue", "green", "black", "red"]
// for(i=0;i<colors.length;i++){
//     console.log("my #1 choice is",colors[i])
// }
// for(let favorite in colors){
//     console.log("my #"+(Number(favorite)+1)+" choice is", colors[favorite])
// }

// //Excercise 2
// // let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"].sort();
// // let secret = '';
// // for (name of names) {
// // 	secret += name.charAt(0)
// // }
// // console.log(secret)


// //Excercise 3

// // let number = prompt("write a number");
// // while(number<10){
// //     number = prompt("write a number");
// // }

// // Excercises 4/
// let people = ["Greg", "Mary", "Devon", "James"];
// // //1.
// // for(names of people){
// // console.log(names);
// // }
// //
// //2.
// people.shift()
// console.log(people);
// //3.
// people.splice(2,1,"Jason");
// console.log(people)

// //4.
// people.push("Andres");
// //5.
// for(names of people){
//     console.log(names);
//     if(names=="Mary"){
//         break;
//     }
// }
// //6.
// let copy = people.slice(1,3)
// console.log(copy);
// //7.
// //8.
// console.log(people.indexOf("foo"))
// //9.
// let last = people[people.length-1];
// console.log(last)

//Excercise 5
// let age = [20,5,12,43,98,55];
// let sum = 0
// for(number of age){
// sum = sum + number;
// } console.log(sum)
// for(number of age){
//     if(number % 2 == 0){
//         console.log(number);
//     }
// }
// Missing the bonus.

//Excercises GOLD XP

//2. (*NUMBER 1 GOT ERASED and I dont want to do it again ( but you did it well!)

// let family = {"Family Name":"Camhi","Members":5,"Nationality":"Chilean"}
// console.log(family);
// for(key in family){
//     console.log(key);
// }
// for(key in family){
//     console.log(family[key]);
// }

//3.
// let building = {
//     number_levels : 4,
//     number_of_apt_by_level : {
//         "1": 3,
//         "2": 4,
//         "3": 9,
//         "4": 2,
//     },
//     name_of_tenants : ["Sarah", "Dan", "David"],
//     number_of_rooms_and_rent:  {
//         "Sarah": [3, 2000],
//         "Dan":  [4, 1000],
//         "David": [1, 10],
//     },
// }
// console.log(building)
// //3.1
// console.log(building.number_levels);

// //3.2
// console.log(building["number_of_apt_by_level"]["1"]);
// console.log(building["number_of_apt_by_level"]["3"]);
// //3.3
// console.log(building.name_of_tenants[1], building.number_of_rooms_and_rent["Dan"][0]);
// //3.4
// function rentCost(name){
//    let rent = building["number_of_rooms_and_rent"][name]["1"];
//    return rent
// }

// if(rentCost("Sarah")+rentCost("David")>rentCost("Dan")){
//     console.log("You have to increase Dan\´s rent");
//     newRent = prompt("How much will be the new rent?");
// }
// console.log(newRent)
// building.number_of_rooms_and_rent["Dan"]["1"]= newRent
// console.log(rentCost("Dan"))
// //NEED TO CREATE FUNCTIONS TO MAKE THE CODE DRY
//Excersise 4

// let person = {
//     "fullName": "Perla",
//     "Mass":59,
//     "Height":1.69,
//     "BMI": function (){
//     return Number(this["Mass"])/(Number(this["Height"])*Number(this["Height"]));
//     }   
// } 
// let person2 = {
//     "fullName": "Andres",
//     "Mass":80,
//     "Height":1.85,
//     "BMI": function (){
//     return Number(this["Mass"])/(Number(this["Height"])*Number(this["Height"]));
// }   
// }

// let  x = function (){
//     if(person.BMI()>person2.BMI()){
//         console.log(person.fullName)
//     } else ( console.log(person2.fullName))
// }

// console.log(x())


// ==========================================
// XP NINJA
// 1.
// let numbers = ["323", "500", "155", "432", "330"]


// function splitToDigit(n){
//     return (n + '').split('').map((i) => { return Number(i); })
//   }
  
//  function divBy3(n){
//      let sumOfDigits = 0
//      for (i=0;i<splitToDigit(n).length;i++){
//         sumOfDigits += splitToDigit(n)[i]
//      } if(sumOfDigits % 3 == 0){
//          console.log(true)
//      } else( console.log(false)) 
//  }

//  console.log(divBy3(3000003))
