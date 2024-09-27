# Document Classifier

This is the final report for the capstone project for [UC Berkeley Professional Certificate in Machine Learning and Artificial Intelligence](https://em-executive.berkeley.edu/professional-certificate-machine-learning-artificial-intelligence). 

The aim of this study is to identify a model which will accurately predict the category of a specific document. Currently, the task of categorizing is done manually by a person upon uploading the document to the site. Automating this process will allow the person to focus on other strategic activities. In the organization, hundreds of documents are produced each year and this study can be used to and adapted to other document classification tasks.

The documents for classification are taken from the UN website, called [Policy Portal](https://policy.un.org). This site contains administrative policy documents categorized by key thematic areas. You can follow the detailed analysis in the [Jupyter notebook](https://github.com/cdungca/document-classifier-final/blob/main/main.ipynb).

## Data Collection and Preparation

The data that we need for this study will be the actual text in each document and the category it was assigned to. The process of extracting these information and compiling to a usable format will be as follows"

- The links to the documents with their corresponding category can be extracted from the [Search Portal](https://policy.un.org/policy-all) page. We've created a utility script to scrape the page and write the links and their assigned category in a csv file.
- After collecting the links, there's another script that will read each pdf and extract the full text.  
- The final data set will be a csv file with the actual full text and the category assigned.

Once we have the final data set, ![alt text](https://github.com/cdungca/document-classifier-final/blob/main/data/data.csv "data.csv"), we will perform cleaning and transformation to prepare the data for our analysis and modeling. Here are the steps done before starting with the analysis:

- Remove rows with null values.
- Change all texts to lower case.
- Remove stop words. Stop words are common words such as and, the, an, etc. which provide little meaning in the document.
- Remove punctuation marks.
- Perform tokenization. This process breaks down the full text into words.

## Data Analysis

After loading the data, here are a couple of observations on the data set:

1. There are four categories in the data set, Accountabilit, Health and Wellbeing, Human Resources, and Travel. Here's a breakdown of the number of documents per category:

|Category|Number of Documents|
|--------|-------------------|
|Accountability|40|
|Health and Wellbeing|11|
|Human Resources|64|
|Travel|74|


As seen above, we have an imbalance data set particularly for the category Health and Wellbeing. We only have 11 documents for this category compared to the rest. Below is the breakdown on a graphical form:

![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/category_freq.png "Category Frequency")

2. Each document contains different number of words. Below is a box plot for the number of words for the documents on each category:

![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/boxplot.png "Word Count Box Plot")

The green line represents the average word count in each category and as observed, the average word count is less than 5000. Here's another way of looking at the distribution of the word count:\

![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/dist_wc_zoom.png "Category Word Count Distribution Zoomed")

Again, most of the documents can be found on the left side of the graph. The word count for these are between 0 to 5000.

3. The figure below shows the most common words in the data set.

![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/wordcloud.png "Most Common Words in the Data Set")

The size of the word represent the frequency it appeared in the entire data set.

## Modeling

The goal is to find the best model which can predict the category of the document. For this use case, each document will only be assigned to a single category. We will be testing the following models:

- Logistic Regression
- Naive Bayes
- Support Vector Machine
- XGBoost

Each model will also be compared to a baseline model which will serve as a benchmark. The baseline model randomly predicts the category. 

We will also be using different techniques to extract the features in the full text. These are:

- Bag-of-words
- TF-IDF

Finally, we will tune the parameters until we find the best performance based on our metric.

We will be using DummyClassifier as our baseline model. The accuracy for our baseline model is **38.46%**.

Here are the results using different combinations of model, feature extraction (CountVectorizer and TfidVectorizer), and hyperparameters

Here's a summary of the metrics on unseen/test data:

##### Bag-of-words
|Model Combination|Train AUC Score|Test AUC Score|
|-----------------|---------------|--------------|
|Baseline Model|0.54|0.56|
|Logistic Regression - Default Parameters|1.00|0.88|
|Logistic Regression - Best Parameters|1.00|0.88|
|Naive Bayes - Default Parameters|0.99|0.91|
|Naive Bayes - Best Parameters|0.99|0.91|
|Support Vector Machine - Default Parameters|0.94|0.84|
|Support Vector Machine - Best Parameters|0.94|0.84|
|XGBoost - Default Parameters|1.00|0.88|
|XGBoost - Best Parameters|1.00|0.86|

##### TF-IDF
|Model Combination|Train AUC Score|Test AUC Score|
|-----------------|---------------|--------------|
|Baseline Model|0.56|0.59|
|Logistic Regression - Default Parameters|0.99|0.90|
|Logistic Regression - Best Parameters|0.99|0.90|
|Naive Bayes - Default Parameters|0.96|**0.89**|
|Naive Bayes - Best Parameters|0.96|0.89|
|Support Vector Machine - Default Parameters|1.00|0.88|
|Support Vector Machine - Best Parameters|1.07|0.88|
|XGBoost - Default Parameters|1.00|0.86|
|XGBoost - Best Parameters|1.00|0.86|

### Best Model

![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/cm_log_tuned.png "Confusion Matrix")

![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/roc_log_tuned.png "ROC AUC")

#### SHAP Analysis

![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/shap_accountability.png "SHAP Accountability")
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/shap_health.png "SHAP Health")
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/shap_hr.png "SHAP HR")
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/shap_travel.png "SHAP Travel")



