// When the user scrolls the page, execute myFunction 
window.onscroll = function() {
  myFunction();
};

// Get the navbar
var navbar = document.getElementById("mobilestick");
var items = document.getElementById("lapgoods")
// Get the offset position of the navbar
var sticky = navbar.offsetTop;
var mobilenav = document.getElementById("myNav")


  // Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky");
  } else {
    navbar.classList.remove("sticky");
  }
} 
/*
function stayThere() {
  if (window.pageYOffset < sticky)
}*/

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
  var distanceFromTop = navbar.offsetTop
  var distanceFromWindowTop = window.pageYOffset
  var offtop = distanceFromTop - distanceFromWindowTop 

  if (window.innerWidth < 300) {
    if (window.pageYOffset >= sticky) {
      mobilenav.style.width = "100%";
      mobilenav.style.top = "40px";
      document.body.classList.add("stop_scrolling");
    } else {
      window.scrollTo(0, distanceFromTop+10)
      mobilenav.style.width = "100%";
      mobilenav.style.top = "40px";
      document.body.classList.add("stop_scrolling");
      console.log(distanceFromTop+80)
    }
  }
  // document.body.classList.add("stop_scrolling");
  // mobilenav.style.top = offsetValue
  if (window.innerWidth < 600 && window.innerWidth > 300) {
    if (window.pageYOffset >= sticky) {
      mobilenav.style.width = "100%";
      mobilenav.style.top = "30px";
      document.body.classList.add("stop_scrolling");
    } else {
      window.scrollTo(0, distanceFromTop)
      mobilenav.style.width = "100%";
      mobilenav.style.top = "30px";
      document.body.classList.add("stop_scrolling");
    }
  }
  if (window.innerWidth >= 600 && window.innerWidth < 1000) {
    if (window.pageYOffset >= sticky) {
      mobilenav.style.width = "60%";
      mobilenav.style.top = "30px";
      document.body.classList.add("stop_scrolling");
      
    } else {
      window.scrollTo(0, distanceFromTop+5)
      mobilenav.style.width = "60%";
      mobilenav.style.top = "30px";
      document.body.classList.add("stop_scrolling");
    }
  }
  if (window.innerWidth >= 1000) {
    if (window.pageYOffset >= sticky) {
      mobilenav.style.width = "30%";
      mobilenav.style.top = "30px";
      document.body.classList.add("stop_scrolling");
    } else {
      window.scrollTo(0, distanceFromTop+5)
      mobilenav.style.width = "30%";
      mobilenav.style.top = "30px";
      document.body.classList.add("stop_scrolling");
    }
  }
}

/* Close when someone clicks on the "x" symbol inside the overlay */
function closeMobileNav() {
  document.getElementById("myNav").style.width = "0%";
  document.body.classList.remove("stop_scrolling")
}


// Get the navbar
var sidenavbar = document.getElementById("mobilestick");

// Get the offset position of the navbar
var sidesticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function sideFunction() {
  if (window.pageYOffset >= sidesticky) {
    sidenavbar.style.top = "20px"
  } else {
    sidenavbar.style.top = "50px"
  }
}

console.log(navbar.offsetTop)