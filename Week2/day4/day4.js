// function sum(a, b){
//     console.log(a+b);
// }
// sum(10,20);


// function evenOdd(num){
//     if(num%2==0){
//         console.log("Even");
//     }else{
//         console.log("odd")
//     }
// }
// evenOdd(23);
// evenOdd(20);
// evenOdd(2131242314);

// function age(){
//     return parseInt(prompt("whats your age?"));
// }

// let userAge = age()

// function double(num){
//     return 2*num
// }

// console.log("Double your age is "+double(userAge))

//Excercise 1

// function parentsAge(myAge){
//     console.log("your mom is "+(2*myAge)+ "years old", "your dad is "+(2.4*myAge)+" years old.");
// }
// parentsAge(27);

//                         EXCERCISES XP

//1.

// function checkDriverAge(){
// let age = prompt("what is your age?");

// if (Number(age) < 18) {
//     alert("Sorry, you are too yound to drive this car. Powering off");
// } else if (Number(age) > 18) {
//     alert("Powering On. Enjoy the ride!");
// } else if (Number(age) === 18) {
//     alert("Congratulations on your first year of driving. Enjoy the ride!");
// }
// }
// checkDriverAge()

// function checkDriverAge(age){
    
//     if (Number(age) < 18) {
//         alert("Sorry, you are too yound to drive this car. Powering off");
//     } else if (Number(age) > 18) {
//         alert("Powering On. Enjoy the ride!");
//     } else if (Number(age) === 18) {
//         alert("Congratulations on your first year of driving. Enjoy the ride!");
//     }
//     }

// //2.

// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100,
// }

// function checkBasket(){
//     let item = prompt("which item do you want?");
//     if(item == "glasses"){
//         console.log("there is " +amazonBasket.glasses+ " in the basket")
//     }else if(item =="books"){
//         console.log("there are " +amazonBasket.books+ " in the basket")
//     }else if(item == "floss"){
//         console.log("there are " +amazonBasket.floss+ " in the basket")
//     } else{console.log("item is not in the basket")}
// }
// checkBasket()

// Excercise 3

// function changeEnough([quarters, dimes, nickels, pennies], due){
  
//     if((quarters*0.25+dimes*0.10+nickels*0.05+pennies*0.01)>due){
//         console.log("Enough change")
//     }else{
//         console.log("Change not enough")
//     }
// }
// changeEnough([2, 100, 0, 0], 4.25);
// changeEnough([2, 100, 0, 0], 14.11);
// changeEnough([0, 0, 20, 5], 0.75);

//Excercise 4

// let shoppingList = ["banana","orange","apple"]

// let stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// let prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 
// let total = 0

// function inStock(item){
//     return stock[item]>0
// }

// function buy(item){
   
//         total += prices[item];
//         stock[item] -=1;
//     }

//     for(item of shoppingList){
//         if(inStock(item)){
//             buy(item);
//         }
//     console.log(myBill());
    


// //Excercise 5
function hotel_cost(){
  let nights =  prompt ("how many nights would you like to stay?");
  hotelCost =  Number(nights)*140;
  return hotelCost;
}

function planeRideCost (){
  let destination =  prompt ("what is your destination?");
  if( destination == "London"){ rideCost =183;
  }else if(destination == "Paris"){rideCost =220;
  }else{rideCost = 300 ;
        }
        return rideCost;
}


function rentalCarCost(){
    let days = Number(prompt("For how many days would you like to rent the car?"));
    if(days>10){ carCost = 0.95*days*40
       
    }else{carCost =  days*40}
    
    return carCost;}



function totalVacationCost(){
  let hc = hotel_cost()
  let pr = planeRideCost()
  let cc = rentalCarCost()
    return hc + pr + cc
}

let total = totalVacationCost()

// EXCERCISES XP NINJA

//Excercise 1

// let string = "abcdefg"
// let output = ""

// let upEven = function (word){
// for(i = 0; i<word.length-1; i++){
//   if(i % 2 == 0){
//     output += word[i].toUpperCase() 
//   }else{
//     output +=word[i]
//   }
// }return console.log(output)
// }
// upEven("gnfadngadfgaga")

//Excercise 2

// let arr = [1,2,3,3,3,3,4,5];
// function unique(array){
//   let filtered = []
//   for(i=0; i<array.length; i++)
//     if(filtered.indexOf(array[i]) === -1){
//       filtered.push(array[i])
//     }
//     return filtered;
// }
// console.log(unique(arr))

//Excercise 3
let array1 = [-1,0,3,100, 99, 2, 99];
const array2 = ['a', 3, 4, 2];
const array3 = []; 

let biggestNum = function (array){
  let max = 0;
  for( i = 0; i<array.lenght-1 ; i++){
    if(typeof(array[i]) == "number" && max<array[i]){
      max = array[i];
    } return max
  }
}
console.log(biggestNum(array1))




