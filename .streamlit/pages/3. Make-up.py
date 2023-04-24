import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
import time 
from sklearn.preprocessing import MinMaxScaler


st.image('.streamlit/streamlit_images/Screenshot 2023-04-12 at 00.41.21.png')

#read in the dataset and manipulate
foundation = pd.read_csv("./data_sets/allShades.csv")
foundation.drop(["url", "description", "imgSrc", "imgAlt"], axis=1, inplace=True)
#drop hue = 230.4 due to irregular value - mess up the scaling
foundation = foundation.drop(foundation[foundation['hue'] == 230.4].index)

#initialize the transformer (optionally, set parameters)
my_min_max = MinMaxScaler(feature_range=(0,1))
#fit_transform to the data add to a new column in datatframe 
foundation["hue_scaled"] = my_min_max.fit_transform(foundation[["hue"]])
#drop hue
foundation.drop(["hue"], axis=1, inplace=True)

#foundation_numbers
foundation_numbers = foundation.copy()
foundation_numbers.drop(["index", "brand", "product", "name", "specific", "colorspace", "hex"], axis=1, inplace=True)

#kmeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(foundation_numbers)
foundation_numbers['cluster'] = kmeans.labels_

#removing the cluster column
foundation_numbers_no_cluster = foundation_numbers.copy() 
foundation_numbers_no_cluster.drop(["cluster"], axis=1, inplace = True)

# Calculate the distances
distances = kmeans.transform(foundation_numbers_no_cluster)

# Add the distances as a new column
foundation_numbers['distance'] = distances.min(axis=1)

#foundation drop number columns so we don't have duplictaed 
foundation.drop(['sat', 'lightness', 'hue_scaled'], axis=1, inplace=True)
foundation_clusters = pd.merge(foundation, foundation_numbers, left_index=True, right_index=True)

st.title("Want to try a New Foundation?!")
st.write(""":brown_heart: Input your favourite foundation and your shade below and get five recommendations for new foundations based on the hue, saturation and lightness.""")

product = st.text_input("Enter Your Favourite Foundation")
shade = st.text_input("Enter Your Shade")

if product:
    if shade:
        #create a point/data for the inputed foundation name and shade
        point = foundation_clusters.loc[foundation_clusters['product'] == product, foundation_clusters.columns != 'product'] 
        point = point[(point['specific'] == shade) | (point['name'] == shade)] 

        #copy point
        point_copy = point.copy()

        #drop categorical information
        point.drop(['index', 'brand', 'name', 'specific', 'colorspace', 'hex', 'cluster', 'distance'], axis=1, inplace=True)

        #get the cluster number for the inputed foundation
        cluster_label = point_copy["cluster"].values[0]

        #store dataframe with only the cluster from the inputed foundation and shade (for use in final result)
        foundation_clusters_input = foundation_clusters.loc[foundation_clusters['cluster'] == cluster_label]

        #create a dataframe with points of the same cluster and product type / drop the none number columns to match the point dataframe
        points_with_same_cluster = foundation_clusters_input.drop(['index', 'brand', 'product', 'name', 'specific', 'colorspace', 'hex', 'cluster', 'distance'], axis=1)

        #calculate the euclidean distance between the selected point and all other points in the same cluster
        distances_to_all_points_same_cluster = euclidean_distances(point, points_with_same_cluster)

        #add euclidean distnace values to a list
        ed_list = distances_to_all_points_same_cluster.tolist()[0]
        
        #add list of euclidean distances to a columns in dataframe 
        foundation_clusters_input = foundation_clusters_input.assign(distance_1=ed_list)

        #drop the inputed value 
        foundation_clusters_input = foundation_clusters_input.drop(foundation_clusters_input.loc[(foundation_clusters_input['product'] == product) & ((foundation_clusters_input['specific'] == shade) | (foundation_clusters_input['name'] == shade))].index)

        #sort results but distance 
        results = foundation_clusters_input.sort_values("distance_1").head(5)

        #print dataframe of columns needed
        results_1 = results[["brand", "product", "name", "specific", "distance_1"]]

        st.table(results_1)
