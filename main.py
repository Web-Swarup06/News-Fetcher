import streamlit as st
import requests

st.header("What's news you wanna know about?")
topic = st.selectbox("Category",['business','entertainment','general','health','science','sports','technology'])

base_url = "https://newsapi.org/v2/top-headlines"

params = {"category":topic if topic else "latest",
          "language":"en",
          "apiKey":<YOUR API KEY>"}

if st.button("Get News"):
    response = requests.get(base_url,params=params)

    if response.status_code == 200:
       news_data = response.json()
       articles = news_data.get("articles",[])

       if articles:
          for i, article in enumerate(articles, start=1):
              st.subheader(f"{i}. {article['title']}")
              st.caption(f"Source: {article['source']['name']}")
              st.write(article['description'] or "No description available.")
              st.markdown(f"[Read More]({article['url']})")
              st.markdown("---")

       else:
          st.warning("No articles found for this search")

    else:
       st.error(f"Failed to retrieve data {response.status_code}") 
