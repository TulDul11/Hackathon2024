// Simulación del contador de objetos
// Tus compañeros pueden reemplazar esto con la lógica de detección real

let contadorObjetos = 0;

// Esta función puede ser llamada por el sistema de visión por computadora cuando se detecte un objeto
function actualizarContador(cantidad) {
    contadorObjetos = cantidad;
    document.getElementById('contador').textContent = contadorObjetos;
}

// Ejemplo de cómo actualizar el contador (simulación)
setInterval(() => {
    // Simulamos el incremento de objetos detectados cada 2 segundos
    let objetosDetectados = Math.floor(Math.random() * 10);
    actualizarContador(objetosDetectados);
}, 2000);

'use strict';

const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const snap = document.getElementById('snap');

const constraints = {
audio: false,
video: true,
};

// Access webcam
async function init() {
try {
const stream = await navigator.mediaDevices.getUserMedia(constraints);
handleSuccess(stream);
} catch (e) {
errorMsgElement.innerHTML = `navigator.getUserMedia error:${e.toString()}`;
}
}

// Success
function handleSuccess(stream) {
window.stream = stream;
video.srcObject = stream;
}

// Load init
init();

// Draw image
var context = canvas.getContext('2d');
snap.addEventListener("click", function() {
context.drawImage(video, 0, 0, 640, 480);
});