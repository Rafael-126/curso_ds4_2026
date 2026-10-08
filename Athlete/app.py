from Game import Game
from Team import Team
from Sport import Sport
from Athlete import Athlete
import json

def load_json_file(file_path):
    data = None
    with open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)
    return data

def convert_json_to_teams(json_data):
    teams = []
    for team_data in json_data:
        team_name = team_data['name']
        sport_name = team_data['sport']['name']
        sport_league = team_data['sport']['league']
        sport_num_players = team_data['sport']['num_players']
        print(team_name,sport_name,sport_league,sport_num_players)
        sport = Sport(sport_name, sport_league, sport_num_players)
        team = Team(team_name, sport)
        for athlete_data in team_data['athletes']:
            athlete_name = athlete_data['name']
            athlete_age = athlete_data['number']
            athlete = Athlete(athlete_name, athlete_age, sport_name)
            team.add_athlete(athlete)
        teams.append(team)

    return teams

def main():
    tournament_data = load_json_file('C:\\Users\\rafa_\\Desktop\\curso_python\\curso_ds4_2026\\Athlete\\tournament.json')
    print("Tournament:", tournament_data)
    teams = convert_json_to_teams(tournament_data)

    team_combinations = list(combinations(teams, 2))
    for local, visitor in team_combinations:
        print(f"Match: {local.name} vs {visitor.name}")
        game = Game(local, visitor)
        game.play()
        game.display()
        print("\n")


if __name__ == "__main__":
    main()