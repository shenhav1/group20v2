document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contactForm');

    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();

        // Fetch form data
        const formData = new FormData(contactForm);
        const subject = formData.get('subject').trim();
        const message = formData.get('message').trim();

        // Basic validation
        if (!subject || !message) {
            alert('Please fill out all fields.');
            return;
        }

        // Subject validation: should contain only letters and spaces
        const subjectRegex = /^[A-Za-z\s]+$/;
        if (!subjectRegex.test(subject)) {
            alert('Subject should contain only letters and spaces.');
            return;
        }

        // Message validation: should contain at least 10 words, each word should contain only letters
        const messageWords = message.split(/\s+/).filter(word => word.length > 0);
        const wordRegex = /^[A-Za-z]+$/;
        const invalidWords = messageWords.filter(word => !wordRegex.test(word));

        if (messageWords.length < 10) {
            alert('Message should contain at least 10 words.');
            return;
        }

        if (invalidWords.length > 0) {
            alert('Each word in the message should contain only letters.');
            return;
        }

        // Example: Clear form after submission
        contactForm.reset();
        alert('Thank you for your message! We will send the message to the therapist');
        window.location.href = "homePage.html";
    });
});