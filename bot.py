from ufo_scraper import get_ufos
import requests

def bot(location):
    ufos = get_ufos()
    sufos = sorted(ufos, key=lambda u: u['date'], reverse=True)
    latest_ufo = sufos[0]

    make_story(location, latest_ufo)

def make_locator_map(starting_location, ending_location):
    base_endpoint = 'https://maps.googleapis.com/maps/api/staticmap'
    myparams = {}
    myparams['size'] = '600x400'
    myparams['markers'] = []
    myparams['markers'].append('color:purple|' + starting_location)
    myparams['markers'].append('color:red|' + ending_location)

    preq = requests.PreparedRequest()
    preq.prepare_url(base_endpoint, myparams)

    return preq.url

def make_story(user_location, ufo):
    storytemplate = """On {date}, a {shape} shape UFO was seen near {place}. The report includes the following summary: {summary}. \n Here is where {user_location} is in relation to the UFO:
    {url}"""

    google_map_url = make_locator_map(user_location, ufo['location'])
    story = storytemplate.format(date=ufo['date'], shape=ufo['shape'], place=ufo['location'], url=google_map_url, user_location=user_location, summary=ufo['summary'])

    print(story.strip())
