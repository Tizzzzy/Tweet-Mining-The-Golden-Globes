"""
This file contains global constants that we used for our functions.

Mostly consists of various stopwords and regular expressions for 
tweet preprocessing, get_hosts, get_awards, get_nominees, get_presenters,
and functions for extra credits. 

"""


import re

OFFICIAL_AWARDS = [
    'cecil b. demille award', 'best motion picture - drama',
    'best performance by an actress in a motion picture - drama',
    'best performance by an actor in a motion picture - drama',
    'best motion picture - comedy or musical',
    'best performance by an actress in a motion picture - comedy or musical',
    'best performance by an actor in a motion picture - comedy or musical',
    'best animated feature film', 'best foreign language film',
    'best performance by an actress in a supporting role in a motion picture',
    'best performance by an actor in a supporting role in a motion picture',
    'best director - motion picture', 'best screenplay - motion picture',
    'best original score - motion picture',
    'best original song - motion picture', 'best television series - drama',
    'best performance by an actress in a television series - drama',
    'best performance by an actor in a television series - drama',
    'best television series - comedy or musical',
    'best performance by an actress in a television series - comedy or musical',
    'best performance by an actor in a television series - comedy or musical',
    'best mini-series or motion picture made for television',
    'best performance by an actress in a mini-series or motion picture made for television',
    'best performance by an actor in a mini-series or motion picture made for television',
    'best performance by an actress in a supporting role in a series, mini-series or motion picture made for television',
    'best performance by an actor in a supporting role in a series, mini-series or motion picture made for television'
]

TITLE = r"(?:[A-Z][a-z]*\.\s*)?"
NAME1 = r"[A-Z][a-z]+,?\s+"
MIDDLE_I = r"(?:[A-Z][a-z]*\.?\s*)?"
NAME2 = r"[A-Z][a-z]+"

WHITE_SPACE = r'\s+'
SINGLE_CHAR = r'(?<!\S)\S(?!\S)'

LINKS = re.compile(
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
)
HASHTAG = re.compile(r'#[\s]+\w+')
TAG = re.compile(r'@[^:]+:')
PUNC = re.compile(r'[^\w\d\s]+')

AWARD_STOPLIST = [
    'best', 'award', 'for', 'or', 'made', 'the', 'in', 'a', 'by',
    'performance', 'an', 'golden', 'globes', 'role', '-', 'of', 'go', 'b.',
    'game', 'yes', 'should', 'could', 'would', 'have', 'been', 'i', 'this',
    'that', 'even', 'with', 'I'
]
NAME_PATTERN = re.compile(r'[A-Z][a-z]+\s[A-Z][a-z]+')
PERSON_AWARD = ['actor', 'actress', 'director', 'demille']
TV_RELATED_AWARD = [
    'tv', 't.v.', 'TV', 'television', 'film', 'motion', 'picture', 'series',
    'animated', 'animation'
]
NOMINATION_WORDS = ["nominated", "nominee", "nominate", "to", "ceremony", "category", "announced", "congratulations", "congrats", "honored", 
                    "prestigious", "deserving", "celebrate", "recognized", "for", "goes to", "deserves", "recognize", "believe", "overlook", "deserved", "up", "rooting", "hope", "hoping",
                   "finally", "happy for", "robbed", "overrated", "pick", "tough", "competition","earned", "well", "favorite", "clear", "clearly", "well-deserved", "right", "direction"]


WINNER = ["musical","comedy","motion", "picture","golden","globe","movie","television","best","or","tv","original","series","animated",
"feature","film","song","drama","-","rt","to","goes","foreign",'the']

VERBS = ['was', 'were', 'is', 'are']

