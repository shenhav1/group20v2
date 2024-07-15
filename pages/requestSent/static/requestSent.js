document.addEventListener('DOMContentLoaded', function () {
    // Find the sign out link by its text content (assuming unique)
    var signOutLink = document.querySelector('a[href="login"]:last-of-type');

    if (signOutLink) {
        signOutLink.addEventListener('click', function (event) {
            // Prevent the default behavior of the link (to navigate)
            event.preventDefault();

            alert('You have been signed out.');

            //redirect to the login page after signing out
            window.location.href = 'login';
        });
    }
});
