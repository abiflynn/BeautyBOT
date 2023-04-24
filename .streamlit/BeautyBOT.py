import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
import time 
import altair as alt

#set a page BeautyBOT 
st.set_page_config(layout="wide",
     page_title="BeautyBOT THIS"
     #page_icon=""
)

#beautybot title
st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-10 at 17.42.57.png")
#images banner
st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-10 at 17.42.48.png")
#black line 
st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-10 at 17.39.47.png")

#opening 
st.title("Welcome to BeautyBOT!")
st.write(""":cherry_blossom:**BeautyBOT** is a brand neutral beauty interface here to provide unbiased recommendations to consumers, helping them navigate the overwhelming number of choices in the beauty industry.BeautyBOT works across the three key areas of the beauty industry.

1. Fragrance
2. Makeup 
3. Skincare

### What can BeautyBOT do?

By using unsupervised machine learning to analyse the features of a user's favourite products, BeautyBOT can recommend new products that are similar to their specific needs and preferences.

- Looking for a new perfume but not sure what you like?
- Do you need a new moisturiser that’s right for your skin?
- Want to try a new foundation but struggling to choose?

### Why BeautyBOT?

The beauty industry is the fastest growing non-food retail sector and is predicted to continue growing strongly, +17% to 2027. 

""")
         
data = {'Year': [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027],
        'Value': [72.37, 80.74, 93.05, 103.8, 108.4, 113.2, 118.5, 125.4]}

df = pd.DataFrame(data)

chart = st.bar_chart(df.set_index('Year')['Value'])
#chart.set_axis_labels("Year", "Revenue in Billions USD")

st.write("""Due to the strong predicted growth of the beauty industry non-specialist retailers are now also entering the market and it is therefore becoming highly saturated. 

**70%** of beauty consumers are overwhelmed by too many beauty product choices.

With the rise of online shopping, accelerated by the COVID-19 pandemic, and the growing demand for personalisation, consumers are becoming increasingly demanding and expecting immediate results. BeautyBOT can meet these expectations by providing instant recommendations that are tailored to each individual user.

As the beauty industry continues to grow, it is clear that retailers need to turn to technology to set themselves apart and provide more personalised experiences for their customers.

BeautyBOT is at the forefront of this trend, offering a solution that provides customers with detailed recommendations from across all brands and products, without the need to download multiple apps, essentially becoming the Netflix of beauty.

### "Netflix of Beauty" 

Companies that can provide the most innovative and personalised experiences for their customers will be the ones that succeed. A brand-neutral interface, such as BeautyBOT, that offers unlimited recommendations, will help retailers drive growth and increase sales and profits.""")

st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-10 at 17.40.31.png") 
st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-10 at 17.39.47.png")        
st.title("BeautyBOT: Recommenders")


col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("")
   st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-06 at 12.11.13.png")
   st.write("""
    - Input your gender and BeautyBOT will generate the top 5 male/female fragrances based on user ratings.
    - Input your favourite fragrance and BeautyBOT will recommend you 5 more fragrances based on the scent, base notes and middle notes.""")

with col2:
   st.subheader("")
   st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-06 at 12.11.26.png")
   st.write("""
    - Input your favourite skincare product and BeautyBOT will recommend you 5 products of the same product type based on the ingredients.
    - BeautyBOT will also recommend you 5 products from different product types based on the ingredients.""")

with col3:
   st.subheader("")
   st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-06 at 12.11.20.png")
   st.write("""
    - Input your favourite foundation product and BeautyBOT will recommend you 5 other foundations based on the hue, saturation and lightness.""")

st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-10 at 17.39.47.png")    
