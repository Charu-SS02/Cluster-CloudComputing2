import json

def get_scenario2_json():
    project_dir = '/var/www/front-end/'

    with open(project_dir + 'data/ABS_-_Data_by_Region_-_Persons_Born_Overseas__GCCSA__2011-2016.json/data8507207769147032238.json') as file:
        data = json.load(file)

    temp = [(d['properties']['gcc_code16'], d['properties']['eng_prof_p_brn_ovs_proficient_eng_pr100'], d['properties']['eng_prof_p_brn_ovs_no_proficient_eng_pr100'], d['properties']['pop_p_brn_ovs_tot_pop_num']) for d in data['features']]
    nsw = [t for t in temp if '1' in t[0]]
    vic = [t for t in temp if '2' in t[0]]
    qld = [t for t in temp if '3' in t[0]]
    sau = [t for t in temp if '4' in t[0]]
    wau = [t for t in temp if '5' in t[0]]
    tas = [t for t in temp if '6' in t[0]]
    nte = [t for t in temp if '7' in t[0]]
    act = [t for t in temp if '8' in t[0]]

    with open(project_dir + 'data/total-tweets-per-state.json', encoding='utf-8') as file:
        total_tweet_count = json.load(file)

    with open(project_dir + 'data/foreign-tweets-per-state.json', encoding='utf-8') as file:
        foreign_tweet_count = json.load(file)

    data = {
        'New South Wales': {
            'state_abbr': "NSW",
            'overseas_population': sum([t[3] for t in nsw]),
            'english_proficiency_%_for_proficient': float('{:.2f}'.format(sum([t[1] * t[3] for t in nsw]) / sum([t[3] for t in nsw]))),
            'english_proficiency_%_for_non_proficient': float('{:.2f}'.format(sum([t[2] * t[3] for t in nsw]) / sum([t[3] for t in nsw]))),
            'foreign_tweet_%': 0.0
        },
        'Victoria': {
            'state_abbr': "VIC",
            'overseas_population': sum([t[3] for t in vic]),
            'english_proficiency_%_for_proficient': float('{:.2f}'.format(sum([t[1] * t[3] for t in vic]) / sum([t[3] for t in vic]))),
            'english_proficiency_%_for_non_proficient': float('{:.2f}'.format(sum([t[2] * t[3] for t in vic]) / sum([t[3] for t in vic]))),
            'foreign_tweet_%': 0.0
        },
        'Queensland': {
            'state_abbr': "QLD",
            'overseas_population': sum([t[3] for t in qld]),
            'english_proficiency_%_for_proficient': float('{:.2f}'.format(sum([t[1] * t[3] for t in qld]) / sum([t[3] for t in qld]))),
            'english_proficiency_%_for_non_proficient': float('{:.2f}'.format(sum([t[2] * t[3] for t in qld]) / sum([t[3] for t in qld]))),
            'foreign_tweet_%': 0.0
        },
        'Western Australia': {
            'state_abbr': "WA",
            'overseas_population': sum([t[3] for t in wau]),
            'english_proficiency_%_for_proficient': float('{:.2f}'.format(sum([t[1] * t[3] for t in wau]) / sum([t[3] for t in wau]))),
            'english_proficiency_%_for_non_proficient': float('{:.2f}'.format(sum([t[2] * t[3] for t in wau]) / sum([t[3] for t in wau]))),
            'foreign_tweet_%': 0.0
        },
        'South Australia': {
            'state_abbr': "SA",
            'overseas_population': sum([t[3] for t in sau]),
            'english_proficiency_%_for_proficient': float('{:.2f}'.format(sum([t[1] * t[3] for t in sau]) / sum([t[3] for t in sau]))),
            'english_proficiency_%_for_non_proficient': float('{:.2f}'.format(sum([t[2] * t[3] for t in sau]) / sum([t[3] for t in sau]))),
            'foreign_tweet_%': 0.0
        },
        'Tasmania': {
            'state_abbr': "TAS",
            'overseas_population': sum([t[3] for t in tas]),
            'english_proficiency_%_for_proficient': float('{:.2f}'.format(sum([t[1] * t[3] for t in tas]) / sum([t[3] for t in tas]))),
            'english_proficiency_%_for_non_proficient': float('{:.2f}'.format(sum([t[2] * t[3] for t in tas]) / sum([t[3] for t in tas]))),
            'foreign_tweet_%': 0.0
        },
        'Northern Territory': {
            'state_abbr': "NT",
            'overseas_population': sum([t[3] for t in nte]),
            'english_proficiency_%_for_proficient': float('{:.2f}'.format(sum([t[1] * t[3] for t in nte]) / sum([t[3] for t in nte]))),
            'english_proficiency_%_for_non_proficient': float('{:.2f}'.format(sum([t[2] * t[3] for t in nte]) / sum([t[3] for t in nte]))),
            'foreign_tweet_%': 0.0
        },
        'Australian Capital Territory': {
            'state_abbr': "ACT",
            'overseas_population': sum([t[3] for t in act]),
            'english_proficiency_%_for_proficient': float('{:.2f}'.format(sum([t[1] * t[3] for t in act]) / sum([t[3] for t in act]))),
            'english_proficiency_%_for_non_proficient': float('{:.2f}'.format(sum([t[2] * t[3] for t in act]) / sum([t[3] for t in act]))),
            'foreign_tweet_%': 0.0
        },
    }

    for key, val in data.items():
        if key != 'Australian Capital Territory':
            val['foreign_tweet_%'] = float('{:.2f}'.format(100 * foreign_tweet_count[key] / total_tweet_count[key])) if total_tweet_count[key] else float('{:.2f}'.format(0.0))

    return data
