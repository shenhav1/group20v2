document.addEventListener('DOMContentLoaded', () => {
    //update welcome message based on the time of day
    function updateWelcomeMessage() {
        const welcomeMessage = document.getElementById('welcome-message');
        const hours = new Date().getHours();
        let greeting;

        if (hours < 12) {
            greeting = 'Good morning, welcome to Happy Soul!';
        } else if (hours < 18) {
            greeting = 'Good afternoon, welcome to Happy Soul!';
        } else {
            greeting = 'Good evening, welcome to Happy Soul!';
        }

        welcomeMessage.textContent = greeting;
    }

    // Function to animate the intro text
    function animateIntroText() {
        const introText = document.getElementById('intro-text');
        introText.style.opacity = 0;
        introText.style.transition = 'opacity 2s';
        setTimeout(() => {
            introText.style.opacity = 1;
        }, 100);
    }
    updateWelcomeMessage();
    animateIntroText();
});