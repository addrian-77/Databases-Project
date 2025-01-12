function flashcardBehaiviour() {
    let flashcardsContainer = document.getElementById('flashcardsContainer');
    let isMouseDown = false;
    let startX;
    let scrollLeft;
    flashcardsContainer.addEventListener('mousedown', (e) => {
    isMouseDown = true;
    startX = e.pageX - flashcardsContainer.offsetLeft;
    scrollLeft = flashcardsContainer.scrollLeft;
    flashcardsContainer.style.cursor = 'grabbing';
    });

    flashcardsContainer.addEventListener('mouseleave', () => {
    isMouseDown = false;
    flashcardsContainer.style.cursor = 'grab';
    });

    flashcardsContainer.addEventListener('mouseup', () => {
    isMouseDown = false;
    flashcardsContainer.style.cursor = 'grab';
    });

    flashcardsContainer.addEventListener('mousemove', (e) => {
    if (!isMouseDown) return;
    e.preventDefault();
    const x = e.pageX - flashcardsContainer.offsetLeft;
    const walk = (x - startX) * 1.5; // Scroll speed
    flashcardsContainer.scrollLeft = scrollLeft - walk;
    });
}
