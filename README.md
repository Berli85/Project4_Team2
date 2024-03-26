# Project4_Team2
This study explores wine variants of “Vinho Verde” wine from Portugal. Team 2 was interested to find any correlation between these wine variants and their features which included fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, and quality score. A database of these features was developed by combining two datasets for machine learning. The machine learning would help with developing a predictive model on wine type (red or white) based on the features. The results would educate the consumer on what aspects make a high-quality wine and its wine type. A third data set was used to bring in cost, region of origin, and rated points to enhance findings from the first and second datasets and determine price points and regions of high-quality wine.

Folders are organized as follows:
1) combined_dataset has all of the code that was developed for machine learning. The machine learning one has all the basic anaylsis on unaltered data, machine learning classification adds the neural network analysis, and finally the one ending in pickle has the imbalance techniques and the final model and h5 file used for the website.
2) second_dataset includes the analysis preformed on the third dataset dealing with regions, ratings, and cost.
3) app has all of the code to build the website
4) presentation, report, and proposal contain the files as titled

   
Overall team 2 found that the XGBClassifier utilizing the SMOTE sampled dataset as the best model for predicting wine types. The features that had the most correlation for determining wine quality were alcohol, density, volatile acidity, and chlorides. Prediciting wine type seemed to be the better approach compared to quality since it had higher correlations based on total sulfur dioxide, volatile acidity, and cholorides.

