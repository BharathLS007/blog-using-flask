// Validate the form before submitting
document.getElementById("submission_form").addEventListener("submit", function(e) {
  e.preventDefault();

  // Get the form data
  var firstName = document.getElementById("first_name").value;
  var lastName = document.getElementById("last_name").value;
  var email = document.getElementById("email").value;
  var subject = document.getElementById("subject").value;
  var comment = document.getElementById("comment").value;

  // Validate the form data
  if (firstName == "" || lastName == "" || email == "" || subject == "" || comment == "") {
    alert("Please fill out all of the required fields.");
    return;
  }

  // Submit the form data
  // TODO: Implement this function to submit the form data to your server
  submitFormData(firstName, lastName, email, subject, comment);
});

// Submit the form data to the server
function submitFormData(firstName, lastName, email, subject, comment) {
  // TODO: Implement this function to submit the form data to your server
  console.log("Form data submitted successfully!");
}
