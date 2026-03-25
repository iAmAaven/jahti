import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Role and emoji
ROLE_ID = 0  # TODO: Replace with desired Discord role ID
EMOJI = "✅"

# Ohjauskanavan ID (send_dm_komennot)
# Control channel is used behind the scenes by the Game Master
CONTROL_CHANNEL_ID = 0  # TODO: Replace with desired Discord control channel ID
# Kuiske channel is the destination where the bot sends messages
KUISKE_CHANNEL_ID = 0  # TODO: Replace with desired Discord kuiske channel ID

# Store message ID for reactions
reaction_message_id = None

RULES_CHANNEL = "https://discord.com/channels/<SERVER_ID>/<RULES_CHANNEL_ID>"  # TODO: Replace with real IDs

# Public-safe configuration
GAME_MASTER_ID = 0  # TODO: Replace with Game Master Discord user ID (you)
PLAYER_2_ID = 0  # TODO: Replace with Player 2 Discord user ID
PLAYER_3_ID = 0  # TODO: Replace with Player 3 Discord user ID
PLAYER_4_ID = 0  # TODO: Replace with Player 4 Discord user ID
PLAYER_5_ID = 0  # TODO: Replace with Player 5 Discord user ID
PLAYER_6_ID = 0  # TODO: Replace with Player 6 Discord user ID

# Syncing slash commands
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
        print(f"{bot.user} has connected!")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

@bot.event
async def on_message(message):
    global reaction_message_id

    if message.author == bot.user:
        return

    # DM-VIESTIEN LUKEMINEN JA VASTAUS
    if isinstance(message.channel, discord.DMChannel):
        await handle_dm_message(message)
        return  # Jos viesti oli DM, ei jatketa

    # BOT-CONTROL KANAVAN KUUNTELU (SEND_DM_KOMENNOT)
    if message.channel.id == CONTROL_CHANNEL_ID:
        if message.content.startswith("send_dm_"):
            await process_dm_command(message)
        elif message.content == "kutsu":
            kuiske_channel = bot.get_channel(KUISKE_CHANNEL_ID)
            await send_file_contents(kuiske_channel, "kutsu.txt")
            await kuiske_channel.send(file=discord.File("symbols/kuiske.jpg"))
            await kuiske_channel.send(f"Säännöt: {RULES_CHANNEL}")
        elif message.content == "kaiku":
            kuiske_channel = bot.get_channel(KUISKE_CHANNEL_ID)
            await send_file_contents(kuiske_channel, "kaiku.txt")

        return

    # KANAVAVIESTIT (KUTSU, SÄÄNNÖT, COUNTDOWN)
    if message.content == "kutsu":
        await send_file_contents(message.channel, "kutsu.txt")
        await message.channel.send(file=discord.File("symbols/kuiske.jpg"))
        await message.channel.send(f"Säännöt: {RULES_CHANNEL}")
    elif message.content == "saannot":
        await send_file_contents(message.channel, "pelin-saannot.txt")
        await message.channel.send("**Aloittaaksesi yksityisviestiketjun JAHTIMESTARIN kanssa, paina JAHTIMESTARIN profiilia ja kirjoita viesti tekstikenttään.**")
    elif message.content == "countdown":
        await send_file_contents(message.channel, "countdown.txt")

    await bot.process_commands(message)

# FUNKTIO: Lähetä yksityisviesti pelaajalle
async def process_dm_command(message):
    # Käsittelee ohjauskanavassa lähetetyt 'send_dm_USER Viesti' -komennot.
    try:
        parts = message.content.split(" ", 2)  # Jakaa viestin: ['send_dm_USER', 'Viesti']
        if len(parts) < 3:
            await message.channel.send(":WARNING:Komento virheellinen! Käytä muotoa: `send_dm_USER Viesti tähän`")
            return

        command, user_id, dm_message = parts

        try:
            user_id = int(user_id)
        except ValueError:
            await message.channel.send(f"Invalid User ID: {user_id}. It must be a number.")
            return

        # Fetch user from ID
        user = await bot.fetch_user(user_id)

        if not user:
            await message.channel.send(f"User with ID **{user_id}** not found.")
            return

        # Send DM
        await user.send(dm_message)
        await message.channel.send(f"✅ Message sent to **{user.name}** (ID: {user_id}).")

    except Exception as e:
        print(f"Virhe DM-viestissä: {e}")
        await message.channel.send("Viestin lähettäminen epäonnistui.")

