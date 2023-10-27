function setGameColors(colors) {
    let toggles = document.getElementsByClassName("toggle");
    for (let i=0; i < toggles.length; i++) {
        toggles[i].style.backgroundcolor = colors[i];
    }
}

function toggleUnmarked(color){
    var element = document.getElementById(color);
    element.classList.toggle("marked");
}

function checkOptions() {
    let toggles = document.getElementsByClassName("toggle");
    let cur_unmarked = document.getElementsByClassName("marked");
    if (cur_unmarked.length == 4) {
        for (let i=0; i < toggles.length; i++) {
            if (!toggles[i].classList.contains("marked")) {
                toggles[i].disabled = true;
            }
        } 
    } else {
        for (let i=0; i < toggles.length; i++) {
            toggles[i].disabled = false;
        }
    }
}