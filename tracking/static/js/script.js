document.addEventListener('DOMContentLoaded', function () {
  const imageUrls = [
    'http://localhost:8000/media/images/2024-06-25_14-58-15.jpg',
  ];

  const bottomSection = document.getElementById('bottom-section');
  const socket = new WebSocket(
    'ws://' + window.location.host + '/fetch-image/'
  );

  // Handle messages received from the WebSocket
  socket.onmessage = function (event) {
    const data = JSON.parse(event.data);
    if (data.image_path) {
      imageUrls.push(data.image_path);
      disabledButtonAndModel();
      displayImages([data.image_path]);
    }
  };

  // Fetch initial image list from the API
  fetch('http://localhost:8000/api/mouse-events')
    .then((response) => response.json())
    .then((data) => {
      const paths = data.map((element) => element.image_path);
      imageUrls.push(...paths); // Spread syntax to add all new paths
      displayImages(paths); // Display all fetched images
    })
    .catch((error) => console.error('Error fetching images:', error));

  // Function to display images
  function displayImages(paths) {
    paths.forEach((url) => {
      const img = document.createElement('img');
      img.src = url;
      img.onclick = function () {
        showModal(url);
      };
      bottomSection.appendChild(img);
    });
  }
});

function toggleTracking() {
  disabledButtonAndModel(true);
  fetch('/start_track')
    .then((response) => response.text())
    .then((data) => console.log(data))
    .catch((error) => console.error('Error starting tracking:', error));
}

function disabledButtonAndModel(is_disable = false) {
  const bottomSection = document.getElementById('bottom-section');
  const button = document.getElementById('trackingButton');
  if (is_disable) {
    bottomSection.classList.add('disabled');
    button.textContent = 'Tracking...';
    button.disabled = true;
  } else {
    bottomSection.classList.remove('disabled');
    button.textContent = 'Start Tracking';
    button.disabled = false;
  }
}

function showModal(imageUrl) {
  const modal = document.getElementById('myModal');
  const modalImg = document.getElementById('modalImage');
  modal.style.display = 'flex';
  modalImg.src = imageUrl;
}

const modal = document.getElementById('myModal');
const span = document.getElementsByClassName('close')[0];

span.onclick = function () {
  modal.style.display = 'none';
};

window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = 'none';
  }
};
