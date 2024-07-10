# Traveler Segmentation Utilizing Google Reviews Data
Through some of the data science classes I've taken at Indiana University, I've learned the methodologies and math behind various clustering algorithms and how to apply them to a given dataset. Knowing the importance the insights and information using clustering can have for businesses and others that rely heavily on data collection to make decisions, I wanted to apply my knowledge on clustering on a dataset with practical and real-world applications. While looking through some of the datasets on the UC Irvine Machine Learning Repository, I found this dataset that contains the average Google ratings travelers in Europe gave for 24 different types of attractions travelers can visit. Finding this dataset made me realize through ML clustering algorithms I can categorize travelers based on the different attractions they enjoyed and the insights gained from this clustering is one way a company like a travel agency could give future travelers personalized recommendations on what to visit based on what group they fall into.

## Table of Contents
- [Key Steps Taken in Project](#Key-Steps-Taken-in-Project)
- [Dataset Used](#Dataset-Used)
- [Clustering Methods](#Clustering-Methods)
- [Evaluation Methods](#Evaluation-Methods)
- [Results/Takeaways](#Results/Takeaways)

## Key Steps Taken in Project
- Data collection by fetching data from UCI ML Repository.
- Preprocessed data and cleaned data to get rid of missing values and making sure all value types in the data are consistent for the clustering algorithms.
- Standardized and scaled data for ML model so differences in distributions between attractions didn't influence the clustering algorithms.
- Performed dimensionality reduction using Principal Component Analysis(PCA) to improve and optimize clustering model performances
- Created various data visualizations to gain insights on the data being worked with.
- Experimented with 3 different types of clustering algorithms to find an optimal clustering model for this data.
- Visualized the clusters of the different models to clearly see the trends and characteristics of each traveler group.
- Utilized clustering metrics such as silhouette score, Davies-Bouldin Index score, and Calinski-Harabasz Index score to determine the best clustering model for this data.

## Dataset Used
Dataset was collected from the UC Irvine Machine Learning Repository. This dataset includes the average ratings for 24 different types of attractions for 5456 travelers who went to Europe. Google review ratings range from 1 to 5.

 [UCI ML Repository link to dataset](https://archive.ics.uci.edu/dataset/485/tarvel+review+ratings)


## Clustering Methods
I experimented with 3 different ML clustering algorithms to find an optimal clustering model for this dataset.

**K-Means Clustering Model:**
- One of the most well-known clustering algorithms, for an arbitrary amount of clusters it find the optimal centroid/center coordinates for each cluster by originally starting each centroid at random points and constantly updating the centroid coordinates until no data points are changing cluster assignments. Data points are assigned to the clusters it is closest to.
- The optimal amount of clusters was 4 and to find the optimal amount I used the elbow method and the Within-Cluster Sum of Square(WCSS) metric which is the combined sum of the squared distances between each data point and their respective cluster centroid. So a smaller WCSS means the clusters are more compact which is desired in clustering.

**Spectral Clustering Model:**
- When I created the correlation matrix in the data visualization section, there weren't many linear relationships between variables so I wanted to test out a model meant to cluster non-linear data like spectral clustering.
- It utilizes a similarity matrix(I tested out the rbf and nearest neighbors options) which is used to create a Laplacian matrix. It uses the first arbitray k-amount of eigenvectors to create a new feature space for the data points then uses k-means clustering to make groups based on the new feature space. So basically doing k-means clustering again but transforming the data it sees using a similarity matrix.
- The optimal amount of clusters was 4 and to find the optimal amount of clusters I graphed the silhouette score of different cluster values. Explanation on what the silhouette score means in the Evaluation Methods section.

**Hierarchical Clustering Model:**
- Hierarchical clustering works by treating each point as its own cluster and merging clusters together based on a certain criteria and until a threshold is reached. The three I criteria methods I tested out were complete, average, and ward.
 
  **Complete criteria:** Takes all the maximum distances between groups and merges the clusters with the smallest maximum distance.

  **Average criteria:** Works by averaging all distances between points in grouped in different clusters and averages all the point distances, then you merge the 2 clusters of points with the smallest average distance. 

  **Ward criteria:** Takes all the changes in variance of different cluster groups after merging and saves the merged clusters which have the smallest increase in variance.

- I used a dendrogram that graphs how the clusters are merged to find the right amount of clusters for each criteria method.
- Ward method was deemed best to use and keep since it had the simplest dendrogram and best silouette score, optimal amount of clusters for this model was 3.

## Evaluation Methods
I used 3 metrics to determine which model performed best on the data:

**Silhouette Score:**
On top of using this score to determine the best model, I also used it to determine the parameters of the spectral and hierarchical models. It was also used to determine it was best to use the 2 component PCA transformed data for the models.

Silhouette scores range from 1 to -1 with 1 being the best an -1 being the worst. The silhouette score measures how well a model clusters points based on how similar data points are to the points in its cluster compared to other clusters.

**Davies-Bouldin Index:**
This score measures how well clusters are separated using intra-cluster distances(how compact the clusters are) and inter-cluster distance(how separated the clusters are from each other). Lower scores indicate a better clustering performance.

**Calinski-Harabasz Index:**
Also known as the Variance Ratio Criterion, its the ratio between the separation of clusters and compactness of the clusters, so how it determines which model clusters better is similar to the Davies-Bouldin Index, with this score higher scores mean better clustering.

## Results/Takeaways
### Results
**K-Means Model:**
- Silhouette Score: .442
- Davies-Bouldin Index: .732
- Calinski-Harabasz Index: 5809.09

**Spectral Model:**
- Silhouette Score: .432
- Davies-Bouldin Index: .726
- Calinski-Harabasz Index: 5310.32

**Hierarchical Model:**
- Silhouette Score: .404
- Davies-Bouldin Index: .831
- Calinski-Harabasz Index: 4581.35

The K-means model and spectral model have very similar silhouette and Davies-Bouldin scores with the hierarchical model lacking a lot in both. The main differentiator is the Calinski-Harabasz score, so I concluded the k-means model perfomed best on this dataset.
### Conclusion

Through the usage of k-means clustering we were able to find an effective way of segmentating travelers based on their interests. Given a new traveler added to the database, you could transform the new data point into the PCA feature space then run the data point through the k-means clustering model to label the new traveler in the appropriate group. 

This clustering model can be used as the basis for a travel recommendation system by a company like Google (company the data comes from) or a travel agency to give personalized and useful travel recommendations so travelers can have a more enjoyable experience researching activites to do while on vacation.

