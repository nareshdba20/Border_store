function opentab() {
    window.open("http://127.0.0.1:5500/grocery_store_project/frontend/login.html", "_blank");
  }


function validatelogin() {
  var username = document.getElementById('username').value;
  var password = document.getElementById('password').value;

  if(username === "" || password === "")
      {
          alert("usernmame  and password are required");
          return false;
      }
  alert("login succesful");
  return true;

}