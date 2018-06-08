import numpy as np
import re
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

class CommentsCleaner:
    '''Methods to clean the Data'''
    def iterate(self):
        for cleanup in [self.remove_url,
                        self.remove_speical_characters]:
            yield cleanup

    def remove_url(self,comments):
        comments.loc[:,'comment_text'].replace(r"\httpS+","",inplace=True)
        return comments

    def remove_speical_characters(self,comments):
        for remove in map(lambda r: re.compile(re.escape(r)),[",", ":", "\"", "=", "&", ";", "%", "$",
                                                                     "@", "%", "^", "*", "(", ")", "{", "}",
                                                                     "[", "]", "|", "/", "\\", ">", "<", "-",
                                                                     "!", "?", ".", "'",
                                                                     "--", "---", "#",'\n']):
            comments.loc[:,'comment_text'].replace(remove, "",inplace=True)
        return comments

def cleanup(comments_df):
    ''' Runs Cleaner '''
    cleaner = CommentsCleaner()
    for cleanup_method in cleaner.iterate():
        comments_df = cleanup_method(comments_df)
    return comments_df