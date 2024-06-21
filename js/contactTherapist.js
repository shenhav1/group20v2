document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contactForm');

    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();

        // Fetch form data
        const formData = new FormData(contactForm);
        const name = formData.get('name');
        const email = formData.get('email');
        const phone = formData.get('phone');
        const subject = formData.get('subject');
        const message = formData.get('message');

        // Basic validation
        if (!name || !email || !phone || !subject || !message) {
            alert('Please fill out all fields.');
            return;
        }

        // Validate email using a regular expression
        if (!isValidEmail(email)) {
            alert('Please enter a valid email address.');
            return;
        }

        // Validate phone number using a regular expression
        if (!isValidPhone(phone)) {
            alert('Please enter a valid phone number.');
            return;
        }


        // Example: Clear form after submission (you can implement this)
        contactForm.reset();
                alert('Thank you for your message! We will send the massage to the therapist');
        window.location.href = "homePage.html";

    });

    // Function to validate email using regular expression
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    // Function to validate phone number using regular expression
    function isValidPhone(phone) {
        // Accepts formats like +1234567890, 1234567890, (123) 456-7890, 123-456-7890, 123.456.7890
        const phoneRegex = /^\+?(\d{1,3})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$/;
        return phoneRegex.test(phone);
    }
});