let keys = document.getElementById("keys");
let scales = document.getElementById("scales");

let a = document.getElementById("A")
let b = document.getElementById("B")
let c = document.getElementById("C")
let d = document.getElementById("D")
let e = document.getElementById("E")
let f = document.getElementById("F")
let g = document.getElementById("G")
let major = document.getElementById("major")
let minorPentatonic = document.getElementById("minorPentatonic")
let minor = document.getElementById("minor")

let img = document.getElementById("img")

let imagenes = [{key:"A", scale:"Minor Pentatonic", img:"ESCALAS/AMinorPentatonic.png"},
                {key:"B", scale:"Minor Pentatonic", img:"ESCALAS/BMinorPentatonic.png"},
                {key:"C", scale:"Minor Pentatonic", img:"ESCALAS/CMinorPentatonic.png"},
                {key:"D", scale:"Minor Pentatonic", img:"ESCALAS/DMinorPentatonic.png"},
                {key:"E", scale:"Minor Pentatonic", img:"ESCALAS/EMinorPentatonic.png"},
                {key:"F", scale:"Minor Pentatonic", img:"ESCALAS/FMinorPentatonic.png"},
                {key:"G", scale:"Minor Pentatonic", img:"ESCALAS/GMinorPentatonic.png"},
                // AQUI EMPIEZA LA ESCALA MAYOR
                {key:"A", scale:"Major", img:"ESCALAS/AMajor.png"},
                {key:"B", scale:"Major", img:"ESCALAS/BMajor.png"},
              ]


  var x = document.getElementById("keys").value;
  var y = document.getElementById("scales").value;

  function changeImg(){
    var x = document.getElementById("keys").value;
    var y = document.getElementById("scales").value;
    if( x == "A" && y == "minorPentatonic"){
      img.setAttribute("src","ESCALAS/AMinorPentatonic.png")
  } else if( x == "B" && y == "minorPentatonic"){
    img.setAttribute("src","ESCALAS/BMinorPentatonic.png")
  } else if( x == "C" && y == "minorPentatonic"){
    img.setAttribute("src","ESCALAS/CMinorPentatonic.png")
  } else if( x == "D" && y == "minorPentatonic"){
    img.setAttribute("src","ESCALAS/DMinorPentatonic.png")
  } else if( x == "E" && y == "minorPentatonic"){
    img.setAttribute("src","ESCALAS/EMinorPentatonic.png")
  } else if( x == "F" && y == "minorPentatonic"){
    img.setAttribute("src","ESCALAS/FMinorPentatonic.png")
  } else if( x == "G" && y == "minorPentatonic"){
    img.setAttribute("src","ESCALAS/GMinorPentatonic.png")
  }
  //AQUI EMPIEZA LA ESCALA MAYOR
    else if( x == "A" && y == "Major"){
    img.setAttribute("src","ESCALAS/AMajor.png")
  }else if( x == "B" && y == "Major"){
    img.setAttribute("src","ESCALAS/BMajor.png")
  }else if( x == "C" && y == "Major"){
    img.setAttribute("src","ESCALAS/CMajor.png")
  }else if( x == "D" && y == "Major"){
    img.setAttribute("src","ESCALAS/DMajor.png")
  }else if( x == "E" && y == "Major"){
    img.setAttribute("src","ESCALAS/EMajor.png")
  }else if( x == "F" && y == "Major"){
    img.setAttribute("src","ESCALAS/FMajor.png")
  }else if( x == "G" && y == "Major"){
    img.setAttribute("src","ESCALAS/GMajor.png")
  }
  //AQUI EMPIEZA LA ESCALA MENOR
  else if( x == "A" && y == "Minor"){
    img.setAttribute("src","ESCALAS/AMinor.png")
  }else if( x == "B" && y == "Minor"){
    img.setAttribute("src","ESCALAS/BMinor.png")
  }else if( x == "C" && y == "Minor"){
    img.setAttribute("src","ESCALAS/CMinor.png")
  }else if( x == "D" && y == "Minor"){
    img.setAttribute("src","ESCALAS/DMinor.png")
  }else if( x == "E" && y == "Minor"){
    img.setAttribute("src","ESCALAS/EMinor.png")
  }else if( x == "F" && y == "Minor"){
    img.setAttribute("src","ESCALAS/FMinor.png")
  }else if( x == "G" && y == "Minor"){
    img.setAttribute("src","ESCALAS/GMinor.png")
  }
}

// METRONOMO   METRONOMO   METRONOMO   METRONOMO   METRONOMO   METRONOMO   

