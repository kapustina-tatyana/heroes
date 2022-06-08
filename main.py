
import requests
from pprint import pprint
import os

api_token = os.getenv("api_token")
api_url = 'https://superheroapi.com/api/2619421814940190/'
heroes = ['Hulk', 'Captain America', 'Thanos']


def intelligence_rate(name):
    url = f"{api_url}search/{name}"
    response = requests.get(url)

    resp = response.json()['results']

    for hero_characters in resp:
        name_hero = hero_characters['name']
        id_hero = hero_characters['id']
        intelig = hero_characters['powerstats']['intelligence']
        hero_dict = {'name': name_hero, 'id':id_hero,'intelligence':intelig}
        if name == name_hero:
            char_hero = hero_dict
    return char_hero

def intelligence_list(intel_list):
    intel_top = 0
    for hero in intel_list:
        name_h = hero
        inteligence_hero = int(intelligence_rate(name_h)['intelligence'])
        if inteligence_hero > intel_top:
            intel_top = inteligence_hero
            inteligence_top = intelligence_rate(name_h)


    return inteligence_top

if __name__ == '__main__':
    top_hero = intelligence_list(heroes)
    top_name = top_hero['name']
    top_id = top_hero['id']
    top_intel = top_hero['intelligence']
    print(f"Из списка {', '.join(heroes)}, самым большим интеллектом {top_intel} обладает {top_name} с id {top_id}")



