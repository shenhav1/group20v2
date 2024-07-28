document.addEventListener('DOMContentLoaded', function () {
    var ratingForm = document.getElementById('ratingForm');

    if (ratingForm) {
        ratingForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission

            // Collect form data
            var formData = {
                therapistRating: parseInt(document.getElementById('therapistRating').value),
                clinicRating: parseInt(document.getElementById('clinicRating').value),
                treatmentHelp: parseInt(document.getElementById('treatmentHelp').value),
                generalRating: parseInt(document.getElementById('generalRating').value)
            };

            // Calculate average rating
            var averageRating = (formData.therapistRating + formData.clinicRating + formData.treatmentHelp + formData.generalRating) / 4;

            console.log('Form data:', formData); // Debugging
            console.log('Average rating:', averageRating); // Debugging

            // Get treatment ID from the hidden input field
            var treatmentId = document.getElementById('treatmentId').value;

            // Send data to server
            fetch('/submit_rating', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    formData: formData,
                    averageRating: averageRating,
                    treatmentId: treatmentId
                })
            })
            .then(response => {
                console.log("Response status:", response.status); // Debugging
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Network response was not ok.');
                }
            })
            .then(data => {
                console.log('Success:', data); // Debugging
                if (data.success) {
                    alert('Rating submitted successfully.');
                    // Optionally redirect or reset form
                    ratingForm.reset();
                } else {
                    alert(data.message || 'There was an error submitting your rating. Please try again.');
                }
            })
            .catch((error) => {
                console.error('There was a problem with the fetch operation:', error);
                alert('There was an error submitting your rating. Please try again.');
            });
        });
    }
});
