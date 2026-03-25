let questions = [
    {
        text: "Sinun eteesi tuodaan kaksi ihmistä - toinen on syyllinen, toinen viaton. Heidän kohtalonsa on käsissäsi, mutta Sinulle ei kerrota kumpi on kumpi. Mitä teet?",
        choices: {
            A: "Kuuntelen heidän sanansa ja punnitsen totuuden ennen kuin teen päätöksen.",
            B: "Olen puolueeton - en langeta tuomiota ilman varmaa tietoa."
        },
        correct: "A"
    },
    {
        text: "Kansa on jakautunut kahtia. Toiset vaativat muutosta, toiset haluavat säilyttää vanhan järjestyksen. Jos et tee päätöstä, kaaos uhkaa vallata kaupungin. Mitä teet?",
        choices: {
            A: "Kutsun heidät yhteen ja sovittelen - järjestys on tärkeintä, mutta niin on myös kansan tahto.",
            B: "Jatkan vallitsevan järjestyksen ylläpitämistä - lait on tehty syystä, eikä niitä murreta kevyin perustein."
        },
        correct: "A"
    },
    {
        text: "Nuori sotilas on rikkonut määräyksiä, mutta hänen tekonsa pelasti viattomia. Jos häntä ei rangaista, järjestys heikkenee. Mitä teet?",
        choices: {
            A: "Lain täytyy päteä kaikille - jos annan poikkeuksen, laki menettää merkityksensä.",
            B: "Etsin ratkaisun, joka säilyttää sekä oikeuden että järjestyksen.",
        },
        correct: "B"
    },
    {
        text: "Eteesi tuodaan hallitsija, joka on käyttänyt valtaansa itsekkäästi, mutta ei ole varsinaisesti rikkonut lakeja. Hänen kansansa kärsii hänen valintojensa vuoksi. Mitä teet?",
        choices: {
            A: "Varmistan, että hänen tekonsa tutkitaan tarkasti - jos hän on rikkonut kansaansa vastaan, oikeuden täytyy tapahtua.",
            B: "Laki on laki - jos hän ei ole rikkonut sitä, hänellä on oikeus hallita."
        },
        correct: "A"
    },
    {
        text: "Ihmiset katsovat Sinua ja odottavat oikeutta. He eivät pelkää, vaan uskovat Sinun tuomitsevan oikein. Mitä olet heille?",
        choices: {
            A: "Tasapaino - jokainen teko punnitaan, ja jokainen saa ansionsa mukaan.",
            B: "Laki - maailma pysyy kasassa vain, jos säännöt ovat ehdottomat."
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
    document.getElementById("title").innerText = "THEMIS";
    showQuestion();
}

function showQuestion() {
    if (currentQuestion >= questions.length) {
        document.getElementById("game").classList.add("hidden");
        document.getElementById("endMessage").innerText = "Sinä olet oikeuden ääni.\nPlayer 5, Sinun koodisi on: KRISIS.";
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
        document.getElementById("lives").innerText = "Elämät: " + "🧡".repeat(lives);
        if (lives === 0) {
            document.getElementById("game").classList.add("hidden");
            document.getElementById("endMessage").innerText = "Vaaka on kallistunut väärään suuntaan.\nMutta oikeus antaa uuden mahdollisuuden niille, jotka sitä etsivät.";
            document.getElementById("restartButton").classList.remove("hidden");
            document.getElementById("endScreen").classList.remove("hidden");
            return;
        }
    }
    currentQuestion++;
    showQuestion();
}