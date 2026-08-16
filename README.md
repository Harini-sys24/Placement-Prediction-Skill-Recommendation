# 🎓 Student Placement Prediction & Skill Recommendation System

An end-to-end Machine Learning project that predicts a student's placement status and recommends the skills they should improve based on their target career role.


<p align="center">

  <a href="https://cite-compound-joseph-lawsuit.trycloudflare.com/">
    <img src="https://img.shields.io/badge/🚀%20Try%20the%20Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Try the Live App">
  </a>

  <a href="https://github.com/Harini-sys24/Placement-Prediction-Skill-Recommendation/new/main?filename=README.md">
    <img src="https://img.shields.io/badge/💻%20View%20Source%20Code-181717?style=for-the-badge&logo=github&logoColor=white" alt="View Source Code">
  </a>

</p>

## 📌 Project Overview

This project combines two Machine Learning/Data Science components


1. **Student Placement Prediction**
   - Predicts whether a student is likely to be placed.
   - Uses academic, technical, and extracurricular features.
   - The final placement model uses a balanced dataset and Logistic Regression.

2. **Skill Recommendation System**
   - Allows students to select their target career role.
   - Collects their current skill levels.
   - Calculates the gap between their current skills and the skills required for the selected role.
   - Uses skill gap and priority to recommend the most important skills to improve.

The complete system is deployed as an interactive Streamlit web application.


## 🚀 Features

### 📊 Placement Prediction

The system takes the following student features:

- Branch
- College Tier
- CGPA
- Backlogs
- Coding Skills
- DSA Score
- Aptitude Score
- Communication Skills
- ML Knowledge
- System Design
- Internships
- Projects Count
- Certifications
- Hackathons
- Open Source Contributions
- Extracurricular Activities

The model predicts:

- **Placed**
- **Not Placed**

It also displays the predicted placement probability.

### 🎯 Skill Recommendation

The student selects a target career role and provides their skill levels:

- Beginner
- Basic
- Intermediate
- Advanced
- Expert

The system then:

1. Identifies the skills required for the selected role.
2. Compares the student's current level with the required level.
3. Calculates the skill gap.
4. Considers skill priority.
5. Calculates a recommendation score.
6. Displays the top skills that need improvement.
7. Shows a learning path for supported skills.



## 🧠 Machine Learning Workflow

### Placement Prediction


Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Selection
   ↓
Train-Test Split
   ↓
Preprocessing
   ↓
Handling Class Imbalance
   ↓
Model Training
   ↓
Model Comparison
   ↓
Hyperparameter Tuning
   ↓
Final Model Selection
   ↓
Model Saving
   ↓
Streamlit Deployment


### Skill Recommendation

Target Career Role
        ↓
Required Skills
        ↓
Student Skill Levels
        ↓
Skill Gap Calculation
        ↓
Priority Weight
        ↓
Recommendation Score
        ↓
Top 5 Skills to Improve
        ↓
Learning Path




## 📐 Recommendation Logic

The recommendation system calculates the skill gap using:

Skill Gap = Required Level - Student Level


Priority weights are:


High   = 3
Medium = 2
Low    = 1


The recommendation score is:


Recommendation Score = Skill Gap × Priority Weight


A higher recommendation score indicates that the skill should receive greater attention.



## 🤖 Models Evaluated

Several classification models were evaluated during the project:

* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost

Model performance was evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Macro F1-score

Because the placement dataset was imbalanced, class balancing was also evaluated.

The final model was selected based on the overall classification performance and suitability for the application.


## ⚠️ Data Leakage Handling

During model evaluation, `salary_package_lpa` was found to have extremely high feature importance and was therefore excluded from the final placement prediction features.

This was done because salary package is closely related to the placement outcome and using it could introduce target leakage.

The final model therefore predicts placement using student-related features available before the placement outcome.



## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Joblib
* Streamlit
* Git & GitHub



## 📂 Project Structure


student-placement-skill-recommendation/
│
├── app.py
├── placement_model.pkl
├── role_skills.csv
├── requirements.txt
└── README.md

### File Description

| File                 | Description                           |
| ---------------------| ------------------------------------- |
| app.py              | Streamlit application                 |
| placement_model.pkl | Trained placement prediction pipeline |
| role_skills.csv     | Role-wise skill requirements          |
| requirements.txt    | Python dependencies                   |
| README.md           | Project documentation                 |



## 💻 Run Locally

### 1. Clone the repository


git clone https://github.com/Harini-sys24/student-placement-skill-recommendation.git


### 2. Navigate to the project


cd student-placement-skill-recommendation


### 3. Install dependencies

pip install -r requirements.txt


### 4. Run the Streamlit application

streamlit run app.py


The application will open in your browser.



## 🌐 Deployment

The application can be deployed using Streamlit Community Cloud.

Deployment flow:


GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Install requirements.txt
       ↓
Run app.py
       ↓
Public Web Application




## 🎯 Example Application Flow


Student
   │
   ├── Academic Details
   │
   ├── Technical Skills
   │
   └── Extracurricular Activities
             │
             ▼
      Placement Prediction
             │
       ┌─────┴─────┐
       ▼           ▼
    PLACED      NOT PLACED
             │
             ▼
       Target Career Role
             │
             ▼
       Skill Assessment
             │
             ▼
        Skill Gap Analysis
             │
             ▼
      Top Skills to Improve




## 📊 Expected Output

### Placement Prediction

Prediction: PLACED

Placement Probability: 78.50%


or


Prediction: NOT PLACED

Placement Probability: 42.30%


### Skill Recommendation


Target Role: Software Developer

1. DSA
   Current Level: Intermediate
   Target Level: Expert
   Priority: High

2. SQL
   Current Level: Basic
   Target Level: Advanced
   Priority: High

3. Git
   Current Level: Beginner
   Target Level: Advanced
   Priority: Medium



## 🔮 Future Improvements

* Add more career roles and skill requirements.
* Use a larger and more diverse skill dataset.
* Add personalized learning resources for each skill.https://github.com/Harini-sys24/Placement-Prediction-Skill-Recommendation/tree/main
* Include course and project recommendations.
* Add visualizations for skill gaps.
* Improve the recommendation algorithm using Machine Learning.
* Add student profile history.
* Add authentication and personalized dashboards.
* Continuously improve the model using real placement data.


## 👩‍💻 Author

**Harini G**

BE Computer Science and Engineering
PSG College of Technology, Coimbatore


<p align="center">
⭐ If you find this project useful, consider giving it a star!
<a href="https://github.com/Harini-sys24/Placement-Prediction-Skill-Recommendation/tree/main"> <img src="https://img.shields.io/github/stars/Harini_sys24/Placement-Prediction-Skill-Recommendation
?style=for-the-badge&logo=github" alt="GitHub Stars"> </a> </p> ```

## ⭐ Project Goal

The goal of this project is to help students understand their placement readiness and identify the skills they should focus on improving for their desired career role.
