// Nav-tabs js code begins here

function openPage(content, current) {
    var tabcontent = document.getElementsByClassName("tabcontent")
    for (i=0; i<tabcontent.length; i++) {
        tabcontent[i].style.display = "none"
    }
    document.getElementById(content).style.display = "block"

    var tablinks = document.getElementsByClassName("tablink")

    for (x=0; x<tablinks.length; x++) {
        tablinks[x].classList.remove("selected")
    }
    current.classList.add("selected")
}

document.getElementById("defaultOpen").click()

// Nav-tabs js code ends here