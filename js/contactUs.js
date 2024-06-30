document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contactForm');

    contactForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const message = document.getElementById('message').value.trim();

        if ( !message) {
            alert('Please fill out all fields.');
            return;
        }

        window.location.href = 'requestSent.html';



        // Simulate form submission (e.g., send data to server)
        console.log('Form submitted successfully:', {message});

        // Reset form
        contactForm.reset();

        // Show success message
        alert('Thank you for your message! We will get back to you soon.');
        window.location.href = "requestSent.html"

    });

});