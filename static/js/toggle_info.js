function toggleInfo() {

    var infoBlock = document.querySelector('.info-about-operations');
    if (infoBlock.style.display == '' || infoBlock.style.display == 'none') {
        infoBlock.style.display = 'block';
    }
    else {
        infoBlock.style.display = 'none';
    }
}