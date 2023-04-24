import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances
import time 

st.image(".streamlit/streamlit_images/Screenshot 2023-04-10 at 18.27.54.png")

skincare_clusters = pd.read_csv("./exported_csvs/skincare_clusters.csv")

st.title("Looking for a New Skincare Product?!")

st.write(""":brown_heart: Input your favourite skincare product below and get five recommendations for the same product type based on the ingredients.""")

product_name = st.text_input("Enter Your Favourite Skincare Product Here:")

values = st.slider(
    'Select a Price Range:',
    0.0, 230.0, (1.95, 220.0))
min_price, max_price = values
st.write('Price Range:', values)

if product_name:
    if values:
        progress_bar = st.progress(0)
        for perc_completed in range(100):
            time.sleep(0.02)
            progress_bar.progress(perc_completed+1)



if product_name:

    #create a point/data for the imputed fragrance name
    point = skincare_clusters.loc[skincare_clusters['product_name'] == product_name, skincare_clusters.columns != 'product_name']
    #select the product type
    product_type = point.iloc[0]['product_type']

    st.header(f"{product_type}s With Similar Ingredients" )

    #drop
    point.drop(['distance', 'product_url', 'product_type', 'price', 'ingredient_1', 'ingredient_2', 'ingredient_3', 'ingredient_4', 'ingredient_5', 'ingredient_6', 'ingredient_7', 'ingredient_8', 'ingredient_9', 'ingredient_10', 'ingredient_11', 'ingredient_12', 'ingredient_13', 'ingredient_14', 'ingredient_15', 'ingredient_16', 'ingredient_17', 'ingredient_18', 'ingredient_19', 'ingredient_20', 'ingredient_21', 'ingredient_22', 'ingredient_23', 'ingredient_24', 'ingredient_25', 'ingredient_26', 'ingredient_27', 'ingredient_28', 'ingredient_29', 'ingredient_30', 'ingredient_31', 'ingredient_32', 'ingredient_33', 'ingredient_34', 'ingredient_35', 'ingredient_36', 'ingredient_37', 'ingredient_38', 'ingredient_39', 'ingredient_40', 'ingredient_41', 'ingredient_42', 'ingredient_43', 'ingredient_44', 'ingredient_45', 'ingredient_46', 'ingredient_47', 'ingredient_48', 'ingredient_49', 'ingredient_50', 'ingredient_51', 'ingredient_52', 'ingredient_53', 'ingredient_54', 'ingredient_55',
        'ingredient_56', 'ingredient_57', 'ingredient_58', 'ingredient_59', 'ingredient_60', 'ingredient_61', 'ingredient_62', 'ingredient_63', 'ingredient_64', 'ingredient_65', 'ingredient_66', 'ingredient_67', 'ingredient_68', 'ingredient_69', 'ingredient_70', 'ingredient_71', 'ingredient_72', 'ingredient_73', 'ingredient_74', 'ingredient_75', 'ingredient_76', 'ingredient_77', 'ingredient_78', 'ingredient_79', 'ingredient_80', 'ingredient_81', 'ingredient_82', 'ingredient_83', 'ingredient_84', 'ingredient_85', 'ingredient_86', 'ingredient_87', 'ingredient_88', 'ingredient_89', 'ingredient_90'], axis=1, inplace = True)

    #get the cluster number from the inputed fragrance name 
    cluster_label = skincare_clusters["cluster"].loc[skincare_clusters['product_name'] == product_name].values[0]

    #store dataframe with only the cluster from the inputed fragrance (for use in final result)
    skincare_clusters_input = skincare_clusters.loc[skincare_clusters['cluster'] == cluster_label]
    skincare_clusters_input = skincare_clusters_input.loc[skincare_clusters_input['product_type'] == product_type]
    
    #create a dataframe with points of the same cluster and product type / drop the none encoded columns to match the point dataframe
    points_with_same_cluster= skincare_clusters_input.drop(['distance', 'product_name', 'product_url', 'product_type', 'price', 'ingredient_1', 'ingredient_2', 'ingredient_3', 'ingredient_4', 'ingredient_5', 'ingredient_6', 'ingredient_7', 'ingredient_8', 'ingredient_9', 'ingredient_10', 'ingredient_11', 'ingredient_12', 'ingredient_13', 'ingredient_14', 'ingredient_15', 'ingredient_16', 'ingredient_17', 'ingredient_18', 'ingredient_19', 'ingredient_20', 'ingredient_21', 'ingredient_22', 'ingredient_23', 'ingredient_24', 'ingredient_25', 'ingredient_26', 'ingredient_27', 'ingredient_28', 'ingredient_29', 'ingredient_30', 'ingredient_31', 'ingredient_32', 'ingredient_33', 'ingredient_34', 'ingredient_35', 'ingredient_36', 'ingredient_37', 'ingredient_38', 'ingredient_39', 'ingredient_40', 'ingredient_41', 'ingredient_42', 'ingredient_43', 'ingredient_44', 'ingredient_45', 'ingredient_46', 'ingredient_47', 'ingredient_48', 'ingredient_49', 'ingredient_50', 'ingredient_51', 'ingredient_52', 'ingredient_53', 'ingredient_54', 'ingredient_55',
                                    'ingredient_56', 'ingredient_57', 'ingredient_58', 'ingredient_59', 'ingredient_60', 'ingredient_61', 'ingredient_62', 'ingredient_63', 'ingredient_64', 'ingredient_65', 'ingredient_66', 'ingredient_67', 'ingredient_68', 'ingredient_69', 'ingredient_70', 'ingredient_71', 'ingredient_72', 'ingredient_73', 'ingredient_74', 'ingredient_75', 'ingredient_76', 'ingredient_77', 'ingredient_78', 'ingredient_79', 'ingredient_80', 'ingredient_81', 'ingredient_82', 'ingredient_83', 'ingredient_84', 'ingredient_85', 'ingredient_86', 'ingredient_87', 'ingredient_88', 'ingredient_89', 'ingredient_90'], axis=1)

    #calculate the euclidean distance between the selected point and all other points in the same cluster
    distances_to_all_points_same_cluster = euclidean_distances(point, points_with_same_cluster)

    #add euclidean distnace values to a list
    ed_list = distances_to_all_points_same_cluster.tolist()[0]
    
    #add list of euclidean distances to a columns in dataframe 
    skincare_clusters_input = skincare_clusters_input.assign(distance_1=ed_list)

    #drop the inputed value 
    skincare_clusters_input = skincare_clusters_input.drop(skincare_clusters_input[skincare_clusters_input['product_name'] == product_name].index)

    results = skincare_clusters_input.loc[(skincare_clusters_input['price'] >= min_price) & (skincare_clusters_input['price'] <= max_price)]
    results_1 = results.sort_values("distance_1").head(5)

    results_2 = results_1[["product_name", "product_type", "price", "distance_1"]]

    st.table(results_2)

    st.header("Other Skincare Products, You Might Like!")
    st.write(""":brown_heart: Using the ingredients from the product inputted, BeautyBOT has also recommended you some other skincare products which are a good match.""")

    #create a point/data for the imputed fragrance name
    point_o = skincare_clusters.loc[skincare_clusters['product_name'] == product_name, skincare_clusters.columns != 'product_name']
    #select the product type
    product_type_o = point_o.iloc[0]['product_type']
    #drop
    point_o.drop(['distance', 'product_url', 'product_type', 'price', 'ingredient_1', 'ingredient_2', 'ingredient_3', 'ingredient_4', 'ingredient_5', 'ingredient_6', 'ingredient_7', 'ingredient_8', 'ingredient_9', 'ingredient_10', 'ingredient_11', 'ingredient_12', 'ingredient_13', 'ingredient_14', 'ingredient_15', 'ingredient_16', 'ingredient_17', 'ingredient_18', 'ingredient_19', 'ingredient_20', 'ingredient_21', 'ingredient_22', 'ingredient_23', 'ingredient_24', 'ingredient_25', 'ingredient_26', 'ingredient_27', 'ingredient_28', 'ingredient_29', 'ingredient_30', 'ingredient_31', 'ingredient_32', 'ingredient_33', 'ingredient_34', 'ingredient_35', 'ingredient_36', 'ingredient_37', 'ingredient_38', 'ingredient_39', 'ingredient_40', 'ingredient_41', 'ingredient_42', 'ingredient_43', 'ingredient_44', 'ingredient_45', 'ingredient_46', 'ingredient_47', 'ingredient_48', 'ingredient_49', 'ingredient_50', 'ingredient_51', 'ingredient_52', 'ingredient_53', 'ingredient_54', 'ingredient_55',
        'ingredient_56', 'ingredient_57', 'ingredient_58', 'ingredient_59', 'ingredient_60', 'ingredient_61', 'ingredient_62', 'ingredient_63', 'ingredient_64', 'ingredient_65', 'ingredient_66', 'ingredient_67', 'ingredient_68', 'ingredient_69', 'ingredient_70', 'ingredient_71', 'ingredient_72', 'ingredient_73', 'ingredient_74', 'ingredient_75', 'ingredient_76', 'ingredient_77', 'ingredient_78', 'ingredient_79', 'ingredient_80', 'ingredient_81', 'ingredient_82', 'ingredient_83', 'ingredient_84', 'ingredient_85', 'ingredient_86', 'ingredient_87', 'ingredient_88', 'ingredient_89', 'ingredient_90'], axis=1, inplace = True)

    #get the cluster number from the inputed fragrance name 
    cluster_label = skincare_clusters["cluster"].loc[skincare_clusters['product_name'] == product_name].values[0]

    #store dataframe with only the cluster from the inputed fragrance (for use in final result)
    skincare_clusters_input_o = skincare_clusters.loc[skincare_clusters['cluster'] == cluster_label]
    skincare_clusters_input_o1 = skincare_clusters_input_o.loc[skincare_clusters_input_o['product_type'] != product_type_o]
    
    #create a dataframe with points of the same cluster and product type / drop the none encoded columns to match the point dataframe
    points_with_same_cluster_o = skincare_clusters_input_o1.drop(['distance', 'product_name', 'product_url', 'product_type', 'price', 'ingredient_1', 'ingredient_2', 'ingredient_3', 'ingredient_4', 'ingredient_5', 'ingredient_6', 'ingredient_7', 'ingredient_8', 'ingredient_9', 'ingredient_10', 'ingredient_11', 'ingredient_12', 'ingredient_13', 'ingredient_14', 'ingredient_15', 'ingredient_16', 'ingredient_17', 'ingredient_18', 'ingredient_19', 'ingredient_20', 'ingredient_21', 'ingredient_22', 'ingredient_23', 'ingredient_24', 'ingredient_25', 'ingredient_26', 'ingredient_27', 'ingredient_28', 'ingredient_29', 'ingredient_30', 'ingredient_31', 'ingredient_32', 'ingredient_33', 'ingredient_34', 'ingredient_35', 'ingredient_36', 'ingredient_37', 'ingredient_38', 'ingredient_39', 'ingredient_40', 'ingredient_41', 'ingredient_42', 'ingredient_43', 'ingredient_44', 'ingredient_45', 'ingredient_46', 'ingredient_47', 'ingredient_48', 'ingredient_49', 'ingredient_50', 'ingredient_51', 'ingredient_52', 'ingredient_53', 'ingredient_54', 'ingredient_55',
                                    'ingredient_56', 'ingredient_57', 'ingredient_58', 'ingredient_59', 'ingredient_60', 'ingredient_61', 'ingredient_62', 'ingredient_63', 'ingredient_64', 'ingredient_65', 'ingredient_66', 'ingredient_67', 'ingredient_68', 'ingredient_69', 'ingredient_70', 'ingredient_71', 'ingredient_72', 'ingredient_73', 'ingredient_74', 'ingredient_75', 'ingredient_76', 'ingredient_77', 'ingredient_78', 'ingredient_79', 'ingredient_80', 'ingredient_81', 'ingredient_82', 'ingredient_83', 'ingredient_84', 'ingredient_85', 'ingredient_86', 'ingredient_87', 'ingredient_88', 'ingredient_89', 'ingredient_90'], axis=1)

    #calculate the euclidean distance between the selected point and all other points in the same cluster
    distances_to_all_points_same_cluster_o = euclidean_distances(point_o, points_with_same_cluster_o)

    #add euclidean distnace values to a list
    ed_list_o = distances_to_all_points_same_cluster_o.tolist()[0]
    
    #add list of euclidean distances to a columns in dataframe 
    skincare_clusters_input_o1 = skincare_clusters_input_o1.assign(distance_1_o=ed_list_o)

    #drop the inputed value 
    skincare_clusters_input_o1 = skincare_clusters_input_o1.drop(skincare_clusters_input_o1[skincare_clusters_input_o1['product_name'] == product_name].index)

    results_o = skincare_clusters_input_o1.loc[(skincare_clusters_input_o1['price'] >= min_price) & (skincare_clusters_input_o1['price'] <= max_price)]
    results_1_o = results_o.sort_values("distance_1_o").head(10)

    results_2_o = results_1_o[["product_name", "product_type", "price", "distance_1_o"]]

    st.table(results_2_o)

   
