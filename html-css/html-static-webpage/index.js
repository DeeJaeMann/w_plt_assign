let slideIndex = 0;
carousel();

function carousel() {
    let slides = document.getElementsByClassName("carousel-image");

    for(let intI = 0; intI < slides.length; intI++) {
        slides[intI].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.display = "block";
    setTimeout(carousel, 2000);
}