  // Efecto al hacer scroll
  window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar-transparent');
    if (window.scrollY > 50) {
      navbar.classList.add('navbar-scrolled');
    } else {
      navbar.classList.remove('navbar-scrolled');
    }
  });