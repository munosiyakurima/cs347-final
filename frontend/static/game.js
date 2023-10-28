let currentPassword = [];
const maxPasswordLen = 4

function setUpBoard(maxAttempts) {
    const gameTable = document.getElementById("gameInfo");
        for (let i = 0; i < maxAttempts; i++) { // creates game board
            const curRow = gameTable.insertRow(i+1);

            const cell1 = curRow.insertCell(0);
            cell1.innerHTML = (i+1).toString();

            const cell2 = curRow.insertCell(1);
            cell2.innerHTML = "?";

            const cell3 = curRow.insertCell(2);
            cell3.innerHTML = "?";
        }
}

function setUpColors(colorList) {
    const colorOptions = document.getElementById("passwordattempt");
        for (let i = 0; i < 6; i++) { // creates and sets color options
            const colorLabel = document.createElement("label");
            colorLabel.for = "color" + (i+1).toString();
            colorLabel.classList.add("colorlabel");
            colorLabel.title = colorList[i];

            const colorButton = document.createElement("input");
            colorButton.type = "checkbox";
            colorButton.classList.add("coloricon");
            colorButton.classList.add("colorbutton");
            colorButton.id = "color" + (i+1).toString();
            colorButton.onclick = function () {toggleUnmarked(colorButton.id)};
            colorButton.style.backgroundColor = colorList[i];

            colorLabel.appendChild(colorButton);
            colorOptions.appendChild(colorLabel);
        }
}

function toggleUnmarked(color){
    const element = document.getElementById(color);
    element.classList.toggle("marked");
}

function checkOptions() {
    let coloricons = document.getElementsByClassName("colorbutton");
    let cur_unmarked = document.getElementsByClassName("marked");
    if (cur_unmarked.length == 4) {
        for (let i=0; i < coloricons.length; i++) {
            if (!coloricons[i].classList.contains("marked")) {
                coloricons[i].disabled = true;
                document.getElementById("submit").value = "Send";
                document.getElementById("submit").disabled = false;
            }
        } 
    } else {
        for (let i=0; i < coloricons.length; i++) {
            coloricons[i].disabled = false;
            document.getElementById("submit").value = "Waiting";
            document.getElementById("submit").disabled = true;
        }
    }
}

function updateCurrentPassword() {
    const activeEle = document.activeElement;
    let activeEleID = activeEle.id;
    if (activeEle.type == "checkbox") {
        if (currentPassword.includes(activeEleID)) {
            let colorIndex = currentPassword.indexOf(activeEleID);
            currentPassword.splice(colorIndex,1);
        } else {
            currentPassword.push(activeEleID);
        }
    }
}