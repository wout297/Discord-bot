import discord
from decouple import config
from wit import Wit
import json

answers = {
    "campus_openingsuren_get": "maandag: 08:00–22:00 \ndinsdag: 08:00–22:00 \nwoensdag: 08:00–22:00 \ndonderdag: 08:00–22:00 \nvrijdag: 08:00–22:00 \nzaterdag: 08:00–17:00 \nzondag: Gesloten \n",
    "site_get": "U kunt onze site onder deze url terug vinden: https://www.vives.be/nl/campussen/brugge/brugge-xaverianenstraat",
    "greeting_get": "goeie dag, waarmee zou de DevChat bot u kunnen verder verhelpen?",
    "opleidingen_get": "de opleidingen zijn onder de volgende link terug te vinden: https://www.vives.be/nl/opleidingen?f%5B0%5D=field_targets%3A9",
    "help_get": "ik kan uw vragen over vives beantwoorden, stel u vraag maar gewoon in de chat en ik zal erop antwoorden",
    "meme_get": "ITS A SUPRAAAAAA!!!!!!",
    "facebook_get": "dit is onze facebook: https://www.facebook.com/viveshogeschool",
    "nieuwsbrief_get": "schrijf je hier in voor onze nieuwsbrief: https://www.vives.be/nl/nieuwsbrief-onderzoek?fbclid=IwAR2O1wxtAe_4h5M4Px-DpDO66USw4Vn70a-ZEx1yIixQZL2dcxINSP-rgqY",
    "stuvo_get": "je kan stuvo onder deze link terug vinden: https://www.vives.be/nl/student/stuvo?fbclid=IwAR1USNc5SWTweFVw_VXk4sgbCqtbd8B1Na07fOe-nGhkQ71OgG3MOf4qg-M",
    "toledo_get": "toledo kunt u hier terug vinden: https://www.vives.be/nl/tools/toledo?fbclid=IwAR0hCcJbejg9XlZIwVdXOwUpuIxYTycq-KoIiNyv3f-i1B-2iprK3bMjyAU",
    "infodagen_get": "onze infodagen zijn beschikbaar hier: https://www.vives.be/nl/student/infodagen",
    "geen_engels_get": "Ik versta geen engels, gelieve in het nederlands tegen mij te praten",
    "instagram_get": "U kunt fotos van ons op onze instagram terug vinden: https://www.instagram.com/viveshogeschool/",
    "naam_bot_get": "DevChat",
    "namen_campus_get": "https://www.vives.be/nl#campussen",
    "studiegebieden_get": "https://www.vives.be/nl#studiegebieden",
    "twitter_get": "https://twitter.com/viveshogeschool",
    "youtube_get": "https://www.youtube.com/channel/UCIIHMWaHo3PJbSO1c3-A-Kg",
    "contactgegevens_get": "https://www.vives.be/nl/contact",
    "inschrijving_get": "https://www.vives.be/nl/inschrijven-bij-vives",
    "locatie_get": "De 2 campusen in brugge bevinden zich eenerzijds in de Xaverianenstraat 10, 8200 Brugge. En anderzijds op het address Spoorwegstraat 12, 8200 Brugge"
}


Witclient = Wit(config('WIT'))

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(''):
        stringToSend = ""
        witanswr = None

        try:
            print(Witclient.message(message.content))
            witanswr = json.loads(str(Witclient.message(message.content)).replace("\'", "\""))["intents"][0]["name"]
            print(answers[witanswr])
            await message.channel.send(answers[witanswr])    
        except:
            await message.channel.send("ik versta uw vraag niet goed, maar het antwoord is vast en zeker terug te vinden op onze site onder: https://www.vives.be/nl")
        
        
client.run(config('BotToken'))