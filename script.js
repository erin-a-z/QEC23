// your-script.js
let map;
let marker;

function initMap() {
    // Default coordinates (e.g., city center)
    const defaultLatLng = [0, 0];

    // Initialize the map
    map = L.map('map').setView(defaultLatLng, 8);

    // Add the OpenStreetMap layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    // Add a marker with a popup
    marker = L.marker(defaultLatLng, { draggable: true }).addTo(map);
    
    marker.bindPopup("Drag me to select a location!").openPopup();

    // Add a click event listener to capture coordinates
    map.on('click', function(event) {
        const clickedLatLng = event.latlng;
        updateMarker(clickedLatLng);
    });

    // Add a dragend event listener to update coordinates when the marker is dragged
    marker.on('dragend', function(event) {
        const draggedLatLng = marker.getLatLng();
        updateMarker(draggedLatLng);
    });
}

function updateMarker(latLng) {
    marker.setLatLng(latLng);
    console.log('Selected Coordinates:', latLng.lat, latLng.lng);

    // You can use these coordinates as needed (e.g., update a form input)
}

// Initialize the map when the document is ready
document.addEventListener('DOMContentLoaded', function() {
    initMap();
});

function callApi() {
  const apiUrl = 'https://api.example.com/endpoint';

  fetch(apiUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      // Process the data from the API
      console.log('API Response:', data);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

function call_api(){
  var startDateValue = Math.floor(new Date(document.getElementById('startDateInput').value).getTime() / 1000);
  console.log(startDateValue);
  var stopDateValue =  Math.floor(new Date(document.getElementById('stopDateInput').value).getTime() / 1000);
  console.log(stopDateValue);

  let coords = marker.getLatLng();
  let apiUrl = `http://127.0.0.1:5000/api/${coords.lng}/${coords.lng}/${startDateValue}/${stopDateValue}`;

  fetch(apiUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      // Process the data from the API
      console.log('API Response:', data);
      var out_img = document.getElementById("output_img")
      out_img.src = data.src;
    })
    .catch(error => {
      console.error('Error:', error);
    });
}

