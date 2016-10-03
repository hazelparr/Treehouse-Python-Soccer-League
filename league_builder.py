import csv

def open_file(file_name):
	'''Takes file name as argument and returns a list of dictionary 
	of players' info'''
	with open(file_name, newline="") as csvfile:
		players = list(csv.DictReader(csvfile, delimiter=","))
	return players


def sort_players(players):
	'''Takes dictionary of players as argument and sorts out the 
	players into experienced and inexperienced players'''
	exp_players = []
	inexp_players = []
		
	for player in players:
		if player["Soccer Experience"] == "YES":
			exp_players.append(player)
		else:
			inexp_players.append(player)

	return exp_players, inexp_players
	


def team_assignment(players):
	'''Takes the experienced and inexperienced player iterables as
	arguments and to divide each group equally among the teams'''
	teams = [
		{"Team Name": "Raptors", "Practice Time": "March 18, 1 pm", "Players": []},
		{"Team Name": "Sharks", "Practice Time": "March 17, 3 pm", "Players": []},
		{"Team Name": "Dragons", "Practice Time": "March 18, 1pm", "Players": []}
	]
	
	for i in range(len(players)):
		for j in range(len(players[i])):
			team_number = j % len(teams)
			teams[team_number]["Players"].append(players[i][j])
	return teams


def write_letters(sorted_teams):
	'''Uses the sorted team list as argument to write to txt file the letters 
	with the players name as file names and includes their guardian(s) names, 
	team name and practice time'''
	
	for team in sorted_teams:
		for player in team["Players"]:
			file_name = "{name}.txt".format(name=player["Name"].lower().replace(" ", "_"))
			with open(file_name, "w") as file:
				file.write("""
Dear {Guardian Name(s)},

We would like to inform you that {Name} has been seleted to play for Team {Team_Name}.

The team's first practice will be on {Practice_Time}.

Kind Regards,

Hazel
League Coordinator
""".format(Team_Name = team["Team Name"], Practice_Time = team["Practice Time"], **player))


def main():
	players = open_file("soccer_players.csv")
	sorted_players = sort_players(players)
	teams = team_assignment(sorted_players)
	write_letters(teams)


if __name__ == "__main__":
	main()

