let questions = [
    {
        text: "Edessäsi on heikko ja haavoittunut sotilas. Hän on vihollisesi, mutta aseeton. Hän pyytää armoa. Mitä teet?",
        choices: {
            A: "Lopetan hänet - sodassa ei ole sääntöjä.",
            B: "Käännyn pois - heikot eivät ansaitse kuolemaa.",
        },
        correct: "A"
    },
    {
        text: "Kaupunki seisoo edessäsi. Sen muurit ovat vahvat, sen kansa puolustuskyvytön. Sinulla on valta valita: säästätkö vai tuhoatko?",
        choices: {
            A: "Jätän kaupungin koskemattomaksi - voitto on jo minun.",
            B: "Poltan sen maahan - jotta he muistaisivat pelätä minua."
        },
        correct: "B"
    },
    {
        text: "Liittolaisesi epäilee Sinua. Hän sanoo, että ilman häntä et olisi saavuttanut valtaasi. Hän saattaa olla oikeassa. Mitä teet?",
        choices: {
            A: "Hyväksyn hänen sanansa - mutta muistutan häntä siitä, kuka todella hallitsee.",
            B: "Poistan hänet - vain vahvimmat ansaitsevat paikkansa rinnallani."
        },
        correct: "B"
    },
    {
        text: "Sota on loppumassa. Voit vetäytyä voittajana tai jatkaa taistelua kunnes kukaan ei ole jäljellä. Mitä valitset?",
        choices: {
            A: "Lopetan sodan - en tarvitse turhaa verenvuodatusta.",
            B: "Jatkan, kunnes viimeinenkin vihollinen on tuhottu."
        },
        correct: "B"
    },
    {
        text: "Ihmiset kuiskaavat nimeäsi pimeydessä. He eivät rukoile - he pelkäävät. Mitä olet heille?",
        choices: {
            A: "Pelko itse - minun varjoni alla he polvistuvat.",
            B: "Johtaja - sota tarvitsee mestarinsa.",
        },
        correct: "A"
    }
];



let currentQuestion = 0;
let lives = 2;

function startGame() {
    document.getElementById("intro").classList.add("hidden");
    document.getElementById("startButton").classList.add("hidden");
    document.getElementById("game").classList.remove("hidden");
    document.getElementById("title").innerText = "ARES";
    showQuestion();
}

function showQuestion() {
    if (currentQuestion >= questions.length) {
        document.getElementById("game").classList.add("hidden");
        document.getElementById("endMessage").innerText = "Sinä olet sodan herra.\nPlayer 2, Sinun koodisi on: KHAOS.";
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
        document.getElementById("lives").innerText = "Elämät: " + "❤️".repeat(lives);
        if (lives === 0) {
            document.getElementById("game").classList.add("hidden");
            document.getElementById("endMessage").innerText = "Sinä kaaduit - mutta sota ei lopu koskaan.\nVeri on valuvaa, mutta taistelu jatkuu aina.";
            document.getElementById("restartButton").classList.remove("hidden");
            document.getElementById("endScreen").classList.remove("hidden");
            return;
        }
    }
    currentQuestion++;
    showQuestion();
}