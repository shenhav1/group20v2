document.addEventListener('DOMContentLoaded', () => {
    const treatments = document.querySelectorAll('.treatment');

    // Add event listeners for each treatment to handle schedule button click
    treatments.forEach(treatment => {
        const scheduleButton = treatment.querySelector('.scheduleButton');
        scheduleButton.addEventListener('click', () => {
            // Redirect to the schedule page
            window.location.href = 'schedule.html';
        });
    });

    // Handle messaging the therapist
    const messageButton = document.querySelector('#messageButton');
    messageButton.addEventListener('click', () => {
        // Redirect to the contact page
        window.location.href = 'contactTherapist.html';
    });
});
