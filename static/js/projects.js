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
      if(stepIndex == formSteps.length - 1) {
        console.log('reached');
        showCustomizationForm();
      }
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
    console.log(formData);

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
      this.reset();
      showDescription();
      currentStep = 0;
      showStep(currentStep);
      currentStep = -1;
      updateProgressBar();
      currentStep = 0;
  });

});

function showDescription() {
  const category = document.getElementById('category').value;
  const descriptionDiv = document.querySelector('.category-description');

  if (category) {
    fetch(`/get_category_description/?category=${encodeURIComponent(category)}`)
      .then(response => response.json())
      .then(data => {
        descriptionDiv.innerHTML = '<p>Basic description:<ul class=description>' + data.description + '</ul>';
        descriptionDiv.classList.remove('hidden'); // Show the description div
      })
      .catch(error => {
        console.error('Error fetching category description:', error);
        descriptionDiv.textContent = 'Unable to fetch description.';
        descriptionDiv.classList.remove('hidden');
      });
  } else {
    descriptionDiv.textContent = ''; // Clear description if no category selected
    descriptionDiv.classList.add('hidden'); // Hide the description div
  }
}

function showCustomizationForm() {
  const category = document.getElementById('category').value;
  const customizationDiv = document.getElementById('guidanceSection');

  if (category) {
    fetch(`/get_category_customization/?category=${encodeURIComponent(category)}`)
      .then(response => response.json())
      .then(data => {
        customizationDiv.innerHTML = '<h2> Personalize Your ' + category + ' </h2>' + data.form;
        customizationDiv.classList.remove('hidden'); // Show the description div
      })
      .catch(error => {
        console.error('Error fetching category description:', error);
        customizationDiv.textContent = 'Unable to fetch description.';
        customizationDiv.classList.remove('hidden');
      });
  } else {
    customizationDiv.textContent = 'Please select a category.'; // Clear description if no category selected
    customizationDiv.classList.add('hidden'); // Hide the description div
  }
}