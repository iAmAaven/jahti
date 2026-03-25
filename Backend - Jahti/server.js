require('dotenv').config();
const express = require('express');
const admin = require('firebase-admin');
const cors = require('cors');

const app = express();
app.use(express.json());
app.use(cors());

admin.initializeApp({
    credential: admin.credential.cert({
        projectId: process.env.FIREBASE_PROJECT_ID,
        private_key: process.env.FIREBASE_PRIVATE_KEY.replace(/\\n/g, '\n'),
        client_email: process.env.FIREBASE_CLIENT_EMAIL
    })
});
const db = admin.firestore();

app.get('/redeem', async (req, res) => {
    try {
        const player = req.query.player;
        if (!player) return res.status(400).json({ error: "Pelaajan nimi puuttuu." });

        const docRef = db.collection('lipukkeet').doc(player);
        const docSnap = await docRef.get();

        if (!docSnap.exists) {
            return res.status(404).json({ error: `Pelaajaa ${player} ei löydy.` });
        }

        res.json({ player, redeemed: docSnap.data().redeemed });
    } catch (error) {
        console.error("Virhe tarkistaessa lipuketta:", error);
        res.status(500).json({ error: "Palvelinvirhe." });
    }
});

app.post('/redeem', async (req, res) => {
    try {
        const player = req.body.player;
        if (!player) return res.status(400).json({ error: "Pelaajan nimi puuttuu." });

        const docRef = db.collection('lipukkeet').doc(player);
        const docSnap = await docRef.get();

        if (!docSnap.exists) {
            return res.status(404).json({ error: `Pelaajaa ${player} ei löydy.` });
        }

        if (docSnap.data().redeemed) {
            return res.status(400).json({ error: `Lipuke on jo lunastettu pelaajalle ${player}.` });
        }

        await docRef.update({ redeemed: true });
        res.json({ success: true, message: `Lipuke lunastettu pelaajalle ${player}!` });
    } catch (error) {
        console.error("Virhe lunastaessa lipuketta:", error);
        res.status(500).json({ error: "Palvelinvirhe." });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Palvelin käynnissä portissa ${PORT}`));
