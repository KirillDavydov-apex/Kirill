let currentIndex = 0;
const images = [
    'image1.jpg',
    'image2.jpg',
    'image3.jpg',
    'image4.jpg',
    'image5.jpg'
];

const slideImage = document.getElementById('slideImage');
const imageCounter = document.getElementById('imageCounter');

function updateSlide() {
    slideImage.src = images[currentIndex];
    imageCounter.textContent = `Изображение ${currentIndex + 1} из ${images.length}`;
}

function changeSlide(direction) {
    currentIndex += direction;

    if (currentIndex < 0) {
        currentIndex = images.length - 1; // Зацикливание
    } else if (currentIndex >= images.length) {
        currentIndex = 0; // Зацикливание
    }

    updateSlide();
}
 
// Начальная инициализация
updateSlide();