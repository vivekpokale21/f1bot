# f1bot
A simple discord bot that returns data about the upcoming Formula 1/2/3 session. Hosted on Heroku.

### Command Usage

* [Invite](https://discord.com/api/oauth2/authorize?client_id=951889203581579304&permissions=274878294080&scope=bot) the bot to your server. 

* `+f1` : returns data about the upcoming Formula 1 session.
  <div align="left">
    <img src="images/Screenshot 2022-03-17 002640.png">
* `+remind f1` : functions as a reminder, notifies the user of the upcoming race session by @username push-notification 5 minutes before the start of a session.
  <div align="left">
    <img src="images/Screenshot 2023-10-06 215150.png">
* `+drivers` : returns drivers' standings.
  <div align="left">
    <img src="images/Screenshot 2023-10-06 213057.png">
* `+teams` : returns teams' standings.
  <div align="left">
    <img src="images/Screenshot 2023-10-06 213057.png">

### Coming Soon

* `+racepace <year> <race>` : returns a swarm-plot of the top-10 drivers' laptimes over the given race session. Uses the FastF1 API
  <div align="left">
    <img src="images/Screenshot 2023-10-06 212319.png">
  
### Built With

* JDK 17
* JDA
  
### Contact

Vivek Pokale - vpokale21@gmail.com
