let progress = 0;

function revealText(id) {
    if(document.getElementById(id).style.display != "block") {
        console.log("Revealed " + id);
        progress++;
        if(progress == 3) {
            document.getElementById("totuus").innerHTML = "TOTUUS LÖYTYI PIMEYDESTÄ";
            document.getElementById("progress").innerHTML = "61.49354127477476, 28.429187040678492";
            document.getElementsByClassName("hidden-area")[0].style.display = "none";
            document.getElementById("part1").style.display = "none";
            document.getElementById("part2").style.display = "none";
            document.getElementById("part3").style.display = "none";
        } else {
            document.getElementById("progress").innerHTML = "LÖYDETTY: " + progress + "/3";
            document.getElementById(id).style.display = "block";
        }
    }
}

function getRandomPosition() {
    return Math.random() * 80 + "%";
}

function createButton(textId) {
    let button = document.createElement("button");
    button.className = "hidden-button";
    button.style.top = getRandomPosition();
    button.style.left = getRandomPosition();
    button.onclick = function() { revealText(textId); };
    button.innerHTML = " ";
    document.getElementById("hiddenArea").appendChild(button);
}

createButton("part1");
createButton("part2");
createButton("part3");