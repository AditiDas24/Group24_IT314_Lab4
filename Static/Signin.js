const form = document.querySelector('form');
const emailInput = document.querySelector('#email');
const passwordInput = document.querySelector('#password');

form.addEventListener('submit', (event) => {
  event.preventDefault();
  
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(emailInput.value)) {
    alert('Please enter a valid email address');
    return;
  }
  
  const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
  if (!passwordRegex.test(passwordInput.value)) {
    alert('Your password must be at least 8 characters long and include at least one lowercase letter, one uppercase letter, and one number.');
    return;
  }
  
  form.submit();
});
