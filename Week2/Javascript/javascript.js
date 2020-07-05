// let age = prompt("what is your age?");
// if (age>18){
//     console.log("Powering On, Enjoy the ride!")
// }
// else if(age==18){
//     console.log("Congratulations on your first year of driving. Enjoy the ride!")
// }
// else {
//     console.log("Sorry, you are too young to drive. Powering off")
// }

// let a = 2 + 2;

// switch (a) {
//   case 3:
//     alert( 'Too small' );
//     break;
//   case 4:
//     alert( 'Exactly!' );
//     break;
//   case 5:
//     alert( 'Too large' );
//     break;
//   default:
//     alert( "I don't know such values" );
// }

// let b = 2 + 2;

// switch (b) {
//   case 4:
//     alert('Right!');
//     break;

//   case 3: // (*) grouped two cases
//   case 5:
//     alert('Wrong!');
//     alert("Why don't you take a math class?");
//     break;

//   default:
//     alert('The result is strange. Really.');
// }

// LEFT UNRESOLVED
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

// //Excercise 5
// function hotel_cost(){
//   let nights =  prompt ("how many nights would you like to stay?");
//    let hotelCost= Number(nights)*140;
//    return hotelCost;
// }
// let hotelCost = hotel_cost();


// function planeRideCost (){
//   let destination =  prompt ("what is your destination?");
//   if( destination == "London"){ rideCost =183;
//   }else if(destination == "Paris"){rideCost =220;
//   }else{rideCost = 300 ;
//         }
//         return rideCost;
// }
// let rideCost = planeRideCost();

// function rentalCarCost(){
//     let days = Number(prompt("For how many days would you like to rent the car?"));
//     if(days>10){ carCost = 0.95*days*40
       
//     }else{carCost =  days*40;
// }   return carCost;}

// let carCost = rentalCarCost();

// function totalVacationCost(){
    
//     let vacationCost = hotelCost+rideCost+carCost;
//     return vacationCost;
// }
// let vacationCost = totalVacationCost()

