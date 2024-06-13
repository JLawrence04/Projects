# NBA Team Seasonal Wins Predictor ML Project Readme

As a data science and math student who loves playing and watching basketball, I decided to combine these passions to create a ML model that will predict how many wins an NBA team will get based on a few metrics you give the model. To find the metrics that will most effectively predict a teams wins, I used the random forests ML method where the algorithm runs different subsets of the training data through decision trees. Gini importance is a metric used in Random Forests models to determine the most important/infleuntial features/metrics when the decision trees are making decisions and predictions. From the Gini importance scores given by the Random Forest model I used, I found the 4 most important metrics to predict the amount of wins for a team's season were Estimated Net Rating(Luck adjusted Net Rating), Net Rating, Team PIE(Player Impact Estimate), and True Shooting Percentage. Through trial and error, I noticed adding more metrics led to overfitting and worse results as well, 4 metrics seemed to be a good balance between complexity but not overfitting the data.

## Table of Contents
-[Key Steps Taken in Project](#Key-Steps-Taken-in-Project)

## Key Steps Taken in Project
- Data collection from API called NBA_api.
- Preprocessed data and did some data visualizations to gain insights on the data being worked with.
- Standardized and scaled data for ML model so differences between feature values didn't interefere with ML model training and predicting.
- Hyperparameter tuned a Support Vector Regression (SVR) model to find the optimal hyperparameters to use for the SVR ML model for the dataset being used in this project.
- Trained model from data of teams from previous seasons and tested models on teams unforeseen to the model including from seasons not used in training.
- Created interactive web interface for user input and test different metric combinations and their associated predicted amount of wins

## Dataset used
Data was collected using an API called NBA_api, specifically the 'leaguedashteamstats' endpoint. This endpoint included a variety of basic and advanced stats about all teams from previous seasons.

Installation site:[NBA_api](https://pypi.org/project/nba-api/)
[Github of NBA_api](https://github.com/swar/nba_api)

## Model
This project used a Support Vector Regression (SVR) ML model which aims to find a line/hyperplane that best fits the data within a specific margin(epsilon hyperparameter) and penalizes predictions when finding the best hyperplane by a factor of the value set for the C hyperparameter.

The linear kernel ended up being the best performing kernel. Normally the epsilon and C hyperparameters make the SVR regression model using a linear act different than a linear regression model. But through hyperparameter tuning, the best C value was 1 and the epsilon value was .0001. So there was basically no margin of error for the model and the error values were just multiplied by one. This means the SVR model acted like a linear regression model in reducing errors since linear regression models have no margin of errors and just try to reduce the mean squared error where the error isn't multiplied by any C value.

I used the Grid Search algorithm to tune the SVR model and find the best hyperparameters for this model given the dataset the model is being applied to.

## Results/Takeaways
# Results
**The model was very accurate in predicting a team's wins on the test set:**
- Mean Average Error(MAE): 2.38
- Root Mean Squared Error(RMSE): 3.07
- R^2 Score: .932

With an MAE score of 2.38 and RMSE of 3.07 that means the model predicts the wins of an NBA team within an average error of 2.38-3.07 wins(depending on which metric you prefer and preference for weughting different errors) which is pretty accurate considering there are 82 games in a given season.

With R^2 scores being between 0 to 1 and scores closer to 1 indicate better model fit to the data, this model fits and predicts the data well with .932 being considered a very high score.

**I also tested the model on the 2016-2017 NBA season which wasn't used in the training or testing sets:**
- MAE: 2.44
- RMSE: 3.14
- R^2 score: .918

On the unforeseen season the model wasn't exposed to, the model was very accurate and was very close to the level of accuracy the model had on the test set.

**Conclusion:**

The accuracy of this model indicates how just 4 metrics can really pin point how well an NBA team will do in a given season. A model like this can be used in the middle of the NBA season (maybe the quarter of half-way mark) to see if a team is overperforming or underperforming based on their metrics and what to expect from them for the rest of the season.

Through the feature selection for this model, it indicates the importance metrics like TS percentage, and PIE have on NBA wins for a team. So a team looking to improve could look for players that specifically excel at these stats but they might not be huge name players which means they can improve their odds of winning games greatly at a discounted price.

## Interactive Web Interface

As part of this project I created an interactive web interface which was built using the web framework library Streamlit.
Users can use sliders for each metric and adjust them to see real time adjustments in the predicted wins for a team with the theoretical metrics inputted.

The web application can be accessed at this url: https://nba-wins-predictor.streamlit.app/
