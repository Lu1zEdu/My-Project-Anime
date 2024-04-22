const loginForm = document.getElementById('login-form');

loginForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  // Replace this with your own logic for checking the username and password
  if (username === 'admin' && password === 'password') {
    window.location.href = 'dashboard.html';
  } else {
    alert('Invalid username or password');
  }
});