## Inspiration
The inspiration behind MediChat stemmed from our collective desire to address the pressing issues of mental health, boredom, and isolation among patients in hospitals. Recognizing the crucial need for support and connection, we set out to create innovative solutions that harness the power of technology to make a meaningful impact.

## What it does
MediChat comprises three groundbreaking implementations tailored to enhance mental health support and alleviate feelings of isolation:

1. **Comprehensive App for Connections and Cultural Exchange:** Our app facilitates diverse connections and cultural exchange opportunities. Patients can engage with fellow patients or non-patients, choosing from a variety of languages to communicate. With built-in translation capabilities, we promote language literacy while fostering meaningful cultural and social interactions within patients and outsiders.

2. **Discord Bot for Monitoring and Support:** Our Discord bot actively monitors conversations within our dedicated server, instantly reaching out via direct message whenever patients express distress or mention trigger words related to stress or suicidal thoughts. The bot gives users the option too chat with a virtual human that we created during this Design-A-Thon.

3. **Virtual Human Companion:** We introduce a revolutionary virtual human companion accessible through the Discord bot. This compassionate AI provides a safe space for patients to articulate their mental health concerns, offering guidance on stress management, life responsibilities, sleep hygiene, and concentration enhancement. The virtual human works via message or voice dictation, ensuring that patients who do not have capabilities of typing to this virtual human can still communicate.

## How we built it
In engineering MediChat, we harmonized technological prowess with human-centric design principles. Here's how we brought our vision to life:

- **Comprehensive App Development:** We meticulously crafted an app interface optimized for intuitive navigation and accessibility using Figma, a collaborative design tool. Additionally, employing HTML, CSS, and JavaScript, we architected a virtual human website characterized by an inviting user interface and seamless user experience. 

- **Discord Bot Infrastructure:** Utilizing Python in conjunction with Discord.py, we engineered a bot infrastructure capable of real-time communication and personalized support.

- **Virtual Human Companion:** Leveraging Dialogflow, an AI-powered conversational platform, we developed a virtual human with sophisticated natural language understanding capabilities, fostering empathetic interactions with patients.

## Setup and Running Guide for Discord Bot (MediPal)

This guide provides instructions on setting up and running the Discord bot named MediPal. MediPal is designed to provide mental health support within Discord communities, identifying and offering assistance to members who express suicidal thoughts or stress-related concerns.

## Prerequisites

Before proceeding, ensure you have the following:

- Python installed on your system (version 3.6 or higher)
- Discord account
- Text editor (e.g., Visual Studio Code, Sublime Text)
- Token for your Discord bot

## Installation Steps

1. Clone or download the repository containing the bot script.
2. Install the required Python packages by running the following command in your terminal or command prompt:

`pip install discord.py`

`python-dotenv`

3. Obtain a Discord bot token from the Discord Developer Portal.
4. Create a `.env` file in the project directory and add the following line:

`TOKEN=your_discord_bot_token`

Replace `your_discord_bot_token` with the token you obtained in step 3.

## Running the Bot

1. Navigate to the directory containing the bot script in your terminal or command prompt.
2. Run the bot script by executing the following command:

`python bot_script.py`

3. Once the bot is running, it will log in and connect to Discord. You should see a message indicating successful connection in the terminal.

## Bot Usage

- Upon joining a Discord server, new members will receive a welcome message from MediPal in their direct messages (DMs).
- MediPal will monitor messages for keywords related to stress or suicidal thoughts. If detected, it will send supportive messages and resources to the user via DM.
- Users can also interact with the bot using commands such as `!hotline` to display the National Suicide Prevention Lifeline information and `!hi` to receive a greeting message from MediPal.

## Customization

- Customize the list of stressed and suicidal words in the bot script (`bot_script.py`) to better suit your community's needs.
- Modify the content of the messages sent by MediPal to tailor them to your preferences or add additional resources.

# Setup and Running Guide for HTML Page with Dialogflow Messenger

This guide explains how to set up and run an HTML page embedded with Dialogflow Messenger, which provides a chat interface for interacting with a Dialogflow agent.

## Prerequisites

Before proceeding, ensure you have the following:

- Dialogflow agent ID
- Access to the Dialogflow Console

## Setup Steps

1. Save the provided HTML code in a file named `index.html`.
2. Obtain your Dialogflow agent ID from the Dialogflow Console.
3. Replace `agent-id` attribute in the `<df-messenger>` tag with your Dialogflow agent ID.
4. Optionally, customize the `chat-title` attribute to set the title of the chat interface.
5. Save any changes made to the HTML file.

## Running the HTML Page

1. Open the HTML file (`index.html`) using a web browser.
2. The Dialogflow Messenger interface will appear on the page, allowing users to interact with your Dialogflow agent.

## Customization

- Customize the appearance of the HTML page by modifying the CSS styles in the `style.css` file.
- Customize the behavior of the chat interface by editing the JavaScript code in the `script.js` file.
- Adjust the content and responses of the Dialogflow agent in the Dialogflow Console.

## Challenges we ran into
Throughout the development journey of MediChat, we encountered several challenges that put our skills to the test:

- Configuring and troubleshooting to get the virtual human to go live on Dialogflow.
- Crafting contextually relevant responses for the virtual human.
- Integrating the Discord bot with trigger word recognition due to limitations in message handling from the Discord API.
- Grappling with simple semantics and encountering Python debugging issues.

## Accomplishments that we're proud of
We are immensely proud of the impactful solutions we've created with MediChat:

- Designing an intuitive app interface that promotes language literacy and cultural exchange.
- Developing a robust Discord bot capable of proactive support.
- Implementing a virtual assistant to work with patients on specific needs.

## What we learned
The journey of building MediChat was rich with valuable lessons and insights:

- Understanding the complexities surrounding mental health support and the importance of leveraging technology to foster meaningful connections.
- Hone technical skills in natural language processing, bot development, and user interface design.
- Perseverance and teamwork are key to overcoming challenges in creating innovative solutions.

## What's next for MediChat
Looking ahead, we are committed to continuous improvement and expansion of MediChat:

- Refining the capabilities of our virtual human companion for more personalized support.
- Enhancing the user experience of our app for seamless interactions.
- Exploring opportunities for partnerships and collaborations to reach a wider audience and make a global impact.
