class homepage_database_scripts {
    get_country_data() {
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
}