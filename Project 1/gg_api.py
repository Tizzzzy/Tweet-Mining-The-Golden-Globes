'''Version 0.4'''

# ============================================ Imports ====================================================
import pandas as pd
import numpy as np
import re
import emoji
import nltk
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from imdb import IMDb
from nltk import pos_tag
import rapidfuzz
from bing_image_downloader import downloader
from global_var import *
from util import *

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download("popular")
nltk.download("maxent_ne_chunker")
nltk.download("words")

global df

# ============================================= Functions ====================================================

def get_hosts(year):
    '''Hosts is a list of one or more strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    df = process_json(year)
    df['text'] = df['text'].apply(remove_stopwords)
    tweets = df['text']
    common_names = []
    for tweet in tweets:
        if re.findall(r"\s[hH]osted?",tweet):
            common_names.extend(extract_name(tweet))
    top = nltk.FreqDist(common_names).most_common(5)
    hosts = [''.join(top[0][0]), ''.join(top[1][0])]          
    print("========================== Get Hosts Finished ================================")
    return hosts

    
   
def get_awards(year):
    '''Awards is a list of strings. Do NOT change the name
    of this function or what it returns.'''
    # Your code here
    df = process_json(year)
    df['text'] = df['text'].apply(remove_stopwords)
    df['award_pairs'] = df['text'].apply(match_pattern)
    award_unique = df['award_pairs'].unique()
    awards = print_award(award_unique)
    print("=========================== Get Awards Finished ==============================")
    return awards 


def get_nominees(year):
    '''Nominees is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change
    the name of this function or what it returns.'''
    # Your code here
    df = process_json(year)
    df['processed'] = df['text'].apply(tweet_preprocess)
    tweets = df.processed.to_list()
    extra_award = dict()
    fresh_names = dict()
    nominees = dict()
    nominee_names = dict()
    for award in OFFICIAL_AWARDS:
        fresh_names[award] = [[item for item in award.split() if not item in TO_DELETE]]
        extra_award[award] = []
        extra_award[award].append(award)
    altAwardName(OFFICIAL_AWARDS, extra_award, fresh_names)
    tweet_by_award_dict = getTweetByAward(OFFICIAL_AWARDS, fresh_names, tweets)
    
    for key, value in tweet_by_award_dict.items():
        value = list(set(value))
        for i in range(len(value)):
            value[i] = re.sub(WHITE_SPACE, ' ', value[i])
            value[i] = re.sub(SINGLE_CHAR, ' ', value[i])
        value = list(set(value))
        tweet_by_award_dict[key] = value
        
        
    for key, value in tweet_by_award_dict.items():
        i = len(value) - 1
        while i >= 0:
            if any(nom_word in value[i] for nom_word in NOMINATION_WORDS):
                words = value[i].split()
                value[i] = ' '.join(['' if word.lower() in AWARD_STOPLIST else word for word in words])
            else:
                value.pop(i)
            i -= 1
    for award in OFFICIAL_AWARDS:
        nominees[award]=[]
        nominee_names[award]=[]
        
    nominee = {}
    # ia = IMDb(accessSystem='http', reraiseExceptions=True)
    for key, value in tweet_by_award_dict.items():
        nominee[key] = {}
        if any([kw in key for kw in PERSON_AWARD]):
            for tweet in value:
                if any([kw in tweet for kw in PERSON_AWARD]):   
                    tweet = tweet.split()
                    tweet = [word for word in tweet if word.lower() not in PERSON_AWARD 
                             and word.lower() not in NOMINATION_WORDS]
                    tweet = ' '.join(tweet)
                    names = re.findall(NAME_PATTERN, tweet)
                    for name in names:
                        if name not in nominee[key]:
                            nominee[key][name] = 1
                        else:
                            nominee[key][name] += 1
        else:
            for tweet in value:
                if not any([kw in tweet for kw in PERSON_AWARD]):
                    tweet = tweet.split()
                    tweet = [word for word in tweet if word.lower() not in WINNER and word.lower() not in NOMINATION_WORDS]
                    tweet = ' '.join(tweet)
                    names = re.findall(NAME_PATTERN, tweet)
                    for name in names:
                        if name not in nominee[key]:
                            nominee[key][name] = 1
                        else:
                            nominee[key][name] += 1
                            
    print("============================= Get Nominee Finished ==============================")
    return nominee


def get_winner(year):
    '''Winners is a dictionary with the hard coded award
    names as keys, and each entry containing a single string.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    winners = {}
    df = process_json(year)
    df['text'] = df['text'].apply(remove_stopwords)
    df['text_process'] = df['text'].apply(tweet_preprocess)
    award_winner_candid = rapid_fuzz(df['text_process'])
    for key, value in award_winner_candid.items():
        lis = []
        for a, b, c in value:
            lis.append(a)
        key_processed = award_name_preprocess(key)
        winner = most_common_words(key_processed, lis)
        winners[key] = winner
    print("============================== Get Winner Finished ==============================")
    return winners



