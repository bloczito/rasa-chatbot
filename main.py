from discord import Client, Intents, Message
from requests import post
from json import loads as load_json
from os import environ

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"
BOT_TOKEN_NAME = "BOT_TOKEN"


async def handle_message(message: Message, user_message: str) -> None:
    rasa_response = post(RASA_URL, json={"message": user_message, "sender": "bloczek"})

    messages = [item["text"] for item in load_json(rasa_response.text)]
    result_msg = "\n".join(messages)

    try:
        await message.channel.send(result_msg)
    except Exception as e:
        print(e)


def get_bot_token() -> str:
    return environ[BOT_TOKEN_NAME]


def run_bot():
    intents = Intents.default()
    intents.message_content = True
    client = Client(intents=intents)

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message: Message):
        if message.author.bot:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} sent {user_message} in {channel}.")

        await handle_message(message, user_message)

    client.run(get_bot_token())


if __name__ == '__main__':
    run_bot()
