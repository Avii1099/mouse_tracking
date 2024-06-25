document.addEventListener('DOMContentLoaded', function () {
  const imageUrls = [];

  const bottomSection = document.getElementById('bottom-section');
  const socket = new WebSocket(
    'ws://' + window.location.host + '/fetch-image/'
  );

  const socket2 = new WebSocket(
    'ws://' + window.location.host + '/mouse-coordinates/'
  );

  socket2.onmessage = function (event) {
    const data = JSON.parse(event.data);
    data.map((elements) => {
      const button = document.getElementById('trackingButton');
      button.textContent = `Tracking... (X: ${elements.x_total}, Y: ${elements.y_total})`;
    });
  };

  // Handle messages received from the WebSocket
  socket.onmessage = function (event) {
    const data = JSON.parse(event.data);
    if (data.image_path) {
      disabledButtonAndModel();
      displaySocketImages(data);
    }
  };

  // Fetch initial image list from the API
  fetch('http://localhost:8000/api/mouse-events/')
    .then((response) => response.json())
    .then((data) => {
      imageUrls.push(...data);
      displayImages(imageUrls);
    })
    .catch((error) => console.error('Error fetching images:', error));

  function displaySocketImages(data) {
    const container = document.createElement('div');
    container.className = 'socket-image';
    const img = document.createElement('img');
    const title = document.createElement('p');
    img.src = data.image_path;
    img.onclick = function () {
      showModal(data.image_path);
    };

    title.innerHTML = `X: ${data.x_coordinate}, Y: ${data.y_coordinate}`;
    container.appendChild(img);
    container.appendChild(title);
    bottomSection.appendChild(container);
  }

  // Function to display images
  function displayImages(data) {
    data.forEach((element) => {
      const container = document.createElement('div');
      const img = document.createElement('img');
      const title = document.createElement('p');

      img.src = element.image_path;
      img.onclick = function () {
        showModal(element.image_path);
      };

      title.innerHTML = `X: ${element.x_coordinate}, Y: ${element.y_coordinate}`;
      container.appendChild(img);
      container.appendChild(title);
      bottomSection.appendChild(container);
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
  const bottomPara = document.getElementById('button-para');

  const button = document.getElementById('trackingButton');
  if (is_disable) {
    bottomSection.classList.add('disabled');
    button.textContent = 'Tracking...';
    button.disabled = true;
    bottomPara.style.display = 'block';
  } else {
    bottomSection.classList.remove('disabled');
    button.textContent = 'Start Tracking';
    button.disabled = false;
    bottomPara.style.display = 'none';
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
