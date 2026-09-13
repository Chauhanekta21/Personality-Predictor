# 📊 Personality Predictor

> **Project Status: Completed**

## 📈 Project Overview

This project uses machine learning to predict a person's personality type from their answers to questions about their habits, preferences, and behaviour. The prediction can be one of three types:

- Introvert
- Ambivert
- Extrovert

The project includes a Jupyter Notebook for learning and analysis, along with a Streamlit app that lets users try the personality predictor through a simple web interface.

## 📈 View Project:

🔹 **Personality Predictor Live App:** Answer behavioural questions and see machine learning turn your responses into a personality prediction. 

**Link:** [personality-predictor-streamlit-app](https://personality-predictor-pp.streamlit.app/)

🔹 **Jupyter Notebook:** See how raw data becomes a working prediction model through exploration, preprocessing, feature selection, and logistic regression. 

**Link:** [personality-predictor-jupyter-notebook](https://github.com/Chauhanekta21/Personality-Predictor/blob/main/jupyter_notebook/personality_predictor.ipynb)

## 📈 Project Workflow

The project follows these steps:

1. Load the personality dataset from the `data` folder.
2. Explore the dataset in the Jupyter Notebook.
3. Separate the personality label from the input features.
4. Convert the text personality labels into numbers with `LabelEncoder`.
5. Split the data into training and testing sets in the notebook.
6. Train a `LogisticRegression` classification model.
7. Use the trained model to predict a personality type from new answers.
8. Display the prediction in the Streamlit app.

## 📈 Dataset Information

The included dataset contains:

- 20,000 records
- 30 columns
- 1 target column: `personality_type`
- Numerical features describing social behaviour, thinking style, lifestyle, and preferences

Some example features are:

- `social_energy`
- `alone_time_preference`
- `talkativeness`
- `deep_reflection`
- `group_comfort`
- `empathy`
- `organization`
- `leadership`
- `risk_taking`
- `public_speaking_comfort`
- `routine_preference`
- `travel_desire`

The target column is `personality_type`, which contains the classes `Introvert`, `Ambivert`, and `Extrovert`.



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
