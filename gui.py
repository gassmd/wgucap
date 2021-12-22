from tkinter import *
from selenium import webdriver
from weighted import get_home_advantage, name_get
from weighted import simulate



driver = webdriver.Firefox() #creates initial webdriver with firefox

window = Toplevel()
window.geometry("900x700")              #initializes window, creates geometry, titles window
window.title("Simulation Program")


title = Label(window, text = 'Welcome to our simulation program!')
data_description = Label(window, text = 'Click images below for visualized data and trends')
data_title1 = Label(window, text = 'Vgs Lines vs Totals')
data_title2 = Label(window, text = 'Vgs Total trends')                  #initializes various labels as titles, headings etc.
data_title3 = Label(window, text = 'Covers vs Totals')
game_label = Label(window, text = ' Todays Games \n   Home   Away   Time')
predict_label = Label(window, text = 'HOME TEAM:                                   AWAY TEAM:')
result_label = Label(window, text = 'Select teams for individual predictions')
odds_title = Label(window, text = 'Todays Odds')

title.place(x=435, y=20, anchor = 'center')
data_description.place(x=435, y=50, anchor = 'center')
data_title1.place(x=150, y=100, anchor = 'center')                      #places labels according to xy coordinates
data_title2.place(x=440, y=100, anchor = 'center')
data_title3.place(x=750, y=100, anchor = 'center')
game_label.place(x=60, y=380)
result_label.place(x=330, y= 350)
odds_title.place(x=390, y = 480)



data1small = PhotoImage(file = "C:/Users/Mike G/Documents/wgu/cap/data1small.png")          #small images to serve as thumbnails for our data visualization pictures
data2small = PhotoImage(file = "C:/Users/Mike G/Documents/wgu/cap/data2small.png")
data3small = PhotoImage(file = "C:/Users/Mike G/Documents/wgu/cap/data3small.png")


textentry1 = Entry(window, width=20, bg="white")                  #text entry boxes for game predictions
textentry2 = Entry(window, width=20, bg="white")

#data1.place(x=450, y=300)
#data1.geometry(x=100, y=100)

title.config(font=900)

def expand1():
    newWindow = Toplevel(window)
    newWindow.title("New Window")
    newWindow.geometry("1600x900")
    data1 = PhotoImage(file = "C:/Users/Mike G/Documents/wgu/cap/data1.png")
    data1_img = Label(newWindow, image=data1, anchor = 'nw')                    #expands image to fullsize when thumbnail clicked
    data1_img.place(x=0, y=0)
    newWindow.mainloop()

def expand2():
    newWindow = Toplevel(window)
    newWindow.title("New Window")
    newWindow.geometry("1600x900")                      #expands image to fullsize when thumbnail clicked
    data1 = PhotoImage(file = "C:/Users/Mike G/Documents/wgu/cap/data2.png")
    data1_img = Label(newWindow, image=data1, anchor = 'nw')
    data1_img.place(x=0, y=0)
    newWindow.mainloop()

def expand3():
    newWindow = Toplevel(window)
    newWindow.title("New Window")
    newWindow.geometry("1600x900")                      #expands image to fullsize when thumbnail clicked
    data1 = PhotoImage(file = "C:/Users/Mike G/Documents/wgu/cap/data3.png")
    data1_img = Label(newWindow, image=data1, anchor = 'nw')
    data1_img.place(x=0, y=0)
    newWindow.mainloop()


def get_predicts():
    #home_team = textentry1.get()
    #away_team = textentry2.get()                #function ran when "predict" button is clicked, gets text from above text boxes
    home_team = home_menu.get()
    away_team = away_menu.get()
    print(home_team)
    print(away_team)
    home_prob = get_home_advantage(home_team, away_team)
    home_win = simulate(home_prob, home_team)
    if (home_win):
        result_label.config(text = 'We predict ' + home_team + ' will win')
    elif(home_win == False):
        result_label.config(text = 'We predict ' + away_team + ' will win')
    print('PREDICTIONS HERE')

data1_btn = Button(window, image = data1small, command = expand1)
data2_btn = Button(window, image = data2small, command = expand2)
data3_btn = Button(window, image = data3small, command = expand3)           #initializes thumbnail images as buttons to expand upon clicking
predict_btn = Button(window, text="Predict", width=6, command = get_predicts)

TEAMS = ['76ers', 'Bucks', 'Bulls', 'Cavaliers', 'Celtics', 'Clippers', 'Grizzlies', 'Hawks', 'Heat', 'Hornets', 'Jazz', 'Kings', 'Knicks', 'Lakers', 'Magic', 'Mavericks', 'Nets', 'Nuggets', 'Pacers', 'Pelicans', 'Pistons', 'Raptors', 'Rockets', 'Spurs', 'Suns', 'Thunder', 'Timberwolves', "Trailblazers", 'Warriors', 'Wizards']


home_menu = StringVar(window)
away_menu = StringVar(window)
menu_test1 = OptionMenu(window, home_menu, *TEAMS)
menu_test1.place(x = 310, y = 400)
menu_test2 = OptionMenu(window, away_menu, *TEAMS)
menu_test2.place(x= 490, y= 400)

#textentry1.place(x=320, y=400)
#textentry2.place(x=450, y=400)                          #places textentry boxes, predict labels and buttons
predict_label.place(x = 300, y = 380)
predict_btn.place(x = 400, y = 430)

