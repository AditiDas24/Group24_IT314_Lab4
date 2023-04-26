// Select the form and the input fields
const form = document.querySelector('form');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');

form.addEventListener('submit', (event) => {
  event.preventDefault(); 

  const name = nameInput.value.trim();
  const email = emailInput.value.trim();
  const password = passwordInput.value.trim();
  const confirmPassword = confirmPasswordInput.value.trim();

  if (name === '') {
    alert('Please enter your name.');
    nameInput.focus();
    return false;
  }

  if (email === '') {
    alert('Please enter your email address.');
    emailInput.focus();
    return false;
  } else if (!validateEmail(email)) {
    alert('Please enter a valid email address.');
    emailInput.focus();
    return false;
  }

  if (password === '') {
    alert('Please enter a password.');
    passwordInput.focus();
    return false;
  } else if (!isPasswordStrong(password)) {
    alert('Password should contain at least 8 characters, including at least one uppercase letter, one lowercase letter, one number, and one special character.');
    passwordInput.focus();
    return false;
  }

  if (confirmPassword === '') {
    alert('Please confirm your password.');
    confirmPasswordInput.focus();
    return false;
  } else if (confirmPassword !== password) {
    alert('Password and Confirm Password fields do not match.');
    confirmPasswordInput.focus();
    return false;
  }

  form.submit();
});

function validateEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

function isPasswordStrong(password) {
  const regex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z])(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
  return regex.test(password);
}
