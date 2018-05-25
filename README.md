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

## 