function signup() {
  window.open("http://127.0.0.1:5500/grocery_store_project/frontend/Register.html", "_blank");
}

document.getElementById('Register').addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the form from submitting normally

  // Get the user details
  var username = document.getElementById('username').value;
  var gmail = document.getElementById('email').value;
  var password = document.getElementById('password').value;

  var data = {
    username: username,
    password: password,
    gmail: gmail
  };

  fetch('http://127.0.0.1:5000/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
  .then(response => {
    if (response.ok) {
      // Registration successful
      alert('Registration successful!');
      // Optionally, redirect to another page
      window.location.href = 'http://127.0.0.1:5500/grocery_store_project/frontend/Login.html';
    } else {
      // Registration failed
      alert('Registration failed. Please try again.');
    }
  })
  .catch(error => {
    console.error('Error:', error);
    alert('An error occurred. Please try again later.');
  });
});
