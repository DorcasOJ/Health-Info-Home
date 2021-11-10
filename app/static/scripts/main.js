
const openDiv = document.querySelector('.open');
const openMenu = document.querySelector('.openMenu');
const closeMenu = document.querySelector('.closeMenu');
const inMenu = document.querySelector('.inMenu');
const footer = document.querySelector('footer');
const main = document.querySelector('main');

//const bannerImg = document.querySelector('.banner-img');
//const pageDesc = document.querySelector('.page-desc');
//const mainDiv = document.querySelector('.main-div');

openDiv.onclick = () => {
    inMenu.style.display = 'block';
    openMenu.style.display = 'none';
    footer.style.display = 'none';
    main.style.display = 'none';
   // bannerImg.style.display = 'none';
   // pageDesc.style.display = 'none';
   // mainDiv.style.display = 'none';
}

closeMenu.onclick = () => {
    openMenu.style.display = 'flex';
    inMenu.style.display = 'none';
    footer.style.display = 'block';
    main.style.display = 'block';
   // bannerImg.style.display = 'block';
   // pageDesc.style.display = 'block';
   // mainDiv.style.display = 'block';
}

// 1. close menu also with Esc key

/*
function handleMouseMove(event) {
  const height = window.innerHeight;
  const width = window.innerWidth;
  // Creates angles of (-20, -20) (left, bottom) and (20, 20) (right, top)
  const yAxisDegree = event.pageX / width * 40 - 20;
  const xAxisDegree = event.pageY / height * -1 * 40 + 20;
  target.style.transform = `rotateY(${yAxisDegree}deg) rotateX(${xAxisDegree}deg)`;
  // Set the sheen position
  setSheenPosition(event.pageX / width, event.pageY / width);
}


function setSheenPosition(xRatio, yRatio) {
    // This creates a "distance" up to 400px each direction to offset the sheen
    const xOffset = 1 - (xRatio - 0.5) * 800;
    const yOffset = 1 - (yRatio - 0.5) * 800;
    target.style.setProperty('--sheenX', `${xOffset}px`)
    target.style.setProperty('--sheenY', `${yOffset}px`)
  }
*/