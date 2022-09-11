import gspread
from twitter import *
import time
import random

#Videos and other links for reference
#Main setup for google sheets, twitter posting "Simple Twitter Bot Python Tutorial" - https://www.youtube.com/watch?v=83o6rU5XArs
#How to run it on google cloud with Tmux "Free Hosting for Python Scripts on Google Cloud" - https://www.youtube.com/watch?v=5OL7fu2R4M8
#How to use Nano Command Line editor - https://linuxize.com/post/how-to-use-nano-text-editor/

#tmux commands
#tmux - start tmux
#tmux ls - list all tmux connections
#tmux a -t # - connect to the specific tmux pipe
#ctrl + d - close the tmux pipe
#tmux cheat sheet - https://tmuxcheatsheet.com/


##consumer keys in twitter keys
consumer_key = "*******FIND******"
consumer_secret = "*******FIND******"

# access token and secret in twitter keys
token = "*******FIND******"
token_secret = "*******FIND******"


#need credential.json info as well
gc = gspread.service_account("credentials.json")
t = Twitter(auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# Open a sheet from a spreadsheet in one go
wks = gc.open("jimmy-g").sheet1

games = wks.get_all_records()

for game in games:
    random_games = random.choice(games)
    game_status = random_games.get("GS")
    if game_status == "Did Not Play":
        status = (
            f"{random_games.get('Date')}\n"
            f"{random_games.get('Tm')} {random_games.get('hva')} {random_games.get('Opp')}\n"
            f"{random_games.get('Result')}\n"
            f"Did not Play\n" 
            f"What say you @elonmusk, @RealSkipBayless, @49ers, @espn?"
        )


    elif game_status == "Injured Reserve":
        status = (
            f"{random_games.get('Date')}\n"
            f"{random_games.get('Tm')} {random_games.get('hva')} {random_games.get('Opp')}\n"
            f"{random_games.get('Result')}\n"
            f"Injured Reserve\n"
            f"What say you @elonmusk, @RealSkipBayless, @49ers, @espn?"
        )


    elif game_status == "Inactive":
        status = (
            f"{random_games.get('Date')}\n"
            f"{random_games.get('Tm')} {random_games.get('hva')} {random_games.get('Opp')}\n"
            f"{random_games.get('Result')}\n"
            f"Inactive\n"
            f"What say you @elonmusk, @RealSkipBayless, @49ers, @espn?"
        )


    else:
        status = (
            f"{random_games.get('Date')}\n"
            f"{random_games.get('Tm')} {random_games.get('hva')} {random_games.get('Opp')}\n"
            f"{random_games.get('Result')}\n"
            f"Comp/Att: {random_games.get('Cmp', 0)}/{random_games.get('Att', 0)}\n"
            f"Pass Yards/Td/Int: {random_games.get('Yds', 0)}/{random_games.get('TD', 0)}/{random_games.get('Int', 0)}\n"
            f"Rating: {random_games.get('Rate', 0)}\n"
            f"YPA: {random_games.get('Y/A', 0)}, AYPA: {random_games.get('AY/A', 0)}\n"
            f"Sacks: {random_games.get('Sk', 0)}/{random_games.get('Yds2', 0)}\n"
            f"Rush Yards: {random_games.get('Yds1', 0)}, Rush TD: {random_games.get('Td1', 0)}\n"
            f"What say you @elonmusk, @RealSkipBayless, @49ers, @espn?"
        )

    #post to twitter
    t.statuses.update(status=status)

#deleted for cron job 7/21/2022
#    time.sleep(21600)

