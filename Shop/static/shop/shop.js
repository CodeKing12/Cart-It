// When the user scrolls the page, execute myFunction 
window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("mobilestick");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
} 


function openNav() {
  document.getElementById("mySidebar").style.width = "150px";
//  document.getElementById("main").style.marginLeft = "0";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
//  document.getElementById("main").style.marginLeft= "0";
}

/* Open when someone clicks on the span element */
function openMobileNav() {
  var mobilenav = document.getElementById("myNav")
  var offsetValue = document.getElementById("navid").offsetHeight + "px"
  // document.body.classList.add("stop_scrolling");
  // mobilenav.style.top = offsetValue
  if (window.innerWidth < 600) {
    mobilenav.style.width = "100%";
    
  }
  if (window.innerWidth >= 600 && window.innerWidth < 1000) {
    document.getElementById("myNav").style.width = "60%";
    document.getElementById("laptent")
  }
  if (window.innerWidth >= 1000) {
    document.getElementById("myNav").style.width = "35%";
  }
}

/* Close when someone clicks on the "x" symbol inside the overlay */
function closeMobileNav() {
  document.getElementById("myNav").style.width = "0%";
  document.body.classList.remove("stop_scrolling")
}
