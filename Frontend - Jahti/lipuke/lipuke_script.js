const apiUrl = "https://lipuke-backend.onrender.com/redeem";
const playerID = document.getElementById('playerID').value;

async function checkRedemptionStatus() {
    try {
        const response = await fetch(`${apiUrl}?player=${playerID}`);
        const data = await response.json();
        document.getElementById("redeemButton").disabled = false;

        if (data.redeemed) {
            document.getElementById("status").innerText = "LUNASTETTU!";
            document.getElementById("redeemButton").disabled = true;
        } else {
            document.getElementById("status").innerText = "";
            document.getElementById("redeemButton").disabled = false;
        }
    } catch (error) {
        document.getElementById("status").innerText = "Virhe haettaessa tietoja.";
    }
}

async function redeem() {
    try {
        const response = await fetch(apiUrl, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ player: playerID })
        });

        const data = await response.json();
        
        if (data.success) {
            document.getElementById("status").innerText = "LUNASTETTU!";
            document.getElementById("redeemButton").disabled = true;
        } else {
            alert("Virhe lunastuksessa!");
        }
    } catch (error) {
        alert("Verkkovirhe. Yritä uudelleen.");
    }
}

async function loadKiitosText() {
    try {
        const response = await fetch('kiitos.txt');
        const text = await response.text();
        document.querySelector('.kiitos').innerHTML = text.replace(/\n/g, '<br>');
    } catch (error) {
        console.error('Error loading text:', error);
    }
}

async function loadJuomakorttiText() {
    try {
        const response = await fetch('juomakortti.txt');
        const text = await response.text();
        document.getElementById('juomakorttiText').innerHTML = text.replace(/\n/g, '<br>');
    } catch (error) {
        console.error('Error loading juomakortti text:', error);
    }
}

function flipCard() {
    document.querySelector('.card-inner').classList.toggle('flipped');
}

checkRedemptionStatus();
loadKiitosText();
loadJuomakorttiText();