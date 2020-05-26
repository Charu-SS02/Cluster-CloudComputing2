import sys
import couchdb
import json
import nltk
from fuzzywuzzy import fuzz
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize as tokenize

wordnet_lemmatizer = WordNetLemmatizer()
nltk.download('punkt')
nltk.download('wordnet')

DB_STRING = "http://group26:group26@172.26.133.189:5984/"
search_terms = ["refugee", "immigrant", "boatpeople", "stoptheboats", "foreigner", "multiculturalism"]


def main(json_file,
         db_name,
         couchdb_address):
    # 1. Create the database.. No error checking here because we want to get exception if db exists
    couch = couchdb.Server(couchdb_address)
    try:
        db = couch.create(db_name)
    except:
        db = couch[db_name]
    # # 2 Read the json line by line and put into the db
    count = 1
    with open(json_file) as jsonfile:
        for row in jsonfile:
            try:
                count = count + 1
                print(count)
                try:
                    tweet = json.loads(row[:-1])
                except:
                    tweet = json.loads(row[:-2])

                doc_id = tweet["doc"]["_id"]

                if doc_id not in db and tweet["doc"]["coordinates"] is not None:
                    text = tweet["doc"]["text"]
                    if does_tweet_match(text):
                        db[doc_id] = {"tweet": tweet}
                        print("new tweet: " + doc_id)
                    else:
                        continue
                else:
                    print("No Geo Tag or tweet in db")
            except ValueError as e:
                print("error reading line", e)
                print(row)
                continue


def does_tweet_match(text):
    for t in str.split(text):
        if t.isalpha():
            for s in search_terms:
                ratio = fuzz.ratio(s, t.lower())
                if ratio > 80:
                    print(ratio)
                    print("text match:", t)
                    return True
    print("No Match")
    return False


if __name__ == '__main__':
    print()
    "Call as <jsondb.json> <new_db> <optional db string>"
    args = sys.argv[1:]
    json_file = args[0]
    try:
        db_name = args[1]
    except:
        print("Error. No DB name provided")
    try:
        db_str = args[2]
    except:
        db_str = DB_STRING
    main(json_file,
         db_name,
         db_str)