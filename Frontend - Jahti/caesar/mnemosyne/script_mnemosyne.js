let questions = [
    {
        text: "Eteesi tuodaan vanha teksti, jonka sanat uhkaavat unohtua ikuisesti. Sen sanat voivat muuttaa historian - mutta sen säilyttäminen voi myös vaarantaa tulevaisuuden. Mitä teet?",
        choices: {
            A: "Säilytän sen - tieto kuuluu niille, jotka sitä etsivät.",
            B: "Annan sen kadota - kaikki tieto ei ole tarkoitettu säilytettäväksi.",
        },
        correct: "A"
    },
    {
        text: "Joku kertoo Sinulle tarinan menneisyydestä. Sinä tiedät, että hän on väärässä - mutta hänen versionsa on ainoa, joka on jäljellä. Mitä teet?",
        choices: {
            A: "Korjaan hänen kertomuksensa - totuus ei ole mielipide, vaan tieto.",
            B: "Annan hänen jatkaa uskomustaan - joskus totuus on merkityksetön."
        },
        correct: "A"
    },
    {
        text: "Sinulta kysytään neuvoa päätökseen, joka voi muuttaa tulevaisuuden kulun. Sinä tiedät, mitä tapahtui aiemmin, ja Sinulla on mahdollisuus vaikuttaa siihen, mitä tulee tapahtumaan. Mitä teet?",
        choices: {
            A: "Jään hiljaiseksi - jokainen valinta on tehtävä ilman historian painoa.",
            B: "Annan menneisyyden puhua - varoitan heitä toistamasta samoja virheitä.",
        },
        correct: "B"
    },
    {
        text: "Edessäsi seisoo henkilö, joka on unohtanut itsensä. Hän ei muista, kuka hän oli, eikä tiedä, mitä on tehnyt. Sinä tiedät hänen menneisyytensä. Mitä teet?",
        choices: {
            A: "Pidän tiedon itselläni - ehkä unohtaminen on joskus armoa.",
            B: "Kerron hänelle totuuden - jokaisella on oikeus tietää, kuka on ollut.",
        },
        correct: "B"
    },
    {
        text: "Ihmiset katsovat Sinua ja odottavat vastauksia menneisyydestä. Oletko heille muistutus vai varoitus?",
        choices: {
            A: "Muistutus - mennyt ei ole unohtunut, vaan elää meissä kaikissa.",
            B: "Varoitus - historian muistaa vain se, joka uskaltaa katsoa taakseen."
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
    document.getElementById("title").innerText = "MNEMOSYNE";
    showQuestion();
}

function showQuestion() {
    if (currentQuestion >= questions.length) {
        document.getElementById("game").classList.add("hidden");
        document.getElementById("endMessage").innerText = "Sinä olet muistin vartija.\nPlayer 3, Sinun koodisi on: LETHÊ.";
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
        document.getElementById("lives").innerText = "Elämät: " + "💛".repeat(lives);
        if (lives === 0) {
            document.getElementById("game").classList.add("hidden");
            document.getElementById("endMessage").innerText = "Muisti on hauras, mutta se ei katoa.\nJos etsit totuutta, sinun on katsottava menneisyyteen uudelleen.";
            document.getElementById("restartButton").classList.remove("hidden");
            document.getElementById("endScreen").classList.remove("hidden");
            return;
        }
    }
    currentQuestion++;
    showQuestion();
}