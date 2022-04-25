### Acquire the data function: 
import numpy as np
import pandas as pd
import os
import zipfile

def get_movie_data():
    r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
    with zipfile.ZipFile("ml-100k.zip") as z:
        with z.open("ml-100k/u1.base") as f:
            rating_train = pd.read_csv(f,  sep='\t', names=r_cols,encoding='utf-8')
    #with zipfile.ZipFile("ml-100k.zip") as z:
        with z.open("ml-100k/u1.test") as f:
            rating_test = pd.read_csv(f,  sep='\t', names=r_cols,encoding='utf-8')
            rating_full = pd.concat([rating_train,rating_test], axis=0)
        
    r_cols = ["movie id", "movie title", "release date", "video release date" ,
              "IMDb URL", "unknown" , "Action" , "Adventure" , "Animation" ,
              "Children's", "Comedy",  "Crime" ,  "Documentary" , "Drama" , "Fantasy" ,
              "Film-Noir" , "Horror" , "Musical" , "Mystery",  "Romance" , "Sci-Fi" ,
              "Thriller" , "War" , "Western" ]
    with zipfile.ZipFile("ml-100k.zip") as z:
        with z.open("ml-100k/u.item") as f:
            item = pd.read_csv(f, sep='|',names=r_cols,encoding='latin-1')
        
        
    r_cols = ["user id", "age" , "gender" , "occupation" ,"zip code" ]
    with zipfile.ZipFile("ml-100k.zip") as z:
        with z.open("ml-100k/u.user") as f:
                user = pd.read_csv(f, sep='|',names=r_cols,encoding='latin-1')

    return rating_full, item, user



def wrangle_movie(): 
    rating_full, item, user = get_movie_data()
    user_rating = pd.merge(rating_full, user, left_on="user_id", right_on="user id").drop('user id', axis=1)
    full_rating = pd.merge(user_rating, item, left_on="movie_id", right_on="movie id").drop('movie id', axis=1)
    full_rating = full_rating.loc[full_rating['unknown']!= 1]
    full_rating.drop(columns=['unix_timestamp','IMDb URL','video release date','unknown'], inplace=True)
    full_rating = full_rating.rename(columns = {"movie title" : "movie_title",
                                            "release date" : "release_date",
                                            "Children's": "Children",}) 
    
    full_rating.columns= full_rating.columns.str.lower()
    full_rating['gender'] = full_rating.gender.map({'F': 1, 'M': 0})
    full_rating.release_date = full_rating.release_date.astype('datetime64[ns]')
    full_rating.release_date.fillna(full_rating.release_date.median(), inplace=True)

    return full_rating



def prep_movie_rating(): 
    full_rating =wrangle_movie()
    most_rated = full_rating.groupby('movie_title').size().sort_values(ascending=False)
    most_rated = pd.DataFrame(most_rated).reset_index()
    most_rated = most_rated.rename(columns = {0: "rating_times",}) 

    mean_rating = full_rating.groupby('movie_title').rating.mean().sort_values(ascending=False)
    mean_rating = pd.DataFrame(mean_rating).reset_index()
    mean_rating = mean_rating.rename(columns = {"rating": "mean_rating",
                                           'movie_title' : "drop"}) 
    mean_age = full_rating.groupby('movie_title').age.mean().sort_values(ascending=False)
    mean_age = pd.DataFrame(mean_age).reset_index()
    mean_age = mean_age.rename(columns = {"age": "mean_age",
                                           'movie_title' : "drop"}) 
    full = pd.merge(most_rated, mean_rating, right_on="drop", left_on="movie_title").drop('drop', axis=1)
    
    full = pd.merge(full, mean_age, right_on="drop", left_on="movie_title").drop('drop', axis=1)
    genre=full_rating[['movie_title', 'action', 'adventure',
       'animation', 'children', 'comedy', 'crime', 'documentary', 'drama',
       'fantasy', 'film-noir', 'horror', 'musical', 'mystery', 'romance',
       'sci-fi', 'thriller', 'war', 'western']]
    
    full = pd.merge(full, genre, right_on="movie_title", left_on="movie_title", how ="left")#.drop('movie_title', axis=1)
    full = full.groupby('movie_title').first()
    return full