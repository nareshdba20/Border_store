
function opentab() {
  window.open("http://127.0.0.1:5500/Grocery_store_pjt/grocery_store_project/frontend/login.html", "_blank");
}


  document.getElementById('loginform').addEventListener('submit', function(event) {
    event.preventDefault(); 

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    var data = {
      username: username,
      password: password
  };

 
  fetch('http://127.0.0.1:5000/getuserdetails', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})

    .then(response => {
      if (response.ok) {
        window.open("http://127.0.0.1:5500/Grocery_store_pjt/grocery_store_project/Home/game.html", "_blank");
      } else {
          
         alert('save failed. Please try again.');
      }
    })
    .catch(error => {
      console.error('Network error:', error);
    });
});