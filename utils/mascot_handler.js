// Select the images
var vglLogo = document.getElementById('vgl-logo');

// Set the hover and click events for the VGL logo
vglLogo.onmouseover = function() {
  this.src = 'assets/vgl_mascot.png'; // Change this to the path of your hover image
}
vglLogo.onmouseout = function() {
  this.src = 'assets/vgl_v2.png'; // Change this back to the original image when the mouse is not hovering
}

// Add a boolean variable to track the click state
var isClicked = false;

vglLogo.onclick = function() {
  if (!isClicked) {
    this.src = 'assets/vgl_mascot.png'; // Change this to the path of your click image
    isClicked = true;
  } else {
    this.src = 'assets/vgl_v2.png'; // Change this back to the original image on second click
    isClicked = false;
  }
}