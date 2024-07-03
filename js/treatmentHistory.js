document.addEventListener('DOMContentLoaded', () => {
    const treatments = [
        {
            type: 'Psychologist Treatment',
            date: '08/02/2024',
            link: 'ratePsychologist.html'
        },
        {
            type: 'Massage',
            date: '03/04/2024',
            link: 'rateMassage.html'
        },
        {
            type: 'Music Therapy',
            date: '10/05/2024',
            link: 'rateMusicTherapy.html'
        }
    ];

    const treatmentList = document.getElementById('treatmentList');

    treatments.forEach(treatment => {
        const listItem = document.createElement('li');

        listItem.innerHTML = `
            ${treatment.type} - ${treatment.date}
            <button onclick="location.href='${treatment.link}'">Rate</button>
        `;

        treatmentList.appendChild(listItem);
    });
});
