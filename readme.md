## Build Setup

``` bash
# Clone the repo
git clone https://github.com/rishabh-90/nfl-dataprocessing.git

# navigate to project folder
cd <project-folder>

#Create Virtual Env for python3
virtualenv venv --python=python3.6

#Activate Virtual Environment
source venv/bin/activate

#Instsll Packages
pip install -r install.txt

#Run the Solution
python solution.py

# Output of solution.py
http://0.0.0.0:5000/
[
    {
        "event_id": "1233827",     
        "event_date": "12-01-2020",
        "away_team_id": "42",      
        "away_nick_name": "Texans",
        "away_city": "Houston",    
        "home_team_id": "63",      
        "home_nick_name": "Chiefs",
        "home_city": "Kansas City",
        "away_rank": "21",
        "home_rank_points": -6.0,
        "event_time": "15:05",
        "away_rank_points": -6.0,
        "home_rank": "21"
    },
    {
        "event_id": "1233912",
        "event_date": "12-01-2020",
        "away_team_id": "52",
        "away_nick_name": "Seahawks",
        "away_city": "Seattle",
        "home_team_id": "39",
        "home_nick_name": "Packers",
        "home_city": "Green Bay",
        "away_rank": "19",
        "home_rank_points": -3.42,
        "event_time": "18:40",
        "away_rank_points": -3.42,
        "home_rank": "19"
    },
    {
        "event_id": "1234560",
        "event_date": "19-01-2020",
        "away_team_id": "62",
        "away_nick_name": "Titans",
        "away_city": "Tennessee",
        "home_team_id": "63",
        "home_nick_name": "Chiefs",
        "home_city": "Kansas City",
        "away_rank": "7",
        "home_rank_points": 10.75,
        "event_time": "15:05",
        "away_rank_points": 10.75,
        "home_rank": "7"
    },
    {
        "event_id": "1234565",
        "event_date": "19-01-2020",
        "away_team_id": "39",
        "away_nick_name": "Packers",
        "away_city": "Green Bay",
        "home_team_id": "58",
        "home_nick_name": "49ers",
        "home_city": "San Francisco",
        "away_rank": "12",
        "home_rank_points": 5.05,
        "event_time": "18:40",
        "away_rank_points": 5.05,
        "home_rank": "12"
    }
]

## Docker Setup

``` bash
# Clone the repo
git clone https://github.com/rishabh-90/nfl-dataprocessing.git

# navigate to project folder
cd <project-folder>

# Run Docker Compose
docker-compose up --build

# Navigate to Browser
http://0.0.0.0:5000/