let questions = [
    {
        text: "Edessäsi on sielu, joka on tullut tiensä päähän. Hän ei tahdo lähteä. Hän anelee vielä yhtä päivää, yhtä hetkeä. Mitä teet?",
        choices: {
            A: "Kuuntelen hänen anomuksensa. Jos hänen aikansa ei ole vielä tullut, miksi kiirehtiä?",
            B: "Otan hänet mukaani - kuolema ei odota, eikä se neuvottele."
        },
        correct: "B"
    },
    {
        text: "Kuljet pimeyden halki, kun huomaat erään sielun harhailevan välitilassa. Hän ei kuulu elävien maailmaan, mutta ei ole myöskään siirtynyt eteenpäin. Hän on kadoksissa. Mitä teet?",
        choices: {
            A: "Ohjaan hänet eteenpäin - hänen paikkansa ei ole täällä.",
            B: "Jätän hänet. En ole hänen tuomarinsa, enkä hänen pelastajansa."
        },
        correct: "B"
    },
    {
        text: "Ihminen yrittää pidentää elämäänsä. Hän rakentaa itselleen keinotekoisen elämän, pidentää päiviään tavalla, jota luonnonlait eivät tue. Sinä näet hänet. Mitä teet?",
        choices: {
            A: "Annat hänen jatkaa - kuolema tulee lopulta jokaiselle, tavalla tai toisella.",
            B: "Päätät hänen aikansa nyt - kukaan ei voi paeta loputonta unta."
        },
        correct: "A"
    },
    {
        text: "Sielujen virta kulkee luoksesi. Yksi heistä ei tahdo astua rajan yli. Hän sanoo, että hänen työnsä ei ole valmis. Mitä sanot hänelle?",
        choices: {
            A: "Sinä päätät - mutta jokainen viivytys vääristää tasapainoa.",
            B: "Sinun kohtalosi on jo kirjoitettu. Kävele eteenpäin."
        },
        correct: "B"
    },
    {
        text: "Kuolevaiset kuiskaavat nimeäsi yön pimeydessä. He pelkäävät Sinua, mutta rukoilevat armoasi. Mitä olet heille?",
        choices: {
            A: "Armo - jokainen ansaitsee lempeän lopun.",
            B: "Väistämätön - en ole hyvä enkä paha, olen vain se, mikä on."
        },
        correct: "B"
    }
];


let currentQuestion = 0;
let lives = 2;

function startGame() {
    document.getElementById("intro").classList.add("hidden");
    document.getElementById("startButton").classList.add("hidden");
    document.getElementById("game").classList.remove("hidden");
    document.getElementById("title").innerText = "THANATOS";
    showQuestion();
}

function showQuestion() {
    if (currentQuestion >= questions.length) {
        document.getElementById("game").classList.add("hidden");
        document.getElementById("endMessage").innerText = "Sinä olet kuoleman käsi.\nPlayer 1, Sinun koodisi on: MEMENTO.";
        document.getElementById("endScreen").classList.remove("hidden");
        return;
    }

    let q = questions[currentQuestion];
    document.getElementById("question").innerText = q.text;
    document.getElementById("optionA").innerText = q.choices.A;
    document.getElementById("optionB").innerText = q.choices.B;
}

function answer(choice) {
    if (choice !== questions[currentQuestion].correct) {
        lives--;
        document.getElementById("lives").innerText = "Elämät: " + "💜".repeat(lives);
        if (lives === 0) {
            document.getElementById("game").classList.add("hidden");
            document.getElementById("endMessage").innerText = "Sinun aikasi ei ollut vielä.\nKuolema odottaa aina - mutta tänään se ei vienyt Sinua.";

            document.getElementById("restartButton").classList.remove("hidden");
            document.getElementById("endScreen").classList.remove("hidden");
            return;
        }
    }
    currentQuestion++;
    showQuestion();
}