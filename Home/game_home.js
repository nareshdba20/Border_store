// Function to add data
function addData() {
  let gameuser = document.getElementById("username").value;
  let gamename = document.getElementById("user_game").value;
  let gamemoney = document.getElementById("game_money").value;
  let dateCreated = document.getElementById("date_created").value;

  let data = {
    username: gameuser,
    user_game: gamename,
    game_money: gamemoney,
    date_created: dateCreated
  };

  // Send data to backend using AJAX
  fetch('http://127.0.0.1:5000/save_game_user', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
  .then(response => {
    if (response.ok) {
      alert('Saved successfully!');
      clearInputs(); // Call clearInputs() after successful submission
      fetchData();
    } else {
      // Handle error
      console.error('Response failed:', response.statusText);
    }
  })
  .catch(error => {
    console.error('Network error:', error);
  });
}


// Function to clear input fields
function clearInputs() {
  document.getElementById("gameuser").value = "";
  document.getElementById("gamename").value = "";
  document.getElementById("gamemoney").value = "";
}

// Function to fetch all data from the backend
function fetchData() {
  fetch('http://127.0.0.1:5000/get_game_users') // Assuming your Flask app serves this route
      .then(response => {
          if (!response.ok) {
              throw new Error('Failed to fetch data');
          }
          return response.json();
      })
      .then(data => {
          // Clear existing table rows
          clearTable();

          // Iterate over the fetched data and display it in the table
          data.forEach(item => {
              displayData(item);
          });
      })
      .catch(error => {
          console.error('Error fetching data:', error);
      });
}

// Function to display data in the table
function displayData(item) {
  let table = document.getElementById("outputTable");
  let newRow = table.insertRow(-1); // Insert row at the end of the table

  let gameUserCell = newRow.insertCell(0);
  let gameNameCell = newRow.insertCell(1);
  let gameMoneyCell = newRow.insertCell(2);
  let dateCell = newRow.insertCell(3);
  let actionCell = newRow.insertCell(4);

  gameUserCell.textContent = item.username;
  gameNameCell.textContent = item.user_game;
  gameMoneyCell.textContent = item.game_money;
  dateCell.textContent = item.date_created;

  // Add any additional logic or elements to the action cell if needed
  actionCell.innerHTML = '<button onclick="deleteRow(this)">Delete</button>';
}

// Function to delete a row
function deleteRow(button) {
  let row = button.parentNode.parentNode;
  row.parentNode.removeChild(row);
}

// Function to clear the table
function clearTable() {
  let table = document.getElementById("outputTable");
  while (table.rows.length > 1) {
      table.deleteRow(1);
  }
}

// Fetch data when the page loads
fetchData();
