document.addEventListener('DOMContentLoaded', () => {
    const signInButton = document.getElementById('signInButton');

    signInButton.addEventListener('click', (event) => {
        event.preventDefault();
        const email = document.getElementById('Email').value;
        const password = document.getElementById('password').value;

        if (validateEmail(email) && validatePassword(password)) {
            alert('Sign-in successful!');
                    window.location.href = "userProfile.html"
            // Here you can add logic to redirect the user to another page or handle the sign-in process
            // For example: window.location.href = 'userProfile.html';
        } else {
            alert('Please enter a valid email and password.');
        }


    });

    function validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    function validatePassword(password) {
        // Simple validation: Password should be at least 6 characters long
        return password.length >= 6;
    }
});