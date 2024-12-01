document.getElementById("registerForm").addEventListener("submit", function(event) {
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirm_password").value;
    const passwordError = document.getElementById("passwordError");

    if (password !== confirmPassword) {
        event.preventDefault(); 
        passwordError.style.display = "block"; // Show error message
    } else {
        passwordError.style.display = "none"; // Hide error message
    }
});
