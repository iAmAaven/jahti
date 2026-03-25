let questions = [
    {
        text: "Valo leikkaa yön halki. Se kutsuu Sinua. Mitä teet?",
        choices: {
            A: "Käännyn pois - valo tulee ja menee, mutta pimeys pysyy.",
            B: "Astun valoon - vaikka se katoaa, voin katsoa, mitä se halusi näyttää."
        },
        correct: "A"
    },
    {
        text: "Kuljet varjoissa, kun joku kutsuu nimeäsi. Ääni ei ole rukoileva, vaan vaativa. Se käskee Sinua paljastamaan itsesi. Mitä teet?",
        choices: {
            A: "Jään piiloon - ne, jotka kutsuvat nimeäni ilman pelkoa, eivät ansaitse vastauksia.",
            B: "Näyttäydyn hetkeksi - mutta en puhu, enkä jää odottamaan."
        },
        correct: "A"
    },
    {
        text: "Kuolevainen kulkee unohduksen rajalla. Hän on unohtamassa, kuka on, ja pian häntä ei ole enää. Sinulla on voima palauttaa hänen muistonsa - mutta pitäisikö Sinun?",
        choices: {
            A: "Annan hänen muistaa - unohdus ei ole vapautus, vaan häviö.",
            B: "Jätän hänet - muistot ovat kuin varjot, ne ilmestyvät ja katoavat omalla ajallaan."
        },
        correct: "B"
    },
    {
        text: "Kuolevainen yrittää vangita pimeyden, kesyttää sen ja kääntää sen omaan tarkoitukseensa. Sinä tunnet hänen suunnitelmansa ja tiedät, että se ei voi onnistua. Mitä teet?",
        choices: {
            A: "Annat hänen yrittää - pimeys nielee kyllä ne, jotka eivät sitä ymmärrä.",
            B: "Estän häntä - varjojen voima ei kuulu kuolevaisille."
        },
        correct: "A"
    },
    {
        text: "Ihmiset katsovat tähtitaivasta ja kuiskaavat nimeäsi. Oletko heille pelko vai lohtu?",
        choices: {
            A: "Lohtu - yön pimeys antaa tilan levätä ja unelmoida.",
            B: "En välitä. He voivat nähdä minut miten haluavat - minä olen, mitä olen."
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
    document.getElementById("title").innerText = "NYX";
    showQuestion();
}

function showQuestion() {
    if (currentQuestion >= questions.length) {
        document.getElementById("game").classList.add("hidden");
        document.getElementById("endMessage").innerText = "Sinä olet todellinen yön voima.\nPlayer 4, Sinun koodisi on: VARJO.";
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
        document.getElementById("lives").innerText = "Elämät: " + "💚".repeat(lives);
        if (lives === 0) {
            document.getElementById("game").classList.add("hidden");
            document.getElementById("endMessage").innerText = "Varjot ovat nielaisseet Sinut.\nMutta yö ei ole armoton - se antaa mahdollisuuden niille, jotka uskaltavat etsiä totuutta uudelleen.";
            document.getElementById("restartButton").classList.remove("hidden");
            document.getElementById("endScreen").classList.remove("hidden");
            return;
        }
    }
    currentQuestion++;
    showQuestion();
}