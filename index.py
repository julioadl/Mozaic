from flask import Flask, render_template
import json
import urllib
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/<date>')
def get_from_date(date):
    return render_template('index.html', date=date)

@app.route('/data/<date>')
def get_data_from_date(date):

    json_file = {}
    open_s3 = urllib.URLopener()

    json_file['name'] = 'Noticias'

    #Medios Tradicionales

    name_file = 'https://pollstr.s3.amazonaws.com/pollstr/Factico/JSON/printed-' + str(date) + '.json'
    cluster_file = open_s3.open(name_file)
    clusters = json.load(cluster_file)
    clusters = clusters['clusters']

    medios_tradicionales = {}

    medios_tradicionales['name'] = "Medios Tradicionales"

    children = []
    total_count = []

    for topic in clusters:
        child = {}
        child['name'] = clusters[topic]['topics']
        child['value'] = clusters[topic]['count']
        children.append(child)
        total_count.append(clusters[topic]['count'])

    medios_tradicionales['children'] = children
    medios_tradicionales['value'] = np.sum(total_count)

    #Medios Digitales

    name_file = 'https://pollstr.s3.amazonaws.com/pollstr/Factico/JSON/digital-' + str(date) + '.json'
    cluster_file = open_s3.open(name_file)
    clusters = json.load(cluster_file)
    clusters = clusters['clusters']

    medios_digitales = {}

    medios_digitales['name'] = "Medios Digitales"

    children = []
    total_count = []

    for topic in clusters:
        child = {}
        child['name'] = clusters[topic]['topics']
        child['value'] = clusters[topic]['count']
        children.append(child)
        total_count.append(clusters[topic]['count'])

    medios_digitales['children'] = children
    medios_digitales['value'] = np.sum(total_count)

    #Append two clusters to json

    json_file['children'] = [medios_digitales, medios_tradicionales]
    json_file['value'] = medios_digitales['value'] + medios_tradicionales['value']

    json_file = json.dumps(json_file)

    return json_file

if __name__ == '__main__':
    app.run(debug = True)
