// signup.js

document.addEventListener('DOMContentLoaded', function() {
    var signupForm = document.querySelector('.signupContainer');

    if (signupForm) {
        signupForm.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Validate form
            var isValid = validateForm();

            if (isValid) {
                // Collect form data
                var formData = {
                    email: document.getElementById('Email').value,
                    name: document.getElementById('Name').value,
                    password: document.getElementById('password').value,
                    city: document.getElementById('city').value,
                    phoneNumber: document.getElementById('phoneNumber').value,
                    dob: document.getElementById('dob').value,
                    entitlement: document.getElementById('entitlement').value
                };

                // Example: Output form data to console (replace with actual submission logic)
                console.log('Form data:', formData);

                // Example: Redirect to a thank you page after submission
                window.location.href = 'login.html'; // Replace with your desired destination
            }
        });
    }

    function validateForm() {
        var email = document.getElementById('Email').value.trim();
        var name = document.getElementById('Name').value.trim();
        var password = document.getElementById('password').value.trim();
        var city = document.getElementById('city').value;
        var phoneNumber = document.getElementById('phoneNumber').value.trim();
        var dob = document.getElementById('dob').value;
        var entitlement = document.getElementById('entitlement').value;

        // Validate required fields
        if (email === '' || name === '' || password === '' || city === '' || phoneNumber === '' || dob === '' || entitlement === '') {
            alert('Please fill in all required fields.');
            return false;
        }

        // Validate email format
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert('Invalid email format.');
            return false;
        }

        // Validate phone number format (simple check for 10 digits)
        var phoneRegex = /^0\d{9}$/;
        if (!phoneRegex.test(phoneNumber)) {
            alert('Invalid phone number format. Please enter 10 digits.');
            return false;
        }

        // Validate name format (only letters)
        var nameRegex = /^[A-Za-z]+$/;
        if (!nameRegex.test(name)) {
            alert('Name must consist only of letters.');
            return false;
        }

        // Validate password length (at least 6 characters)
        if (password.length < 6) {
            alert('Password must be at least 6 characters long.');
            return false;
        }

        // Validate age (must be over 18 based on date of birth)
        var today = new Date();
        var birthDate = new Date(dob);
        var age = today.getFullYear() - birthDate.getFullYear();
        var monthDiff = today.getMonth() - birthDate.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }
        if (age < 18) {
            alert('You must be over 18 years old to sign up.');
            return false;
        }

        // Additional validations as needed

        return true; // Form is valid
    }
});
