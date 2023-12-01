javascript
function validateForm(event) {
  event.preventDefault(); // Prevent form submission

  // Get form inputs
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;

  // Perform validation
  if (username === "" || password === "") {
    document.getElementById("error-message").textContent = "Please fill in all fields.";
  } else {
    // Successful login, redirect to main website
    window.location.href = "mainpage.html";
  }
}


