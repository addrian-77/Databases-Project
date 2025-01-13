let technologies = [];
document.addEventListener('DOMContentLoaded', () => {
    // Lista de tehnologii

    let currentSlide = 0;

    // Funcția care afișează tehnologia curentă
    function showTechnology(index) {
        const technology = technologies[index];
        console.log(technology);
        document.getElementById('techName').textContent = technology.name;
        document.getElementById('techDescription').textContent = technology.description;
        let category_obj = technology.category
        document.getElementById('techCategory').textContent = category_obj.name;
        let manufacturer_obj = technology.manufacturer
        document.getElementById('techManufacturer').textContent = manufacturer_obj.name;
    }


    // Swipe cu mouse-ul
    const slideContainer = document.getElementById('slideContainer');
    slideContainer.style.cursor = 'grab';
    let startX;

    slideContainer.addEventListener('mousedown', (e) => {
        startX = e.clientX;
        e.preventDefault()
    });

    slideContainer.addEventListener('mouseup', (e) => {
        const endX = e.clientX;
        if (startX > endX + 50) {
            currentSlide = (currentSlide === technologies.length - 1) ? 0 : currentSlide + 1;
        } else if (startX < endX - 50) {
            currentSlide = (currentSlide === 0) ? technologies.length - 1 : currentSlide - 1;
        }
        showTechnology(currentSlide);
    });

    // Swipe pe mobil
    slideContainer.addEventListener('touchstart', (e) => {
        startX = e.touches[0].clientX;
    });

    slideContainer.addEventListener('touchend', (e) => {
        const endX = e.changedTouches[0].clientX;
        if (startX > endX + 50) {
            currentSlide = (currentSlide === technologies.length - 1) ? 0 : currentSlide + 1;
        } else if (startX < endX - 50) {
            currentSlide = (currentSlide === 0) ? technologies.length - 1 : currentSlide - 1;
        }
        showTechnology(currentSlide);
    });

    // Inițializare
    showTechnology(currentSlide);

    const techniqueSelect = document.getElementById('techniqueSelect');
    const customTechniqueInput = document.getElementById('customTechnique');

    // Event listener for dropdown selection change
    techniqueSelect.addEventListener('change', function() {
    if (this.value === 'add-your-own') {
        // Show the custom text input
        customTechniqueInput.style.display = 'block';
        // Set the required attribute for the custom input
        customTechniqueInput.required = true;
    } else {
        // Hide the custom text input
        customTechniqueInput.style.display = 'none';
        // Remove the required attribute
        customTechniqueInput.required = false;
    }
    });

    const manufacturerSelect = document.getElementById('manufacturerSelect');
    const customManufacturerNameInput = document.getElementById('customManufacturerName');
    const customManufacturerAddressInput = document.getElementById('customManufacturerAddress');

    // Event listener for dropdown selection change
    manufacturerSelect.addEventListener('change', function() {
    if (this.value === 'add-your-own') {
        // Show the custom text input
        customManufacturerNameInput.style.display = 'block';
        // Set the required attribute for the custom input
        customManufacturerNameInput.required = true;
        customManufacturerAddressInput.style.display = 'block';
        // Set the required attribute for the custom input
        customManufacturerAddressInput.required = true;
    } else {
        // Hide the custom text input
        customManufacturerNameInput.style.display = 'none';
        // Remove the required attribute
        customManufacturerNameInput.required = false;
        customManufacturerAddressInput.style.display = 'none';
        // Remove the required attribute
        customManufacturerAddressInput.required = false;
    }
    });
});
