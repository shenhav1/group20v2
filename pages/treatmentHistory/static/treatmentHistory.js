document.addEventListener('DOMContentLoaded', () => {
    const treatmentList = document.getElementById('treatmentList');

    treatments.forEach(treatment => {
        const listItem = document.createElement('li');

        listItem.innerHTML = `
            ${treatment.type} - ${treatment.date}
            <button onclick="location.href='${treatment.link}'">Rate treatment</button>
        `;

        treatmentList.appendChild(listItem);
    });
});
