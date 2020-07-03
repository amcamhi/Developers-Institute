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

function create() { 
            
  // Create table object. 
  var table = document.createElement("TABLE"); 
  table.setAttribute("id", "MyTable"); 
  document.body.appendChild(table); 

  var row1 = document.createElement("TR"); 
  row1.setAttribute("id", "MyTr"); 
  document.getElementById("MyTable").appendChild(row1); 
  var row2 = document.createElement("TR"); 
  row2.setAttribute("id", "MyTr2"); 
  document.getElementById("MyTable").appendChild(row2); 

  var cell1 = document.createElement("TD"); 
  var  textCell1 = document.createTextNode(allBooks[0].title + " written by: " + allBooks[0].author); 
  cell1.appendChild(textCell1); 
  document.getElementById("MyTr").appendChild(cell1); 
  
  var cell3 = document.createElement("TD"); 
  var  image3 = document.createElement("img");
  image3.setAttribute("src",allBooks[0].image)
  image3.style.width = "100px" 
  cell3.appendChild(image3); 
  if(allBooks[0].alreadyRead == true){
    cell1.style.color = "red"
  }
  document.getElementById("MyTr").appendChild(cell3); 

  var cell2 = document.createElement("TD"); 
  var  textCell2 = document.createTextNode(allBooks[1].title + " written by: " + allBooks[1].author); 
  cell2.appendChild(textCell2); 
  document.getElementById("MyTr2").appendChild(cell2); 

  var cell4 = document.createElement("TD"); 
  var  image4 = document.createElement("img");
  image4.setAttribute("src",allBooks[1].image)
  image4.style.width = "100px" 
  cell4.appendChild(image4); 
  if(allBooks[1].alreadyRead == true){
    cell2.style.color = "red"
  }
  document.getElementById("MyTr2").appendChild(cell4); 
} 

create()

// let table = document.createElement("table");
// for(index in allBooks){
//   let row = document.createElement("tr")
// }


// let row = document.createElement("tr");
// let row2 = document.createElement("tr");
// let column1 = document.createElement("tc");
// let column2 = document.createElement("tc");
// let cell1 = document.createElement("td");
// let cell2 = document.createElement("td");

// let text1 = document.createTextNode(allBooks[0].title+" written by: " +allBooks[0].author);
// let text2 = document.createTextNode(allBooks[1].title+" written by: " +allBooks[1].author);
// console.log(text1)


// cell1 = cell1.appendChild(text1);
// cell2 = cell2.appendChild(text2);

// column1 = column1.appendChild(cell1);
// column2 = column2.appendChild(cell2);
// row = row.appendChild(column1);
// row2 = row2.appendChild(column2);

// table = table.appendChild(row);
// table = table.appendChild(row2);


// let body = document.querySelector("body");

// body = body.appendChild(table)