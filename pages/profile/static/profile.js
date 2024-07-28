document.addEventListener('DOMContentLoaded', () => {
    const treatments = document.querySelectorAll('.treatment');

    // Add event listeners for each treatment to handle schedule button click
    treatments.forEach(treatment => {
        const scheduleButton = treatment.querySelector('.scheduleButton');
        scheduleButton.addEventListener('click', () => {
            // Redirect to the schedule page
            window.location.href = 'schedule';
        });
    });


    document.addEventListener('DOMContentLoaded', function () {
        const scheduleButtons = document.querySelectorAll('.scheduleButton');
        scheduleButtons.forEach(button => {
            button.addEventListener('click', function () {
                const therapist = this.dataset.therapist;
                const address = this.dataset.address;
                const treatment = this.dataset.treatment;
                const url = `{{ url_for('schedule.index') }}?therapist=${encodeURIComponent(therapist)}&address=${encodeURIComponent(address)}&treatment=${encodeURIComponent(treatment)}`;
                window.location.href = url;
            });
        });
    });
});
