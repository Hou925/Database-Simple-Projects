function openTab(evt, weekName) {
    var i, tabcontent, tablinks;

    // Hide all tab contents
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
        tabcontent[i].classList.remove('active');
    }

    // Remove the 'active' class from all buttons
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab and add 'active' class to the clicked button
    document.getElementById(weekName).style.display = "block";
    document.getElementById(weekName).classList.add('active');
    evt.currentTarget.className += " active";
}

// Default open the first tab
document.getElementsByClassName('tablinks')[0].click();
