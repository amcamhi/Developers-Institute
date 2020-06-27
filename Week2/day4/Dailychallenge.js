let sentence ="this,is,a,test,sentence";
//  prompt("write a a few words separated by a coma");//input del string
let words = sentence.split(",")//lo convertimos en un array
console.log(words);

let longest = 0
for(word of words){
    if(word.length>longest){
        longest = word.length}
}
let topLine = "*".repeat(longest + 4);
console.log(topLine);
for(word of words){
    let line = ("* "+word+" ".repeat(longest-word.length)+" *");
    console.log(line);
}
console.log(topLine);
