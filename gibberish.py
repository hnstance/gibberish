#!/usr/bin/env python
import string
import random

__all__ = ('generate_word', 'generate_words')

initial_consonants = list(set(string.ascii_lowercase) - set('aeiou')
                      # add some crunchy clusters
                      | set(['bl', 'br', 'cl', 'cr', 'ch', 'dr', 
                             'dj', 'fl', 'fr', 'gl', 'gh', 'gr',
                             'gn', 'll', 'kr', 'kh', 'kw', 'pl',
                             'pr', 'ps', 'pw', 'ph', 'rw', 'sk',
                             'sl', 'sm', 'sn', 'sp', 'st', 'str',
                             'sw', 'sh', 'sr', 'sch', 'squ',
                             'tr', 'th', 'qu', 'qw', 'wr', 'wh'])
                      )

final_consonants = list(set(string.ascii_lowercase) - set('aeiou')
                    # remove the confusables
                    - set('qj')
                    # crunchy clusters
                    | set(['ct', 'ch', 'ck', 'ft', 'lk', 'lm', 
                           'ld', 'lp', 'lb', 'lt', 'mp', 'mn', 
                           'nd', 'ng', 'nk', 'nt', 'nh', 'nm',
                           'pt', 'ph', 'rb', 'rg', 'rk', 'rl',
                           'rf', 'rn', 'rm', 'rc', 'rs', 'rq',
                           'rt', 'rp', 'rd', 'rr', 'sk', 'sn',
                           'sm', 'sp', 'ss', 'st', 'sh', 'tt',
                           'tch', 'tck', 'wr', 'wk', 'wl'])
                    )

vowels = ['a', 'e', 'i', 'o', 'u', 'ou', 'uou', 
          'au', 'eu', 'ae', 'iu', 'ui', 'ie', 'oi',
          'ue', 'ea', 'ao', 'oa', 'ee', 'oo', 'ii',
          'uu', 'y', 'ye']


def generate_group1():
    """Returns a generator of consonant-vowel-consonant pseudo-word."""
    for i in initial_consonants:
        for v in vowels:
            for f in final_consonants:
                yield ''.join([i,v,f])

if __name__ == '__main__':
    for w in generate_group1():
        print w
        for v in vowels:
            n = w + v
            print n
            for f in final_consonants:
                print (n + f)
