from datetime import datetime, date
import requests
from django.shortcuts import render

# Create your views here.

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4c76ee90b8907726c4097ede0bc5409e'
    city = 'Nepal'

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city' : city,
        'temperature' : r['main']['temp'],  # When there is not more than one Dictionary in Arry
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    return render(request, 'Weather.html', {'city_weather':city_weather})

def club_squad(request, club_id):
    API_KEY = "8fd00bba632f433da69b16ed3d09d4b0"  # Replace with your Football-Data.org key
    headers = {"X-Auth-Token": API_KEY}

    url = f"https://api.football-data.org/v4/teams/{club_id}"
    resp = requests.get(url, headers=headers)

    # If API fails, return an empty squad
    if resp.status_code != 200:
        return render(request, "Club.html", {"squad": [], "error": "API request failed"})

    data = resp.json()

    

    # For Dictionary inside Arry
    squad = data.get("squad", [])

    #To featch single data in Dictionary
    coach_info = {
        'name': data['coach']['name'],
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

    return render(request, "Club.html", {"squad": squad, "error": None, 'coach':coach_info, 'club':club_info})

def player_info(request, player_id):

    url = f"https://api.football-data.org/v4/persons/{player_id}"

    headers = {
    'X-Auth-Token': '8fd00bba632f433da69b16ed3d09d4b0'
    }

    response = requests.get( url, headers=headers).json()
    

    player_data = {
        'id': response['id'],
        'name': response['name'],
        'DOB': response['dateOfBirth'],
        

        'nation': response['nationality'],
        'position': response['position'],
        'shirtnumber': response['shirtNumber'],


        'current_team': response['currentTeam']['shortName'],
        'current_team_id': response['currentTeam']['id'],
        'current_team_color': response['currentTeam']['clubColors'],
        'current_team_logo': response['currentTeam']['crest'],
        'current_team_website': response['currentTeam']['website'],
        'current_team_venue': response['currentTeam']['venue'],

        'Competitions': response['currentTeam']['runningCompetitions'][0]['name'],
        'Competitions_logo': response['currentTeam']['runningCompetitions'][0]['emblem'],

        'contract': f"{response['currentTeam']['contract']['start']}/{response['currentTeam']['contract']['until']}"
    }
    # AGE logic 
    dob_str = response['dateOfBirth']
    dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    ####***####


    currentTeam = response.get('currentTeam')

    competition = currentTeam.get('runningCompetitions')




    return render(request, 'player_info.html',{'player_data':player_data, 'player_id':player_id, 'competition':competition, 'age':age})



def live_match_info(request):

    url = f"https://api.football-data.org/v4/matches/"

    API_KEY = '8fd00bba632f433da69b16ed3d09d4b0'
    headers = {
        "X-Auth-Token": API_KEY
    }
    result = requests.get(url, headers=headers).json()


    live_match = []
    for live in result['matches']:
        live_match.append({
            'name': live['competition']['name'],
            'logo': live['competition']['emblem'],
            'type': live['competition']['type'],

            'Date': live['utcDate'],
            'Day': live['matchday'],


            'home_team_id': live['homeTeam']['id'],
            'home_team': live['homeTeam']['shortName'],
            'home_logo': live['homeTeam']['crest'],

            'match_winner': live['score']['winner'],

            'away_team_id': live['awayTeam']['id'],
            'away_team': live['awayTeam']['shortName'],
            'away_logo': live['awayTeam']['crest'],


        })


    return render(request, 'live_match.html',{'result':result, 'live_match':live_match,})

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

    return render(request, 'pl_match.html',{'leauge_info':leauge_info, 'matches':matches })