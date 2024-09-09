function toggleMenu() {
    var burgerNav = document.querySelector('.burger-nav-container');
    if (burgerNav.classList.contains('active')) {
        burgerNav.style.height = "0"; // Collapse the menu
    } else {
        burgerNav.style.height = "200px"; // Expand the menu (adjust the height as needed)
    }
    burgerNav.classList.toggle('active');
}