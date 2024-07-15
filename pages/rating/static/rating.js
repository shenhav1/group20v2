document.addEventListener('DOMContentLoaded', () => {
    const ratingForm = document.getElementById('ratingForm');

    ratingForm.addEventListener('submit', (event) => {
        event.preventDefault();

        // Fetch form data
        const formData = new FormData(ratingForm);
        const therapistRating = formData.get('therapistRating');
        const clinicRating = formData.get('clinicRating');
        const treatmentHelp = formData.get('treatmentHelp');
        const generalRating = formData.get('generalRating');
        const comments = formData.get('comments');

        // Basic validation
        if (!therapistRating || !clinicRating || !treatmentHelp || !generalRating) {
            alert('Please fill out all required fields.');
            return;
        }

        console.log({
            therapistRating,
            clinicRating,
            treatmentHelp,
            generalRating,
            comments
        });

        alert('Thank you for your rating!');
        window.location.href = 'requestsent';
    });
});