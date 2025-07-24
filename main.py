import discord
from discord.ext import commands
import re
import os

intents = discord.Intents.default()
intents.message_content = True 

triggers = {
    "fiery fury gate has opened":
    "🔥 Fury Gates is active.",
    "big iceberg has been washed up at the coast north of port hope":
    "❄️ Chakoya Iceberg is active.",
    "wild animals north of the green claw swamp clearly dominate":
    "🐾 Poacher Caves is active and game dominates.",
    "poachers are ravaging the wildlife north of the green claw swamp. but the animals seem to fight back":
    "🔫 Poacher Caves is active and Poachers dominate.",
    "poachers have slaughtered nearly all wild animals north of the green claw swamp. but vengeful spirits show up":
    "👻 Poacher Caves is active and Ghost Wolves dominate.",
    "hive infestation has been sighted south-west of liberty bay":
    "🐝 Hive Outpost is active.",
    "strange sounds echo through trapwood":
    "🌴 Jungle Camp is active.",
    "sandstorm travels through darama, leading to isles full of deadly creatures inside a nightmare. avoid the northernmost coast":
    "🌪 Nightmare Isles is active and its portal is located at Darama's northernmost coast.",
    "sandstorm travels through darama, leading to isles full of deadly creatures inside a nightmare. avoid the river near drefia":
    "🌪 Nightmare Isles is active and its portal is located close to the river near Drefia.",
    "sandstorm travels through darama, leading to isles full of deadly creatures inside a nightmare. avoid the ankrahmun tar pits":
    "🌪 Nightmare Isles is active and its portal is located close to Ankhramun tar pits.",
    "full moon has a strange impact on the island of grimvale":
    "🌕 Grimvale is active.",
    "stampede! the ape god has stirred up tiquanda's elephants again":
    "🐘 Stampede is active.",
    "several banks in major coastal towns are being robbed":
    "🏦 Bank Robbery is active.",
    "nomads travel the eternal sands of ankrahmun's desert":
    "🏜 Nomads is active.",
    "judging by the unnerved mammoths in svargrond":
    "❄️ Thawing is active.",
    "the river in zao steppe runs deep":
    "🐟 River Runs Deep is active.",
    "noodles has taken some royal freedom and left the castle":
    "🍜 Noodles is Gone is active.",
    "oriental ships sighted":
    "🚢 Oriental Trader is active.",
    "queen's own royal trees are being cut down":
    "🌳 Lumberjack is active.",
    "volcano on goroma sends its fiery message into the sky":
    "🌋 Fire from the Earth is active.",
    "hail to the king! it's kingsday in thais":
    "👑 Kingsday is active.",
    "river south of the outlaw camp is flooding":
    "🌊 Down the Drain is active.",
    "witch wyda seems to be bored":
    "🧙‍♀️ Bored is active.",
    "bibby bloodbath and her crew are roaming":
    "⚔️ Warpath is active.",
    "whole nest of spiders needs to be exterminated":
    "🕷 Spider Nest is active.",
    "use devovorga's very essence to enter a boss lair":
    "🐙 Devovorga's Essence is active.",
    "ice bridge now connects svargrond to a frosty island":
    "❄️ Chyllfroest is active.",
    "spirit gate in the daramian mountains":
    "🪦 Spirit Grounds is active at Darama.",
    "spirit gate in the ghostlands":
    "🪦 Spirit Grounds is active at Ghostlands.",
    "spirit gate in vengoth":
    "🪦 Spirit Grounds is active at Vengoth.",
}


def find_response(text: str) -> str | None:
    text = text.lower()
    for phrase, response in triggers.items():
        if phrase in text:
            return response
    return None


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def curry(ctx, *, wiadomosc: str):
    lines = re.split(r'\d{1,2}:\d{2}\s+', wiadomosc)
    lines = [line for line in lines if line.strip() != '']

    odpowiedzi = []
    for line in lines:
        odp = find_response(line)
        if odp:
            odpowiedzi.append(odp)

    if not odpowiedzi:
        await ctx.send("Nie znaleziono żadnych pasujących informacji.")
    else:
        await ctx.send("\n".join(odpowiedzi))

    await ctx.message.delete()


if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    bot.run(TOKEN)
