# Document Classifier
<br/>
The aim of this study is to identify a model which will accurately predict the category of a specific document. Currently, the task of categorizing a document is done manually by a person. Automating this process will allow the person to focus on other strategic activities. In the organization, hundreds of documents are produced each year and this model can be used for other document classification tasks.
<br/>
The documents for classification are taken from the UN website, called [Policy Portal](https://policy.un.org). This site contains administrative policy documents categorized by key thematic areas. You can follow the detailed analysis in the [Jupyter notebook](https://github.com/cdungca/document-classifier-final/blob/main/main.ipynb).
<br/>
## Data Collection and Preparation
<br/>
The data that needed for this study will be the actual text in each document and the category it was assigned to. The process of extracting these information and compiling it to a usable format will be as follows:
<br/>
- The links to the documents with their corresponding category can be extracted from the [Search Portal](https://policy.un.org/policy-all) page. There's a utility script to scrape the links and their assigned category and write them in a csv file.
- After collecting the links, there's another script that will read each pdf and extract the full text.  
- The final data set will be a csv file with the actual full text and the category assigned.
<br/>
To prepare the data for the analysis/modeling, the following steps and transformations were done:
<br/>
- Remove rows with null values.
- Change all texts to lower case.
- Remove stop words. Stop words are common words such as and, the, an, which provide little meaning in the document.
- Remove punctuation marks.
- Perform tokenization. This process breaks down the full text into words.
<br/>
The data can now be used in the analysis and modeling.
<br/>
## Data Analysis
<br/>
After loading the data, here are a couple of observations on the data set:
<br/>
1. There are 189 documents and each are labeled with a single category.
<br/>
2. The four categories in the data set are Accountability, Health and Wellbeing, Human Resources, and Travel. <br/>
<br/>
Here's a breakdown of the number of documents per category:<br/>
<br/>
|Category|Number of Documents|
|--------|-------------------|
|Accountability|40|
|Health and Wellbeing|11|
|Human Resources|64|
|Travel|74|
<br/>
As seen above, there's an imbalance in the data set particularly for the category, Health and Wellbeing. There are only 11 documents for this category compared to the rest which contains around 40 - 74. 
<br/>
Below is the breakdown in graphical form:
<br/>
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/category_freq.png "Number of samples per Category")
<br/>
3. Each document contains different number of words. The box plot below shows further information on the word count per category:
<br/>
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/boxplot.png "Word Count Box Plot")
<br/>
The green line represents the median word count in each category and as observed, the average word count is less than 5,000 for all categories. The word count distribution for Accountability is larger than the rest with a document containing more than 20,000 words. Health and Wellbeing has the smallest range for word count and both Human Resources and Travel are almost the same.
<br/>
Here's the word count distribution across the entire data set:
<br/>
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/dist_wc_zoom.png "Word Count Distribution")
<br/>
Again, most of the documents can be found on the left side of the graph. The word count for these are between 0 to 5,000.
<br/>
3. The figure below shows the most common words in the data set.
<br/>
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/wordcloud.png "Most Common Words in the Data Set")
<br/>
Before modeling, the data set will be split into: 70% training and 30% test set.
<br/>
Training set contains 132 documents.<br/>
Test set contains 57 documents.
<br/>
## Modeling
<br/>
The goal is to find the best model which can accurately predict the category of the document. For this use case, each document is only assigned to a single category. The models that will be used are:
<br/>
- Logistic Regression
- Naive Bayes
- Support Vector Machine
- XGBoost
<br/>
Each model will also be compared to a baseline model. The baseline model randomly predicts the category. 
<br/>
Unlike in other use cases, e.g. cancer diagnosis, where the cost for misclassification is high, true positive rate or recall will be used to evaluate the performance of the model.  This is the proportion of all actual positives that were classified correctly as positives.
<br/>
Aside from comparing different models, different feature extraction techniques (bag-of-words and term frequency-inverse document frequence) and hyperparamaters will be used to come up with the most performant model based on the recall score. 
<br/>
Here are the recall scores for the different settings between train and test sets:
<br/>
### Bag-of-words
<br/>
|Model|Train Micro Recall Score|Test Micro Recall Score|
|-----------------|---------------|--------------|
|Baseline Model|0.30|0.33|
|Logistic Regression - Default Parameters|0.95|0.68|
|Naive Bayes - Default Parameters|0.91|0.74|
|Support Vector Machine - Default Parameters|0.63|0.53|
|**XGBoost - Default Parameters**|0.95|**0.75**|
|Logistic Regression - Best Parameters|0.95|0.65|
|Naive Bayes - Best Parameters|0.81|0.74|
|Support Vector Machine - Best Parameters|0.79|0.58|
|XGBoost - Best Parameters|0.95|0.68|
<br/>
### Term frequency-inverse document frequency (TF-IDF)
<br/>
|Model Combination|Train AUC Score|Test AUC Score|
|-----------------|---------------|--------------|
|Baseline Model|0.27|0.28|
|Logistic Regression - Default Parameters|0.91|0.74|
|Naive Bayes - Default Parameters|0.85|0.72|
|Support Vector Machine - Default Parameters|0.95|0.72|
|XGBoost - Default Parameters|0.95|0.67|
|Logistic Regression - Best Parameters|0.94|0.74|
|Naive Bayes - Best Parameters|0.86|0.70|
|Support Vector Machine - Best Parameters|0.92|0.68|
|XGBoost - Best Parameters|0.95|0.61|
<br/>
## Conclusion and Next Steps
<br/>
### Best Model
<br/>
The best model with the highest micro recall score on the test set is XGBoost using bag-of-words with default parameters.
<br/>
The Micro Recall Score using the test set is **0.75**. The perfect score for the recall is 1.0.
<br/>
To further explore the performance of this model, the ROC AUC (area under the cureve) score is used.  ROC AUC shows the performanc of the model at various threshold settings. 
<br/>
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/roc_best.png "ROC AUC")
<br/>
Finally, the confusion matrix below shows the performance of the model on accurately predicting the correct category on the unseen test set.
<br/>
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/cm_best.png "Confusion Matrix")
<br/>
The model correctly predicted the actual category each class:
<br/>
Accountabily - **10 out of 12**<br/>
Health and Wellbeing - **3 of 3**<br/>
Human Resources - **10 out of 19**<br/>
Travel - **20 out of 23**
<br/>
#### SHAP Analysis
<br/>
Here are some graphs that shows the most important words that contributed for each category:
<br/>
**Most Important Words for Accountability**
<br/>
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/shap_accountability.png "SHAP Accountability")
<br/>
**Most Important Words for Health and Wellbeing**
<br/>
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/shap_health.png "SHAP Health")
<br/>
**Most Important Words for Human Resources**
<br/>
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/shap_hr.png "SHAP HR")
<br/>
**Most Important Words for Travel**
<br/>
![alt text](https://github.com/cdungca/document-classifier-final/blob/main/images/shap_travel.png "SHAP Travel")
<br/>

### Next Steps
<br/>
For possible future improvements, the following can be explored:
<br/>
- As seen in the initial analysis, there's an imbalance in the data set and getting additional samples can improve the model.
- Due to resource constraints, only a maximum of 1,000 features where used in the modeling. Further increasing and testing it might be beneficial.
- Deep learning, recurrent neural network, and transformer architecture should be tested in the next iteration.




