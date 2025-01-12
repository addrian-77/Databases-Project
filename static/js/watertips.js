function showInfo(user, tipText) {
    // Find the tip-info div and make it visible
    const tipInfoDiv = document.querySelector('.tip-info');
    tipInfoDiv.classList.remove('hidden'); // Show the div

    // Display the message and the user who added the tip
    document.getElementById('tipMessage').textContent = `Tip: ${tipText}`;
    document.getElementById('userMessage').textContent = `Added by: ${user}`;
}

document.addEventListener("mousedown", (e) => {
    const tipInfoDiv = document.querySelector('.tip-info');
    if (!tipInfoDiv.contains(e.target)) {
        tipInfoDiv.classList.add('hidden');
    }
});