document.addEventListener('DOMContentLoaded', () => {
    const treatments = document.querySelectorAll('.treatment');

    // Add event listeners for each treatment to handle details button click
    treatments.forEach(treatment => {
        const detailsButton = treatment.querySelector('.details-button');
        detailsButton.addEventListener('click', () => {
            const treatmentTitle = treatment.querySelector('.treatment-title').textContent;
            const treatmentLocation = treatment.querySelector('.treatment-location').textContent;
        });
    });

    // Handle messaging the therapist
    const messageButton = document.querySelector('.message-me-button');
    messageButton.addEventListener('click', () => {
        const therapistName = document.querySelector('h2').textContent;
        // Replace alert with actual messaging functionality if required
    });
});