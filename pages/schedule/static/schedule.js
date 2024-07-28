document.addEventListener('DOMContentLoaded', function () {
    var scheduleForm = document.querySelector('.treatment-form form');

    if (scheduleForm) {
        scheduleForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission

            // Collect form data
            var formData = {
                therapist: document.getElementById('therapist').value,
                address: document.getElementById('address').value,
                typeOfTreatment: document.getElementById('typeOfTreatment').value,
                date: document.getElementById('date').value,
                time: document.getElementById('time').value
            };

            console.log("Form data to be sent:", formData); // Debugging

            // Send data to server
            fetch('/schedule', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
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
                        // Clear form after successful submission
                        scheduleForm.reset();
                        alert('Appointment scheduled successfully.');
                        window.location.href = data.redirect; // Use the redirect URL from the server response
                    } else {
                        alert(data.message || 'There was an error scheduling your appointment. Please try again.');
                    }
                })
                .catch((error) => {
                    console.error('There was a problem with the fetch operation:', error);
                    alert('There was an error scheduling your appointment. Please try again.');
                });
        });
    }
});
