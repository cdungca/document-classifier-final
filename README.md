# Document Classifier: Final Report

This is the first part of the capstone project for [UC Berkeley Professional Certificate in Machine Learning and Artificial Intelligence](https://em-executive.berkeley.edu/professional-certificate-machine-learning-artificial-intelligence). 

The aim of this study is to identify a model which will accurately predict the category of a specific document. Currently, the task of categorizing is done manually by a person upon uploading the document to the site. Automating this process will allow the person to focus more on other strategic activities. This activity can also be used and scaled for other document classification tasks in the organization.

The documents for classification are taken from the UN website, called [Policy Portal](https://policy.un.org). You can follow the analysis in the [Jupyter notebook](https://github.com/cdungca/document-classifier/blob/main/main.ipynb).

## Data Collection and Preparation

To extract the documents with their corresponding category, we will first scrape the links in the [Search Portal](https://policy.un.org/policy-all) page. Once we've collected the urls, we will extract the full text on the pdf documents and save them in a csv file. 

Data cleaning will be done on both csv generation and when we load the data in the Jupyter notebook. In the csv generation, we will be removing line breaks (e.g. \n) and other characters present in the full text extraction. The goal is to only have the words in the full text. 

Here are the high level steps for cleaning and preparing the data in the Jupyter notebook:

1. Remove rows with null values
2. Change all texts to lower case
3. Perform tokenization
4. Remove stop words 
5. Remove non alphabetic texts
6. Apply word lemmatizatiom

## Data Analysis

After loading the data, here is a breakdown of the number of documents per category:

|Category|Number of Documents|
|--------|-------------------|
|Travel|75|
|Human Resources|66|
|Accountability|42|
|Health and Wellbeing|11|




## Modeling

To find the best model for our objective, we will be looking at accuracy in comparing the different models, feature extraction techniques, and hyperparameters.

We will be using DummyClassifier as our baseline model. The accuracy for our baseline model is **38.46%**.

Here are the results using different combinations of model, feature extraction (CountVectorizer and TfidVectorizer), and hyperparameters

#### Word Count Box Plot
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/boxplot.png "Word Count Box Plot")
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/category_freq.png "Category Frequency")
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/cm_log_tuned.png "Confusion Matrix")
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/dist_wc_zoom.png "Category Word Count Distribution Zoomed")
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/dist_wc.png "Category Word Count Distribution")
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/roc_log_tuned.png "ROC AUC")
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/shap_accountability.png "SHAP Accountability")
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/shap_health.png "SHAP Health")
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/shap_hr.png "SHAP HR")
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/shap_travel.png "SHAP Travel")

Here's a summary of the accuracy on unseen/test data:

|Model Combination|Train AUC Score|Test AUC Score|
|-----------------|---------------|--------------|
|CountVectorizer - Baseline Model|0.54|0.49|
|CountVectorizer - Logical Regression - Default Parameters|0.99|0.89|
|CountVectorizer - Logical Regression - Best Parameters|0.99|0.89|
|CountVectorizer - Naive Bayes - Default Parameters|0.98|0.91|
|CountVectorizer - Naive Bayes - Best Parameters|0.98|0.91|
|CountVectorizer - Support Vector Machine - Default Parameters|0.96|0.87|
|CountVectorizer - Support Vector Machine - Best Parameters|0.96|0.87|
|CountVectorizer - XGBoost - Default Parameters|1.00|0.88|
|CountVectorizer - XGBoost - Best Parameters|1.00|0.88|
|TfidVectorizer - Baseline Model|0.49|0.47|
|TfidVectorizer - Logical Regression - Default Parameters|1.00|0.92|
|TfidVectorizer - Logical Regression - Best Parameters|1.00|0.92|
|TfidVectorizer - Naive Bayes - Default Parameters|0.98|**0.91**|
|TfidVectorizer - Naive Bayes - Best Parameters|0.98|0.91|
|TfidVectorizer - Support Vector Machine - Default Parameters|0.96|0.88|
|TfidVectorizer - Support Vector Machine - Best Parameters|0.96|0.88|
|TfidVectorizer - XGBoost - Default Parameters|1.00|0.86|
|TfidVectorizer - XGBoost - Best Parameters|1.00|0.86|

