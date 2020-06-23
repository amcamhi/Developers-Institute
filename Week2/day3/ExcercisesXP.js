//Excercise1

// let colors = ["blue", "green", "black", "red"]
// for(i=0;i<colors.length;i++){
//     console.log("my #1 choice is",colors[i])
// }
// for(let favorite in colors){
//     console.log("my #"+(Number(favorite)+1)+" choice is", colors[favorite])
// }

//Excercise 2
let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort();
for(let person of names){
    for(let first of person){
    first.substring(0,1);
    console.log(first);
    }
}
