# Jerome Bot

## Intro
A simple, nicely written and semi-modular LLM AI Discord bot. However it is not simply an LLM interface for a Discord bot, as the custom modelfiles cause the LLM to communicate less like a robot and more human, erratic and less reliably. A certain authenticity is added by the ways that it will subtely lie for no reason and have a total disregard for any of the values that are hard-coded into apps like ChatGPT.

## Getting Started
> Note: Only Linux is supported and tested as of now. May work on other unix-based systems.

### Setup Ollama
Download and install Ollama from [ollama.com](https://ollama.com/)

> Note: Ollama may also be available through distro repositories, including Homebrew.

Ollama is free & open-source software.


Once Ollama is properly set up, install a model. The only currently supported and recommended model for use with this project is `llama3.2` which should be suitable for a wide range of use cases. The 1B size is recommended as it is the fastest, however any size can be used drop-in as well and will work perfectly with Jerome Bot.

Run:
```sh
ollama pull llama3.2:1b # You can choose any size of the model: 1b, 3b etc.
```

### Setup Jerome Bot

Create a text file named `TOKEN` and put your Discord bot's token in it.

In config.json:
- Change the `ignored_channels` list from the sample ones to your own preferences.
- Change the `users_to_be_angry_at` list from the sample ones to your own preferences. This determines which users will trigger the use of the `jerome_angry` model instead.

Run the following commands to get set up:
```sh
python -m venv .venv # Create a python virtual environment, for installing the necessary packages for Jerome Bot
```

```sh
source .venv/bin/activate # Activate the virtual environment which was just created
```

```sh
pip install -r requirements.txt # Install the requirements for Jerome Bot into that virtual environment
```

```sh
python3 main.py # Run Jerome Bot
```

It will first try and build the ModelFiles, and put them into Ollama.

If it is able to connect to Discord and run the bot, then it will be confirmed in the output.

## Bot Usage

### Interacting using @Mentions
For example:
```
@Jerome Bot, are you conscious? 
```
After the message, the bot should react with an emoji to your message and respond shortly.

### Interacting via Slash Commands
To simply ask the bot a question, use the following command and enter the prompt.
```
/ask
```

To ask the bot a question, with specification of the model used for the response and whether the message is shown only to the prompting user (ephemeral) or not.
```
/ask_with_model
```
