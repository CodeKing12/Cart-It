window.onscroll = function() {myFunction()};

var navbar = document.getElementById("sticknav");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

// Beginning of slideshow code

var slideNumber = 1
showSlides(slideNumber);

// Goes to the next of previous slide by adding or subtracting a number from slideNumber
function nextSlide(n) {
    showSlides(slideNumber += n)
}

// Shows a slide according to the number given
function showSlides(n) {
    // To be used later in the for loop
    var i;
    // Extracts the slides from the html page
    var slides = document.getElementsByClassName("product_slides");
    // Extracts the dots at the bottom of the slides which indicate the number of slides and which ones are active
    var slide_markers = document.getElementsByClassName("slide_markers")
    // When the slideshow reaches the last slide, it resets slideNumber to 1 which starts the slideshow from the beginning
    if (n > slides.length) {slideNumber = 1};
    // When the slideshow is at the first image and the previous button is pressed,it resets slideNumber to the number of slides
    if (n < 1) {slideNumber = slides.length};
    // Makes all the slides except for the active style to have no display i.e., they won't show
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    // Makes all the slideMarkers grey except for the slideMarker that depicts the current image
    for (i = 0; i < slide_markers.length; i++) {
        slide_markers[i].className = slide_markers[i].className.replace("active", "")
    }
    // Determines the slide that will show. It begins at 0 by subtracting 1 from the slideNumber which starts at 1
    slides[slideNumber - 1].style.display = "block";
    // Determines the slideMarker that will show, then adds the active class to it which makes it a darker grey than the other markers to indicate that it is the active slide.
    slide_markers[slideNumber - 1].classList.add("active");
}

// End of slideshow code