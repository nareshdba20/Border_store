document.getElementById('gameUserForm').addEventListener('submit', function(event) {
  event.preventDefault();
  var formData = new FormData(this);
  fetch('http://127.0.0.1:5000/save_game_user', {
      method: 'POST',
      body: JSON.stringify(Object.fromEntries(formData)),
      headers: {
          'Content-Type': 'application/json'
      }
  })
  .then(response => response.json())
  .then(data => {
      alert(data.message);
  })
  .catch(error => {
      console.error('Error:', error);
  });
});
