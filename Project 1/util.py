"""
This file contains all the helper functions that we used when extracting informations of tweets 
based on the given `year`
"""


import re
import pandas as pd
import numpy as np
import emoji
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from imdb import IMDb
from nltk import pos_tag
import rapidfuzz
from collections import Counter
from global_var import *

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download("popular")
nltk.download("maxent_ne_chunker")
nltk.download("words")


"""
General Helper Functions used for data pre-processing:

- process_json(year)
- remove_stopwords(year)
- tweet_preprocess(year)
"""

def process_json(year):
    """
    This function reads in the json file given the year as an input and reads as a pandas dataframe
    
    Input: year - A string that represents the year of the Golden Globe or any other ceremony
    Output: a pandas dataframe that represents the tweets
    """
    year = str(year)
    try:
        f = open('gg' + year + '.json')
        data = pd.read_json(f)
        return data
    except:
        return False

    
def remove_stopwords(text):
    """
    Preprocesses the input text by removing common stopwords and replacing specific terms.
    
    Input:
    - text (str): The input text to preprocess.
    Output:
    - str: The processed text with stopwords removed and specific terms replaced.
    """
    word_tokens = word_tokenize(text)
    filtered_words = []
    for w in word_tokens:
        if w == '&':
            filtered_words.append('and')
        elif w.lower() == 'tv':
            filtered_words.append('telvision')
        elif w.lower() == 'mini-series' or w.lower() == 'miniseries':
            filtered_words.append('mini series')
        else:
            if w.lower() not in STOP_WORDS:
                filtered_words.append(w)
    return ' '.join(filtered_words)


def tweet_preprocess(tweet):
    """
    Preprocesses a tweet by removing emojis, hashtags, mentions, links, and punctuations.

    Parameters:
    - tweet (str): The input tweet text to preprocess.
    Returns:
    - str: The preprocessed tweet with emojis, hashtags, mentions, links, and punctuations removed.
    """
    tweet = emoji.replace_emoji(tweet, replace='')
    tweet = re.sub(HASHTAG, '', tweet)
    tweet = re.sub(TAG, '', tweet)
    tweet = re.sub(LINKS, '', tweet)
    tweet = re.sub(PUNC, ' ', tweet)
    return tweet
  

"""
Helper Functions used within `get_award(year)`
"""
    
def match_pattern(sentence):
    """
    Searches for a specific pattern in a sentence and extracts an award name if found.
    The function looks for a pattern that includes actions, award names, and genre terms in the input sentence.

    Inputs:
    - sentence (str): The input sentence to search for the pattern.
    Outputs:
    - str or None: The extracted award name if found, or None if no match is found.
    """
    
    pattern = r"(?i)(?:" + "|".join(ACTIONS) + r") [\w\s]+ (the )?(?P<award>(best|cecil) [\w\s@#&/,-]+?(" + "|".join(GENRE) + r")) [\w\s]+"

    match = re.search(pattern, sentence)

    if match:
        return match.group("award")

    
def award_filter(award):
    """
    Filters out common stopwords from an award name.

    Inputs:
    - award (str): The award name to filter.
    Outputs:
    - str: The filtered award name with common stopwords removed.
    """
    filtered_words = []
    for word in award:
        if word not in STOP_WORDS_AWARD:
            filtered_words.append(word)
    filtered_string = ' '.join(filtered_words)
    return filtered_string


def print_award(award_unique):
    """
    Filters a list of unique awards, removing duplicates and similar entries.

    Inputs:
    - award_unique (list of str): A list of unique award names.
    Outputs:
    - list of str: A filtered list of unique award names, removing duplicates and similar entries.
    """
    unique_award_pairs = award_unique
    final_unique_awards = []

    for unique_award in unique_award_pairs:
        if unique_award:
            is_unique = True
            for other_award in unique_award_pairs:
                if other_award:
                  # print('unique_award: ', unique_award)
                    temp1 = award_filter(list(unique_award.lower().split(" ")))
                    temp2 = award_filter(list(other_award.lower().split(" ")))
                  # print('temp1: ', temp1)
                  # print('temp2: ', temp2)
                    if unique_award != other_award and temp1 == temp2 or unique_award != other_award and unique_award.lower() in other_award.lower() or unique_award != other_award and unique_award.lower() == other_award.lower():
                        is_unique = False
                        break
            if is_unique:
                final_unique_awards.append(unique_award)
    return final_unique_awards


