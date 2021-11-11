
const openDiv = document.querySelector('.open');
const openMenu = document.querySelector('.openMenu');
const closeMenu = document.querySelector('.closeMenu');
const inMenu = document.querySelector('.inMenu');
const header = document.querySelector('header');
const footer = document.querySelector('footer');
const main = document.querySelector('main');


openDiv.onclick = () => {
    inMenu.style.display = 'block';
    header.style.backgroundImage = "none";
    openMenu.style.display = 'none';
    footer.style.display = 'none';
    main.style.display = 'none';
}

closeMenu.onclick = () => {
    openMenu.style.display = 'flex';
    inMenu.style.display = 'none';
    header.style.backgroundImage = "linear-gradient(150deg, var(--primary-color), var(--overlay-color) )";
    footer.style.display = 'block';
    main.style.display = 'block';
}
