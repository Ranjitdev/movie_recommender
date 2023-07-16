import pandas as pd
import streamlit as st
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import MovieData
from src.pipeline.movie_pipeline import MoviePipe
from src.components.fetch_poster import FetchPoster


class RecommendMovies(MovieData):
    def __init__(self, selected='default'):
        MovieData.__init__(self)
        self.option = ''
        self.__movie_tags_similarities = ''
        self.top_five = []
        self.selected_movie = selected

    def save_features_similarity(self):
        MoviePipe().pickling_similarities()

    def show_names(self):
        try:
            st.title('Movie Recommender System')
            self.option = st.selectbox('Choose a movie', self.titles)
            if st.button('Recommend'):
                st.write(self.option)
                return self.option
        except Exception as e:
            raise CustomException(e, sys)


    def top_five_reccommendation(self):
        try:
            movie_tags_similarities = MoviePipe().load_similarity()
            logging.info('module loaded in streamlit')
            movie_index = self.data[
                self.data['Title'] == self.selected_movie.casefold()
            ].index[0]
            distances = movie_tags_similarities[movie_index]
            recommended = sorted(list(
                enumerate(distances)),
                reverse=True,
                key=lambda x: x[1])[1:6]
            movies_frame = {}
            for i, j in recommended:
                movies_frame[self.data.iloc[i, 1]] = [
                    FetchPoster(movie_id=int(self.data.iloc[i, 0])).get_poster_path(),
                    FetchPoster(movie_id=int(self.data.iloc[i, 0])).get_others()
                ]
            df = pd.DataFrame(movies_frame)
            df.dropna(axis=1, inplace=True)
            top_five = df.iloc[:5, :]
            return top_five
        except Exception as e:
            raise CustomException(e, sys)


if __name__=='__main__':
    RecommendMovies('iron man').top_five_reccommendation()