def get_presenters(year):
    '''Presenters is a dictionary with the hard coded award
    names as keys, and each entry a list of strings. Do NOT change the
    name of this function or what it returns.'''
    df = process_json(year)
    extra_award = dict()
    tweets = df['text'].to_list()
    
    fresh_names = dict()
    for award in OFFICIAL_AWARDS:
        fresh_names[award] = [[item for item in award.split() if not item in TO_DELETE]]
        extra_award[award] = []
        extra_award[award].append(award)
    altAwardName(OFFICIAL_AWARDS, extra_award, fresh_names)
    
    tweet_by_award_dict = getTweetByAward(OFFICIAL_AWARDS, fresh_names, tweets)
    
    ia = IMDb()
    presenters_dict_by_awards = {}
    stop_base = ['Foreign', 'Award', 'Best']
    single_presenter_pattern = re.compile(r'[A-Z][a-z]+\s[A-Z][a-z]+(?=\s(?:is|was)?\s*present\w*\b)')
    
    multiple_presenters_pattern = re.compile(r'[A-Z][a-z]+\s[A-Z][a-z]+\sand\s[A-Z][a-z]+\s[A-Z][a-z]+(?=\spresent|\sintroduc)')
    
    for award in tweet_by_award_dict:
        stop = stop_base
        for name in fresh_names[award]:
            stop.extend([s.capitalize() for s in name])
        presenters_dict_by_awards[award] = []
    
        for tweet in tweet_by_award_dict[award]:
            multiple_presenters = re.findall(multiple_presenters_pattern, tweet)
    
            for presenter in multiple_presenters:
                pp = presenter.split(' and ')
                p1 = pp[0]
                if any(word in p1 for word in stop):
                    continue
    
                pp = presenter.split(' and ')
                pt = pp[1]
                ptt = pt.split(' ')
                pttname = ptt[0:2]
                p2 = ' '.join(pttname)
                if any(word in p2 for word in stop):
                    continue
    
                person = ia.search_person(p1)
                if person:
                    p1 = person[0]['name']
                person = ia.search_person(p2)
                if person:
                    p2 = person[0]['name']
                if p1 not in presenters_dict_by_awards[award]:
                    presenters_dict_by_awards[award].append(p1)
                if p2 not in presenters_dict_by_awards[award]:
                    presenters_dict_by_awards[award].append(p2)
    
            single_presenter = re.findall(single_presenter_pattern, tweet)
            for presenter in single_presenter:
                if any(word in presenter for word in stop):
                    continue
                person = ia.search_person(presenter)
                if person:
                    presenter = person[0]['name']
                if presenter not in presenters_dict_by_awards[award]:
                    presenters_dict_by_awards[award].append(presenter)
    print("============================= Get Presenters Finished ===========================")
    return presenters_dict_by_awards


# extra credit
def best_dressed(year):
    df = process_json(year)
    df['text'] = df['text'].apply(remove_stopwords)
    dic = dict()
    for tweet in df['text']:
        if 'best dress' in tweet:
            word_tokens = word_tokenize(tweet)
            filtered_sentence = [w for w in word_tokens if w.lower() not in STOP_WORDS_dress]
            names = re.findall(TITLE + NAME1 + MIDDLE_I + NAME2, ' '.join(filtered_sentence))
            for name in names:
                if name not in dic:
                    dic[name] = 1
                else:
                    dic[name] += 1


    k = Counter(dic)
    high = k.most_common(1)
    for person in high:
        prob = person[1]/sum(dic.values())
        print('Best dress: ', person[0])
        print('prob: ', prob)

    name = person[0]
    search = name + " " + str(year) + " Golden Globes Dress"

    downloader.download(search, limit=1,  output_dir='dataset',
    adult_filter_off=True, force_replace=False, timeout=60)


