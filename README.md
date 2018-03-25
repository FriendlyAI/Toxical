# Toxical

A Discord bot built to find toxicity in chats, notify the users, and ban/warn repetitive toxic members to make Discord chats less "cancerous" and ultimately a safer environment

## Adding it to Your Server

Click [this](https://discordapp.com/oauth2/authorize?client_id=427147274498342932&scope=bot) link, select the server you want the bot to join (you need a certain level of authorization to be able to add it to a server), and authorize the bot.

## Testing the Bot

Default prefix: "!"

### Commands (WIP)

##### !score - returns the overall sentiment value of a user 

--insert gif here--

### Automoderation

* Warning a toxic user

--insert gif here

* Banning repeated toxic users

--insert gif here--


## Built With

* [MongoDB](https://docs.mongodb.com/manual/) - The databse we used to store user and server info
* [IBM Watson Tone Analyzer](https://www.ibm.com/watson/services/tone-analyzer/) - One of the AI's we used to detect the emotion chat logs
* [discord.py](http://discordpy.readthedocs.io/en/latest/) - Used to implement a functional Discord bot
* [Vader Sentiment Analysis](https://github.com/cjhutto/vaderSentiment) - The other AI that returned the relative negativity of chat logs

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Anyone whose code we used to make our code work
* Inspiration from the many toxic chats we had among friends
* The Discord API server for helping us with issues we had 
