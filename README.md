# Premier League Data

Match-wise results and statistics scraped from [premierleague.com](http://www.premierleague.com/en-gb/matchday/results.html).

## Columns (Codebook)

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
