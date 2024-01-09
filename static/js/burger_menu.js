function BurgerMenu(){
    var side_bar = document.querySelector('.side_bar')

    if (side_bar.style.display == '' || side_bar.style.display == 'none'){
        side_bar.style.display = 'flex'
    }
    else {
        side_bar.style.display = 'none'
    }

}