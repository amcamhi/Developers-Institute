let age = prompt("what is your age?");
if (age>18){
    console.log("Powering On, Enjoy the ride!")
}
else if(age==18){
    console.log("Congratulations on your first year of driving. Enjoy the ride!")
}
else {
    console.log("Sorry, you are too young to drive. Powering off")
}

let a = 2 + 2;

switch (a) {
  case 3:
    alert( 'Too small' );
    break;
  case 4:
    alert( 'Exactly!' );
    break;
  case 5:
    alert( 'Too large' );
    break;
  default:
    alert( "I don't know such values" );
}

let b = 2 + 2;

switch (b) {
  case 4:
    alert('Right!');
    break;

  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}