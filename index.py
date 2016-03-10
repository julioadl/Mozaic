from flask import Flask, render_template, redirect
import json
import urllib
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('howto.html')

@app.route('/<date>')
def get_from_date(date):

    try:
        open_s3 = urllib.URLopener()
        headlines_name_file = 'https://pollstr.s3.amazonaws.com/pollstr/Datasets/Text/News/Headlines/US/headers-' + str(date) + '.json'
        headlines_cluster_file = open_s3.open(headlines_name_file)
        headlines_cluster_dict = json.loads(headlines_cluster_file.read())

        world_name_file = 'https://pollstr.s3.amazonaws.com/pollstr/Datasets/Text/News/World/US/world-' + str(date) + '.json'
        world_cluster_file = open_s3.open(world_name_file)
        world_cluster_dict = json.loads(world_cluster_file.read())

        politics_name_file = 'https://pollstr.s3.amazonaws.com/pollstr/Datasets/Text/News/Politics/US/politics-' + str(date) + '.json'
        politics_cluster_file = open_s3.open(politics_name_file)
        politics_cluster_dict = json.loads(politics_cluster_file.read())

        clusters = {}

        for topic in headlines_cluster_dict['clusters']:
            tag = "headlines-" + str(topic)
            clusters[tag] = headlines_cluster_dict['clusters'][topic]

        for topic in world_cluster_dict['clusters']:
            tag = "world-" + str(topic)
            clusters[tag] = world_cluster_dict['clusters'][topic]

        for topic in politics_cluster_dict['clusters']:
            tag = "politics-" + str(topic)
            clusters[tag] = politics_cluster_dict['clusters'][topic]

        return render_template('index.html', date=date, clusters=clusters)

    except:
        return render_template('error.html')

@app.route('/data/<date>')
def get_data_from_date(date):

    try:
        json_file = {}
        open_s3 = urllib.URLopener()

        json_file['name'] = 'News'

        #Headlines

        name_file = 'https://pollstr.s3.amazonaws.com/pollstr/Datasets/Text/News/Headlines/US/headers-' + str(date) + '.json'
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
            child['cluster'] = 'headlines-' + str(topic)
            children.append(child)
            total_count.append(clusters[topic]['count'])

        headlines['children'] = children
        headlines['value'] = np.sum(total_count)

        #MWorld

        name_file = 'https://pollstr.s3.amazonaws.com/pollstr/Datasets/Text/News/World/US/world-' + str(date) + '.json'
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
            child['cluster'] = 'world-' + str(topic)
            children.append(child)
            total_count.append(clusters[topic]['count'])

        world['children'] = children
        world['value'] = np.sum(total_count)

        #Politics

        name_file = 'https://pollstr.s3.amazonaws.com/pollstr/Datasets/Text/News/Politics/US/politics-' + str(date) + '.json'
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
            child['cluster'] = 'politics-' + str(topic)
            children.append(child)
            total_count.append(clusters[topic]['count'])

        politics['children'] = children
        politics['value'] = np.sum(total_count)

        #Append two clusters to json

        json_file['children'] = [headlines, world, politics]
        json_file['value'] = np.sum([headlines['value'], world['value'], politics['value']])

        json_file = json.dumps(json_file)

        return json_file

    except:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug = False)
