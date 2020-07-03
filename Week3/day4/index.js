// let array = [5, 10 , 3, 300, 324, 525]

// let biggestNum = function (array){
//     let max_num = 0
//     for(i=0; i<array.length; i++){
//         if(array[i]>max_num){
//             max_num = array[i]
//         }
//     }
//     return max_num;
// }

// let sum = function (array){
//     let total = 0
//     for(number of array){
//         total += number
//     } return total
// }

// let average = function (array){
//     return sum(array)/array.length}


// let excercise = function(){
//     console.log("the biggest number is : "+biggestNum(array)+" the total is: "+sum(array)+" the average is "+average(array))
// }
// excercise()
let upper = 1000;
let lower = 0;
function make_guess(upper, lower){
    return Math.round((upper - lower) / 2)
}