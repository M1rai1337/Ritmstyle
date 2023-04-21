const reviewsSlider = new Swiper('.reviews-slider', {
    speed: 500,
    initialSlide: 1,
    centeredSlides: true,
    simulateTouch: false,
    pagination: { el: '.reviews-pagination', clickable: true, },
   
    breakpoints: {
        1760: { slidesPerView: 3,   spaceBetween: 100, },
        1500: { slidesPerView: 2.8, spaceBetween: 80, },
        1300: { slidesPerView: 2.6, spaceBetween: 80, },
        992:  { slidesPerView: 2.2, spaceBetween: 70, },
        768:  { slidesPerView: 1.9, spaceBetween: 60, },
        541:  { slidesPerView: 1.3, spaceBetween: 20, },
        0:    { slidesPerView: 1.1, spaceBetween: 10, },
    }
});
