document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.delete-button').forEach(function (button) {
        button.addEventListener('click', function () {
            var treatmentId = this.getAttribute('data-tid');
            var treatmentElement = document.getElementById('treatment-' + treatmentId);

            fetch(`/userprofile/delete_treatment/${treatmentId}`, {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
                .then(response => {
                    treatmentElement.remove();
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        });
    });


    // Function to update user details
    function updateUserDetails(details) {
        document.querySelector('.user-details ul').innerHTML = `
            <li><strong>Name:</strong> ${details.name}</li>
            <li><strong>Email:</strong> ${details.email}</li>
            <li><strong>Age:</strong> ${details.age}</li>
            <li><strong>Location:</strong> ${details.location}</li>
            <li><strong>Entitlement:</strong> ${details.entitlement}</li>
        `;
    }

    // Update the user details on page load
    updateUserDetails(userDetails);

    // Handling future treatments status update
    const futureTreatments = [
        {treatment: 'Psychological Evaluation', status: 'Approved'},
        {treatment: 'Physical Therapy', status: 'Denied'},
        {treatment: 'Massage', status: 'Awaiting Approval'}
    ];

    function updateFutureTreatments(treatments) {
        const list = treatments.map(treatment => `<li>${treatment.treatment} - ${treatment.status}</li>`).join('');
        document.querySelector('.future-treatments ul').innerHTML = list;
    }

    // Update the future treatments on page load
    //updateFutureTreatments(futureTreatments);

    // Adding a new message
    function addMessage(date, message) {
        const newMessage = document.createElement('li');
        newMessage.innerHTML = `<strong>${date}:</strong> ${message}`;
        document.querySelector('.messages ul').appendChild(newMessage);
    }

});
