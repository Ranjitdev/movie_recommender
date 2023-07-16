import requests
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
# https://api.themoviedb.org/3/movie/(movie id)?api_key=965366106f072ea0ae0437fe54d96da5&language=en-US
# https://image.tmdb.org/t/p/w500/(poster link)


class FetchPoster:
    def __init__(self, movie_id):
        self.url = (
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=965366106f072ea0ae0437fe54d96da5&language=en-US'
        )
    def get_poster_path(self):
        try:
            response = requests.get(self.url).json()
            path = "https://image.tmdb.org/t/p/w500/" + str(response['poster_path'])
            return path
        except Exception as e:
            logging.info('e')
            return np.nan

    def get_others(self):
        try:
            response = requests.get(self.url).json()
            others = {
                'Homepage' : response['homepage'],
                'Language' : response['original_language'],
                'Title' : response['original_title'],
                'Overview' : response['overview'],
                'Popularity' : response['popularity'],
                'Releasedate' : response['release_date'],
                'Runtime' : response['runtime'],
                'Rating' : response['vote_average'],
                'Votes' : response['vote_count']
            }
            return others
        except Exception as e:
            logging.info('e')
            return np.nan