# FUNKTIO: Käsittele DM-viestit
async def handle_dm_message(message):
    # Käsittelee DM-viestit ja vastaa niihin.
    author_id = message.author.id
    msg_lower = message.content.lower()


    # DM-VASTAUKSET KÄYTTÄJÄN MUKAAN
    if author_id == GAME_MASTER_ID:
        print("\033[91mGAME_MASTER SAID:", msg_lower, "\033[0m")
        if msg_lower == "game_master":
            await message.channel.send("Sinä olet Game Master.")
            return






    elif author_id == PLAYER_2_ID:
        print("\033[95mPLAYER_2 SAID:", msg_lower, "\033[0m")
        if msg_lower == "player2":
            await message.channel.send("Sinä olet Player 2.")
            return
        elif msg_lower == "caesar":
            print("\033[92m", message.author ,"GOT THE 1st PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send(":jigsaw: Caesar -7 aohuhavz")
            return
        elif msg_lower == "thanatos":
            print("\033[92m", message.author ,"GOT THE 2nd PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send(":jigsaw: [Tervetuloa jumalien keskuuteen, Player 2](<https://jahti.onrender.com/caesar/thanatos/index.html>)")
            return
        elif msg_lower == "memento":
            print("\033[92m", message.author ,"GOT THE 3rd PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 1**"
            "\n> _Minut voi peittää, mutta en ole maa."
            "\n> Minut voi kadottaa, mutta en ole esine."
            "\n> Minut voi kuulla, mutta en koskaan puhu."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "kaiku":
            print("\033[92m", message.author ,"GOT THE 4th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 2**"
            "\n> _Minut voi avata, mutta en ole laatikko."
            "\n> Minusta voi kulkea läpi, mutta en ole ovi."
            "\n> Minä yhdistän kaksi maailmaa, mutta en ole silta."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "ikkuna":
            print("\033[92m", message.author ,"GOT THE 5th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 3**"
            "\n> _Minulla ei ole alkua, mutta minua on aina ollut."
            "\n> Minä voin rientää, mutta en voi kävellä."
            "\n> Minä voin kulua, mutta en koskaan mene huonoksi."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "aika":
            print("\033[92m", message.author ,"GOT THE 6th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send("‎")
            await message.channel.send(":jigsaw: 12.619085087982144, [...](<https://jahti.onrender.com/caesar/thanatos/thanatosloc.html>)")
            return
        elif msg_lower == "butterball" or msg_lower == "butter ball" or msg_lower == "krishna's butter ball" or msg_lower == "krishna's butterball" or msg_lower == "krishna":
            print("\033[92m", message.author ,"GOT THE LAST PUZZLE CORRECT!!!!!!", "\033[0m")
            file_path = "symbols/symbol1.jpg"
            try:
                await message.channel.send(":white_check_mark:")
                await message.channel.send("**Player 2**. Löydät itsesi muutaman metrin päästä Portista, mutta Sen edessä on siirtolohkare, joka peittää Polkusi.\nKivi on pakko kiertää, mutta et näe minkäänlaista reittiä sen ohi.\nKiveen on kaiverrettu teksti ja outo symboli:")
                await message.channel.send("_OLEN PIILOSSA. LÖYDÄ MINUT, JA OTA MUKAASI._", file=discord.File(file_path))
            except FileNotFoundError:
                await message.channel.send("Järjestelmässäni havaittiin virhe. Ole hyvä, ja ilmoita asiasta JAHDIN järjestäjälle.")
            return






    elif author_id == PLAYER_3_ID:
        print("\033[91mPLAYER_3 SAID:", msg_lower, "\033[0m")
        if msg_lower == "player3":
            await message.channel.send("Sinä olet Player 3.")
            return
        elif msg_lower == "caesar":
            print("\033[92m", message.author ,"GOT THE 1st PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send(":jigsaw: Caesar -7 hylz")
            return
        elif msg_lower == "ares":
            print("\033[92m", message.author ,"GOT THE 2nd PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send(":jigsaw: [Tervetuloa jumalien keskuuteen, Player 3](<https://jahti.onrender.com/caesar/ares/index.html>)")
            return
        elif msg_lower == "khaos":
            print("\033[92m", message.author ,"GOT THE 3rd PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 1**"
            "\n> _Minut voi peittää, mutta en ole maa."
            "\n> Minut voi kadottaa, mutta en ole esine."
            "\n> Minut voi kuulla, mutta en koskaan puhu."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "kaiku":
            print("\033[92m", message.author ,"GOT THE 4th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 2**"
            "\n> _Minut voi avata, mutta en ole laatikko."
            "\n> Minusta voi kulkea läpi, mutta en ole ovi."
            "\n> Minä yhdistän kaksi maailmaa, mutta en ole silta."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "ikkuna":
            print("\033[92m", message.author ,"GOT THE 5th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 3**"
            "\n> _Minulla ei ole alkua, mutta minua on aina ollut."
            "\n> Minä voin rientää, mutta en voi kävellä."
            "\n> Minä voin kulua, mutta en koskaan mene huonoksi."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "aika":
            print("\033[92m", message.author ,"GOT THE 6th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send("‎")
            await message.channel.send(":jigsaw: 52.36098198721238, [...](<https://jahti.onrender.com/caesar/ares/aresloc.html>)")
            return
        elif msg_lower == "big rock":
            print("\033[92m", message.author ,"GOT THE LAST PUZZLE CORRECT!!!!!!", "\033[0m")
            file_path = "symbols/symbol2.jpg"
            try:
                await message.channel.send(":white_check_mark:")
                await message.channel.send("**Player 3**. Löydät itsesi muutaman metrin päästä Portista, mutta Sen edessä on siirtolohkare, joka peittää Polkusi.\nKivi on pakko kiertää, mutta et näe minkäänlaista reittiä sen ohi.\nKiveen on kaiverrettu teksti ja outo symboli:")
                await message.channel.send("_OLEN PIILOSSA. LÖYDÄ MINUT, JA OTA MUKAASI._", file=discord.File(file_path))
            except FileNotFoundError:
                await message.channel.send("Järjestelmässäni havaittiin virhe. Ole hyvä, ja ilmoita asiasta JAHDIN järjestäjälle.")
            return





    elif author_id == PLAYER_4_ID:
        print("\033[94mPLAYER_4 SAID:", msg_lower, "\033[0m")
        if msg_lower == "player4":
            await message.channel.send("Sinä olet Player 4.")
            return
        elif msg_lower == "caesar":
            print("\033[92m", message.author ,"GOT THE 1st PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send(":jigsaw: Caesar -7 tultvzful")
            return
        elif msg_lower == "mnemosyne":
            print("\033[92m", message.author ,"GOT THE 2nd PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send(":jigsaw: [Tervetuloa jumalien keskuuteen, Player 4](<https://jahti.onrender.com/caesar/mnemosyne/index.html>)")
            return
        elif msg_lower == "lethê":
            print("\033[92m", message.author ,"GOT THE 3rd PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 1**"
            "\n> _Minut voi peittää, mutta en ole maa."
            "\n> Minut voi kadottaa, mutta en ole esine."
            "\n> Minut voi kuulla, mutta en koskaan puhu."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "kaiku":
            print("\033[92m", message.author ,"GOT THE 4th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 2**"
            "\n> _Minut voi avata, mutta en ole laatikko."
            "\n> Minusta voi kulkea läpi, mutta en ole ovi."
            "\n> Minä yhdistän kaksi maailmaa, mutta en ole silta."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "ikkuna":
            print("\033[92m", message.author ,"GOT THE 5th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 3**"
            "\n> _Minulla ei ole alkua, mutta minua on aina ollut."
            "\n> Minä voin rientää, mutta en voi kävellä."
            "\n> Minä voin kulua, mutta en koskaan mene huonoksi."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "aika":
            print("\033[92m", message.author ,"GOT THE 6th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send("‎")
            await message.channel.send(":jigsaw: 41.95806750837248, [...](<https://jahti.onrender.com/caesar/mnemosyne/mnemosyneloc.html>)")
            return
        elif msg_lower == "plymouth rock" or msg_lower == "plymouth":
            print("\033[92m", message.author ,"GOT THE LAST PUZZLE CORRECT!!!!!!", "\033[0m")
            file_path = "symbols/symbol3.jpg"
            try:
                await message.channel.send(":white_check_mark:")
                await message.channel.send("**Player 4**. Löydät itsesi muutaman metrin päästä Portista, mutta Sen edessä on siirtolohkare, joka peittää Polkusi.\nKivi on pakko kiertää, mutta et näe minkäänlaista reittiä sen ohi.\nKiveen on kaiverrettu teksti ja outo symboli:")
                await message.channel.send("_OLEN PIILOSSA. LÖYDÄ MINUT, JA OTA MUKAASI._", file=discord.File(file_path))
            except FileNotFoundError:
                await message.channel.send("Järjestelmässäni havaittiin virhe. Ole hyvä, ja ilmoita asiasta JAHDIN järjestäjälle.")
            return






    elif author_id == PLAYER_5_ID:
        print("\033[96mPLAYER_5 SAID:", msg_lower, "\033[0m")
        if msg_lower == "player5":
            await message.channel.send("Sinä olet Player 5.")
            return
        elif msg_lower == "caesar":
            print("\033[92m", message.author ,"GOT THE 1st PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send(":jigsaw: Caesar -7 ufe")
            return
        elif msg_lower == "nyx":
            print("\033[92m", message.author ,"GOT THE 2nd PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send(":jigsaw: [Tervetuloa jumalien keskuuteen, Player 5](<https://jahti.onrender.com/caesar/nyx/index.html>)")
            return
        elif msg_lower == "varjo":
            print("\033[92m", message.author ,"GOT THE 3rd PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 1**"
            "\n> _Minut voi peittää, mutta en ole maa."
            "\n> Minut voi kadottaa, mutta en ole esine."
            "\n> Minut voi kuulla, mutta en koskaan puhu."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "kaiku":
            print("\033[92m", message.author ,"GOT THE 4th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 2**"
            "\n> _Minut voi avata, mutta en ole laatikko."
            "\n> Minusta voi kulkea läpi, mutta en ole ovi."
            "\n> Minä yhdistän kaksi maailmaa, mutta en ole silta."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "ikkuna":
            print("\033[92m", message.author ,"GOT THE 5th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 3**"
            "\n> _Minulla ei ole alkua, mutta minua on aina ollut."
            "\n> Minä voin rientää, mutta en voi kävellä."
            "\n> Minä voin kulua, mutta en koskaan mene huonoksi."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "aika":
            print("\033[92m", message.author ,"GOT THE 6th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send("‎")
            await message.channel.send(":jigsaw: 61.49354127477476, [...](<https://jahti.onrender.com/caesar/nyx/nyxloc.html>)")
            return
        elif msg_lower == "kummakivi":
            print("\033[92m", message.author ,"GOT THE LAST PUZZLE CORRECT!!!!!!", "\033[0m")
            file_path = "symbols/symbol5.jpg"
            try:
                await message.channel.send(":white_check_mark:")
                await message.channel.send("**Player 5**. Löydät itsesi muutaman metrin päästä Portista, mutta Sen edessä on siirtolohkare, joka peittää Polkusi.\nKivi on pakko kiertää, mutta et näe minkäänlaista reittiä sen ohi.\nKiveen on kaiverrettu teksti ja outo symboli:")
                await message.channel.send("_OLEN PIILOSSA. LÖYDÄ MINUT, JA OTA MUKAASI._", file=discord.File(file_path))
            except FileNotFoundError:
                await message.channel.send("Järjestelmässäni havaittiin virhe. Ole hyvä, ja ilmoita asiasta JAHDIN järjestäjälle.")
            return






    elif author_id == PLAYER_6_ID:
        print("\033[93mPLAYER_6 SAID:", msg_lower, "\033[0m")
        if msg_lower == "player6":
            await message.channel.send("Sinä olet Player 6.")
            return
        elif msg_lower == "caesar":
            print("\033[92m", message.author ,"GOT THE 1st PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send(":jigsaw: Caesar -7 aoltpz")
            return
        elif msg_lower == "themis":
            print("\033[92m", message.author ,"GOT THE 2nd PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send(":jigsaw: [Tervetuloa jumalien keskuuteen, Player 6](<https://jahti.onrender.com/caesar/themis/index.html>)")
            return
        elif msg_lower == "krisis":
            print("\033[92m", message.author ,"GOT THE 3rd PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 1**"
            "\n> _Minut voi peittää, mutta en ole maa."
            "\n> Minut voi kadottaa, mutta en ole esine."
            "\n> Minut voi kuulla, mutta en koskaan puhu."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "kaiku":
            print("\033[92m", message.author ,"GOT THE 4th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 2**"
            "\n> _Minut voi avata, mutta en ole laatikko."
            "\n> Minusta voi kulkea läpi, mutta en ole ovi."
            "\n> Minä yhdistän kaksi maailmaa, mutta en ole silta."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "ikkuna":
            print("\033[92m", message.author ,"GOT THE 5th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("‎")
            await message.channel.send(":scroll: **ARVOITUS nro. 3**"
            "\n> _Minulla ei ole alkua, mutta minua on aina ollut."
            "\n> Minä voin rientää, mutta en voi kävellä."
            "\n> Minä voin kulua, mutta en koskaan mene huonoksi."
            "\n> Mikä minä olen?_")
            return
        elif msg_lower == "aika":
            print("\033[92m", message.author ,"GOT THE 6th PUZZLE CORRECT!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            await message.channel.send("**Hyvää työtä, Valittu. Olet askeleen lähempänä Porttia.**")
            await message.channel.send("‎")
            await message.channel.send(":jigsaw: 50.0500008639507, [...](<https://jahti.onrender.com/caesar/themis/themisloc.html>)")
            return
        elif msg_lower == "logan rock" or msg_lower == "logan" or msg_lower == "loganrock":
            print("\033[92m", message.author ,"GOT THE LAST PUZZLE CORRECT!!!!!!", "\033[0m")
            await message.channel.send(":white_check_mark:")
            file_path = "symbols/symbol4.jpg"
            try:
                await message.channel.send("**Player 6**. Löydät itsesi muutaman metrin päästä Portista, mutta Sen edessä on siirtolohkare, joka peittää Polkusi.\nKivi on pakko kiertää, mutta et näe minkäänlaista reittiä sen ohi.\nKiveen on kaiverrettu teksti ja outo symboli:")
                await message.channel.send("_OLEN PIILOSSA. LÖYDÄ MINUT, JA OTA MUKAASI._", file=discord.File(file_path))
            except FileNotFoundError:
                await message.channel.send("Järjestelmässäni havaittiin virhe. Ole hyvä, ja ilmoita asiasta JAHDIN järjestäjälle.")
            return


    
    # Yleinen vastaus, jos DM ei täsmää mihinkään
    if msg_lower == "kuiske.exe" or msg_lower == "kuiske":
        await message.channel.send("KUISKE.exeen ei saatu yhteyttä...")
    elif msg_lower == "jahtimestari":
        await message.channel.send("Hei, se olen minä! :sunglasses:")
    else:
        with open("wrong_dm.txt", "r", encoding="utf-8") as file:
            contents = file.read()
            await message.channel.send(contents)



# FUNKTIO: Lähetä tiedoston sisältö
async def send_file_contents(channel, filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
            await channel.send(contents)
    except FileNotFoundError:
        await channel.send(f"En löytänyt tiedostoa: {filename}!")
    except Exception as e:
        await channel.send(f"Virhe: {e}")



BOT_TOKEN = "<DISCORD_BOT_TOKEN>"
if BOT_TOKEN == "<DISCORD_BOT_TOKEN>":
    raise RuntimeError("Set BOT_TOKEN in jahtimestari.py before running")

bot.run(BOT_TOKEN)