"""
The rest functions are used inter-changablely between functions like:
get_nominee(year), get_presenters(year), and get_winners(year);
we group them together as follows.

"""

def extract_from_tweet(tweet):
    """
    Extracts relevant text from a tweet based on specific patterns.

    Inputs:
    - tweet (str): The input tweet text to extract information from.
    Outputs:
    - str or []: Extracted text from the tweet, or an empty list if no match is found.
    """
    
    # Tokenize and tag the tweet
    tokens = word_tokenize(tweet)

    for i, word in enumerate(tokens):
        # If the word is one of the verbs and the next word is in nominated words, 
        # extract everything before the verb
        if word in VERBS and i < len(tokens) - 1 and tokens[i + 1] in NOMINATION_WORDS:
            return ' '.join(tokens[:i])

        # If the word is in nominated words and there's no verb before it,
        # extract everything after it
        elif word in NOMINATION_WORDS and (i == 0 or tokens[i - 1] not in VERBS):
            return ' '.join(tokens[i+1:])

    return []  # Return None if no matching pattern is found



def extract_name(quote, language='english'):
    """
    Extracts person names from a given text using natural language processing.

    Inputs:
    - quote (str): The input text from which person names will be extracted.
    - language (str): The language of the input text (default is 'english').
    Outputs:
    - list of str: A list of person names found in the input text.
    """
    
    tokens = word_tokenize(quote)
    tags = nltk.pos_tag(tokens)
    tree = nltk.ne_chunk(tags)
    names=[]
    for subtree in tree.subtrees():
        if subtree.label() == 'PERSON':
            leave = " ".join(l[0] for l in subtree.leaves())
            names.append(leave)
    return names



def rapid_fuzz(text_process):
    """
    Uses rapidFuzz to find potential award candidates from a list of text values.

    Inputs:
    - text_process (pandas.Series): A Pandas Series containing text values to search for award-related keywords.
    Outputs:
    - dict: A dictionary containing award categories as keys and lists of potential award candidates as values.
    """
    text_values = text_process.to_list()
    texts = set()
    for award in ['best', 'actor', 'actress', 'award', 'drama', 'televison', 
                  'series', 'movie', 'picture', 'director', 'song']:
        # Check if 'golden' is present in any of the text values
        # if any(award in text.lower() for text in text_values):
        for text in text_values:
            if award in text.lower():
                texts.add(text.lower())
    # print(texts)

    award_winner_candid = {}
    for award in OFFICIAL_AWARDS:
        award_winner_candid[award] = rapidfuzz.process.extract(award, texts, score_cutoff=80)
    return award_winner_candid


def most_common_words(key, sentences):
    """
    Finds the most common words in a list of sentences after tokenization and preprocessing.

    Inputs:
    - key (str): A key or label related to the text data.
    - sentences (list of str): A list of sentences to analyze.
    Outputs:
    - str: The most common word or words, based on the specified key and sentence content.
    
    """
    # Tokenize and count words
    word_counts = Counter()
    for sentence in sentences:
        # Tokenize and remove punctuation, then filter out stopwords
        words = [word for word in re.findall(r'\w+', sentence.lower()) if word not in STOP_WORDS_winner and len(word) > 2]
        word_counts.update(words)

    # Get the N most common words
    N = 5
    most_common_words = word_counts.most_common(N)

    winner = ''
    if 'film' in key or len(most_common_words) < 2:
        winner = most_common_words[0][0]
    else:
        winner += most_common_words[0][0]
        winner += ' '
        winner += most_common_words[1][0]

    return winner


