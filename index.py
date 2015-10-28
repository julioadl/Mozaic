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

    json_file['name'] = 'News'

    #Headlines

    name_file = 'https://pollstr.s3.amazonaws.com/pollstr/News/headers-' + str(date) + '.json'
    cluster_file = open_s3.open(name_file)
    clusters = json.load(cluster_file)
    clusters = clusters['clusters']

    headlines = {}

    headlines['name'] = "Headlines"

    children = []
    total_count = []

    for topic in clusters:
        child = {}
        child['name'] = clusters[topic]['topics']
        child['value'] = clusters[topic]['count']
        children.append(child)
        total_count.append(clusters[topic]['count'])

    headlines['children'] = children
    headlines['value'] = np.sum(total_count)

    #MWorld

    name_file = 'https://pollstr.s3.amazonaws.com/pollstr/News/world-' + str(date) + '.json'
    cluster_file = open_s3.open(name_file)
    clusters = json.load(cluster_file)
    clusters = clusters['clusters']

    world = {}

    world['name'] = "World"

    children = []
    total_count = []

    for topic in clusters:
        child = {}
        child['name'] = clusters[topic]['topics']
        child['value'] = clusters[topic]['count']
        children.append(child)
        total_count.append(clusters[topic]['count'])

    world['children'] = children
    world['value'] = np.sum(total_count)

    #Politics

    name_file = 'https://pollstr.s3.amazonaws.com/pollstr/News/politics-' + str(date) + '.json'
    cluster_file = open_s3.open(name_file)
    clusters = json.load(cluster_file)
    clusters = clusters['clusters']

    politics = {}

    politics['name'] = "Politics"

    children = []
    total_count = []

    for topic in clusters:
        child = {}
        child['name'] = clusters[topic]['topics']
        child['value'] = clusters[topic]['count']
        children.append(child)
        total_count.append(clusters[topic]['count'])

    politics['children'] = children
    politics['value'] = np.sum(total_count)

    #Append two clusters to json

    json_file['children'] = [headlines, world, politics]
    json_file['value'] = np.sum([headlines['value'], world['value'], politics['value']])

    json_file = json.dumps(json_file)

    return json_file

if __name__ == '__main__':
    app.run(debug = True)
