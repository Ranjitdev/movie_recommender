from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import os
import sys
from src.utils import save_obj, load_obj
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=5000, stop_words='english')
from sklearn.metrics.pairwise import cosine_similarity
from src.utils import MovieData


def stemmer(obj):
    lis = []
    for i in obj.split(','):
        lis.append(ps.stem(i))
    return ' '.join(lis)


@dataclass
class DataTransformationConfig:
    similarities_file_path = os.path.join('artifacts', 'similarities.pkl')
    features_file_path = os.path.join('artifacts', 'features.pkl')


class MoviePipe(MovieData):
    def __init__(self):
        MovieData.__init__(self)
        self.data_transformation_config = DataTransformationConfig()
        self._similarities = ''
        self._features = ''

    def pickling_similarities(self):
        stemmed_data = self.data['tags'].apply(stemmer)
        features_array = cv.fit_transform(stemmed_data).toarray()
        movie_similarities = cosine_similarity(features_array)
        save_obj(
            file_path=self.data_transformation_config.features_file_path,
            obj=features_array
        )
        logging.info('Features pickling done')
        save_obj(
            file_path=self.data_transformation_config.similarities_file_path,
            obj=movie_similarities
        )
        logging.info('Similarity Pickling done in pipeline')


    def load_similarity(self):
        try:
            self._similarities = load_obj(
                self.data_transformation_config.similarities_file_path
            )
            # self._features = load_obj(
            #     self.data_transformation_config.features_file_path
            # )
            logging.info('Similarity loading done in pipeline')
            return self._similarities
        except Exception as e:
            raise CustomException(e, sys)