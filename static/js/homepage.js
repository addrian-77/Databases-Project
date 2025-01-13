function map_click_behaviour() {
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

function highlightCountry(name) {
    // Loop through the state_specific object to find the country by name
    for (const countryCode in simplemaps_worldmap_mapdata.state_specific) {
      const country = simplemaps_worldmap_mapdata.state_specific[countryCode];
  
      // Check if the country's name matches the given name
      if (country.name === name) {
        // Highlight the country
        simplemaps_worldmap_mapdata.state_specific[countryCode].color = '#53c920'; // Highlight color (red)
        simplemaps_worldmap_mapdata.state_specific[countryCode].hover_color = '#6be835'; // Hover color (light red)
        simplemaps_worldmap_mapdata.state_specific[countryCode].description = `${name} is highlighted`; // Tooltip text
  
        // Refresh the map to apply the changes
        return; // Exit the function once the country is found and updated
      }
    }
  
    // If country not found
    console.error(`Country with name '${name}' not found in the map data.`);
  }
  

// Helper method to close the popup
function closePopup() {
    const popup = document.getElementById('popup');
    popup.style.display = "none";
    popup.classList.remove('show');
    document.getElementById('popup-content').innerHTML = ""; // Clear content
}


function closePopupOnOutsideClick() {
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


// Function to enable/disable scroll behavior
function handleScrollBehavior() {
    document.addEventListener("DOMContentLoaded", () => {
        const mapDiv = document.getElementById('map');
        const mapContainer = document.getElementById('mapdiv');
        let isInteractive = true; // Tracks whether the map is interactive

        // Enable map interaction on click
        mapContainer.addEventListener("click", () => {
            isInteractive = true;
            mapDiv.style.pointerEvents = 'all'; // Enable interaction
            console.log("Map is now interactive");
        });

        // Disable map interaction on scrollwheel or scrolling
        window.addEventListener("wheel", (event) => {
            // console.log(simplemaps_worldmap.clone.zooming_complete);
            // console.log(simplemaps_worldmap.hooks.zooming_complete)
            this.closePopup();
            if (isInteractive == true && simplemaps_worldmap.zoom_level == 'out' && event.deltaY > 0) {
                isInteractive = false;
                mapDiv.style.pointerEvents = 'none'; // Disable interaction
                console.log("Map interaction disabled due to scrolling");
            }
        });

        // Optionally disable interaction on touch scroll (for mobile devices)
        window.addEventListener("touchmove", (event) => {
            if (isInteractive) {
                isInteractive = false;
                mapDiv.style.pointerEvents = 'none'; // Disable interaction
                console.log("Map interaction disabled due to touch scroll");
            }
        });
    });
}