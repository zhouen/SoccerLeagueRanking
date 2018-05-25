#!/usr/bin/venv python
import argparse
import random

def generate_random_game_results(filename):
    """
    Generate a random game list with random score between 0 and 5 for each team.
    :return Write the list to file called game_results.txt
    """
    team_names = [
        'Tarantulas', 'Lions', 'FC Awesome', 'Snakes', 'Grouches', 'Rockets', 'Worriors'
    ]
    file = open(filename, 'w')
    playlist = []
    for i in range(len(team_names)*2):
        team1 = random.choice(team_names)
        team2 = random.choice(team_names)

        while team2 == team1:
            team2 = random.choice(team_names)
        score1 = random.randint(0, 5)
        score2 = random.randint(0, 5)
        if f'{team1}:{team2}' not in playlist:
            playlist.append(f'{team1}:{team2}')
            file.write(f'{team1} {score1}, {team2} {score2}\n')
    file.close()


def create_parsed_args():
    """
    Get options from command line input.
    """

    parser = argparse.ArgumentParser(
        prog='Soccer League Ranking',
        description='This a command line application that reads soccer game '\
            'results from and text file and return the ranking to an output file.',
        usage='python soccer_league_ranking.py --file path_to_game_results_file'
    )

    parser.add_argument('-i', '--input',
                        default=None,
                        required=True,
                        help='Input file where game results are stored.'
                       )
    parser.add_argument('-o', '--output',
                        default=None,
                        required=True,
                        help='Output file where team ranking are stored.'
                        )
    return parser.parse_args()


def read_game_results(input_file):
    """
    This function reads game results from the given input file.
    :param input_file:
    :return: A list of dictionaries which store team name and its goals.
    """
    file = open(input_file, 'r')
    results = []
    for line in file:
        game = {}
        for item in line.split(','):
            cleaned_item = item.strip().split(' ')
            name = ' '.join(cleaned_item[:-1])
            goals = int(cleaned_item[-1])
            game.update({name: goals})
        results.append(game)
    file.close()
    return results


def update_team_score(team_scores, team_name, score):
    """
    Added team and its score to the team_scores list.
    :param team_scores:
    :param team_name:
    :param score:
    :return:
    """
    if team_name in team_scores:
        team_scores[team_name] += score
    else:
        team_scores.update(
            {team_name: score}
        )


def calculate_team_scores(game_results):
    """
    Base on Win, Tie and Loose rules work out score for each team.
    :param game_results:
    :return:
    """
    team_scores = {}
    for game in game_results:
        team_list = list(game.keys())
        team_1 = team_list[0]
        team_2 = team_list[1]
        # Win = 3
        if game[team_1] > game[team_2]:
            update_team_score(team_scores, team_1, 3)
            update_team_score(team_scores, team_2, 0)
        # Tie = 1
        elif game[team_1] == game[team_2]:
            update_team_score(team_scores, team_1, 1)
            update_team_score(team_scores, team_2, 1)
        # Loose = 0
        else:
            update_team_score(team_scores, team_1, 0)
            update_team_score(team_scores, team_2, 3)
    return team_scores


def output_team_ranking(team_scores, output_file):
    """
    This function sort teams by scores and output them to a given file.
    :param team_scores:
    :param output_file:
    :return:
    """
    randed_teams = {}
    for team_name, scores in team_scores.items():
        if scores in randed_teams:
            randed_teams[scores].append(team_name)
        else:
            randed_teams.update(
                {scores: [team_name]}
            )
    randed_scores = list(randed_teams.keys())
    randed_scores =  sorted(randed_scores, reverse=True)

    file = open(output_file, 'w')
    count = 1
    for score in randed_scores:
        unit = 'pt' if score <=1 else 'pts'
        teams = randed_teams[score]
        for team in sorted(teams):
            # print(f'{count}. {team}, {score} {unit}\n')
            file.write(f'{count}. {team}, {score} {unit}\n')
        count += len(teams)
    file.close()
    print(f'Team ranks are saved in {output_file}.')


def main():
    """
    """
    input_args = create_parsed_args()
    input_file = input_args.input
    output_file = input_args.output
    game_results = read_game_results(input_file)
    team_scores = calculate_team_scores(game_results)
    output_team_ranking(team_scores, output_file)


if __name__ == '__main__':
    # generate_random_game_results()
    main()