STOP_WORDS_AWARD = {
    'both', 'before', '-', 'their', 't', '--', 'herself', "you'll", 'through',
    'she', 'to', 'yourself', "should've", 'ours', 'be', 'ourselves', 'about',
    'each', 'doing', "shan't", "shouldn't", 'will', "weren't", 'which', 'a',
    'very', 'd', 'more', 'most', "didn't", 'have', 'other', 'above', 'at',
    'don', 'yourselves', "mightn't", "you'd", 'those', 'off', 'wouldn', 'wasn',
    'they', 'has', 'same', 'too', 'only', 'once', "won't", 'that', 'couldn',
    'haven', 'under', 'was', "haven't", 'won', 'm', 'during', 'are', 'with',
    'few', 'didn', 'out', 'the', 'these', "couldn't", 'any', 'shan', 'so',
    'him', 'i', 'some', 'this', "aren't", 'himself', 'ma', 'shouldn', 'am',
    'your', 'when', 'our', 'o', 'how', 'all', "isn't", 'its', "it's",
    'between', "she's", 'such', 'll', 'until', 'not', 'over', 'doesn', 'and',
    'who', 'being', "wouldn't", 'on', 'as', "hasn't", 'hasn', 'hadn', 'mightn',
    'now', 'me', 'again', 'itself', 'own', 'but', "don't", "hadn't", 'no',
    're', 'you', 'should', 'we', 'nor', 'had', 'up', 'were', 'if', 'does',
    'whom', 'he', 'do', 'aren', 'there', 'my', 'it', "you've", "needn't",
    "that'll", 'or', 'just', 'theirs', 'then', 'an', 'than', 'weren', 's',
    'hers', 'here', 'themselves', 'after', 'ain', 'can', 'down', 'because',
    'into', 'why', "wasn't", 'by', 'against', 'them', 'his', 'yours',
    "doesn't", 'isn', 'her', 'been', 've', 'mustn', 'is', "you're", 'having',
    'while', 'needn', 'myself', 'of', 'below', "mustn't", 'in', 'for', 'where',
    'did', 'what', 'further', 'from', 'y'
}

STOP_WORDS_winner = {'both', 'before', 'their', 't', 'herself', "you'll", 'through',
                    'she', 'to', 'yourself', "should've", 'ours', 'be', 'ourselves', 'about',
                    'each', 'doing', "shan't", "shouldn't", 'will', "weren't", 'which', 'a',
                    'very', 'd', 'more', 'most', "didn't", 'have', 'other', 'above', 'at',
                    'don', 'yourselves', "mightn't", "you'd", 'those', 'off', 'wouldn', 'wasn',
                    'they', 'has', 'same', 'too', 'only', 'once', "won't", 'that', 'couldn',
                    'haven', 'under', 'was', "haven't", 'won', 'm', 'during', 'are', 'with',
                    'few', 'didn', 'out', 'the', 'these', "couldn't", 'any', 'shan', 'so',
                    'him', 'i', 'some', 'this', "aren't", 'himself', 'ma', 'shouldn', 'am',
                    'your', 'when', 'our', 'o', 'how', 'all', "isn't", 'its', "it's",
                    'between', "she's", 'such', 'll', 'until', 'not', 'over', 'doesn', 'and',
                    'who', 'being', "wouldn't", 'on', 'as', "hasn't", 'hasn', 'hadn', 'mightn',
                    'now', 'me', 'again', 'itself', 'own', 'but', "don't", "hadn't", 'no',
                    're', 'you', 'should', 'we', 'nor', 'had', 'up', 'were', 'if', 'does',
                    'whom', 'he', 'do', 'aren', 'there', 'my', 'it', "you've", "needn't",
                    "that'll", 'or', 'just', 'theirs', 'then', 'an', 'than', 'weren', 's',
                    'hers', 'here', 'themselves', 'after', 'ain', 'can', 'down', 'because',
                    'into', 'why', "wasn't", 'by', 'against', 'them', 'his', 'yours',
                    "doesn't", 'isn', 'her', 'been', 've', 'mustn', 'is', "you're", 'having',
                    'while', 'needn', 'myself', 'of', 'below', "mustn't", 'in', 'for', 'where',
                    'did', 'what', 'further', 'from', 'y', 'the', 'is', 'a', 'in', 'on', 'and', 'here', 'as', 'well',
                    'for', 'actress', '-', 'best', 'cecil', 'series', 'made',
                    'picture', 'demille', 'b.', 'motion', 'original', 'award',
                    'comedy', 'in', 'language', 'screenplay', 'series,', 'supporting',
                    'drama', 'role', 'mini-series', 'performance', 'director', 'feature',
                    'a', 'actor', 'or', 'an', 'animated', 'song', 'musical', 'score',
                    'by', 'film', 'television', 'foreign', 'mini', 'goes', 'to', 'of'}


