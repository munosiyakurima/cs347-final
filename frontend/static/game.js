function setGameColors(colors) {
    let colortoggles = document.getElementsByClassName("colortoggle");
    for (let i=0; i < colortoggles.length; i++) {
        colortoggles[i].style.backgroundcolor = colors[i];
    }
}

function toggleUnmarked(color){
    var element = document.getElementById(color);
    element.classList.toggle("unmarked");
}

(function checkOptions() {
    let colortoggles = document.getElementsByClassName("colortoggle");
    let cur_unmarked = document.getElementsByClassName("unmarked");
    if (cur_unmarked.length == 2) {
        for (let i=0; i < colortoggles.length; i++) {
            if (colortoggles[i].classList.contains("unmarked")) {
                colortoggles[i].disabled = true;
            }
        } 
    } else {
        for (let i=0; i < colortoggles.length; i++) {
            colortoggles[i].disabled = false;
        }
    }
})();