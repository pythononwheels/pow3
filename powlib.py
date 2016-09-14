import re
import os

#
# (pattern, search, replace) regex english plural rules tuple
# taken from : http://www.daniweb.com/software-development/python/threads/70647
rule_tuple = (
    ('[ml]ouse$', '([ml])ouse$', '\\1ice'),
    ('child$', 'child$', 'children'),
    ('booth$', 'booth$', 'booths'),
    ('foot$', 'foot$', 'feet'),
    ('ooth$', 'ooth$', 'eeth'),
    ('l[eo]af$', 'l([eo])af$', 'l\\1aves'),
    ('sis$', 'sis$', 'ses'),
    ('man$', 'man$', 'men'),
    ('ife$', 'ife$', 'ives'),
    ('eau$', 'eau$', 'eaux'),
    ('lf$', 'lf$', 'lves'),
    ('[sxz]$', '$', 'es'),
    ('[^aeioudgkprt]h$', '$', 'es'),
    ('(qu|[^aeiou])y$', 'y$', 'ies'),
    ('$', '$', 's')
    )
def regex_rules(rules=rule_tuple):
    # also to pluralize
    for line in rules:
        pattern, search, replace = line
        yield lambda word: re.search(pattern, word) and re.sub(search, replace, word)

def plural(noun):
    #print noun
    # the final pluralisation method.
    for rule in regex_rules():
        result = rule(noun)
        #print result
        if result:
            return result

def pluralize(noun):
    return plural(noun)

def singularize(word):
    # taken from:http://codelog.blogial.com/2008/07/27/singular-form-of-a-word-in-python/
    sing_rules = [lambda w: w[-3:] == 'ies' and w[:-3] + 'y',
              lambda w: w[-4:] == 'ives' and w[:-4] + 'ife',
              lambda w: w[-3:] == 'ves' and w[:-3] + 'f',
              lambda w: w[-2:] == 'es' and w[:-2],
              lambda w: w[-1:] == 's' and w[:-1],
              lambda w: w,
              ]
    word = word.strip()
    singleword = [f(word) for f in sing_rules if f(word) is not False][0]
    return singleword


def rel_dec(what, who):
    # We're going to return this decorator
    def simple_decorator(f):
        # This is the new function we're going to return
        # This function will be used in place of our original definition
        def wrapper():
            print(what)
            f()
            print(who)
        return wrapper
    return simple_decorator


#
# a class decorator that executres at import.
# ala flask app.route()
# see: http://ains.co/blog/things-which-arent-magic-flask-part-1.html
# 
# For the relation part see: 
# http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#building-a-relationship
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String

class powDec():
    def __init__(self):
        self.relations = {}
    # who is the classname of the related model  (e.g. post)
    def has_many(self, rel):
        # cls is the class that has many of the related models (e.g. user)
        def decorator(cls):
            self.relations[rel] = cls
            #first we need to set the foreign key in <who>
            #this makes from <class 'models.user.User'>
            rel_name = str(rel).split("'")[1].split(".")[2].lower()
            cls_name = str(cls).split("'")[1].split(".")[2].lower()
            setattr(rel, cls_name, relationship(cls_name.capitalize(), back_populates=pluralize(rel_name)) )
            setattr(rel, cls_name + "_id", Column(Integer, ForeignKey(pluralize(cls_name)+".id")))
            ##print(dir(rel))
            print("I see a: " + str(cls_name) + " has many: " + pluralize(rel_name))
            setattr(cls, pluralize(rel_name), 
                relationship(singularize(rel_name).capitalize(), order_by=rel.id,
                    back_populates=cls_name))
            return cls
        return decorator

relation = powDec()


