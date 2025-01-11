// Așteaptă până când DOM-ul este complet încărcat
document.addEventListener("DOMContentLoaded", function () {
  // Selectăm toate slide-urile și butoanele
  const formSteps = document.querySelectorAll(".form-step");
  const nextBtns = document.querySelectorAll(".next-btn");
  const prevBtns = document.querySelectorAll(".prev-btn");
  const progress = document.getElementById("progress");
  const guidanceSection = document.getElementById("guidanceSection");

  let currentStep = 0;
  // Funcția care afișează slide-ul curent
  function showStep(stepIndex) {
    formSteps.forEach((step, index) => {
      step.classList.toggle("active", index === stepIndex);
    });
  }

  // Actualizează bara de progres
  function updateProgressBar() {
    progress.style.width = `${((currentStep + 1) / formSteps.length) * 100}%`;
  }

  // Gestionarea butonului Next
  nextBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      if (currentStep < formSteps.length - 1) {
        currentStep++;
        showStep(currentStep);
        updateProgressBar();
      }
    });
  });

  // Gestionarea butonului Back
  prevBtns.forEach((btn) => {
    btn.addEventListener("click", () => {
      if (currentStep > 0) {
        currentStep--;
        showStep(currentStep);
        updateProgressBar();
      }
    });
  });

  // Gestionarea trimiterii formularului și afișarea ghidului dinamic
  document.getElementById("projectForm").addEventListener("submit", function (event) {
    event.preventDefault(); // Previne comportamentul implicit al formularului

    // Gather form data
    const form = event.target;
    const formData = new FormData(form);

    // Send POST request using Fetch API
    fetch('/submit_project/', {
      method: 'POST',
      headers: {
        'X-CSRFToken': formData.get('csrfmiddlewaretoken'), // Pass the CSRF token
      },
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.status === 'success') {
          alert(data.message);

          // Optionally redirect to a different page
          window.location.href = '/projects/';
        } else {
          alert(data.message || 'Something went wrong. Please try again.');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
      });
      currentStep = 0;
      showStep(currentStep)
  });

});
