document.getElementById('search-bar').addEventListener('click', function() {
    document.getElementById('suggestions').style.display = 'block';
});

document.addEventListener('click', function(event) {
    const searchBar = document.getElementById('search-bar');
    const suggestions = document.getElementById('suggestions');

    if (!searchBar.contains(event.target) && !suggestions.contains(event.target)) {
        suggestions.style.display = 'none';
    }
});


//NAVBAR OF ALL PAGES

document.addEventListener("DOMContentLoaded", function() {
    // Get the current page URL path
    var currentPage = window.location.pathname;

    // Get all the nav links
    var navLinks = document.querySelectorAll(".navbar li a");

    // Loop through the links
    navLinks.forEach(function(link) {
        // Create a URL object to compare paths correctly
        var linkPath = new URL(link.href).pathname;

        // If the paths match, add the active class
        if (currentPage === linkPath) {
            link.classList.add("active");
        }
    });
});





document.addEventListener("DOMContentLoaded", function() {
    const searchBar = document.getElementById("search-bar-contactpg");
    const suggestions = document.getElementById("suggestions-contactpg");

    searchBar.addEventListener("focus", function() {
        suggestions.style.display = "block";
    });

    searchBar.addEventListener("click", function() {
        suggestions.style.display = "block";
    });

    document.addEventListener("click", function(event) {
        if (!searchBar.contains(event.target) && !suggestions.contains(event.target)) {
            suggestions.style.display = "none";
        }
    });

    suggestions.addEventListener("mousedown", function(event) {
        event.preventDefault(); // Prevents the search bar from losing focus when clicking on suggestions
    });
});
