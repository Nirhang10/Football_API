import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4c76ee90b8907726c4097ede0bc5409e'
    city = 'China'

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],  # When there is not more than one Dictionary in Arry
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    return render(request, 'improved_index_template.html', {'city_weather':city_weather})

def club_squad(request, club_id):
    API_KEY = "8fd00bba632f433da69b16ed3d09d4b0"  # Replace with your Football-Data.org key
    headers = {"X-Auth-Token": API_KEY}

    url = f"https://api.football-data.org/v4/teams/{club_id}"
    resp = requests.get(url, headers=headers)

    # If API fails, return an empty squad
    if resp.status_code != 200:
        return render(request, "improved_football.html", {"squad": [], "error": "API request failed"})

    data = resp.json()

    # For Dictionary inside Arry
    squad = data.get("squad", [])

    #To featch single data in Dictionary
    coach_info = {

        'lastname': data['coach']['lastName'],
        'nation': data['coach']['nationality'],
        'contract': f"{data['coach']['contract']['start']} -- {data['coach']['contract']['until']}",
    }

    club_info = {
        'place_name': data['area']['name'],
        'place_flag': data['area']['flag'],

        'club_name': data['shortName'],
        'club_logo': data['crest'],
        'club_venue': data['venue'],
    }

    return render(request, "improved_football.html", {"squad": squad, "error": None, 'coach':coach_info, 'club':club_info})

def match_info(request):

    url = f"https://api.football-data.org/v4/matches/"

    API_KEY = '8fd00bba632f433da69b16ed3d09d4b0'
    headers = {
        "X-Auth-Token": API_KEY
    }
    result = requests.get(url, headers=headers).json()

    match = {
        'competition': result['matches'][0]['competition']['name'],
        'logo': result['matches'][0]['competition']['emblem'],


        'first_team_home': result['matches'][0]['homeTeam']['shortName'],
        'first_team_home_logo': result['matches'][0]['homeTeam']['crest'],

        'first_away_team': result['matches'][0]['awayTeam']['shortName'],
        'first_away_team_logo': result['matches'][0]['awayTeam']['crest'],
    }

    return render(request, 'improved_match.html',{'result':result, 'match':match})

def Pl_match(request):

    matchday = 1
    url = f"https://api.football-data.org/v4/competitions/PL/matches?matchday={matchday}"

    API_KEY = '8fd00bba632f433da69b16ed3d09d4b0'
    headers = {
        "X-Auth-Token": API_KEY
    }

    result = requests.get(url, headers=headers).json()

    leauge_info = {
        'season': result['filters']['season'],
        'matchday': result['filters']['matchday'],


        'league_name': result['competition']['name'],
        'league_logo': result['competition']['emblem'],

    }


    matches = []
    for match in result['matches']:
        matches.append({
            'match_date': match['utcDate'],

            'home_team_id': match['homeTeam']['id'],
            'home_team': match['homeTeam']['shortName'],
            'home_logo': match['homeTeam']['crest'],

            'match_winner': match['score']['winner'],

            'away_team_id': match['awayTeam']['id'],
            'away_team': match['awayTeam']['shortName'],
            'away_logo': match['awayTeam']['crest'],
        })

    return render(request, 'improved_pl_match.html',{'leauge_info':leauge_info, 'matches':matches })