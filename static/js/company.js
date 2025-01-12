// Asigurăm că scriptul rulează după ce pagina este încărcată
document.addEventListener('DOMContentLoaded', () => {
    // Selectăm formularul și butonul
    const form = document.getElementById('companyForm');
    const registerButton = document.getElementById('registerButton');

    // Gestionăm trimiterea formularului
    form.addEventListener('submit', (e) => {
        e.preventDefault();

        // Preluăm valorile introduse
        const companyName = document.getElementById('companyName').value.trim();
        const username = document.getElementById('username').value.trim();
        const country = document.getElementById('country').value;
        const location = document.getElementById('location').value.trim();

        // Verificăm dacă toate câmpurile sunt completate
        if (companyName && username && country && location) {
            showSuccessMessage(`Company "${companyName}" registered successfully!`);
            form.reset(); // Resetăm formularul
        } else {
            showErrorMessage('Please fill in all fields.');
        }
    });

    // Funcție pentru afișarea mesajului de succes
    function showSuccessMessage(message) {
        const messageBox = document.createElement('div');
        messageBox.className = 'success-message';
        messageBox.textContent = message;
        document.body.appendChild(messageBox);

        // Eliminăm mesajul după 3 secunde
        setTimeout(() => {
            messageBox.remove();
        }, 3000);
    }

    // Funcție pentru afișarea mesajului de eroare
    function showErrorMessage(message) {
        const messageBox = document.createElement('div');
        messageBox.className = 'error-message';
        messageBox.textContent = message;
        document.body.appendChild(messageBox);

        // Eliminăm mesajul după 3 secunde
        setTimeout(() => {
            messageBox.remove();
        }, 3000);
    }
});
