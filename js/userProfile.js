document.addEventListener('DOMContentLoaded', () => {
    // Example: Updating user details dynamically
    const userDetails = {
        name: 'Dani Din',
        email: 'Dani1234@gmail.com',
        age: 26,
        location: 'Ramat Gan, Israel',
        entitlement: 'reservist'
    };

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

    // Example: Handling future treatments status update
    const futureTreatments = [
        {treatment: 'Psychological Evaluation', status: 'Approved'},
        {treatment: 'Physical Therapy', status: 'denied'},
        {treatment: 'Massage', status: 'Awaiting Approval'}
    ];

    function updateFutureTreatments(treatments) {
        const list = treatments.map(treatment => <li>${treatment.treatment} - ${treatment.status}</li>).join('');
        document.querySelector('.future-treatments ul').innerHTML = list;
    }

    // Update the future treatments on page load
    updateFutureTreatments(futureTreatments);

    // Example: Adding a new message
    function addMessage(date, message) {
        const newMessage = document.createElement('li');
        newMessage.innerHTML = <strong>${date}:</strong> ${message};
        document.querySelector('.messages ul').appendChild(newMessage);
    }

    // Add a new message
    addMessage('January 21', 'Your appointment has been confirmed');
});