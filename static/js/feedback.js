document.addEventListener('DOMContentLoaded', () => {
  const feedbackForm = document.getElementById('feedbackForm');

  feedbackForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const project = document.getElementById('project').value;
    const feedback = document.getElementById('feedback').value;

    // Simulează trimiterea feedback-ului
    alert(`Feedback pentru ${project}: "${feedback}" a fost trimis cu succes!`);

    // Curăță formularul după submit
    feedbackForm.reset();
  });
});
