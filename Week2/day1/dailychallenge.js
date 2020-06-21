var array = ["Banana", "Apples", "Oranges", "Blueberries"];
array.reverse();
array.pop(); //sacamos la banana
array.sort(); //Apples, Blueberries, Oranges
array.push("Kiwi"); //Apples, Blueberries, Oranges, Kiwi
array.reverse();
array.pop(); //Kiwi, Oranges, Blueberries
console.log(array);

var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(array2[1][1][0]);