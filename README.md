# F1 Discord Bot

A Discord bot that provides Formula 1 data visualization and analysis using the FastF1 API.

## Features

- **Telemetry Visualization**
  - Speed trace comparison between drivers
  - Gear shift visualization on track maps
  - Track dominance analysis with mini-sectors

- **Race Analysis**
  - Race pace comparison between drivers
  - Team pace comparison
  - Lap section analysis (braking, cornering, acceleration, full throttle)

- **Information**
  - Next F1 event details
  - Driver standings
  - Constructor standings

## Setup

### Prerequisites

- Python 3.8 or higher
- Discord Bot Token
- Discord Developer Portal access

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/f1-discord-bot.git
   cd f1-discord-bot
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Discord bot token as an environment variable:
   ```bash
   # Linux/macOS
   export token=your_discord_bot_token

   # Windows
   set token=your_discord_bot_token
   ```

4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

The bot uses the prefix `+` for all commands.

### Telemetry Commands

- **Speed Trace Comparison**
  ```
  +speedtrace [year] [race] [session] [driver1] [driver2]
  ```
  Example: `+speedtrace 2023 Monaco Q VER HAM`

- **Gear Shifts Visualization**
  ```
  +gearshifts [year] [race] [session] [driver]
  ```
  Example: `+gearshifts 2023 Monaco Q VER`

- **Track Dominance Analysis**
  ```
  +trackdominance [year] [race] [session] [driver1] [driver2] [driver3]
  ```
  Example: `+trackdominance 2023 Monaco Q VER HAM PER`
  
  Note: Drivers are optional. If not provided, the top 3 fastest drivers will be used.

### Race Analysis Commands

- **Race Pace Comparison**
  ```
  +racepace [year] [race]
  ```
  Example: `+racepace 2023 Monaco`

- **Team Pace Comparison**
  ```
  +teampace [year] [race]
  ```
  Example: `+teampace 2023 Monaco`

- **Lap Sections Analysis**
  ```
  +lapsections [year] [race] [session] [driver1] [driver2] ...
  ```
  Example: `+lapsections 2023 Monaco Q VER HAM PER`
  
  Note: Drivers are optional. If not provided, the top 5 fastest drivers will be used.

### Information Commands

- **Next F1 Event**
  ```
  +f1
  ```

- **Driver Standings**
  ```
  +drivers [year]
  ```
  Example: `+drivers` or `+drivers 2023`

- **Constructor Standings**
  ```
  +constructors [year]
  ```
  Example: `+constructors` or `+constructors 2023`

- **Help**
  ```
  +help [command]
  ```
  Example: `+help` or `+help speedtrace`

## Project Structure

```
f1-discord-bot/
├── bot.py                  # Main entry point
├── config.py               # Configuration
├── requirements.txt        # Dependencies
├── README.md               # Documentation
├── data/                   # Data files
│   ├── country_flags.json  # Flag data
│   └── sched.csv           # Schedule data
├── commands/               # Discord command modules
│   ├── __init__.py
│   ├── telemetry.py        # Telemetry commands
│   ├── race_analysis.py    # Race analysis commands
│   └── info.py             # Information commands
├── services/               # Business logic
│   ├── __init__.py
│   ├── telemetry_service.py
│   ├── race_analysis_service.py
│   ├── standings_service.py
│   └── schedule_service.py
└── utils/                  # Utility functions
    ├── __init__.py
    ├── logging_setup.py
    ├── error_handler.py
    └── embed_builder.py
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [FastF1](https://github.com/theOehrly/Fast-F1) - For providing the F1 data API
- [discord.py](https://github.com/Rapptz/discord.py) - For the Discord API wrapper