def award_name_preprocess(award):
    """
    Preprocesses an award name by replacing 'mini-series' with 'mini series' and removing commas.

    Inputs:
    - award (str): The award name to preprocess.
    Outputs:
    - str: The preprocessed award name.
    """
    
    if "mini-series" in award:
        award.replace("mini-series", "mini series")
    if "," in award:
        award.replace(",", "")
    return award



"""
    Reference: This code is modified based on the code here:
               https://github.com/amitadate/EECS-337-NLP-Project-01/blob/master/src/gg_api.py

    Updates extra award categories and their associated names based on official award names.

    This function is designed to adapt and extend the list of award categories and their associated names to 
    account for variations, subcategories, and alternate forms of official award names. It is typically used 
    in the context of award ceremonies or events where awards may change over the years or have different 
    names based on categories.

    This function is a recursive function. It uses recursion to ensure that all possible alternative award names
    are processed and added to the dictionaries.

    Inputs: 
        - OFFICIAL_AWARDS : a list of strings representing the awards for each year. This should be replaced
                            based on different years or different ceremonies.
        - extra_award : A dictionary containing extra award categories associated with official awards. 
                        The function updates this dictionary with alternative award names if they are generated.
        - extra_name : A dictionary containing names associated with the extra award categories. 
                       Like `extra_award`, this dictionary is updated with additional names corresponding 
                       to the extra award categories.
    """
def altAwardName(OFFICIAL_AWARDS, extra_award, extra_name):
  flag = 0

  for official in OFFICIAL_AWARDS:
    for award in extra_award[official]:
      if "score" in award:
        extra = "score"
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])
      if "song" in award:
        extra = "song"
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])
      if "television" in award:
        extra = award.replace("television", 'tv')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace("television", 't.v.')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

      if "motion picture" in award:
        extra = award.replace("motion picture", "movie")
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace("motion picture", "film")
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

      if "film" in award:
        extra = award.replace("film", "motion picture")
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace("film", "movie")
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

      if "comedy or musical" in award:
        extra = award.replace("comedy or musical", 'comedy')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace("comedy or musical", 'musical')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

      if "made for television" in award:
        extra = award.replace("made for television", 'television')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace("made for television", 'tv')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace("made for television", 't.v.')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

      if "series, mini-series or motion picture made for television" in award:
        extra = award.replace(
            "series, mini-series or motion picture made for television",
            'series')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace(
            "series, mini-series or motion picture made for television",
            'mini-series')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace(
            "series, mini-series or motion picture made for television",
            'miniseries')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace(
            "series, mini-series or motion picture made for television", 'tv')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace(
            "series, mini-series or motion picture made for television",
            'television')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace(
            "series, mini-series or motion picture made for television",
            'tv movie')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace(
            "series, mini-series or motion picture made for television",
            'tv series')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace(
            "series, mini-series or motion picture made for television",
            'television series')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

      if "mini-series or motion picture made for television" in award:
        extra = award.replace(
            "mini-series or motion picture made for television", 'miniseries')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace(
            "mini-series or motion picture made for television", 'mini-series')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace(
            "mini-series or motion picture made for television", 'tv movie')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace(
            "mini-series or motion picture made for television",
            'television movie')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

      if "television series" in award:
        extra = award.replace("television series", 'series')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace("television series", 'tv')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace("television series", 't.v.')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

        extra = award.replace("television series", 'television')
        if extra not in extra_award[official]:
          flag = 1
          extra_award[official].append(extra)
          extra_name[official].append(
              [item for item in extra.split() if not item in TO_DELETE])

      if "television series - comedy or musical" in award:

        for word in [
            "tv comedy", "tv musical", "comedy series", "t.v. comedy",
            "t.v. musical", "television comedy", "television musical"
        ]:
          extra = award.replace("television series - comedy or musical", word)
          if extra not in extra_award[official]:
            flag = 1
            extra_award[official].append(extra)
            extra_name[official].append(
                [item for item in extra.split() if not item in TO_DELETE])

      if "television series - drama" in award:
        for word in [
            "tv drama", "drama series", "television drama", "t.v. drama"
        ]:
          extra = award.replace("television series - drama", word)
          if extra not in extra_award[official]:
            flag = 1
            extra_award[official].append(extra)
            extra_name[official].append(
                [item for item in extra.split() if not item in TO_DELETE])
  if flag == 1:
    altAwardName(OFFICIAL_AWARDS, extra_award, extra_name)

    
    
