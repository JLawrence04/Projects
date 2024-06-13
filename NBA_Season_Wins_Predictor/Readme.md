# NBA Team Seasonal Wins Predictor ML Project Readme

As a data science and math student who loves playing and watching basketball, I decided to combine these passions to create a ML model that will predict how many wins an NBA team will get based on a few metrics you give the model. To find the metrics that will most effectively predict a teams wins, I used the random forests ML method where the algorithm runs different subsets of the training data through decision trees. Gini importance is a metric used in Random Forests models to determine the most important/infleuntial features/metrics when the decision trees are making decisions and predictions. From the Gini importance scores given by the Random Forest model I used, I found the 4 most important metrics to predict the amount of wins for a team's season were Estimated Net Rating(Luck adjusted Net Rating), Net Rating, Team PIE(Player Impact Estimate), and True Shooting Percentage. Through trial and error, I noticed adding more metrics led to overfitting and worse results as well, 4 metrics seemed to be a good balance between complexity but not overfitting the data.

## Key Steps Taken in Project
- Data collection from API called NBA_api.
- Preprocessed data and did some data visualizations to gain insights on the data being worked with.
- Standardized and scaled data for ML model so differences between feature values didn't interefere with ML model training and predicting.
- Hyperparameter tuned a Support Vector Machine (SVR) model to find the optimal hyperparameters to use for the SVR ML model for the dataset being used in this project.
- Trained model from data of teams from previous seasons and tested models on teams unforeseen to the model including from seasons not used in training.
- Created interactive web interface for user input and test different metric combinations and their associated predicted amount of wins

## Dataset used
Data was collected using an API called NBA_api, specifically the 'leaguedashteamstats' endpoint. This endpoint included a variety of basic and advanced stats about all teams from previous seasons.

Installation site:[NBA_api](https://pypi.org/project/nba-api/)
[Github of NBA_api](https://github.com/swar/nba_api)
