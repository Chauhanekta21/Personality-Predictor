# 📊 Personality Predictor

> **Project Status: Completed**

![data](thumbnail.png)

## 📈 Project Overview

This project uses machine learning to predict a person's personality type from their answers to questions about their habits, preferences, and behaviour. The prediction can be one of three types:

- Introvert
- Ambivert
- Extrovert

The project includes a Jupyter Notebook for learning and analysis, along with a Streamlit app that lets users try the personality predictor through a simple web interface.

## 📈 View Project:

🔹 **Personality Predictor Live App:** Answer behavioural questions and see machine learning turn your responses into a personality prediction. 

**Link:** [personality-predictor-streamlit-app](https://personality-predictor-pp.streamlit.app/)

**Personality Predictor App Preview:**

![data](app.png)

🔹 **Jupyter Notebook:** See how raw data becomes a working prediction model through exploration, preprocessing, feature selection, and logistic regression. 

**Link:** [personality-predictor-jupyter-notebook](https://github.com/Chauhanekta21/Personality-Predictor/blob/main/jupyter_notebook/personality_predictor.ipynb)

**Jupyter Notebook Preview:**

![data](jupyter.png)


## 📈 Project Workflow

```text
Raw Dataset
     ↓
Data Import
     ↓
Data Inspection
     ↓
Data Cleaning & Transformation
     ↓
Feature & Target Separation
     ↓
Label Encoding
     ↓
Train-Test Split
     ↓
Logistic Regression Model Training
     ↓
Model Evaluation
     ↓
Streamlit App
```

## 📈 Dataset Information

The included dataset contains:

- 20,000 records
- 30 columns
- 1 target column: `personality_type`, which contains the classes `Introvert`, `Ambivert`, and `Extrovert`.
- Numerical features describing social behaviour, thinking style, lifestyle, and preferences

**Link:** [personality-dataset](https://github.com/Chauhanekta21/Personality-Predictor/blob/main/data/personality_dataset.csv)

**Dataset Preview:**

![data](data.png)


## 📈 Key Steps & Results

🔹 Data Import

Loaded the personality dataset from the data folder.

![data](data_import.png)

🔹 Data Inspection

Checked the dataset for missing values and duplicate records.

- Null values: None

- Duplicate records: None

- **Personality Type Distribution:** Countplot shows that the personality classes are well balanced.

![data](personality.png)

- **Social Energy Distribution:** Histogram shows the distribution of social energy scores, while the KDE curve shows the overall distribution trend.

![data](social.png)


- **Feature Relationships:** Pair plot was used to see relationships between talkativeness, empathy, creativity, and personality_type.

![data](feature.png)


🔹 Data Cleaning & Transformation

No major cleaning was required as the dataset contained no missing or duplicate values.


🔹 Feature Selection with ANOVA

Used ANOVA to identify features that have a statistically significant relationship with the target.

Three features had p-values ≥ 0.05 and were excluded from model training:

- emotional_stability
- stress_handling
- creativity

The remaining features were retained for training.

![data](f_selection.png)


🔹 Target Encoding

Encoded the categorical personality_type target using LabelEncoder.

![data](encoding.png)

🔹 Split X and y features.

Separated the dataset into:

X: Input features
y: Target (personality_type)

![data](split.png)


🔹 Model Training

Created and trained a Logistic Regression classification model using the training data.

![data](tarining.png)

🔹 Model Evaluation

Evaluated the trained model using:

- **Confusion Matrix —** to see correct and incorrect predictions for each personality type.

![data](matrix.png)

- **Accuracy Score —** to measure the overall percentage of correct predictions.

- **Classification Report —** to evaluate precision, recall, and F1-score for each personality type.


![data](accuracy.png)



## 📈 Tools and Libraries

- Python
- Jupyter Notebook
- Pandas for loading and working with the data
- NumPy for numerical operations
- Matplotlib and Seaborn for visualizations in the notebook
- Scikit-learn for label encoding and logistic regression
- Streamlit for the interactive web app

## 📈 Repository Structure

```text
Personality_Predictor/
|-- data/
|   `-- personality_dataset.csv
|-- jupyter_notebook/
|   `-- personality_predictor.ipynb
|-- streamlit_app/
|   |-- app.py
|   `-- requirements.txt
|-- .gitignore
`-- README.md
```

## 📈 Skills Demonstrated

- Exploratory data analysis
- Data inspection and preprocessing
- Feature selection
- Label encoding
- Classification with logistic regression
- Train/test splitting
- Data visualization
- Building an interactive Streamlit application

## 📈 Author

**Ekta Singh Chauhan**

Data Analyst

Focused on building projects in:

- Excel 
- SQL
- Python
- Power BI
- Data Analytics
- Machine Learning

## 📈 Disclaimer

This project is for educational and portfolio purposes only. The prediction should not be used as a medical, clinical, or professional psychological assessment.
