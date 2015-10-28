# -*- coding: utf-8 -*-
import json
import time as t
import pandas as pd
import header_analysis as h

#Headers US
url_wsj = "http://api.import.io/store/data/bec29dfb-6b35-4b48-a2a7-9d4090b04345/_query?input/webpage/url=http%3A%2F%2Fwww.wsj.com%2Fnews%2Fpolitics&_user=0aca1f14-40c5-43d7-b3ba-67afbe751631&_apikey=0aca1f1440c543d7b3ba67afbe7516311763ee2c75e5865c72ed42a6c29a96fd23c39a1c4dc92179c03c97daa3640babf81c6d42a1f079ab6cd180a8308c28974b353c0d72ae4cb53c59ae9363ef1957"
url_latimes = "http://api.import.io/store/data/7f443129-88c7-4ef4-8d58-28c20d9fa530/_query?input/webpage/url=http%3A%2F%2Fwww.latimes.com%2Fpolitics%2F&_user=0aca1f14-40c5-43d7-b3ba-67afbe751631&_apikey=0aca1f1440c543d7b3ba67afbe7516311763ee2c75e5865c72ed42a6c29a96fd23c39a1c4dc92179c03c97daa3640babf81c6d42a1f079ab6cd180a8308c28974b353c0d72ae4cb53c59ae9363ef1957"
url_nytimes = "http://api.import.io/store/data/252ea721-4ad5-4823-8913-4f3aea3e7404/_query?input/webpage/url=http%3A%2F%2Fwww.nytimes.com%2Fpages%2Fpolitics%2Findex.html%3Faction%3Dclick%26pgtype%3DHomepage%26region%3DTopBar%26module%3DHPMiniNav%26contentCollection%3DPolitics%26WT.nav%3Dpage&_user=0aca1f14-40c5-43d7-b3ba-67afbe751631&_apikey=0aca1f1440c543d7b3ba67afbe7516311763ee2c75e5865c72ed42a6c29a96fd23c39a1c4dc92179c03c97daa3640babf81c6d42a1f079ab6cd180a8308c28974b353c0d72ae4cb53c59ae9363ef1957"

#Tag header/_text
urls_media_headers = [url_wsj, url_latimes, url_nytimes]
media_headers = {'header/_text': urls_media_headers}
h.request_media(media_headers)
headers = h.get_media()

#Get time

time_now = t.strftime("%Y-%m-%d", t.gmtime())


media_headers_json = h.pollstr_analysis('julio', 'english', headers)

headers_file_json = 'politics-' + time_now + '.json'

with open(headers_file_json, 'w') as digital_outfile:
    json.dump(media_headers_json, digital_outfile)
