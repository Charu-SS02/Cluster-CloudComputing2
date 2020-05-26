import json


def get_scenario1_json():
    project_dir = '/var/www/front-end/'

    feature_list = []
    states_list = ['New South Wales', 'Victoria', 'Queensland', 'South Australia', 'Western Australia', 'Tasmania', 'Northern Territory', 'Australian Capital Territory']
    states_abbr = ['NSW', 'VIC', 'QLD', 'SA', 'WA', 'TAS', 'NT', 'ACT']

    with open(project_dir + 'data/total-tweets-per-state.json', encoding='utf-8') as file:
        total_tweet_count = json.load(file)

    with open(project_dir + 'data/foreign-tweets-per-state.json', encoding='utf-8') as file:
        foreign_tweet_count = json.load(file)

    with open(project_dir + 'data/state-coordinates.json', encoding='utf-8') as file:
        coordinates = json.load(file)

    with open(project_dir + 'data/total-tweets-per-state.json', encoding='utf-8') as file:
        total_tweet_count = json.load(file)

    with open(project_dir + 'data/total-tweets-per-state-and-languages.json', encoding='utf-8') as file:
        tweet_lang_count = json.load(file)

    with open(project_dir + 'data/ABS_-_Data_by_Region_-_Persons_Born_Overseas__GCCSA__2011-2016.json/data8507207769147032238.json') as file:
        data = json.load(file)

    temp = [(d['properties']['gcc_code16'], d['properties']['eng_prof_p_brn_ovs_proficient_eng_pr100'], d['properties']['eng_prof_p_brn_ovs_no_proficient_eng_pr100'], d['properties']['pop_p_brn_ovs_tot_pop_num']) for d in data['features']]

    ctr = 1
    for state in states_list:
        state_population_data = [t for t in temp if f'{ctr}' in t[0]]

        geometry_type = 'Polygon' if state == 'Australian Capital Territory' else 'MultiPolygon'

        if state == 'Australian Capital Territory':
            total_tweet_count[state] = 0
            foreign_tweet_count[state] = 0
            tweet_lang_count[state] = 'N/A (0 tweets)'

        feature = {
            'type': 'Feature',
            'id': ctr,
            'geometry': {
                'type': geometry_type,
                'coordinates': coordinates[state]
            },
            'properties': {
                'state_id': ctr,
                'state_name': state,
                'state_abbr': states_abbr[ctr - 1],
                'total_tweet_count': total_tweet_count[state],
                'foreign_language_tweet_count': foreign_tweet_count[state],
                'most_tweeted_foreign_language': f'{tweet_lang_count[state][0]} ({tweet_lang_count[state][1]} tweets)',
                'overseas_population': sum([t[3] for t in state_population_data]),
                'immigrants_proficient_in_English': float('{:.2f}'.format(sum([t[1] * t[3] for t in state_population_data]) / sum([t[3] for t in state_population_data]))),
                'immigrants_non_proficient_in_English': float('{:.2f}'.format(sum([t[2] * t[3] for t in state_population_data]) / sum([t[3] for t in state_population_data])))
            }
        }

        feature_list.append(feature)
        ctr += 1

    data = {
        'type': 'FeatureCollection',
        'features': feature_list
    }

    with open(project_dir + 'data/statesData.geojson', 'w') as output:
        json.dump(data, output)

    return data
