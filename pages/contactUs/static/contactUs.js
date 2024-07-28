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

        // Convert FormData to JSON
        const formDataJson = {};
        formData.forEach((value, key) => {
            formDataJson[key] = value;
        });

        // Send the form data to the server
        fetch('/contactus', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formDataJson)
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Network response was not ok.');
                }
            })
            .then(data => {
                // Clear form after successful submission
                contactForm.reset();
                alert('Thank you for your message! We will response as fast as we can.');
                window.location.href = 'requestsent';
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('There was an error submitting your message. Please try again.');
            });
    });

    function validateMessage(message) {
        const wordCount = message.split(/\s+/).filter(word => word.length > 0).length;
        return wordCount >= 10;
    }
});
