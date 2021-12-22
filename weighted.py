import random
import excel_populate
from team import Team
from teamcreate import get_team_map


team_map = get_team_map()

def flip(p):
    return 'H' if random.random() < p else 'T'


def simulate(home_win_probability_boost, home_team):
    N = 65
    home_win_probability = .5 + home_win_probability_boost
    home_win = True
    flips = [flip(home_win_probability) for i in range(1, N)]    #higher the "probability" more likely to be heads, lower tails
    print('home win prob ' + str(home_win_probability))
    print(flips)
    percent = float(flips.count('H'))/N
    if percent >= .5:
        print('home team ' + home_team + ' win!')
        return home_win
    elif percent < .5:
        print('home team ' + home_team + ' lose')
        home_win = False
        return home_win

    print(percent)

def game_differential(home_wins, away_wins):
    win_diff = int(home_wins) - int(away_wins)
    negative = False                    #takes home team wins and away team wins and finds difference, marks as negative if so
    if win_diff < 0:
        win_diff = abs(win_diff)       #away team has more wins, home team win probability will decrease
        negative = True                  #home teams has more wins, home team win probability will increase
    win_prob = {range(0, 4): .00,
                range(4, 8): .01,
                range(8, 13): .02,
                range(13, 19): .03,
                range(19, 25): .04,
                range(25, 29): .05,
                range(29, 33): .06,
                range(33, 60): .07}
    for win_range in win_prob:
        if win_diff in win_range:
            home_win_prob = win_prob[win_range]
            if negative is True:
                home_win_prob = home_win_prob * -1
            return home_win_prob        #returns negative probability if away team has more wins


def season_differential(last_ten_home_wins, last_ten_away_wins):
    win_diff = int(last_ten_home_wins) - int(last_ten_away_wins)
    negative = False
    if win_diff < 0:
        win_diff = abs(win_diff)       #away team has more wins, home team win probability will decrease
        negative = True
    win_prob = {range(0, 1): .00,
                range(1, 3): .01,
                range(3, 5): .02,
                range(5, 7): .03,
                range(7, 9): .04,
                range(9, 10): .05}
    for win_range in win_prob:
        if win_diff in win_range:
            home_win_prob = win_prob[win_range]
            if negative is True:
                home_win_prob = home_win_prob * -1

            return home_win_prob        #returns negative probability if away team has more wins

def elo_differential(home_elo, away_elo):
    elo_diff = int(home_elo) - int(away_elo)
    negative = False
    if elo_diff < 0:
        elo_diff = abs(elo_diff)
        negative = True
    elo_prob = {range(0, 50): .00,
                range(50, 100): .01,
                range(100, 150): .02,
                range(150, 200): .03,
                range(200, 250): .04,
                range(250, 300): .05,
                range(300, 400): .06,
                range(400, 500): .07}
    for elo_range in elo_prob:
        if elo_diff in elo_range:
            elo_win_prob = elo_prob[elo_range]
            if negative is True:
                elo_win_prob = elo_win_prob * -1
            return elo_win_prob

def home_field_advantage():
    return .02


def name_get(team_term):
    #print('team term before ' + team_term)
    team_term = excel_populate.team_dict(team_term)
    #print('team term after ' + team_term)
    for i in range(0, team_map.__sizeof__()):
        team = team_map.get(i)
        if team is not None and team.name == team_term:
            return team

def get_home_advantage(home, away):
    home_team = name_get(home)
    away_team = name_get(away)
    season_prob = game_differential(home_team.last_season_wins, away_team.last_season_wins)
    print('away |' + away_team.name + '| VS |' + home_team.name + '| home')
    print('away team last season ' + str(away_team.last_season_wins))
    print('home team last season ' + str(home_team.last_season_wins))
    print(season_prob)
    last10_prob = season_differential(home_team.last_10_wins, away_team.last_10_wins)
    print('away team last10 ' + str(away_team.last_10_wins))
    print('home team last10 ' + str(home_team.last_10_wins))
    print(last10_prob)
    elo_prob = elo_differential(home_team.elo, away_team.elo)
    print('away team elo ' + str(away_team.elo))
    print('home team elo ' + str(home_team.elo))
    print(elo_prob)
    home_prob = home_field_advantage()
    print('HOME PROBABILITY BOOST ' + str(home_prob))
    total_prob = season_prob + last10_prob + elo_prob + home_prob
    total_prob = round(total_prob, 2)
    print('total prob ' + str(total_prob))
    return total_prob

