import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
import time 

st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-11 at 13.37.47.png")
# st.subheader("Contact Info:")
# st.write("""
# :arrow_forward: London :arrow_forward: 07876744960 :arrow_forward: abigailflynn@icloud.com :arrow_forward: www.linkedin.com/in/abigail-flynn :arrow_forward: www.github.com/abiflynn""")

col1, col2 = st.columns([1.5,3])

with col1:
   st.header("")
   st.image("/Users/abigailflynn/Desktop/WBS CODING /Final Project /streamlit_images/Screenshot 2023-04-06 at 11.56.45.png")
   st.subheader("Contact Information:")
   st.write("""	:arrow_forward: Number: 07876744960""")
   st.write("""	:arrow_forward: Email: abigailflynn@icloud.com""")
   st.write("""	:arrow_forward: GitHub: www.github.com/abiflynn""")
   st.write("""	:arrow_forward: LinkedIn: www.linkedin.com/in/abigail-flynn""")

with col2:
   st.title("About Me:")
   # st.write(""":round_pushpin: London""")
   st.write("""🎓 BA (Hons) Buying and Merchandising""")
   st.write(""":computer: Data Science Bootcamp Graduate: WBS Coding School""")
   
   st.write("""I am an accomplished analyst and merchandiser seeking to transition my career to a data science role. With over four years of experience as a Merchandiser at retail giant Next, I have enhanced my numerical and analytical skills and developed strong communication, teamwork, and management skills.

Having always had a strong passion for problem solving, I moved into a Project Analyst role. In this position, I led multiple projects across various areas within Next to invent new processes and implement them effectively. Through this role, I gained invaluable skills in stakeholder management, leadership, and data analysis.

I am passionate about using data analysis to influence business decisions and drive growth and profitability. To further develop my skills in this area, I recently completed the Data Science Bootcamp at the WBS Coding School. 

Through this program, I gained a comprehensive understanding of the data science field and developed a range of technical skills, including SQL, Python, Machine Learning, Cloud Computing, Automation, Tableau, and A/B Testing.

As a quick learner who enjoys embracing new challenges, I am excited about the next steps in my career and look forward to developing my skills further make a valuable contribution and help drive growth and success.
""")


# st.write("""
# :telephone_receiver: 07876744960 :email: abigailflynn@icloud.com :large_blue_square: www.linkedin.com/in/abigail-flynn	:large_purple_square: www.github.com/abiflynn""")

# st.title("Contact Info:")
# st.write("""
# :telephone_receiver: 07876744960 :email: abigailflynn@icloud.com :large_blue_square: www.linkedin.com/in/abigail-flynn	:large_purple_square: www.github.com/abiflynn""")

# :telephone_receiver: Number: 07876744960 :email: Email: abigailflynn@icloud.com :large_blue_square: LinkedIn: www.linkedin.com/in/abigail-flynn	:large_purple_square: GitHub: www.github.com/abiflynn""")

# st.write("""	:arrow_forward: LinkedIn: www.linkedin.com/in/abigail-flynn""")
# st.write("""	:arrow_forward: GitHub: www.github.com/abiflynn""")
# st.write("""	:arrow_forward: Number: 07876744960""")
# st.write("""	:arrow_forward: Email: abigailflynn@icloud.com""")

    