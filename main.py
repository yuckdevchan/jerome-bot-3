import discord, subprocess, random
from pathlib import Path

from config import config
import ai

models = ai.build_model_files()

bot = discord.Bot()

letter_emojis = {"A": "🇦", "B": "🇧", "C": "🇨", "D": "🇩", "E": "🇪", "F": "🇫", "G": "🇬", "H": "🇭", "I": "🇮", "J": "🇯",}

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name} - [{bot.user.id}]")
    print("------")
    bot_presence = await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=config["activity"]["name"], url=config["activity"]["url"]))

async def react(message, angry=False):
    try:
        if angry:
            await message.add_reaction(random.choice([
                "😡", "😠", "🤬", "😤", "😾", "👿", "💢"
            ]))
        else:
            if random.randint(0, 100) <= 20:
                for letter in config["simple_bot_name"]:
                    await message.add_reaction(letter_emojis[letter].upper())
                await message.add_reaction("👍")
            else:
                await message.add_reaction(random.choice([
                    "🫡", "🫰", "👌", "🤌", "🙆"
                ]))
    except:
        pass

async def reply(message_object: discord.Message, response: str):
    try:
        print(f"💬  {response}")
        await message_object.reply(response)
    except discord.Forbidden:
        print("❌ Permission error: Unable to send message in this channel.")
    except discord.HTTPException as e:
        print(f"❌ HTTP error: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

@bot.event
async def on_message(message):
    if message.channel.id in config["ignored_channels"]:
        return
    if message.author == bot.user:
        return
    angry = message.author.id in config["users_to_be_angry_at"]
    message_content = message.content.replace(f"<@{bot.user.id}>", "").strip()
    if bot.user.mentioned_in(message):
        print(f"📝{"💢" if angry else " "} {message.author.name} - {message_content} in #{message.channel.name} - [{message.channel.id}]")
        await react(message)
        ai_response = ai.get_ai_response(message_content, model="jerome")
        await reply(message, ai_response)
    elif angry and random.randint(0, 100) <= 100:
        await react(message, angry=True)
        await reply(message, ai.get_ai_response(message_content, model="jerome_angry"))
    elif random.randint(0, 100) <= 1:
        await react(message)
        if random.randint(0, 100) <= 50:
            await reply(message, random.choice(config["pre_made_responses"]))
        elif random.randint(0, 100) <= 50:
            await reply(message, ai.get_ai_response(message_content, model="jerome_short"))

@bot.command(description=f"Ask {config["bot_name"]} a question")
async def ask(ctx, *, question: str):
    await ctx.respond("Thinking...")
    await ctx.respond(ai.get_ai_response(question, model="jerome"))

@bot.command(name="ask_model", description=f"Ask {config['bot_name']} a question using a specific model")
async def ask_model(
    ctx: discord.ApplicationContext,
    model: discord.Option(str, description="The model to use", choices=models),
    prompt: discord.Option(str, description="The prompt to send to the model"),
    private: discord.Option(str, description="Show the response to everyone else, or just you?", choices=["Yes", "No"]),
):
    await ctx.respond("🤔 Thinking...", ephemeral=True)
    await ctx.respond(ai.get_ai_response(prompt, model=model), ephemeral=private == "Yes")

bot.run(open("TOKEN").read().strip())
