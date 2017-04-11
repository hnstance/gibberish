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


def generate_word():
    """Returns a random consonant-vowel-consonant pseudo-word."""
    return ''.join(random.choice(s) for s in (initial_consonants,
                                              vowels,
                                              final_consonants))


def generate_words(wordcount):
    """Returns a list of ``wordcount`` pseudo-words."""
    return [generate_word() for _ in xrange(wordcount)]


def console_main():
    import sys
    try:
        wordcount = int(sys.argv[1])
    except (IndexError, ValueError):
        wordcount = 1
    print(' '.join(generate_words(wordcount)))


if __name__ == '__main__':
    console_main()
