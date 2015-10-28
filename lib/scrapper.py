import json
import requests
import pandas as pd

class scrapper:
    def __init__(self):
        self.headers = []

    def request_headers(self, url, tag):
        r = requests.get(url)
        data = json.loads(r.text)
        number_of_results = len(data['results'])

        for result in range(number_of_results):
            try:
                type_of_header = type(data['results'][result][tag])

                if type_of_header == type([]):
                    number_of_headers = len(data['results'][result][tag])

                    for header in range(number_of_headers):
                        try:
                            text = data['results'][result][tag][header]
#                            encoded_header = text.encode('utf-8')
                            self.headers.append(encoded_header)

                        except:
                            pass

                else:
                    try:
                        text = data['results'][result][tag]
                        encoded_header = text.encode('utf-8')
                        self.headers.append(encoded_header)

                    except:
                        pass

            except:
                pass

    def get_headers(self):
        return self.headers

    def get_csv(self, name_of_file):
        csv = pd.DataFrame({'text': self.headers})
        name = name_of_file + '.csv'
        csv.to_csv(name)
