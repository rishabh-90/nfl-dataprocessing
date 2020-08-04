import pandas as pd
import requests
from datetime import datetime, date, time
from dateutil.rrule import rrule, DAILY
import json

'''
    This Function will Make a dataframe of teamRanking API
    league = String eg. 'NFL'
    It will return Pandas DataFrame of Team Ranking API
'''
def teamRankingDataframe(league):
    response = requests.get(f'https://delivery.chalk247.com/team_rankings/{league}.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0')
    response_json = response.json()
    response_df = pd.DataFrame(response_json['results']['data'])
    return response_df

'''
    This Function will Make a dataframe of Score Board API
    league = String eg. 'NFL'
    startDate = String eg: '2020-01-12'
    endDate = String eg: '2020-01-19'
    It will return Pandas DataFrame of ScoreBoard API
'''
def scoreBoardDateFrame(league, startDate, endDate):
    scoreboard_api_response = requests.get(f'https://delivery.chalk247.com/scoreboard/{league}/{startDate}/{endDate}.json?api_key=74db8efa2a6db279393b433d97c2bc843f8e32b0')
    scoreboard_json = scoreboard_api_response.json()
    score_board_df = pd.DataFrame()
    scoreboard_columns = ['event_id',
                 'event_date', 
                 'away_team_id',
                 'away_nick_name',
                 'away_city',
                 'home_team_id',
                 'home_nick_name',
                 'home_city'
                ]
    a = date(*map(int, startDate.split('-')))
    b = date(*map(int, endDate.split('-')))
    for dt in rrule(DAILY, dtstart=a, until=b):
        if isinstance(scoreboard_json['results'][dt.strftime("%Y-%m-%d")], dict):
            scoreboard_json['results'][dt.strftime("%Y-%m-%d")]['data']
            keys = list(scoreboard_json['results'][dt.strftime("%Y-%m-%d")]['data'])
            for key in keys:
                scoreboard_json['results'][dt.strftime("%Y-%m-%d")]['data'][key]
                temp = pd.DataFrame(scoreboard_json['results'][dt.strftime("%Y-%m-%d")]['data'][key], columns=scoreboard_columns, index={0})
                score_board_df = score_board_df.append(temp)
    return score_board_df

'''
    This Function will prcoess Team Ranking Dataframe and ScoreBoard DataFrame and Joing them on "Team_id"
    team_df = Pandas DataFrame eg. TeamRanking DF
    score_df = Pandas Dataframe eg ScoreBoard DF
    It will return Pandas DataFrame of Both Dataframe and give combined DF.
'''
def processData(team_df, score_df):
    merge_df = pd.merge(score_df,team_df, how='left',left_on=['away_team_id'], right_on=['team_id']).dropna()
    final_columns = ['event_id',
                 'event_date', 
                 'away_team_id',
                 'away_nick_name',
                 'away_city',
                 'rank',
                 'adjusted_points',
                 'home_team_id',
                 'home_nick_name',
                 'home_city'
                ]
    process_data = merge_df.drop(merge_df.columns.difference(final_columns), axis=1)
    process_data['event_date']= pd.to_datetime(process_data['event_date'])
    process_data['event_time'] = process_data['event_date']
    process_data['event_date'] = pd.to_datetime(process_data['event_date']).dt.date
    process_data['event_date']= pd.to_datetime(process_data['event_date'])
    process_data['event_date'] = process_data['event_date'].dt.strftime('%d-%m-%Y')
    process_data['event_time'] = pd.to_datetime(process_data['event_time']).dt.strftime('%H:%M')
    process_data['adjusted_points'] = process_data['adjusted_points'].astype(float).round(decimals=2)
    process_data.rename(columns = {'adjusted_points':'home_rank_points', 'rank':'away_rank'}, inplace = True)
    process_data['away_rank_points'] = process_data['home_rank_points']
    process_data['home_rank'] = process_data['away_rank']
    return process_data

'''
        This Function will convert the df to JSON
        It will print Json of Processed Data
'''
def teamScoreApi(team_score_df):
    list_dict = []

    for index, row in list(team_score_df.iterrows()):
        list_dict.append(dict(row))
    print(json.dumps(list_dict, indent=4))

team_dataframe = teamRankingDataframe('NFL')
score_dateframe = scoreBoardDateFrame('NFL','2020-01-12', '2020-01-19')

team_score_dataframe = processData(team_dataframe, score_dateframe)

teamScoreApi(team_score_dataframe)