def getTweetByAward(OFFICIAL_AWARDS, extra_name, tweets):
    """
    Reference: This code is modified based on the code here:
               https://github.com/amitadate/EECS-337-NLP-Project-01/blob/master/src/presenter.py
    
    This function organizes tweets by their relevance to official and extra award categories.
    It initializes an empty dictionary named 'tweet_by_award_dict' to store tweets organized by award category.
    It then Sorts the official award names in 'OFFICIAL_AWARDS' by their length in descending order to 
    prioritize longer names and prevent partial matches.
    It iterates through sorted official award names and tweets, checking for keyword relevance to 
    award categories and associated names.
    And finally determines the relevance of each tweet to award categories and adds them to corresponding lists 
    in 'tweet_by_award_dict'.

    Inputs:
    - OFFICIAL_AWARDS (list of str): Official award names for a specific year or ceremony. 
                                     These names serve as a reference for categorizing tweets.
    - extra_name (dict): A dictionary containing names associated with extra award categories. 
                         These names help identify tweets relevant to specific awards.
    - tweets (list of str): A list of tweets to be organized based on their connection to award categories.
    
    Output:
    - dict: A dictionary where keys represent award categories, and values are lists of tweets relevant to each award.
    """
    
    tweet_by_award_dict = dict()
    for award in OFFICIAL_AWARDS:
        tweet_by_award_dict[award] = []
    
    OFFICIAL_AWARDS.sort(key=lambda s: len(s), reverse=True)
    for award in OFFICIAL_AWARDS:
        tweet_length = len(tweets)
        for i in range(tweet_length - 1, -1, -1):
            tweet = tweets[i]
            for extra in extra_name[award]:
                if 'actor' in tweet.lower() or 'actress' in tweet.lower():
                    if 'actor' in award or 'actress' in award:
                        if 'actor' in extra or 'actress' in extra:
                            if 'supporting' in tweet.lower():
                                if 'supporting' in award:
                                    if 'supporting' in extra:
                                        flag = True
                                        for word in extra:
                                            if flag == True:
                                                flag = flag and word.lower() in tweet.lower()
    
                                        if flag == True:
                                            tweet_by_award_dict[award].append(tweet)
                                            break
                            else:
                                flag = True
                                for word in extra:
                                    if flag == True:
                                        flag = flag and word.lower() in tweet.lower()
    
                                if flag == True:
                                    tweet_by_award_dict[award].append(tweet)
                                    break
                else:
                    flag = True
                    for word in extra:
                        if flag == True:
                            flag = flag and word.lower() in tweet.lower()
    
                    if flag == True:
                        tweet_by_award_dict[award].append(tweet)
                        break
    return tweet_by_award_dict


def print_max_occurrence(best_dress, person, time):
    """
    Finds the person with the maximum occurrences and their probability.

    Inputs:
    - best_dress (dict): A dictionary with names as keys and their occurrences as values.
    - person (str): The name with the maximum occurrences.
    - time (int): The number of occurrences of the most frequent person.
    Outputs:
    - tuple: A tuple containing the name with the maximum occurrences and their probability.
    """
    for name, occurrences in best_dress.items():
        if occurrences > time:
            person = name
            time = occurrences
            prob = time/sum(best_dress.values())
    return person, prob