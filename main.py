import discord, subprocess, random, json
from pathlib import Path

import ai

with open("config.json") as f:
    config = json.load(f)

i = 0
for item in Path("models").iterdir():
    print(f"⚙️ Building model: '{item}'")
    if item.name.endswith(".ModelFile"):
        i += 1
        subprocess.run(["/usr/local/bin/ollama", "create", item.name.split(".")[0], "-f", "models/" + item.name])

print("------")
print(f"✅ Built {i} ModelFiles")

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name} - [{bot.user.id}]")
    print("------")
    bot_presence = await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=config["activity"]["name"], url=config["activity"]["url"]))

@bot.event
async def on_message(message):
    if message.channel.id in config["ignored_channels"]:
        return
    if message.author == bot.user:
        return
    if bot.user.mentioned_in(message):
        ai_response = ai.get_ai_response(message.content.replace(f"<@{bot.user.id}>", "").strip(), model="grok")
        if message.author.id in config["users_to_be_angry_at"]:
            ai_response = ai_response.upper()
        await message.reply(ai_response)
    elif message.author.id in config["users_to_be_angry_at"] and random.randint(0, 100) <= 100:
        await message.reply(ai.get_ai_response(message.content.replace(f"<@{bot.user.id}>", "").strip(), model="grok_shut_up").upper())
    elif random.randint(0, 100) <= 1:
        if random.randint(0, 100) <= 50:
            await message.reply(random.choice([
                "Haha, true!",
                "Are you being for real right now?",
                "That's a good one!",
                "I can't believe you just said that!",
                "You really think so?",
                "That's a bold statement!",
                "I don't know about that one!",
                "That's a hot take!",
                "Interesting perspective!",
                "I see where you're coming from!",
                "That's a unique way to look at it!",
                "True, true, true!",
            ]))
        if random.randint(0, 100) <= 50:
            await message.reply(ai.get_ai_response(message.content.replace(f"<@{bot.user.id}>", "").strip(), model="grok_short"))

@bot.command(description="Ask Grok a question")
async def ask(ctx, *, question: str):  # Use * to capture all arguments as one string
    await ctx.respond("Thinking...")
    await ctx.respond(ai.get_ai_response(question, model="grok"))

bot.run(open("TOKEN").read().strip())
