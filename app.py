from src.components.streamlit_run import RecommendMovies
import streamlit as st
import requests

RecommendMovies().save_features_similarity()
selected_movie = RecommendMovies().show_names()
if selected_movie is not None:
    df = RecommendMovies(
        selected=selected_movie
    ).top_five_reccommendation()

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(df.iloc[0, 0])
        st.subheader(df.columns[0])
        st.text('Rating')
        st.text(
            f'{df.iloc[1, 0]["Rating"]}/{df.iloc[1, 0]["Votes"]}'
        )
        st.text('Story')
        st.write(df.iloc[1, 0]['Overview'])

    with col2:
        st.image(df.iloc[0, 1])
        st.subheader(df.columns[1])
        st.text('Rating')
        st.text(
            f'{df.iloc[1, 1]["Rating"]}/{df.iloc[1, 1]["Votes"]}'
        )
        st.text('Story')
        st.write(df.iloc[1, 1]['Overview'])

    with col3:
        st.image(df.iloc[0, 2])
        st.subheader(df.columns[2])
        st.text('Rating')
        st.text(
            f'{df.iloc[1, 2]["Rating"]}/{df.iloc[1, 2]["Votes"]}'
        )
        st.text('Story')
        st.write(df.iloc[1, 2]['Overview'])

    with col4:
        st.image(df.iloc[0, 3])
        st.subheader(df.columns[3])
        st.text('Rating')
        st.text(
            f'{df.iloc[1, 3]["Rating"]}/{df.iloc[1, 3]["Votes"]}'
        )
        st.text('Story')
        st.write(df.iloc[1, 3]['Overview'])

    with col5:
        st.image(df.iloc[0, 4])
        st.subheader(df.columns[4])
        st.text('Rating')
        st.text(
            f'{df.iloc[1, 4]["Rating"]}/{df.iloc[1, 4]["Votes"]}'
        )
        st.text('Story')
        st.write(df.iloc[1, 4]['Overview'])
