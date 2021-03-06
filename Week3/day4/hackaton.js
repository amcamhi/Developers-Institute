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
// Existing code unchanged.
window.onload = function play() {
  var context = new AudioContext();
  // Setup all nodes
}

// One-liner to resume playback when user interacted with the page.
document.querySelector('a').addEventListener('click', function() {
  context.resume().then(() => {
    console.log('Playback resumed successfully');
  });
});

var audioContext = null;
var unlocked = false;
var isPlaying = false;      // Are we currently playing?
var startTime;              // The start time of the entire sequence.
var current16thNote;        // What note is currently last scheduled?
var tempo = 120.0;          // tempo (in beats per minute)
var lookahead = 25.0;       // How frequently to call scheduling function 
                            //(in milliseconds)
var scheduleAheadTime = 0.1;    // How far ahead to schedule audio (sec)
                            // This is calculated from lookahead, and overlaps 
                            // with next interval (in case the timer is late)
var nextNoteTime = 0.0;     // when the next note is due.
var noteResolution = 0;     // 0 == 16th, 1 == 8th, 2 == quarter note
var noteLength = 0.05;      // length of "beep" (in seconds)
var canvas,                 // the canvas element
    canvasContext;          // canvasContext is the canvas' context 2D
var last16thNoteDrawn = -1; // the last "box" we drew on the screen
var notesInQueue = [];      // the notes that have been put into the web audio,
                            // and may or may not have played yet. {note, time}
var timerWorker = null;     // The Web Worker used to fire timer messages


// First, let's shim the requestAnimationFrame API, with a setTimeout fallback
window.requestAnimFrame = (function(){
    return  window.requestAnimationFrame ||
    window.webkitRequestAnimationFrame ||
    window.mozRequestAnimationFrame ||
    window.oRequestAnimationFrame ||
    window.msRequestAnimationFrame ||
    function( callback ){
        window.setTimeout(callback, 1000 / 60);
    };
})();

function nextNote() {
    // Advance current note and time by a 16th note...
    var secondsPerBeat = 60.0 / tempo;    // Notice this picks up the CURRENT 
                                          // tempo value to calculate beat length.
    nextNoteTime += 0.25 * secondsPerBeat;    // Add beat length to last beat time

    current16thNote++;    // Advance the beat number, wrap to zero
    if (current16thNote == 16) {
        current16thNote = 0;
    }
}

function scheduleNote( beatNumber, time ) {
    // push the note on the queue, even if we're not playing.
    notesInQueue.push( { note: beatNumber, time: time } );

    if ( (noteResolution==1) && (beatNumber%2))
        return; // we're not playing non-8th 16th notes
    if ( (noteResolution==2) && (beatNumber%4))
        return; // we're not playing non-quarter 8th notes

    // create an oscillator
    var osc = audioContext.createOscillator();
    osc.connect( audioContext.destination );
    if (beatNumber % 16 === 0)    // beat 0 == high pitch
        osc.frequency.value = 880.0;
    else if (beatNumber % 4 === 0 )    // quarter notes = medium pitch
        osc.frequency.value = 440.0;
    else                        // other 16th notes = low pitch
        osc.frequency.value = 220.0;

    osc.start( time );
    osc.stop( time + noteLength );
}

function scheduler() {
    // while there are notes that will need to play before the next interval, 
    // schedule them and advance the pointer.
    while (nextNoteTime < audioContext.currentTime + scheduleAheadTime ) {
        scheduleNote( current16thNote, nextNoteTime );
        nextNote();
    }
}

function play() {
    if (!unlocked) {
      // play silent buffer to unlock the audio
      var buffer = audioContext.createBuffer(1, 1, 22050);
      var node = audioContext.createBufferSource();
      node.buffer = buffer;
      node.start(0);
      unlocked = true;
    }

    isPlaying = !isPlaying;

    if (isPlaying) { // start playing
        current16thNote = 0;
        nextNoteTime = audioContext.currentTime;
        timerWorker.postMessage("start");
        return "stop";
    } else {
        timerWorker.postMessage("stop");
        return "play";
    }
}

function resetCanvas (e) {
    // resize the canvas - but remember - this clears the canvas too.
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    //make sure we scroll to the top left.
    window.scrollTo(0,0); 
}

function draw() {
    var currentNote = last16thNoteDrawn;
    var currentTime = audioContext.currentTime;

    while (notesInQueue.length && notesInQueue[0].time < currentTime) {
        currentNote = notesInQueue[0].note;
        notesInQueue.splice(0,1);   // remove note from queue
    }

    // We only need to draw if the note has moved.
    if (last16thNoteDrawn != currentNote) {
        var x = Math.floor( canvas.width / 18 );
        canvasContext.clearRect(0,0,canvas.width, canvas.height); 
        for (var i=0; i<16; i++) {
            canvasContext.fillStyle = ( currentNote == i ) ? 
                ((currentNote%4 === 0)?"red":"blue") : "black";
            canvasContext.fillRect( x * (i+1), x, x/2, x/2 );
        }
        last16thNoteDrawn = currentNote;
    }

    // set up to draw again
    requestAnimFrame(draw);
}

function init(){
    var container = document.createElement( 'div' );

    container.className = "container";
    canvas = document.createElement( 'canvas' );
    canvasContext = canvas.getContext( '2d' );
    canvas.width = window.innerWidth; 
    canvas.height = window.innerHeight; 
    document.body.appendChild( container );
    container.appendChild(canvas);    
    canvasContext.strokeStyle = "#ffffff";
    canvasContext.lineWidth = 2;

    // NOTE: THIS RELIES ON THE MONKEYPATCH LIBRARY BEING LOADED FROM
    // Http://cwilso.github.io/AudioContext-MonkeyPatch/AudioContextMonkeyPatch.js
    // TO WORK ON CURRENT CHROME!!  But this means our code can be properly
    // spec-compliant, and work on Chrome, Safari and Firefox.

    audioContext = new AudioContext();

    // if we wanted to load audio files, etc., this is where we should do it.

    window.onorientationchange = resetCanvas;
    window.onresize = resetCanvas;

    requestAnimFrame(draw);    // start the drawing loop.

    timerWorker = new Worker("js/metronomeworker.js");

    timerWorker.onmessage = function(e) {
        if (e.data == "tick") {
            // console.log("tick!");
            scheduler();
        }
        else
            console.log("message: " + e.data);
    };
    timerWorker.postMessage({"interval":lookahead});
}

window.addEventListener("load", init );

