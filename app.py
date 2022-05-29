import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests

def get_poster(movie_id):
     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ba6c16c3663125a5133b9aa773f7c01c&language=en-US'.format(movie_id))
     data = response.json()
     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]
     distances = similarity[movie_index]
     movies_list = sorted(list(enumerate(distances)),reverse=True, key=lambda x:x[1])[0:11]
     recommended_movies = []
     recommendedMoviesPosters=[]
     for i in movies_list:
          movie_id = movies.iloc[i[0]].movie_id
          #poster API
          recommended_movies.append(movies.iloc[i[0]].title)
          recommendedMoviesPosters.append(get_poster(movie_id))
     return recommended_movies, recommendedMoviesPosters

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
st.title('Movie Recommendation Engine')

similarity=pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox(
     'Choose your movie',
     movies['title'].values)

if st.button('Search'):
     names, posters=recommend(selected_movie_name)
     col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11 = st.columns(11)
     with col1:
          st.text(names[0])
          st.image(posters[0])
     with col2:
          st.text(names[1])
          st.image(posters[1])

     with col3:
          st.text(names[2])
          st.image(posters[2])
     with col4:
          st.text(names[3])
          st.image(posters[3])
     with col5:
          st.text(names[4])
          st.image(posters[4]+'\n')
     st.text("\n")
     st.text("\n")
     with col6:
          st.text(names[5])
          st.image(posters[5])
     with col7:
          st.text(names[6])
          st.image(posters[6])
     with col8:
          st.text(names[7])
          st.image(posters[7])
     with col9:
          st.text(names[8])
          st.image(posters[8])
     with col10:
          st.text(names[9])
          st.image(posters[9])
     with col11:
          st.text(names[10])
          st.image(posters[10])