STOP_WORDS = [
    '.org', 'aahh', 'aarrgghh', 'abt', 'ftl', 'ftw', 'fu', 'fuck', 'fucks',
    'gtfo', 'gtg', 'haa', 'hah', 'hahah', 'haha', 'hahaha', 'hahahaha', 'hehe',
    'heh', 'hehehe', 'hi', 'hihi', 'hihihi', 'http', 'https', 'huge', 'huh',
    'huhu', 'huhuhu', 'idk', 'iirc', 'im', 'imho', 'imo', 'ini', 'irl', 'ish',
    'isn', 'isnt', 'j/k', 'jk', 'jus', 'just', 'justwit', 'juz', 'kinda',
    'kthx', 'kthxbai', 'kyou', 'laa', 'laaa', 'lah', 'lanuch', 'leavg', 'leh',
    'lol', 'lols', 'ltd', 'mph', 'mrt', 'msg', 'msgs', 'muahahahahaha', 'nb',
    'neways', 'ni', 'nice', 'pls', 'plz', 'plzz', 'psd', 'pte', 'pwm', 'pwned',
    'qfmft', 'qft', 'tis', 'tm', 'tmr', 'tyty', 'tyvm', 'um', 'umm', 'viv',
    'vn', 'vote', 'voted', 'w00t', 'wa', 'wadever', 'wah', 'wasn', 'wasnt',
    'wassup', 'wat', 'watcha', 'wateva', 'watever', 'watnot', 'wats', 'wayy',
    'wb', 'weren', 'werent', 'whaha', 'wham', 'whammy', 'whaow', 'whatcha',
    'whatev', 'whateva', 'whatevar', 'whatever', 'whatnot', 'whats',
    'whatsoever', 'whatz', 'whee', 'whenz', 'whey', 'whore', 'whores',
    'whoring', 'wo', 'woah', 'woh', 'wooohooo', 'woot', 'wow', 'wrt', 'wtb',
    'wtf', 'wth', 'wts', 'wtt', 'www', 'xs', 'ya', 'yaah', 'yah', 'yahh',
    'yahoocurrency', 'yall', 'yar', 'yay', 'yea', 'yeah', 'yeahh', 'yeh',
    'yhoo', 'ymmv', 'young', 'youre', 'yr', 'yum', 'yummy', 'yumyum', 'yw',
    'zomg', 'zz', 'zzz', 'loz', 'lor', 'loh', 'tsk', 'meh', 'lmao', 'wanna',
    'doesn', 'liao', 'didn', 'didnt', 'omg', 'ohh', 'ohgod', 'hoh', 'hoo',
    'bye', 'byee', 'byeee', 'byeeee', 'lmaolmao', 'yeahhh', 'yeahhhh',
    'yeahhhhh', 'yup', 'yupp', 'hahahahahahaha', 'hahahahahah', 'hahhaha',
    'wooohoooo', 'wahaha', 'haah', '2moro', 'veh', 'noo', 'nooo', 'noooo',
    'hahas', 'ooooo', 'ahahaha', 'ahahahahah', 'tomolow', 'accent', 'accented',
    'accents', 'acne', 'ads', 'afaik', 'aft', 'ago', 'ahead', 'ain', 'aint',
    'aircon', 'alot', 'am', 'annoy', 'annoyed', 'annoys', 'anycase', 'anymore',
    'app', 'apparently', 'apps', 'argh', 'ass', 'asses', 'awesome', 'babeh',
    'bad', 'bai', 'based', 'bcos', 'bcoz', 'bday', 'bit', 'biz', 'blah',
    'bleh', 'bless', 'blessed', 'blk', 'blogcatalog', 'bro', 'bros', 'btw',
    'byee', 'com', 'congrats', 'contd', 'conv', 'cos', 'cost', 'costs',
    'couldn', 'couldnt', 'cove', 'coves', 'coz', 'crap', 'cum', 'curnews',
    'curr', 'cuz', 'dat', 'de', 'diff', 'dis', 'doc', 'doesn', 'doesnt', 'don',
    'AAWWW', 'dont', 'dr', 'dreamt', 'drs', 'due', 'dun', 'dunno', 'duper',
    'eh', 'ehh', 'emo', 'emos', 'eng', 'esp', 'fadein', 'ffs', 'fml', 'frm',
    'fwah', 'g2g', 'gajshost', 'gd', 'geez', 'gg', 'gigs', 'gtfo.1', 'gtg.1',
    'hasn', 'hasnt', 'hav', 'haven', 'havent', 'hee', 'hello', 'hey', 'hmm',
    'ho', 'hohoho', 'lotsa', 'lotta', 'luv', 'ly', 'macdailynews', 'nite',
    'nom', 'noscript', 'nvr', 'nw', 'ohayo', 'omfg', 'omfgwtf', 'omgwtfbbq',
    'omw', 'org', 'pf', 'pic', 'pm', 'pmsing', 'ppl', 'pre', 'pro', 'rawr',
    'rawrr', 'rofl', 'roflmao', 'rss', 'rt', 'sec', 'secs', 'seem', 'seemed',
    'seems', 'sgreinfo', 'shd', 'shit', 'shits', 'shitz', 'shld', 'shouldn',
    'shouldnt', 'shudder', 'sq', 'sqft', 'sqm', 'srsly', 'stfu', 'stks', 'su',
    'suck', 'sucked', 'sucks', 'suckz', 'sux', 'swf', 'tart', 'tat', 'tgif',
    'thanky', 'thk', 'thks', 'tht', 'tired', 'hahahahahahahahaha',
    'hahahahaha', 'hahahahah', 'zzzzz', 'hahahahha', 'lolololol', 'lololol',
    'lolol', 'lol', 'dude', 'hmmm', 'humm', 'tumblr', 'kkkk', 'fk', 'yayyyyyy',
    'fffffffuuuuuuuuuuuu', 'zzzz', 'noooooooooo', 'hahahhaha', 'woohoo',
    'lalalalalalala', 'lala', 'lalala', 'lalalala', 'whahahaahahahahahah',
    'hahahahahahahahahahaha', 'ahhh', 'RT', 'rt', 'gif', 'amp', '.com', '.ly',
    '.net', """'""", ',', '.', ';'
]

