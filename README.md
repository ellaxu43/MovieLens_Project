# MovieLens_Project

## Project Description
Recommendation systems have revolutionized e-commerce. Companies like Amazon
sell all manner of products to their customers and actively collect reviews 
which are stored in massive databases. Machine learning tools are
then used to recommend products across the full range of customers in a tailored
and highly specific way. This process enables data driven companies to increase 
their pool of satisfied returning consumers. This same process is also used 
to great effect by media companies such as youtube, youtube music and Netflix.

In 2006, Netflix issued a challenge to data scientists worldwide. It was quite
simple, $1 million dollars would be awarded to the team or individual that could
improve the recommendation algorithm by 10%. The winners were announced in 2009.

## Project Goal

We are accessing the MovieLens dataset which consists of 100k ratings on 3,900 movies from 6,040 MovieLens users. Our goals include predicting movie rating that more accurately provide personalized content for the modern consumers.Our main objective is to predict movie recommendations using MovieLens dat.

# Project Planning
Plan -> Acquire -> Prepare -> Explore -> Model & Evaluate -> Deliver
Planning:

***Create a README file (check!)***
* Ensure my dataprep.py modules are well documents and functional

***Acquisition***

* Obtain Zillow data from Codeup mySQL database via dataprep.py

***Preparation***

* Clean Zillow data from Codeup mySQL database via wrangldataprepe.py


***Exploration and Pre-processing***

* Ask and answer statistical questions about the Zillow data
* Visually represent findings with charts

***Exploration and Clustering***
* Clustering Algorithm KMeans to find clusters within the data to improve our estimate of the log error.

***Modeling***

* Split data appropriately
* Use knowledge acquired from statistical questions to help choose a model
* Create a predictions csv file from the best model

# Data Dictionary
GroupLens Research currently operates a movie recommender based on
collaborative filtering:

        http://www.movielens.org/

DETAILED DESCRIPTIONS OF DATA FILES
==============================================

Here are brief descriptions of the data.

ml-data.tar.gz   -- Compressed tar file.  To rebuild the u data files do this:
                gunzip ml-data.tar.gz
                tar xvf ml-data.tar
                mku.sh

u.data     -- The full u data set, 100000 ratings by 943 users on 1682 items.
              Each user has rated at least 20 movies.  Users and items are
              numbered consecutively from 1.  The data is randomly
              ordered. This is a tab separated list of 
	         user id | item id | rating | timestamp. 
              The time stamps are unix seconds since 1/1/1970 UTC   

u.info     -- The number of users, items, and ratings in the u data set.

u.item     -- Information about the items (movies); this is a tab separated
              list of
              movie id | movie title | release date | video release date |
              IMDb URL | unknown | Action | Adventure | Animation |
              Children's | Comedy | Crime | Documentary | Drama | Fantasy |
              Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
              Thriller | War | Western |
              The last 19 fields are the genres, a 1 indicates the movie
              is of that genre, a 0 indicates it is not; movies can be in
              several genres at once.
              The movie ids are the ones used in the u.data data set.

u.genre    -- A list of the genres.

u.user     -- Demographic information about the users; this is a tab
              separated list of
              user id | age | gender | occupation | zip code
              The user ids are the ones used in the u.data data set.

u.occupation -- A list of the occupations.
# Steps to Reproduce
You will need your own env file with database credentials along with all the necessary files listed below to run the "Final Report" notebook.

Read this README.md

Download at the aquire.py and Final Report.ipynb file into your working directory

Create a .gitignore for your .env file

Add your own env file to your directory with username, password, and host address.

Import Basemap package. 

Run the final_report.ipynb notebook

# Initial Questions:
### What are the Top 10 most rated movies? 
### What are the Top 10 highest rated movies? 
### Distribution of gender? 
### Distribution of occupation?
### Age distribution? 
### Does age impact rating? 
### Does year released date impact rating? 
***
# Model
Select a metric to use for evaluating models and explain why that metric was chosen.
Create and evaluate a baseline model.
Find mean value of target
Set all predictions to that value
Evaluate based on selected evaluation metric
Develop Four models.
Evaluate all four models on the train sample, note observations.
Evaluate the top performing model on the test sample, note observations.
# Key Findings 

There is a relationship between age, and released year in predicting the movie rating. 

Our dataset contains a large number of student followed by educator and engineers.

Most of our users are in the age group of 20-33 (since there are a large number of student)

Most of the movies in the item are released between 1994-1998

Our item have most of the movie of Drama genre followed by comedy genre.

However, the movies listed here are of mixed genre, hence the sum of the count of histogram might not add up.
Most of the female users are from the age group 18,29-30 or 44

I was able to succeffuly design a ML model to predict movie rating.

# Recommendations

 I recommend removing outliers from these columns to improve future modeling.

# Next Steps

With more time I would work on improving the model by adding more parameters.


I would like to dive deeper into the this dataset discover the best combination of cluster and to build a simple content based recomandation system. 