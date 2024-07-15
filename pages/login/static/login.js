document.addEventListener('DOMContentLoaded', () => {
    const signInButton = document.getElementById('signInButton');

    signInButton.addEventListener('click', (event) => {
        event.preventDefault();
        const email = document.getElementById('Email').value;
        const password = document.getElementById('password').value;

        if (validateEmail(email) && validatePassword(password)) {
            window.location.href = 'userprofile';

        } else {
            alert('Please enter a valid email and password.');
        }


    });

    function validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    function validatePassword(password) {
        return password.length >= 6;
    }
});