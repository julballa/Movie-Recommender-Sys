# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
warnings.filterwarnings('ignore')

df = pd.read_csv('u.data', sep='\t', names=['user_id','item_id','rating','timestamp'])

movie_titles = pd.read_csv('Movie_Titles')

df = pd.merge(df, movie_titles, on='item_id')

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings['number_of_ratings'] = df.groupby('title')['rating'].count()

#check relationship between rating and number of ratings
#sns.jointplot(x='rating', y='number_of_ratings', data=ratings)

movie_matrix = df.pivot_table(index='user_id', columns='title', values='rating')

#print(ratings.sort_values('number_of_ratings', ascending=False).head(10))
#lets pick AFO and Contact

AFO_user_rating = movie_matrix['Air Force One (1997)']
contact_user_rating = movie_matrix['Contact (1997)']

similar_to_air_force_one=movie_matrix.corrwith(AFO_user_rating)
similar_to_contact = movie_matrix.corrwith(contact_user_rating)

corr_contact = pd.DataFrame(similar_to_contact, columns=['Correlation'])
corr_contact.dropna(inplace=True)

corr_AFO = pd.DataFrame(similar_to_air_force_one, columns=['correlation'])
corr_AFO.dropna(inplace=True)

corr_AFO = corr_AFO.join(ratings['number_of_ratings'])
corr_contact = corr_contact.join(ratings['number_of_ratings'])

corr_AFO[corr_AFO['number_of_ratings'] > 100].sort_values(by='correlation', ascending=False).head(10)
corr_contact[corr_contact['number_of_ratings'] > 100].sort_values(by='Correlation', ascending=False).head(10)




