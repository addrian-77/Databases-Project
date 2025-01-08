class about_other_scripts {
    mouse_swipe_behaiviour() {
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
}

class homepage_other_scripts {
    map_click_behaviour() {
        simplemaps_worldmap.hooks.click_state = function (id) {
            const countryData = simplemaps_worldmap_mapdata.state_specific[id];
            const countryName = countryData?.name || "Unknown Country";

            // Capture the mouse event
            const event = window.event; // Get the global event object
            const mouseX = event.clientX; // X coordinate of the click
            const mouseY = event.clientY; // Y coordinate of the click

            // Adjust for popup positioning
            const popupOffsetX = 10; // Offset to prevent overlap with the cursor
            const popupOffsetY = 10;

            // Position the popup near the mouse click
            const popup = document.getElementById('popup');
            popup.style.left = `${mouseX + popupOffsetX}px`;
            popup.style.top = `${mouseY + popupOffsetY}px`;
            popup.style.display = "block";
            popup.classList.add('show'); // Add fade-in effect
            event.stopPropagation();

            // Fetch and update the popup content
            fetch(`/get_country_data/?name=${encodeURIComponent(countryName)}`)
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        document.getElementById('popup-content').innerHTML = `
                            <strong>${data.data.name}</strong><br>
                            Population: ${data.data.population || 'N/A'}<br>
                            Capital: ${data.data.capital || 'N/A'}
                        `;
                    } else {
                        document.getElementById('popup-content').innerHTML = 'Error fetching country data.';
                    }
                })
                .catch(error => {
                    console.error(error);
                    document.getElementById('popup-content').innerHTML = 'An error occurred.';
                });
        };
    }

    closePopup() {
        const popup = document.getElementById('popup');
        popup.style.display = "none";
    }

    closePopupOnOutsideClick() {
        document.addEventListener("mousedown", (mousedown) => {
            if (!document.getElementById('popup').contains(mousedown.target)) {
                this.closePopup();
            }
        });
    }
}