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
        simplemaps_worldmap.hooks.click_state = function (id, event) {
            const countryData = simplemaps_worldmap_mapdata.state_specific[id];
            const countryName = countryData?.name || "Unknown Country";
        
            if (countryName !== "Unknown Country") {
                // Capture mouse coordinates
                const mouseX = event.clientX || 0;
                const mouseY = event.clientY || 0;
        
                // Position the popup
                const popup = document.getElementById('popup');
                popup.style.left = `${mouseX + 10}px`;
                popup.style.top = `${mouseY + 10}px`;
                popup.style.display = "block";
                popup.classList.add('show');
        
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
            }
        };
        
        // Close popup on outside click or drag
        document.addEventListener("mousedown", (e) => {
            const popup = document.getElementById('popup');
            if (!popup.contains(e.target)) {
                popup.style.display = "none";
                popup.classList.remove('show');
            }
        });
        
    }

    // Helper method to close the popup
    closePopup() {
        const popup = document.getElementById('popup');
        popup.style.display = "none";
        popup.classList.remove('show');
        document.getElementById('popup-content').innerHTML = ""; // Clear content
    }
    

    closePopupOnOutsideClick() {
        // Get the map container element
        const mapContainer = document.getElementById('map'); // Replace with your map container's ID
    
        // Close popup on mouse down outside or during map drag
        document.addEventListener("mousedown", (mousedown) => {
            const popup = document.getElementById('popup');
    
            // Check if the click was outside the popup
            if (!popup.contains(mousedown.target)) {
                this.closePopup();
            }
        });
    
        // Detect map drag and close popup
        mapContainer.addEventListener("mousedown", () => {
            // Add a temporary mousemove listener to detect dragging
            const onMouseMove = () => {
                this.closePopup(); // Close the popup on drag start
                // Clean up the mousemove listener once the drag is detected
                mapContainer.removeEventListener("mousemove", onMouseMove);
            };
    
            // Attach the mousemove listener to detect dragging
            mapContainer.addEventListener("mousemove", onMouseMove);
    
            // Clean up the listener on mouseup to prevent unintended closures
            const onMouseUp = () => {
                mapContainer.removeEventListener("mousemove", onMouseMove);
                mapContainer.removeEventListener("mouseup", onMouseUp);
            };
    
            mapContainer.addEventListener("mouseup", onMouseUp);
        });
    }
    
}