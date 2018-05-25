# SoccerLeagueRanking

## Description

This code is a command line base application which will calculate the ranking table for a soccer league.

The input and output will be text. Either using stdin/stdout or taking file names on the command line is fine.

The input contains results of games, one per line. See “Sample input” for details.
The output should be ordered from most to least points, following the format specified in “Expected output”.

In this league, a draw (tie) is worth 1 point and a win is worth 3 points. A loss is worth 0 points.
If two or more teams have the same number of points, they should have the same rank and be printed in alphabetical order (as in the tie for 3rd place in the sample data).

#### Sample input:

```text
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
```

#### Expected output:

```text
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```

## Installation

1. Clone the repository from `Github`
    
    ```bash
    $ git clone https://github.com/zhouen/SoccerLeagueRanking.git
    ```
2. Create virtual environment using `Python 3.6` in `SoccerLeagueRanking/`
    
    ```bash
    $ cd SoccerLeagueRanking
    $ python3.6 -m venv venv
    ```
3. Activate virtual environment
    
    ```bash
    $ source venv/bin/activate
    ```

4. Install Dependencies

    ```bash
    $ pip install -r requirements.txt
    ```

## Command Option

-i, --input

--Path to the input file where game results are stored.

-o, --output

--Path to the output file where team ranks are stored.


## Run with Sample Input and Ouput

Once the virtual environment is created in the application directory, 
it must be activated before the application is able to run.

There is a input file called `sample_input.txt` in the application directory.

```bash
$ python soccer_league_ranking.py -i sample_input.txt -o sample_output.txt
``` 

After a successful execution of above command, the output file named `sample_output.txt`
will be created. If there is no directory specified, it will be in the application
directory.

## Run Tests

All the tests are created in `test_soccer_league_ranking.py` and the data
is used by the tests are store in the `test_data` directory.

```bash
$ pytest -v test_soccer_league_ranking.py 
```

Test output:

```bash
==================================================================================== test session starts =====================================================================================
platform linux -- Python 3.6.5, pytest-3.6.0, py-1.5.3, pluggy-0.6.0 -- /home/nathan/Projects/SoccerLeagueRanking/venv/bin/python3.6
cachedir: .pytest_cache
rootdir: ~/SoccerLeagueRanking, inifile:
collected 3 items                                                                                                                                                                            

test_soccer_league_ranking.py::test_read_game_results PASSED                                                                                                                           [ 33%]
test_soccer_league_ranking.py::test_calculate_team_scores PASSED                                                                                                                       [ 66%]
test_soccer_league_ranking.py::test_output_team_ranking PASSED                                                                                                                         [100%]

================================================================================== 3 passed in 0.72 seconds ==================================================================================
```



## Generate Random Game Results

This functionality is used to generate dummy game results for the following teams:

```text
'Tarantulas', 'Lions', 'FC Awesome', 'Snakes', 'Grouches', 'Rockets', 'Worriors'
```

Their goals are generated randomly between 0 and 5. A file name must be supplied
so that the game results can be created in a text file.

```bash
python -c "from soccer_league_ranking import generate_random_game_results; generate_random_game_results('dummy_result.txt')"
```

Then this file can be used as input file to the application.



## Known Issues

This application was not tested against scaled data since the it is not practical for soccer league to have a million teams or games.