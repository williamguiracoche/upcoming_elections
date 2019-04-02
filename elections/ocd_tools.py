import requests
from elections.us_states import postal_abbreviations
import json

def create_url(state, city):
    ''' Takes in state(str) and city (str) and creates a custom 
        url to draw from the Democracy Works public API'''

    state_str = state.lower() #use lowercase for url
    city_str = (city.lower()).replace(' ', '_') #use lowercase for url and replace spaces with underscores
 
    url = 'https://api.turbovote.org/elections/upcoming?district-divisions=ocd-division/country:us/state:%s,ocd-division/country:us/state:%s/place:%s' \
        % (state_str, state_str, city_str)
    return url

def get_json(state, city):
    ''' Takes in state(str) and city (str) and returns 
        the JSON file with information '''

    url = create_url(state, city)
    headers = {"Accept": "application/json"} #Makes url response return JSON format instead of default EDN format
    data = requests.get(url, headers=headers)
    
    json_data = json.loads(data.text)

    if not json_data:
        return None

    # To view JSON data received, uncomment below:
    # print(json_data[0])

    # To view description of election, uncomment below:
    #print(json_data[0]['description'])
    return json_data[0]

def get_description(state, city):
    ''' Takes state(str) and city (str) and outputs the description of the upcoming election'''
    data = get_json(state, city)
    description = data['description']
    return description

def get_website(state, city):
    ''' Takes state(str) and city (str) and outputs the website for the upcoming election'''

    data = get_json(state, city)
    website = data['website']
    return website

def get_polling_place_url(state, city):
    ''' Takes state(str) and city (str) and outputs the url for the poll locator'''

    data = get_json(state, city)
    polling_place_url = data['polling-place-url']
    return polling_place_url

def get_polling_place_url_shortened(state,city):
    ''' Takes state(str) and city (str) and outputs the shortened url for the poll locator'''

    data = get_json(state, city)
    polling_place_url_shortened = data['polling-place-url-shortened']
    return polling_place_url_shortened

def get_date(state, city):
    ''' Takes state(str) and city (str) and outputs the date for the upcoming election'''

    data = get_json(state, city)
    date = data['date']
    return date

def get_all(state, city):
    ''' Takes state(str) and city (str) to output an array of informatino about the upcoming election.
        Output: [website, polling_place_url, description, date]

        Recommend using this function isntead of the functions to get individual values so that you
        don't keep requesting the data from the public API for each value
     '''
    data = get_json(state, city)
    
    if data:

        # Try to store the variables. 
        # If the variable is not in the JSON data (KeyError)
        # the variable should be set to None.
        try:
            website = data['website']
        except KeyError:
            website = None

        try:
            polling_place_url = data['polling-place-url']
        except KeyError:
            website = None

        try: 
            description = data['description']
        except KeyError:
            description = None
        
        try:
            date = data['date']
        except KeyError:
            description = None
        
        all_info = [website, polling_place_url, description, date]
        return all_info
    else:
        print('No upcoming elections here')
        return None