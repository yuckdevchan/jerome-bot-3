# Jerome Bot

## Intro
A simple, nicely written and semi-modular LLM AI Discord bot. However it is not simply an LLM interface for a Discord bot, as the custom modelfiles cause the LLM to communicate less like a robot and more human, erratic and less reliably. A certain authenticity is added by the ways that it will subtely lie for no reason and have a total disregard for any of the values that are hard-coded into apps like ChatGPT. By the way, in the code the models are referred to as grok, as a joke. This may be changed in future.

## Getting Started
> Note: Only Linux is supported and tested as of now. May work on other unix-based systems.

### Install Ollama
[Download and install Ollama](https://ollama.com/)

Ollama may also be available through distro repositories.

### Setup Jerome Bot

Create a text file named `TOKEN` and put your Discord bot's token in it.

In config.json:
- Change the `ignored_channels` list from the sample ones to your own preferences.
- Change the `users_to_be_angry_at` list from the sample ones to your own preferences. This determines which users will trigger the use of the `grok_shut_up` model instead.

Run:
Activate the virtual environment:

```sh
python -m venv .venv
```

```sh
source .venv/bin/activate
```

```sh
pip install -r requirements.txt
```

```sh
python3 main.py
```

It will first try and build the ModelFiles, and put them into Ollama.

If it is able to connect to Discord and run the bot, then it will be confirmed in the output.