data1_btn.place(x = 20, y = 130)
data2_btn.place(x = 310, y = 130)                       #places thumbnail images
data3_btn.place(x = 610, y = 130)

def game_list():
    games_today =  ['7:00pm', 'Wizards', '@Knicks', '\n', '9:00pm', 'Bucks', '@Suns', '10:00pm', 'Lakers', '@Jazz']
    games_string = "7:00pm Wizards @Knicks \n\n 9:00pm Bucks @Suns \n\n 10:00pm Lakers @Jazz"
    return games_string




nba_teams = ['76ers', 'Blazers', 'Bucks', 'Bulls', 'Cavaliers', 'Celtics', 'Clippers', 'Grizzlies', 'Hawks', 'Heat', 'Hornets', 'Jazz', 'Kings', 'Knicks', 'Lakers', 'Magic', 'Mavericks', 'Nets', 'Nuggets', 'Pacers', 'Pelicans', 'Pistons', 'Raptors', 'Rockets', 'Spurs', 'Suns', 'Thunder', 'Timberwolves', 'Trail Blazers', 'Warriors', 'Wizards']

def get_todays_games():
    prob_list = []
    driver.get("https://theathletic.com/nba/schedule/")
    schedule = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div[2]/table/tbody[2]")
    words = schedule.text.split()
    valid_teams = []                                    #get todays current games and appends them to list
    print(words)
    for word in words:
        if ':' in word or 'Postponed' in word or 'LIVE' in word:
            valid_teams.append(word)
        if word in nba_teams:
            valid_teams.append(word)
    newline = '\n\n'

    #home_teams = valid_teams[::3]
    #away_teams = valid_teams[1::3]                 #iterates every 3rd to separates away teams, home teams and times. individual variables if necessary
    #times = valid_teams[2::3]

    schedule_list = [x for y in (valid_teams[i:i+3] + [newline] * (i < len(valid_teams)-2) for i in range(0, len(valid_teams), 3)) for x in y]
    print(schedule_list)

    schedule_string = '   '.join(schedule_list)
    print(schedule_string)
    return schedule_string

game_schedule = Label(window, text=get_todays_games())
game_schedule.place(x=39, y=430)


def get_today_simulate():
    prob_list = []
    driver.get("https://theathletic.com/nba/schedule/")
    schedule = driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/div[2]/div[2]/table/tbody[2]")
    words = schedule.text.split()
    valid_teams = []
    results = []
    for word in words:
        if word in nba_teams:
            valid_teams.append(word)
    home_teams = valid_teams[::2]
    away_teams = valid_teams[1::2]
    print(home_teams)
    print(away_teams)
    for i in range(0, len(home_teams)):
        home_name = home_teams[i]
        away_name = away_teams[i]
        print(home_name)
        print(away_name)
        home_prob = get_home_advantage(home_name, away_name)
        print(home_prob)
        prob_list.append([home_prob, home_name, away_name])
    print(prob_list)
    for game in prob_list:
        prob = game[0]
        ht = game[1]
        at = game[2]
        home_win = simulate(prob, ht)
        print(home_win)
        if (home_win):
            results.append('We predict ' + ht + ' will win')
        if(home_win == False):
            results.append('We predict ' + at + ' will win')
    return results
#get_todays_games()

def get_todays_predicts():
    res = get_today_simulate()
    newline = '\n\n'
    predict_list = [x for y in (res[i:i+1] + [newline] * (i < len(res)) for i in range(0, len(res), 1)) for x in y]
    predict_string = ' '.join(predict_list)
    print(predict_string)
    return predict_string

def get_todays_odds():
    driver.get("https://www.lines.com/betting/nba/odds")
    away_team_names = driver.find_element_by_class_name("odds-list")
    odds = away_team_names.text
    odds_list = odds.split()
    if 'Trail' in odds_list:
        odds_list.remove('Trail')
    print(odds_list)
    home_teams = odds_list[5::12]
    home_odds = odds_list[7::12]
    print(home_teams)
    print(home_odds)
    driver.get("https://www.lines.com/betting/nba/odds/over-under")
    away_team_totals = driver.find_element_by_class_name("odds-list")
    total_text = away_team_totals.text
    totals_list = total_text.split()
    #print(totals_list)
    totals = totals_list[7::12]
    print(totals)
    for i in range(0, len(totals)):
        prev_total = totals[i]
        new_total = prev_total[1:]
        totals[i] = new_total
    print(totals)

    res = [None]*(len(home_teams)+len(home_odds)+len(totals))
    res[::3] = home_teams
    res[1::3] = home_odds
    res[2::3] = totals
    print(res)

    newline = '\n\n'

    odds_list = [x for y in (res[i:i+3] + [newline] * (i < len(res)-2) for i in range(0, len(res), 3)) for x in y]
    print(odds_list)
    odd_string = ' '.join(odds_list)
    print(odd_string)
    return odd_string


todays_predicts = Label(window, text = get_todays_predicts())
today_predict_title = Label(window, text = 'Todays Predictions')
today_predict_title.place(x=660, y = 390)
todays_predicts.place(x = 640, y = 430)
today_odds = Label(window, text = get_todays_odds())
today_odds.place(x=370, y =510)


window.mainloop()