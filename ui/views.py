from django.http import HttpResponse
from django.shortcuts import render
import operator
import os
import collections
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sn
import pickle

def homepage(request):
    return render(request, 'ui/home.html')

def count(request):
    fulltext = request.GET['fulltext']

    word_freqT1 = collections.Counter(fulltext.split(" "))

    with open('1.pickle', 'rb') as f:
        dicts = pickle.load(f)

        prior_prob = dicts['prior_prob']
        cond_prob0 = dicts['cond_prob0']
        cond_prob1 = dicts['cond_prob1']


    spam_score = 0
    ham_score = 0
    spam_score += (np.log(prior_prob['spam']))
    ham_score += (np.log(prior_prob['ham']))

    for word in word_freqT1.items():
        if (word[0] in cond_prob0) and (word[0] in cond_prob1):

            spam_score += (np.log(cond_prob1[word[0]]))
            ham_score  += (np.log(cond_prob0[word[0]]))

        elif (word[0] in cond_prob0) and (word[0] not in cond_prob1):
            ham_score  += abs(np.log(cond_prob0[word[0]]))

        elif (word[0] in cond_prob1) and (word[0] not in cond_prob0):
            spam_score += abs(np.log(cond_prob1[word[0]]))

    return render(request, 'ui/count.html',{'spam_score':spam_score,'ham_score':ham_score})
