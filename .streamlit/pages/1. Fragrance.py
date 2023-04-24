import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
import time 


st.image('.streamlit/streamlit_images/Screenshot 2023-04-11 at 13.34.24.png')

st.title("Want to try a New Perfume?! Not sure where to Start?!")
st.write(""":brown_heart: Input your favourite below and BeautyBOT will make recommendations using the scents, base notes and middle notes.""")

gender = st.radio("Gender", ("Female", "Male"))

st.header(f"Our Top {gender} Fragrances")
st.write(""":brown_heart: The top fragrances based on user ratings.""")


#read in the dataset
perfume_merge_women = pd.read_csv("./exported_csvs/perfume_merge_women_1.csv")
perfume_clusters_women = pd.read_csv("./exported_csvs/perfume_clusters_women_1.csv")

perfume_merge_men = pd.read_csv("./exported_csvs/perfume_merge_men_1.csv")
perfume_clusters_men = pd.read_csv("./exported_csvs/perfume_clusters_men_1.csv")

if gender == "Female":
    top_perfumes = perfume_clusters_women.sort_values(by='item_rating', ascending=False)[["brand", "name"]].head(5)
    st.table(top_perfumes)
else:
    top_perfumes = perfume_clusters_men.sort_values(by='item_rating', ascending=False)[["brand", "name"]].head(5)
    st.table(top_perfumes)

user_input = st.text_input("Enter Your Favourite Fragrance Here:")

if user_input:
    if user_input not in perfume_merge_women["name"].tolist() and user_input not in perfume_merge_men["name"].tolist():
        st.warning("Information not found for this product")
    else:
        progress_bar = st.progress(0)
        for perc_completed in range(100):
            time.sleep(0.02)
            progress_bar.progress(perc_completed+1)
        st.success("Fragrance Inputed")
        if gender == "Female":
            st.header(f"Fragrances Similar to {user_input}")
            st.write(""":brown_heart: Based on the scents, base notes and middle notes, here are some fragrances we think you will like!""")
        
        #create a point/data for the imputed fragrance name
        point = perfume_clusters_women.loc[perfume_clusters_women['name'] == user_input, perfume_clusters_women.columns != 'name']
        point.drop(['cluster', 'distance', 'brand', 'concentration', 'department', 'scents', 'item_rating', 'base_note_1', 'base_note_2', 'base_note_3', 'base_note_4', 'base_note_5', 'base_note_6', 'base_note_7', 'base_note_8', 'base_note_9', 'base_note_10', 'base_note_11', 'middle_note_1', 'middle_note_2', 'middle_note_3', 'middle_note_4', 'middle_note_5', 'middle_note_6', 'middle_note_7', 'middle_note_8', 'middle_note_9', 'middle_note_10', 'middle_note_11', 'middle_note_12'], axis=1, inplace = True)

        #get the cluster number from the inputed fragrance name 
        cluster_label = perfume_clusters_women["cluster"].loc[perfume_clusters_women['name'] == user_input].values[0]

        #store dataframe with only the cluster from the inputed fragrance (for use in final result)
        perfume_clusters_input = perfume_clusters_women.loc[perfume_clusters_women['cluster'] == cluster_label]

        #create a dataframe with points of the same cluster / drop the none encoded columns to match the point dataframe
        points_with_same_cluster = perfume_clusters_women.loc[perfume_clusters_women['cluster'] == cluster_label]
        points_with_same_cluster_1 = points_with_same_cluster.drop(['cluster', 'distance', 'brand', 'name', 'concentration', 'department', 'scents', 'item_rating', 'base_note_1', 'base_note_2', 'base_note_3', 'base_note_4', 'base_note_5', 'base_note_6', 'base_note_7', 'base_note_8', 'base_note_9', 'base_note_10', 'base_note_11', 'middle_note_1', 'middle_note_2', 'middle_note_3', 'middle_note_4', 'middle_note_5', 'middle_note_6', 'middle_note_7', 'middle_note_8', 'middle_note_9', 'middle_note_10', 'middle_note_11', 'middle_note_12'], axis=1)

        #calculate the euclidean distance between the selected point and all other points in the same cluster
        distances_to_all_points_same_cluster = euclidean_distances(point, points_with_same_cluster_1)

        ed_list = distances_to_all_points_same_cluster.tolist()
        df_ed = pd.DataFrame(ed_list)
        df_ed = df_ed.melt()    

        results = pd.merge(perfume_clusters_input, df_ed, left_index=True, right_index=True)[["brand", "name", "concentration", "department", "scents", "item_rating", "cluster", "value"]]
        results_1 = results.sort_values("value").head(5)
        results_1.drop(["cluster", "value"], axis=1, inplace=True)

        st.table(results_1)

    else:
        st.header(f"Fragrances Similar to {user_input}")
        #create a point/data for the imputed fragrance name
        point = perfume_clusters_men.loc[perfume_clusters_men['name'] == user_input, perfume_clusters_men.columns != 'name']
        point.drop(['cluster', 'distance', 'brand', 'concentration', 'department', 'scents', 'item_rating', 'base_note_1', 'base_note_2', 'base_note_3', 'base_note_4', 'base_note_5', 'base_note_6', 'base_note_7', 'base_note_8', 'base_note_9', 'base_note_10', 'base_note_11', 'middle_note_1', 'middle_note_2', 'middle_note_3', 'middle_note_4', 'middle_note_5', 'middle_note_6', 'middle_note_7', 'middle_note_8', 'middle_note_9', 'middle_note_10', 'middle_note_11', 'middle_note_12'], axis=1, inplace = True)

        #get the cluster number from the inputed fragrance name 
        cluster_label = perfume_clusters_men["cluster"].loc[perfume_clusters_men['name'] == user_input].values[0]

        #store dataframe with only the cluster from the inputed fragrance (for use in final result)
        perfume_clusters_input = perfume_clusters_men.loc[perfume_clusters_men['cluster'] == cluster_label]

        #create a dataframe with points of the same cluster / drop the none encoded columns to match the point dataframe
        points_with_same_cluster = perfume_clusters_men.loc[perfume_clusters_men['cluster'] == cluster_label]
        points_with_same_cluster_1 = points_with_same_cluster.drop(['cluster', 'distance', 'brand', 'name', 'concentration', 'department', 'scents', 'item_rating', 'base_note_1', 'base_note_2', 'base_note_3', 'base_note_4', 'base_note_5', 'base_note_6', 'base_note_7', 'base_note_8', 'base_note_9', 'base_note_10', 'base_note_11', 'middle_note_1', 'middle_note_2', 'middle_note_3', 'middle_note_4', 'middle_note_5', 'middle_note_6', 'middle_note_7', 'middle_note_8', 'middle_note_9', 'middle_note_10', 'middle_note_11', 'middle_note_12'], axis=1)

        #calculate the euclidean distance between the selected point and all other points in the same cluster
        distances_to_all_points_same_cluster = euclidean_distances(point, points_with_same_cluster_1)

        ed_list = distances_to_all_points_same_cluster.tolist()
        df_ed = pd.DataFrame(ed_list)
        df_ed = df_ed.melt()    

        results = pd.merge(perfume_clusters_input, df_ed, left_index=True, right_index=True)[["brand", "name", "concentration", "department", "scents", "item_rating", "cluster", "value"]]
        results_1 = results.sort_values("value").head(5)
        results_1.drop(["cluster", "value"], axis=1, inplace=True)

    st.table(results_1)
