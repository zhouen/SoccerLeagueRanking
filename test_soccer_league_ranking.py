#!/usr/bin/env python

from soccer_league_ranking import *


def test_read_game_results():
    """
    Test read_game_results() with a given file and expected content.
    """
    test_input_file = './test_data/test_input.txt'
    file_content = read_game_results(test_input_file)
    expected_content = [
        {'Lions': 3, 'Snakes': 3},
        {'Tarantulas': 1, 'FC Awesome': 0},
        {'Lions': 1, 'FC Awesome': 1},
        {'Tarantulas': 3, 'Snakes': 1},
        {'Lions': 4, 'Grouches': 0}
    ]
    assert expected_content == file_content, \
        f'Failed to read {test_input_file}. ' \
        f'Expect: {expected_content}, but got: {file_content}'


def test_calculate_team_scores():
    """
    Test calculate_team_scores() with a given results and expected scores.
    """
    test_game_results = [
        {'Lions': 3, 'Snakes': 3},
        {'Tarantulas': 1, 'FC Awesome': 0},
        {'Lions': 1, 'FC Awesome': 1},
        {'Tarantulas': 3, 'Snakes': 1},
        {'Lions': 4, 'Grouches': 0}
    ]
    # expected_game_scores =
    worked_out_scores = calculate_team_scores(test_game_results)
    expected_scores = {
        'Lions': 5, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1, 'Grouches': 0
    }
    assert worked_out_scores == expected_scores, \
        f'Expected scores: {expected_scores}, but got: {worked_out_scores}'


def test_output_team_ranking():
    """
    Given a list of team scores, expect the correct file is created.
    """
    test_output_file = './test_data/test_output_file.txt'
    test_team_sores = {
        'Lions': 5, 'Snakes': 1, 'Tarantulas': 6, 'FC Awesome': 1, 'Grouches': 0
    }
    output_team_ranking(test_team_sores, test_output_file)

    file = open(test_output_file, 'r')
    test_team_ranking = []
    for line in file:
        test_team_ranking.append(line.replace('\n', ''))
    expected_ranking = [
        '1. Tarantulas, 6 pts',
        '2. Lions, 5 pts',
        '3. FC Awesome, 1 pt',
        '3. Snakes, 1 pt',
        '5. Grouches, 0 pt'
    ]
    assert test_team_ranking == expected_ranking, \
        f'Expect team ranking: {expected_ranking}, but got: {test_team_ranking}'