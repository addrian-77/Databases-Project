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
    event.preventDefault();

    const category = document.getElementById("category").value;
    let guidanceContent = "";

    switch (category) {
      case "Rainwater Harvesting":
        guidanceContent = `
          <h2>Rainwater Harvesting Guide</h2>
          <ul>
            <li>Identify rain collection areas (e.g., rooftops).</li>
            <li>Choose a storage solution (e.g., tanks).</li>
            <li>Install a filtration system.</li>
          </ul>
        `;
        break;

      case "Greywater Recycling":
        guidanceContent = `
          <h2>Greywater Recycling Guide</h2>
          <ul>
            <li>Identify greywater sources (e.g., sinks, showers).</li>
            <li>Install a recycling system with filters.</li>
            <li>Use recycled water for irrigation.</li>
          </ul>
        `;
        break;

      case "Leak Detection and Fixing":
        guidanceContent = `
          <h2>Leak Detection and Fixing Guide</h2>
          <ul>
            <li>Conduct a full water audit.</li>
            <li>Check faucets, toilets, and water lines for visible leaks.</li>
            <li>Fix leaks promptly to prevent water waste.</li>
          </ul>
        `;
        break;

      default:
        guidanceContent = `<h2>Please select a valid project category.</h2>`;
    }

    guidanceSection.innerHTML = guidanceContent;
    guidanceSection.classList.remove("hidden");
  });

  // 🔥 Adăugăm logica de redirecționare aici 🔥
  const nextBtn = document.getElementById("nextBtn");
  const categorySelect = document.getElementById("category");

  nextBtn.addEventListener("click", () => {
    const selectedCategory = categorySelect.value;

    if (selectedCategory) {
      // Redirecționăm utilizatorul către pagina proiectului selectat
      window.location.href = `/projects/${selectedCategory}/`;
    } else {
      // Afișăm un mesaj de eroare dacă nu a fost selectată o categorie
      alert("Please select a category to continue.");
    }
  });
});

