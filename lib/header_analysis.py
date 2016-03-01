import json
import requests
import scrapper as s

pollstr_url = 'http://pollstr.io:8080/api/explore/cluster/'

s = s.scrapper()

def request_media(media_tag_dictionary):
    tag = media_tag_dictionary.keys()[0]
    urls = media_tag_dictionary[tag]

    for url in urls:
        try:
            s.request_headers(url, tag)

        except:
            pass

def get_media():

    return s.get_headers()

def pollstr_analysis(username, language, media):

    data_cluster = {'username': username, 'language': language}
    data_to_analyze = {'data': data_cluster, 'text': media, 'to_remove': []}

    data_to_analyze = json.dumps(data_to_analyze)

    r = requests.post(url = pollstr_url, data = data_to_analyze)

    result = json.loads(r.text)

    return result
