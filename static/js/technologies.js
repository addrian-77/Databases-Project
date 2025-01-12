document.addEventListener('DOMContentLoaded', () => {
    // Lista de tehnologii
    let technologies = [
        {
            name: "Solar Panel X3000",
            description: "Advanced solar panel technology for residential and industrial use.",
            category: "Renewable Energy",
            manufacturer: "EcoTech Inc."
        },
        {
            name: "Water Purifier Pro",
            description: "High-efficiency water purification system.",
            category: "Water Management",
            manufacturer: "Aqua Solutions"
        }
    ];

    let currentSlide = 0;

    // Funcția care afișează tehnologia curentă
    function showTechnology(index) {
        const technology = technologies[index];
        document.getElementById('techName').textContent = technology.name;
        document.getElementById('techDescription').textContent = technology.description;
        document.getElementById('techCategory').textContent = technology.category;
        document.getElementById('techManufacturer').textContent = technology.manufacturer;
    }

    // Formular pentru adăugare tehnologie
    const form = document.getElementById('technologyForm');
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const newTechnology = {
            name: document.getElementById('name').value,
            description: document.getElementById('description').value,
            category: document.getElementById('category').value,
            manufacturer: document.getElementById('manufacturer').value
        };
        technologies.push(newTechnology);
        alert('Technology added!');
        form.reset();
        currentSlide = technologies.length - 1;
        showTechnology(currentSlide); // Arată tehnologia nou adăugată
    });

    // Swipe cu mouse-ul
    const slideContainer = document.getElementById('slideContainer');
    let startX;

    slideContainer.addEventListener('mousedown', (e) => {
        startX = e.clientX;
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
});
