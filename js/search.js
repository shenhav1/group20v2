// script.js

document.addEventListener('DOMContentLoaded', function () {
    // Find the form and inputs
    var searchForm = document.querySelector('.formContainer');
    var searchByNameInput = document.getElementById('searchByName');
    var treatmentTypeSelect = document.getElementById('TreatmentType');
    var citySelect = document.getElementById('city');
    var hmoSelect = document.getElementById('HMO');
    var therapistGenderSelect = document.getElementById('therapistGender');
    var entitlementSelect = document.getElementById('entitlement');

    // Add submit event listener to the form
    if (searchForm) {
        searchForm.addEventListener('submit', function (event) {
            // Prevent the form from submitting and refreshing the page
            event.preventDefault();

            // Get values from inputs
            var searchByNameValue = searchByNameInput.value.trim();
            var treatmentTypeValue = treatmentTypeSelect.value;
            var cityValue = citySelect.value;
            var hmoValue = hmoSelect.value;
            var therapistGenderValue = therapistGenderSelect.value;
            var entitlementValue = entitlementSelect.value;

            // Validate at least one search criterion is provided
            if (
                searchByNameValue === '' &&
                treatmentTypeValue === '' &&
                cityValue === '' &&
                hmoValue === '' &&
                therapistGenderValue === '' &&
                entitlementValue === ''
            ) {
                alert('Please fill in at least one search criteria.');
                return;
            }

            // Construct the search query based on selected options
            var searchQuery = '?';
            if (searchByNameValue !== '') {
                searchQuery += 'searchByName=' + encodeURIComponent(searchByNameValue) + '&';
            }
            if (treatmentTypeValue !== '') {
                searchQuery += 'treatmentType=' + encodeURIComponent(treatmentTypeValue) + '&';
            }
            if (cityValue !== '') {
                searchQuery += 'city=' + encodeURIComponent(cityValue) + '&';
            }
            if (hmoValue !== '') {
                searchQuery += 'hmo=' + encodeURIComponent(hmoValue) + '&';
            }
            if (therapistGenderValue !== '') {
                searchQuery += 'therapistGender=' + encodeURIComponent(therapistGenderValue) + '&';
            }
            if (entitlementValue !== '') {
                searchQuery += 'entitlement=' + encodeURIComponent(entitlementValue);
            }

            // Redirect to search result page with the constructed query
            window.location.href = 'searchResult.html';
        });
    }
});
