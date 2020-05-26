from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
from flaskr.scenario1 import *
from flaskr.scenario2 import *

blueprint = Blueprint('main', __name__, url_prefix='/main')
    
@blueprint.route('/scenario1', methods=['GET'])
def scenario1():
    data = get_scenario1_json()

    return render_template('visualization/scenario1.html', data=data)

@blueprint.route('/scenario2', methods=['GET'])
def scenario2():
    data = get_scenario2_json()

    categories = []
    eng_prof_y = []
    eng_prof_n = []
    foreign_tweet = []

    for key, val in data.items():
        categories.append(val['state_abbr'])
        eng_prof_y.append(val['english_proficiency_%_for_proficient'])
        eng_prof_n.append(val['english_proficiency_%_for_non_proficient'])
        foreign_tweet.append(val['foreign_tweet_%'])

    data = {
        'categories': categories,
        'eng_prof_y': eng_prof_y,
        'eng_prof_n': eng_prof_n,
        'foreign_tweet': foreign_tweet
    }

    return render_template('visualization/scenario2.html', data=data)
