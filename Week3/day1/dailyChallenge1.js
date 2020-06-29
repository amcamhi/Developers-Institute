let allBooks =[
  {
    title:"Kafa en la Orilla",
    author:" Haruki Murakami",
    image: "https://pladlibroscl3.cdnstatics.com/usuaris/libros/fotos/93/m_libros/92997_kafka-en-la-orilla_9788483103562.jpg",
    alreadyRead:true
  },
  {
    title:"Un Mundo Feliz",
    author:"Aldous Huxley",
    image: "https://images-na.ssl-images-amazon.com/images/I/51IikE1TS1L._SX323_BO1,204,203,200_.jpg",
    alreadyRead: true
  }
]

let table = document.createElement("table");
let row = document.createElement("row");
let row2 = document.createElement("row");
let column1 = document.createElement("tc");
let column2 = document.createElement("tc");
let cell1 = document.createElement("td");
let cell2 = document.createElement("td");

let text1 = document.createTextNode(allBooks[0].title+" written by: " +allBooks[0].author);
let text2 = document.createTextNode(allBooks[1].title+" written by: " +allBooks[1].author);
console.log(text1)


cell1 = cell1.appendChild(text1);
cell2 = cell2.appendChild(text2);

column1 = column1.appendChild(cell1);
column2 = column2.appendChild(cell2);
row = row.appendChild(column1);
row2 = row2.appendChild(column2);

table = table.appendChild(row);


let body = document.querySelector("body");

body = body.appendChild(table)