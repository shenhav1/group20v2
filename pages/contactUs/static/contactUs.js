// contactUs.js

document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contactForm');

    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();

        // Fetch form data
        const formData = new FormData(contactForm);
        const message = formData.get('message').trim();

        if (!validateMessage(message)) {
            alert('Please enter a valid message with at least 10 words.');
            return;
        }

        //Clear form after submission
        contactForm.reset();
        alert('Thank you for your message! We will send the message to the therapist.');
        window.location.href = 'requestsent';
    });

    function validateMessage(message) {
        const wordCount = message.split(/\s+/).filter(word => word.length > 0).length;
        const containsNumbers = /\d/.test(message);

        return wordCount >= 10 && !containsNumbers;
    }
});