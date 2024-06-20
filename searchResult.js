document.addEventListener('DOMContentLoaded', () => {
    const therapistButtons = document.querySelectorAll('.therapist button');

    therapistButtons.forEach(button => {
        button.addEventListener('click', () => {
            const therapistName = button.id;
            window.location.href = "profile.html";
        });
    });
});