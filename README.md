# NBA-Leaderboard
NBA Leaderboard project to track statistics throughout the season using a chosen API 

🏀 NBA Standings CLI
A simple, fast Python script that pulls live NBA standings using the NBA API (via RapidAPI) and prints a clean, sorted leaderboard directly in the terminal.
This project focuses on:
Accurate league-wide standings
Sorting by win percentage
Displaying home/away splits, last-10 record, streaks, and games behind
Easy expansion for tiebreakers or additional stat tracking
📌 Features
✔ Live NBA standings from the API
Uses the api-nba-v1 endpoint to retrieve team standings for a specified season.
✔ Fully sorted leaderboard
Sorted by:
win percentage (descending)
Future enhancements planned for:
head-to-head tiebreakers
divisional tiebreakers
conference separation
✔ Clean, readable CLI output
Displays:
Team name
Wins / losses
Win %
Home record
Away record
Last 10
Streak
Games behind
📂 Example Output
NBA League Standings

1. Boston Celtics 12W 2L W% 0.857 Home 7-0 Away 5-2 L10 9-1 Streak W3
2. Denver Nuggets 11W 3L W% 0.786 Home 6-1 Away 5-2 L10 8-2 Streak W2
...
🧠 How It Works
1. Call the NBA standings endpoint
url = "https://api-nba-v1.p.rapidapi.com/standings"
querystring = {"league": "standard", "season": "2024"}
2. Sort the teams by win percentage
teams.sort(key=lambda x: float(x['win']['percentage']), reverse=True)
3. Format and print each team’s info
The script extracts:
wins
losses
win%
games behind
home record
away record
last 10
streak state (W/L)
And prints each line cleanly.
🚀 Running the Script
1. Install dependencies
pip install requests
2. Run
python nba_standings.py
🔑 API Key
The script uses RapidAPI headers:
headers = {
    "X-RapidAPI-Key": "...",
    "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}
You can:
Replace the key directly in the script
Or load it from an environment variable (recommended)
📦 Project Structure
nba-standings/
│
├── nba_standings.py    # main script
├── README.md
└── requirements.txt
🛠 Roadmap
Planned improvements:
Add conference filtering (East/West)
Format output into aligned columns
Add tiebreaker logic
Export to CSV / JSON
Colorize terminal output
Live updating mode (--watch)
