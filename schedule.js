document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('treatmentform');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form submission

        // Validate form fields
        const date = document.getElementById('date').value;
        const time = document.getElementById('time').value;

        if (!date || !time) {
            alert('Please fill in all required fields.');
            return;
        }

        // Optionally, validate date and time format or range here

        // If form is valid, submit (for demonstration, redirect to a success page)
        window.location.href = "requestSent.html";
    });
});