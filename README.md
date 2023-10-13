# f1bot
A simple discord bot that returns data about Formula 1 sessions of the past and present. Hosted on AWS.

### Now Live : Data Visualization Commands

* `+gearshifts <year> <race> <session> <driver>` : returns a plot showing which gear is being utilised by a driver at different points on the specified track.
  <div align="left">
    <img src="images/gearshifts.png">

* `+speedtrace <year> <race> <session> <driver1> <driver2>` : returns the two drivers' speedtraces for the given session, along with annotated corner numbers for comparison.
  <div align="left">
    <img src="images/speedtrace.png">

* `+teampace <year> <race> ` : returns a box-plot visualizing and ranking each of the 10 teams' race pace.
  <div align="left">
    <img src="images/teampace.png">
    
* `+racepace <year> <race>` : returns a swarm-plot of the top-10 drivers' laptimes over the given race session.
  <div align="left">
    <img src="images/racepace.png">

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
    <img src="images/Screenshot 2023-10-06 213136.png">

### Coming Soon


  
### Built With

* JDK 17
* JDA
* Python 3.10
* discord.py
* FastF1 

### Contact

Vivek Pokale - vpokale21@gmail.com
