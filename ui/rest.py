from flask import Flask, request, render_template, jsonify
import json
from bson import json_util
from bson.objectid import ObjectId
from pymongo import MongoClient
import csv
import pickle
import random

# Flask
app = Flask(__name__ , template_folder='templates')

# MongoDB connection
connection = MongoClient('localhost', 27017)
db = connection.findb

'''
@app.route('/', methods=['GET'])
def toJson(data):
    print(data)
    """Convert Mongo object(s) to JSON"""
    json_object = json.dumps(data, default=json_util.default)
    return render_template('test1.html', s_data=json_object)
    #return json.dumps(data, default=json_util.default)
'''
'''
@app.route('/sightings/<sighting_id>', methods=['GET'])
def sighting(sighting_id):
  """Return specific UFO sighting
  ex) GET /sightings/123456
  """
  if request.method == 'GET':
    result = db['collection'].find_one({'imp_desc@6pm': sighting_id})
    return toJson(result)
'''

@app.route('/', methods=['POST'])
def my_form_post():



    text = request.form['text']

    user_id = random.randint(1,943)
    rec_items = db['recommend'].find({'user_id':user_id})
    past_hist = db['history'].find({'user_id':user_id})
    print(user_id)

    result = db['za_eb_6pm'].find({'imp_desc@6pm': text})
    brand = db['za_eb_6pm'].find({'imp_desc@6pm': text}, {'brand@6pm':1,'_id':0})
    if result.count()==0:
        result = db['za_eb_6pm'].find({'imp_desc@eastbay': text})
        brand = db['za_eb_6pm'].find({'imp_desc@eastbay': text}, {'brand@6pm':1,'_id':0})
        if result.count()==0:
            result = db['za_eb_6pm'].find({'imp_desc@zappos': text})
            brand = db['za_eb_6pm'].find({'imp_desc@zappos': text}, {'brand@6pm':1,'_id':0})
            if result.count()==0:
                result = db['6pm_za'].find({'imp_desc@zappos': text})
                brand = db['6pm_za'].find({'imp_desc@zappos': text}, {'brand@6pm':1,'_id':0})
                if result.count()==0:
                    result = db['6pm_za'].find({'imp_desc@6pm': text})
                    brand = db['6pm_za'].find({'imp_desc@6pm': text}, {'brand@6pm':1,'_id':0})
                    if result.count()==0:
                        result = db['eb_6pm'].find({'imp_desc@eastbay': text})
                        brand = db['eb_6pm'].find({'imp_desc@eastbay': text}, {'brand@6pm':1,'_id':0})
                        if result.count()==0:
                            result = db['eb_6pm'].find({'imp_desc@6pm': text})
                            brand = db['eb_6pm'].find({'imp_desc@6pm': text}, {'brand@6pm':1,'_id':0})
                            if result.count()==0:
                                result = db['za_eb'].find({'imp_desc@zappos': text})
                                bramd = db['za_eb'].find({'imp_desc@zappos': text}, {'brand@6pm':1,'_id':0})
                                if result.count()==0:
                                    result = db['za_eb'].find({'imp_desc@eastbay': text})
                                    brand = db['za_eb'].find({'imp_desc@eastbay': text}, {'brand@6pm':1,'_id':0})
                                    #if result is None:
                                    #    result = db['6pm'].find({'imp_desc@6pm': text})
                                    #    if result is None:
                                    #       result = db['zappos'].find({'improved_description@zappos': text})
                                    #        if result is None:
                                    #            result = db['eastbay'].find({'improved_description@eastbay': text})

    dc = {}
    count = 0
    #print(brand[0])
    for d in result:
        #print(d)
        dc[count] = d
        count += 1
    rec_res = {}
    count = 0

    for item in rec_items:
        res = db['za_eb_6pm'].find_one({'product_id': item['product_id']})
        rec_res[count] = res
        count += 1

    past_res = {}
    count = 0
    for item in past_hist:
        res = db['za_eb_6pm'].find_one({'product_id': item['product_id']})
        past_res[count] = res
        count += 1

    bigjson = {}
    bigjson['recommend'] = rec_res
    bigjson['results'] = dc
    bigjson['past_history'] = past_res
    #print("NJNNJ")
    #print(bigjson)
    #json_object = json.dumps(dc, default=json_util.default)
    json_object = json.dumps(bigjson, default=json_util.default)
    return render_template('test1.html', s_data=json_object)

# Route to home page
#@app.route('/', methods=['GET', 'POST'])
#@app.route('/home', methods=['GET', 'POST'])
@app.before_first_request
@app.route('/', methods=['GET', 'POST'])
def show_home():
    with open('src.pickle','rb')as f:
        src = pickle.load(f)
    return render_template('index.html', data=json.dumps(src))
    #return jsonify(json_list = src)

if __name__ == '__main__':
  app.run(debug=True)