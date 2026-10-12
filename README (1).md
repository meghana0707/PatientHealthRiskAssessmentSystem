# Patient Health Risk Assessment System

## Project Overview
The **Patient Health Risk Assessment System** is a machine-learning academic project that demonstrates how health-related and lifestyle attributes can be used to classify a record into one of three health-risk categories: **Low, Medium, or High**.

The project was developed using **Python in Google Colab** and compares three supervised classification algorithms:
- Logistic Regression
- Decision Tree
- Random Forest

> **Important:** This project is an educational prototype only. It is not a medical diagnostic tool and must not be used to make clinical decisions.

## Objectives
- Explore a small labelled dataset containing patient-related attributes.
- Prepare categorical data for machine-learning algorithms.
- Train and compare three classification models.
- Demonstrate a basic machine-learning workflow from data inspection to evaluation.
- Understand the limitations of predictions made from a very small dataset.

## Dataset
The project dataset is a small, project-created dataset. The intended version for this project contains **10 records**.

The attributes described in the project include:

| Attribute | Description |
|---|---|
| Age | Patient age |
| Gender | Gender category |
| Blood Pressure | Blood-pressure measurement |
| Blood Glucose | Blood-glucose measurement |
| BMI | Body Mass Index |
| Cholesterol | Cholesterol measurement |
| Smoking | Smoking status |
| Physical Activity | Physical-activity category |
| Health Risk | Target label: Low, Medium, or High |

The exact dataset values and class counts should be taken from the final notebook used for submission.

## Technologies Used
- **Python** — programming language
- **Google Colab** — notebook development and execution environment
- **Pandas** — data inspection and manipulation
- **Scikit-learn** — preprocessing and machine-learning models
- **Matplotlib / visualization tools** — use only where included in the notebook

## Machine-Learning Workflow
1. Load and inspect the dataset.
2. Explore the dataset and review its structure.
3. Encode categorical attributes into numeric values.
4. Separate input features (`X`) and target labels (`y`).
5. Split the data into training and testing sets.
6. Train Logistic Regression, Decision Tree, and Random Forest classifiers.
7. Generate predictions on the test data.
8. Evaluate and compare the models.

## Algorithms
### 1. Logistic Regression
A supervised classification algorithm used as a baseline model for predicting the health-risk category.

### 2. Decision Tree
A rule-based classifier that predicts a category by splitting data according to feature conditions.

### 3. Random Forest
An ensemble classifier that combines predictions from multiple decision trees.

## Results
The previously prepared project report recorded an accuracy of **0.50** for each of the three classifiers. It also recorded the following Logistic Regression metrics:

- Precision: **1.00**
- Recall: **0.50**
- F1-score: **0.6667**

**Please verify these metrics by rerunning the final 10-record notebook before publishing them as final results.** Earlier project material also described a 16-record version, so results can differ if the notebook or dataset version changes. Do not treat these results as evidence of clinical performance.

## How to Run
The project was developed in Google Colab.

1. Open the project notebook in Google Colab.
2. Upload or load the dataset file used by the notebook.
3. Run the notebook cells in order, starting with imports and data loading.
4. Review the dataset exploration, preprocessing, model-training, and evaluation outputs.

The exact Colab notebook URL and dataset filename were not included in the current request. Add them here before publishing if you want readers to open and reproduce the project directly.

## Team Members
| Name | Roll Number |
|---|---|
| K. Akshitha Reddy | 2520030233 |
| T. Meghana Sai | 2520030245 |
| Sreekara Karthik | 2520030235 |

## Guide
**Mr. Ravindra Gaddam**

## Limitations and Responsible Use
- The dataset is very small and may not represent real patient populations.
- Evaluation results from a tiny test set can be unstable.
- Predictions depend on the quality and correctness of the labels and input values.
- The project does not replace professional medical assessment.
- Any real-world use would require larger representative data, suitable validation, privacy protections, and review by qualified healthcare professionals.

## Future Improvements
- Use a larger, representative dataset with clearly documented provenance.
- Validate the models using appropriate repeated or stratified evaluation methods.
- Add a confusion matrix and per-class precision, recall, and F1-scores.
- Improve preprocessing and ensure transformations are applied consistently.
- Document the exact dataset, notebook, parameters, and reproducible results.

## License
No license has been specified yet. Add a license if you intend to allow others to reuse or modify this repository.
