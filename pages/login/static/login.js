document.addEventListener('DOMContentLoaded', () => {
    const signInButton = document.getElementById('signInButton');

    signInButton.addEventListener('click', async (event) => {
        event.preventDefault();
        const email = document.getElementById('Email').value;
        const password = document.getElementById('password').value;

        if (validateEmail(email) && validatePassword(password)) {
            try {
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({email: email, password: password}),
                });

                const result = await response.json();

                if (result.success) {
                    window.location.href = 'userprofile';
                } else {
                    alert(result.message);
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            }
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