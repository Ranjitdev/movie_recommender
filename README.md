# Movie Recommender

## Overview of Amazon sales data analysis: -  
**Its movie time, watch movies you liked most just type a movie name and get 5 similar movies.**

## Data location: -  
- data:
  - Processed data: [Here](notebook/data.csv)
  - credits raw data: [Here](notebook\tmdb_5000_credits.csv)
  - Moviees raw data: [Here](notebook\tmdb_5000_movies.csv)
  - Features pickle: [Here](artifacts\features.pkl)
  - Similarities pickle: [Here](artifacts\similarities.pkl)
- project notebook: [notebook](data\Untitled.ipynb)  


## Setup: -
  - Run for create virtual environment
    - > conda create -p venv python=3.10 -y
  - Run before start application: -
    - > pip install -r requirements.txt
  - Run the application
    - > streamlit run app.py
  - Run for create docker image: -
    - > docker build -t ranjitkundu/car_price_predictor:v1 .
  - Show docker images: -
    - > docker images
  - Run the docker image in container: - 
    - > docker run -p 8501:8501 ranjitkundu/car_price_predictor:v1
  - Initiate GitHub: -
    - > git init
  - Add all files in GitHub: -
    - > git add .
  - Commit code in GitHub: -
    - > git commit -m "message"
  - Push code in GitHub: -
    - > git push -u origin main