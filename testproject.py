#!/usr/bin/env python
# coding: utf-8

# In[2]:


#A Dictionary of movie critics and their ratings of a small set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0,
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

import math
def p_correlation(input_data,p1,p2):
    
    
    # finding the list of common items between person 1 and person 2
    common = {}
    for item in input_data[p1]:
        if item in input_data[p2]:
            common[item] = 1
    
    # If there are no items in common, then returning 0
    if len(common) == 0:
        return 0
    
    n = len(common)
    
    # finding sigma(x) and sigma(y)
    sigma_x = sum([input_data[p1][item] for item in common])
    sigma_y = sum([input_data[p2][item] for item in common])
    
    # finding sigma_xsquare and sigma_ysquare
    sigma_xsquare = sum([pow(input_data[p1][item], 2) for item in common])
    sigma_ysquare = sum([pow(input_data[p2][item], 2) for item in common])
    
    # finding sigma(xy)
    sigma_xy = sum([input_data[p1][item] * input_data[p2][item] for item in common])
    
    # Calculations for Pearson score
    s_xy = sigma_xy - sigma_x * sigma_y / n
    s_xx = sigma_xsquare - pow(sigma_x, 2) / n
    s_yy = sigma_ysquare - pow(sigma_y, 2) / n
    denominator = math.sqrt(s_xx * s_yy)
    if denominator == 0:
        return 0
    
    #pearson correlation score(r)
    r = s_xy / denominator
    #print(r)
   
    return r

def TopNPersons(input_data,p1,n=3):
    #print(type(p1))
    #finding the pearson correlation scores for a given person with all the other persons and arranging them in a list
    scores = [(p_correlation(input_data, p1, other),other) for other in input_data if other != p1]
    #print(scores)
    scores.sort(reverse = True)
    return scores

import sys

H = TopNPersons(critics,sys.argv[1],n=5)
for i in range(len(H)):
   print(H[i])
sys.stdout.flush()


# In[ ]:




