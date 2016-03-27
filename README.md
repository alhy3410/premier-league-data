# Premier League Data

Match-wise results and statistics scraped from [premierleague.com](http://www.premierleague.com/en-gb/matchday/results.html).

Every match played is one row in the data.

## Columns (codebook)

Below is a list of columns available in the dataset with a rough description of each column.

| Name | Description |
| ---- | ----------- |
| `date` | Date when the match was played, ex: `Sunday 20 March 2016` |
| `home_team` | The team that is playing at home |
| `away_team` | The visiting team |
| `home_manager` | Manager of the home team |
| `away_manager` | Manager of the visiting team |
| `venue` | Name of the stadium (of `home_team`) |
| `result` | Match result |
| `home_goals` | Goals scored by the `home_team` |
| `home_goals_details` | Names of the players of `home_team` with the time when they scored |
| `away_goals` | Goals scored by the `away_team` |
| `away_goals_details` | Names of the players of `away_team` with the time when they scored |
| `referee` | Name of the referee |
| `attendance` | Number of people who attended the match live (at `venue`) |
| `assists_home_team` | Number of assists by players of `home_team` |
| `assists_away_team` | Number of assists by players of `away_team` |
| `free_kicks_home_team` | Number of free kicks won by the `home_team` |
| `free_kicks_away_team` | Number of free kicks won by the `away_team` |
| `penalties_home_team` | Number of penalties scored by the `home_team` |
| `penalties_away_team` | Number of penalties scored by the `away_team` |
| `total_shots_home_team` | Total shots attempted by the `home_team` |
| `total_shots_away_team` | Total shots attempted by the `away_team` |
| `shots_on_target_home_team` | Number of shots on target by `home_team` |
| `shots_on_target_away_team` | Number of shots on target by `away_team` |
| `shots_off_target_home_team` | Number of shots off target by `home_team` |
| `shots_off_target_away_team` | Number of shots off target by `away_team` |
| `crosses_home_team` | Number of crosses made by the `home_team` |
| `crosses_away_team` | Number of crosses made by the `away_team` |
| `corners_home_team` | Number of corners won by the `home_team` |
| `corners_away_team` | Number of corners won by the `away_team` |
| `throw_ins_home_team` | Number of throw ins by the `home_team` |
| `throw_ins_away_team` | Number of throw ins by the `away_team` |
| `saves_home_team` | Number of saves made by the goalkeeper of `home_team` |
| `saves_away_team` | Number of saves made by the goalkeeper of `away_team` |
| `blocks_home_team` | Number of blocks by the `home_team` |
| `blocks_away_team` | Number of blocks by the `away_team` |
| `clearances_home_team` | Number of clearances made by the `home_team` |
| `clearances_away_team` | Number of clearances made by the `away_team` |
| `offsides_home_team` | Number of times `home_team` players were caught offside |
| `offsides_away_team` | Number of times `away_team` players were caught offside |
| `handballs_home_team` | Number of times `home_team` players were caught with a handball |
| `handballs_away_team` | Number of times `away_team` players were caught with a handball |
| `fouls_home_team` | Number of fouls committed by `home_team` |
| `fouls_away_team` | Number of fouls committed by `away_team` |
| `yellow_cards_home_team` | Number of yellow cards `referee` gave the `home_team` |
| `yellow_cards_away_team` | Number of yellow cards `referee` gave the `away_team` |
| `red_cards_home_team` | Number of `home_team` players that the `referee` sent off |
| `red_cards_away_team` | Number of `away_team` players that the `referee` sent off |

## Sample exploration

Data exploration examples using `pandas`.

#### What data is available?

```python
In [1]: import pandas as pd

In [2]: df = pd.read_csv('2015-16/data.csv')

In [3]: df.columns
Out[3]:
Index([u'assists_away_team', u'assists_home_team', u'attendance',
       u'away_goals', u'away_goals_details', u'away_manager', u'away_team',
       u'blocks_away_team', u'blocks_home_team', u'clearances_away_team',
       u'clearances_home_team', u'corners_away_team', u'corners_home_team',
       u'crosses_away_team', u'crosses_home_team', u'date', u'fouls_away_team',
       u'fouls_home_team', u'free_kicks_away_team', u'free_kicks_home_team',
       u'handballs_away_team', u'handballs_home_team', u'home_goals',
       u'home_goals_details', u'home_manager', u'home_team',
       u'offsides_away_team', u'offsides_home_team', u'penalties_away_team',
       u'penalties_home_team', u'red_cards_away_team', u'red_cards_home_team',
       u'referee', u'result', u'saves_away_team', u'saves_home_team',
       u'season', u'shots_off_target_away_team', u'shots_off_target_home_team',
       u'shots_on_target_away_team', u'shots_on_target_home_team',
       u'throw_ins_away_team', u'throw_ins_home_team',
       u'total_shots_away_team', u'total_shots_home_team', u'venue',
       u'yellow_cards_away_team', u'yellow_cards_home_team'],
      dtype='object')
```

#### How many shots have Leicester taken when playing in home this season?

```python
In [4]: sum(df[df.home_team == 'Leicester'].total_shots_home_team)
Out[4]: 155
```

#### How many goals have Man Utd scored so far this season?

```python
In [5]: sum(df[df.home_team == 'Man Utd'].home_goals) + sum(df[df.away_team == 'Man Utd'].away_goals)
Out[5]: 38
```


... and the possibilities are endless! :smile:
