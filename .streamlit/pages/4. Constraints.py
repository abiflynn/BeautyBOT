import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
import time 
from sklearn.preprocessing import MinMaxScaler

st.image('/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-11 at 17.12.19.png')

st.write("""As with any recommendation system the lack of comprehensive data was a major limitation of this project. Without a thorough understanding of user preferences, behaviors, and demographics, the system is unable to make accurate and personalised recommendations. Additionally, using a limited dataset can also limit the input options available for users, which can negatively impact the customer experience.
""")
         
col1, col2 = st.columns(2)

with col1:
    st.subheader('Consumer Facing Limitations:')
    st.write(""" 
    - User inputs must be written the same as they appear in the dataset, including spelling, grammer and capitalisation. 
    - Recommenders will only work for brands/products/shades that are included in the datasets that were available. Meaning certain brands and products will be unavailable to the consumers.  
    """)
    st.subheader('Data Limitations:')
    st.write("""
     - **User to User Data:** Reviews, rankings and ratings. 
     - **Sales Data:**  Current most popular products by sales.
     - **New Releases:** Newest products on the market.
     - **User Shopping Habits:** Previous purchases, clicks and products viewed.
     - **Product Information:** Missing information price, gender and size.""")


with col2:
    st.title("")
    st.title("")
    st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-11 at 21.13.52.png")

st.subheader('Future Capabilities:')
st.write("""If these limitations were not a factor, the project could evolve to include data on user demographics, behaviours, preferences, and past interactions, allowing for a more personalised and effective approach to recommendations. As well as this with access to sales and market data this interface would be able to include recommendations based on sales, new releases and market trends. With a bigger dataset including more brands and products the blue sky future of BeautyBOT is to become the Netflix of Beauty.
""")

st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-11 at 22.37.36.png")
st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-10 at 17.40.31.png")
st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-10 at 17.39.47.png")

# col3, col4 = st.columns(2)

# with col3:
#     st.title("")
#     st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-11 at 21.13.52.png")

# with col4:
#     st.title("")
#     st.subheader('Future Capabilities:')
#     st.write(""" 
#     - User inputs must be written the same as they appear in the dataset, including spelling, grammer and capitalisation. 
#     - Recommenders will only work for brand/products/shades that are included in the dataset that were available. Meaning certain brands and products will be unavailable to the consumers.  
#     """)