STOP_WORDS_dress = {
    'both', 'before', 'their', 't', 'herself', "you'll", 'through',
    'she', 'to', 'yourself', "should've", 'ours', 'be', 'ourselves', 'about',
    'each', 'doing', "shan't", "shouldn't", 'will', "weren't", 'which', 'a',
    'very', 'd', 'more', 'most', "didn't", 'have', 'other', 'above', 'at',
    'don', 'yourselves', "mightn't", "you'd", 'those', 'off', 'wouldn', 'wasn',
    'they', 'has', 'same', 'too', 'only', 'once', "won't", 'that', 'couldn',
    'haven', 'under', 'was', "haven't", 'won', 'm', 'during', 'are', 'with',
    'few', 'didn', 'out', 'the', 'these', "couldn't", 'any', 'shan', 'so',
    'him', 'i', 'some', 'this', "aren't", 'himself', 'ma', 'shouldn', 'am',
    'your', 'when', 'our', 'o', 'how', 'all', "isn't", 'its', "it's",
    'between', "she's", 'such', 'll', 'until', 'not', 'over', 'doesn', 'and',
    'who', 'being', "wouldn't", 'on', 'as', "hasn't", 'hasn', 'hadn', 'mightn',
    'now', 'me', 'again', 'itself', 'own', 'but', "don't", "hadn't", 'no',
    're', 'you', 'should', 'we', 'nor', 'had', 'up', 'were', 'if', 'does',
    'whom', 'he', 'do', 'aren', 'there', 'my', 'it', "you've", "needn't",
    "that'll", 'or', 'just', 'theirs', 'then', 'an', 'than', 'weren', 's',
    'hers', 'here', 'themselves', 'after', 'ain', 'can', 'down', 'because',
    'into', 'why', "wasn't", 'by', 'against', 'them', 'his', 'yours',
    "doesn't", 'isn', 'her', 'been', 've', 'mustn', 'is', "you're", 'having',
    'while', 'needn', 'myself', 'of', 'below', "mustn't", 'in', 'for', 'where',
    'did', 'what', 'further', 'from', 'y', 'the', 'is', 'a', 'in', 'on', 'and', 'here', 'as', 'well',
    'for', 'actress', '-', 'best', 'cecil', 'series', 'made',
    'picture', 'demille', 'b.', 'motion', 'original', 'award',
    'comedy', 'in', 'language', 'screenplay', 'series,', 'supporting',
    'drama', 'role', 'mini-series', 'director', 'feature',
    'a', 'actor', 'or', 'an', 'animated', 'song', 'musical', 'score',
    'by', 'film', 'television', 'foreign', 'mini', 'goes', 'to', 'of', 'golden',
   'globe', 'awards', 'can', 'who', 'the' 'globes'
}

ACTIONS = [
    " ", "won", "win", "was awarded", "award", "received", "receive",
    "was honored with", "honor with", "was presented with", "present with",
    "was recognized with", "recognize with", "earned", "earn", "was given",
    "give", "was bestowed with", "bestow with", "secured", "secure",
    "was decorated with", "decorate with", "took home", "take home",
    "was the recipient of", "be the recipient of", "picked up", "pick up",
    "was conferred", "confer"
]

GENRE = [
    'award', 'drama', 'musical', 'comedy', 'film', 'picture', 'television'
]

TO_DELETE = [
    '-', 'a', 'an', 'award', 'best', 'by', 'for', 'in', 'made', 'or',
    'performance', 'role', 'feature', 'language'
]