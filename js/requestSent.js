// script.js

document.addEventListener('DOMContentLoaded', function () {
    // Find the sign out link by its text content (assuming unique)
    var signOutLink = document.querySelector('a[href="login.html"]:last-of-type');

    // Add a click event listener to the sign out link
    if (signOutLink) {
        signOutLink.addEventListener('click', function (event) {
            // Prevent the default behavior of the link (to navigate)
            event.preventDefault();

            // Perform sign out logic here (e.g., clearing session, redirecting to login page)
            alert('You have been signed out.'); // Example alert

            // Optionally, redirect to the login page after signing out
            window.location.href = 'login.html';
        });
    }
});
