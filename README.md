

# Get Tokens From Botfather

## Obtain the Bot Token:

Open Telegram and search for "BotFather" or click on the following link: https://t.me/BotFather.

- Start a conversation with BotFather by clicking on the "Start" button.

- Type "/newbot" and follow the prompts to create a new bot. You will be asked to provide a name and username for your bot. Once you have completed the process, BotFather will provide you with a Bot Token. Keep this token secure, as it will be used to authenticate your bot.

- Copy the Bot Token provided by BotFather.

- In your Python script, assign the Bot Token to the `TELEGRAM_TOKEN` variable or make a `.env` file and write inside:

        TELEGRAM_TOKEN = "<your_bot_token>"

## Obtaining the Chat ID

Here are the steps to obtain the Chat ID:

- Start a conversation with your bot in Telegram.

- Send a message to your bot.

- Visit the following URL in your web browser:

in bash:
    
    https://api.telegram.org/bot<your_bot_token>/getUpdates

- Replace <your_bot_token> with the Bot Token obtained from BotFather.

- Look for the chat object in the JSON response and find the id value. This is your chat ID.

- In your Python script, assign the chat ID to the CHAT_ID variable or add the following line in your `.env` file previously created:

        CHAT_ID = "<your_chat_id>"

Replace <your_chat_id> with the chat ID obtained in step 4.

## Install Requirements

    pip install requests python-dotenv


Run the script and have fun :)
