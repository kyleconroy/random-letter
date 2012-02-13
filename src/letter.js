function getRandomInt(min, max) {  
  return Math.floor(Math.random() * (max - min + 1)) + min;  
}

function loadLetter() {
  container = document.getElementById("letter");
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  index = getRandomInt(0, alpha.length - 1);
  container.data = alpha[index] + ".svg";
  container.appendChild(document.createElement("span"));
  container.style.display = "block";
}

function reloadLetter() {
  loadLetter();
}
