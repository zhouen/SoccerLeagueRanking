#!/usr/bin/venv python
import argparse
import operator


def create_parsed_args():
    """
    --single: Find one given movie's rating
    --path: Find all movies' rating in the given path
    --poster: Find movie rating with poster path
    --preview: Find movie rating with preview link
    --verify: Verify the found movie's id at www.themoviedb.org
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

    :param input_file:
    :return: A list of dictionary and each dict stores team name and its goals.
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

    :param game_results:
    :return:
    """
    team_scores = {}
    for game in game_results:
        team_list = list(game.keys())
        team_1 = team_list[0]
        team_2 = team_list[1]
        if game[team_1] > game[team_2]:
            update_team_score(team_scores, team_1, 3)
            update_team_score(team_scores, team_2, 0)
        elif game[team_1] == game[team_2]:
            update_team_score(team_scores, team_1, 1)
            update_team_score(team_scores, team_2, 1)
        else:
            update_team_score(team_scores, team_1, 0)
            update_team_score(team_scores, team_2, 3)
    return team_scores


def output_team_ranking(team_scores, output_file):
    """

    :param team_scores:
    :return:
    """

    team_scores_sorted = dict(
        sorted(team_scores.items(), key=(operator.itemgetter(1)), reverse=True)
    )
    file = open(output_file, 'w')
    count = 0
    for team_name in list(team_scores_sorted.keys()):
        count += 1
        score = team_scores_sorted[team_name]
        unit = 'pt' if score <=1 else 'pts'
        file.write(f'{count}. {team_name}, {score} {unit}\n')
    file.close()


def soccer_league_ranking(input_args):
    """
    :param game_result:
    :return:
    """
    input_file = input_args.input
    output_file = input_args.output
    game_results = read_game_results(input_file)
    team_scores = calculate_team_scores(game_results)
    output_team_ranking(team_scores, output_file)


if __name__ == '__main__':

    parsed_args = create_parsed_args()
    soccer_league_ranking(parsed_args)
