// Preluăm formularul și lista proiectelor
const projectForm = document.getElementById('add-project-form');
const projectList = document.getElementById('projects');

// Adăugăm un eveniment pentru submit-ul formularului
projectForm.addEventListener('submit', function (event) {
    event.preventDefault(); // Oprim reîncărcarea paginii

    // Preluăm valorile din formular
    const projectName = document.querySelector('#add-project-form input[type="text"]').value;
    const locationId = document.querySelector('#add-project-form input[type="number"]').value;

    // Validăm datele
    if (!projectName || !locationId) {
        alert('Please fill out both fields.');
        return;
    }

    // Adăugăm proiectul în listă
    const li = document.createElement('li');
    li.textContent = `${projectName} - Location ID: ${locationId}`;
    projectList.appendChild(li);

    // Resetăm formularul
    projectForm.reset();
});