def worst_dressed(year):
    """
    Extra Credit: get the worst dressed 
    """
    df = process_json(year)
    df['text'] = df['text'].apply(remove_stopwords)
    dic = dict()
    for tweet in df['text']:
        if 'worst dress' in tweet:
            word_tokens = word_tokenize(tweet)
            filtered_sentence = [w for w in word_tokens if w.lower() not in STOP_WORDS_dress]
            names = re.findall(TITLE + NAME1 + MIDDLE_I + NAME2, ' '.join(filtered_sentence))
            for name in names:
                if name not in dic:
                    dic[name] = 1
                else:
                    dic[name] += 1
    k = Counter(dic)
    high = k.most_common(2)
    for person in high:
        prob = person[1]/sum(dic.values())
        print('Worst dress: ', person[0])
        print('prob: ', prob)

    for person in high:
      name = person[0]
      search = name + " " + str(year) + " Golden Globes Dress"
  
      downloader.download(search, limit=2,  output_dir='dataset',
      adult_filter_off=True, force_replace=False, timeout=60)

def best_joke(year):
    """
    Extra Credit: get the best joke of the given year
    """
    df = process_json(year)
    df['text'] = df['text'].apply(remove_stopwords)
    dic = dict()
    for tweet in df['text']:
        if 'joke' in tweet:
            word_tokens = word_tokenize(tweet)
            filtered_sentence = [w for w in word_tokens if w.lower() not in STOP_WORDS_dress]
            names = re.findall(TITLE + NAME1 + MIDDLE_I + NAME2, ' '.join(filtered_sentence))
            for name in names:
                if name not in dic:
                    dic[name] = 1
                else:
                    dic[name] += 1
    k = Counter(dic)
    high = k.most_common(5)
    for person in high:
        prob = person[1]/sum(dic.values())
        print('Best joke: ', person[0])
        print('prob: ', prob)


def performer(year):
    df = process_json(year)
    df['text'] = df['text'].apply(remove_stopwords)
    dic = dict()
    for tweet in df['text']:
        if 'perform' in tweet:
            word_tokens = word_tokenize(tweet)
            filtered_sentence = [w for w in word_tokens if w.lower() not in STOP_WORDS_dress]
            names = re.findall(TITLE + NAME1 + MIDDLE_I + NAME2, ' '.join(filtered_sentence))
            for name in names:
                if name not in dic:
                    dic[name] = 1
                else:
                    dic[name] += 1
    k = Counter(dic)
    high = k.most_common(5)
    for person in high:
        prob = person[1]/sum(dic.values())
        print('Performer: ', person[0])
        print('prob: ', prob)
    
    
def pre_ceremony():
    '''This function loads/fetches/processes any data your program
    will use, and stores that data in your DB or in a json, csv, or
    plain text file. It is the first thing the TA will run when grading.
    Do NOT change the name of this function or what it returns.'''
    # Your code here
    global df
    df = process_json('2013')
    df['text'] = df['text'].apply(remove_stopwords)
    print("==========================Pre-ceremony processing complete===========================")
    return



def get_result_and_json(year):
    hosts = get_hosts(year)
    host = ', '.join(hosts)
    award_generated = get_awards(year)
    print("===========================Extra Credit (Best Joke, etc) =========================")
    best_dressed(year)
    worst_dressed(year)
    best_joke(year)
    performer(year)
    
    print("===========================Extra Credit Finished =================================")
    
    print(f"==========================Results for {year}===========================\n")
    
    print(f'Host: {host}\n')

    presenters_dict = get_presenters(year)
    print(presenters_dict)
    winner_dict = get_winner(year)
    print(winner_dict)
    nominees_dict = get_nominees(year)
    awards_data = {
            "year": year,
            "host": host,
            "awards": award_generated,
            "results": {}
    }

    for award in OFFICIAL_AWARDS:
        presenters = ', '.join(presenters_dict[award])
        nominees = ', '.join(nominees_dict[award])
        winner = winner_dict[award]
        print(f'''
            Award: {award} \n
            Presenters: {presenters} \n
            Nominees: {nominees} \n
            Winner: {winner} \n
            '''
        )

        awards_data["results"][award] = {
            "Presenters": presenters,
            "Nominees": nominees,
            "Winner": winner
        }
        
    
    
    with open('result'+str(year)+'.json', 'w') as fp:
        json.dump(awards_data, fp)

    print("==========================Json File Generated===========================\n")

    

def main():
    '''This function calls your program. Typing "python gg_api.py"
    will run this function. Or, in the interpreter, import gg_api
    and then run gg_api.main(). This is the second thing the TA will
    run when grading. Do NOT change the name of this function or
    what it returns.'''
    # Your code here
   
    year = 2013
    pre_ceremony()
    get_result_and_json(year)
    

if __name__ == '__main__':
    main()

