import joblib
import pandas as pd
import streamlit as st
model = joblib.load("placement_model.pkl")
rdf = pd.read_csv("role_skills.csv")
st.set_page_config(
    page_title="Student Placement & Skill Recommendation",
    page_icon="🎓",
    layout="wide"
)
st.info(
    "ℹ️ Disclaimer: This application is developed for educational and "
    "demonstration purposes using a synthetic dataset. The placement "
    "prediction is not a real-world hiring decision and should not be "
    "considered a guarantee of placement."
)
st.title("🎓 Student Placement Prediction & Skill Recommendation System")

st.write(
    "Predict placement status and identify the skills you should improve "
    "for your target career role."
)


def recommendation_skills(student_skills,target_role):

      required_skills = rdf[ rdf["Role"] == target_role]
      recommendations= []
      for _,row in required_skills.iterrows():
        skill = row["Skill"]
        required_level = row["Required_Level"]
        priority  = row["Priority"]

        student_level = student_skills.get(skill,0)
        gap = required_level - student_level

        recommendations.append((skill,required_level,student_level,gap,priority))
      skill_gap_df = pd.DataFrame(recommendations,columns=["Skill","Required_Level","Student_Level","Gap","Priority"])
      skill_gaps = skill_gap_df[ skill_gap_df["Gap"]>0].copy()
      skill_gaps = skill_gaps.sort_values(by="Gap",ascending = False)
      skill_gaps["Priority Weight"] = skill_gaps["Priority"].map({
        "High":3,
        "Medium":2,
        "Low":1
    })
      skill_gaps["Recommendation_score"] = skill_gaps["Gap"]*skill_gaps["Priority Weight"]
      recommendation_df = skill_gaps.sort_values(by="Recommendation_score",ascending = False)

      level_names = {
        1: "Beginner",
        2: "Basic",
        3: "Intermediate",
        4: "Advanced",
        5: "Expert"
    }
      recommendation_df["Current Level"] = recommendation_df["Student_Level"].map(level_names)
      recommendation_df["Target Level"] = recommendation_df["Required_Level"].map(level_names)

      top_recommendations = recommendation_df.head(5).copy()
      top_recommendations["Recommendation"] = ("Improve " + top_recommendations["Skill"] + " from " +top_recommendations["Current Level"] + " to " + top_recommendations["Target Level"] )

      def get_priority_label(score):
        if score>=6:
            return "🔴 High Priority"
        if score>=3:
            return "🟠 Medium Priority"
        else:
            return "🟢 Low Priority"

      top_recommendations["Recommendation Level"] = top_recommendations["Recommendation_score"].apply(get_priority_label)

      learning_path = {

        'DSA': [
            'Arrays & Strings',
            'Linked Lists',
            'Stacks & Queues',
            'Trees & Graphs',
            'Dynamic Programming'
        ],

        'SQL': [
            'SELECT & Filtering',
            'Joins',
            'Subqueries',
            'CTEs',
            'Window Functions'
        ],

        'Python': [
            'Python Basics',
            'OOP',
            'NumPy',
            'Pandas',
            'Advanced Python'
        ],

        'Git': [
            'Git Basics',
            'Branching',
            'Merging',
            'GitHub',
            'Pull Requests'
        ],

        'Machine Learning': [
            'Data Preprocessing',
            'Regression',
            'Classification',
            'Model Evaluation',
            'Model Deployment'
        ]
    }

      top_recommendations["Learning path"] = top_recommendations["Skill"].map(learning_path)
      return top_recommendations

placement_tab, skill_tab = st.tabs([
    "📊 Placement Prediction",
    "🎯 Skill Recommendation"
])

with skill_tab:
  import streamlit as st
  levels = [
      "Beginner",
      "Basic",
      "Intermediate",
      "Advanced",
      "Expert"
  ]
  target_role = st.selectbox("Select Target Role",rdf["Role"].unique())
  role_required_skills = rdf[rdf["Role"] == target_role]["Skill"].tolist()
  student_skills = {}
  st.subheader("Rate your skills")
  for skill in role_required_skills:
      skill_level = st.selectbox(f"Select level for {skill}",levels)
      student_skills[skill] =skill_level
  level_mapping = {
      "Beginner": 1,
      "Basic": 2,
      "Intermediate": 3,
      "Advanced": 4,
      "Expert": 5
  }
  student_skills = {
      skill : level_mapping[level]
      for skill,level in student_skills.items()
  }
  recommendations = recommendation_skills(student_skills,target_role)
  if st.button(
        "🔍 Get Skill Recommendations",
        key="recommend_button"
    ):

        st.subheader("⭐ Top Skills to Improve")

        if recommendations.empty:

            st.success(
                "🎉 Great! You already meet the required skill levels "
                f"for {target_role}."
            )

        else:

            st.dataframe(
                recommendations[
                    [
                        "Skill",
                        "Current Level",
                        "Target Level",
                        "Gap",
                        "Priority",
                        "Recommendation"
                    ]
                ],
                use_container_width=True,
                hide_index=True
            )

with placement_tab:



    st.header("📊 Student Placement Prediction")

    st.write(
        "Enter your academic, technical and extracurricular details "
        "to predict your placement status."
    )

    # -----------------------------
    # Student academic details
    # -----------------------------

    st.subheader("🎓 Academic Details")

    col1, col2, col3,col4 = st.columns(4)

    with col1:
        cgpa = st.number_input(
            "CGPA",
            min_value=0.0,
            max_value=10.0,
            value=7.0,
            step=0.1
        )

    with col2:
        backlogs = st.number_input(
            "Number of Backlogs",
            min_value=0,
            max_value=20,
            value=0,
            step=1
        )

    with col3:
        branch = st.selectbox(
            "Branch",
            ["CSE", "IT", "ECE", "EEE", "MECH",
             "Civil", "Chemical", "EE"]
        )

    with col4:
        college_tier = st.selectbox(
                "College Tier",
                 ["Tier-1", "Tier-2", "Tier-3"]
                  )


    # -----------------------------
    # Skill scores
    # -----------------------------

    st.subheader("💻 Technical & Skill Scores")

    col1, col2, col3 = st.columns(3)

    with col1:
        coding_skills = st.number_input(
            "Coding Skills",
            min_value=0,
            max_value=10,
            value=5,
            step=1
        )

        dsa_score = st.number_input(
            "DSA Score",
            min_value=0,
            max_value=10,
            value=5,
            step=1
        )

        aptitude_score = st.number_input(
            "Aptitude Score",
            min_value=20.0,
            max_value=100.0,
            value=65.0,
            step=1.0
        )

        open_source_contributions = st.number_input(
            "Number of Open Source Contributions",
            min_value=0,
            max_value=20,
            value=1,
            step=1
        )


    with col2:
        communication_skills = st.number_input(
            "Communication Skills",
            min_value=0,
            max_value=10,
            value=5,
            step=1
        )

        ml_knowledge = st.number_input(
            "ML Knowledge",
            min_value=0,
            max_value=10,
            value=5,
            step=1
        )

        system_design = st.number_input(
            "System Design",
            min_value=0,
            max_value=10,
            value=5,
            step=1
        )

        extracurriculars = st.number_input(
            "Extracurricular Activities",
            min_value=0,
            max_value=20,
            value=1,
            step=1
        )


    with col3:
        projects_count = st.number_input(
            "Number of Projects",
            min_value=0,
            max_value=20,
            value=2,
            step=1
        )

        certifications = st.number_input(
            "Number of Certifications",
            min_value=0,
            max_value=20,
            value=1,
            step=1
        )
        internships = st.number_input(
            "Number of Internships",
            min_value=0,
            max_value=20,
            value=1,
            step=1
        )

        hackathons = st.number_input(
            "Number of Hackathons",
            min_value=0,
            max_value=20,
            value=1,
            step=1
        )



    # -----------------------------
    # Prediction button
    # -----------------------------

    if st.button(
        "🔮 Predict Placement",
        key="placement_button"
    ):

        # Create input DataFrame
        input_data = pd.DataFrame({
            "branch": [branch],
            "college_tier": [college_tier],
            "cgpa": [cgpa],
            "backlogs": [backlogs],
            "coding_skills": [coding_skills],
            "dsa_score": [dsa_score],
            "aptitude_score": [aptitude_score],
            "communication_skills": [communication_skills],
            "ml_knowledge": [ml_knowledge],
            "system_design": [system_design],
            "internships": [internships],
            "projects_count": [projects_count],
            "certifications": [certifications],
            "hackathons": [hackathons],
            "open_source_contributions": [open_source_contributions],
            "extracurriculars": [extracurriculars]
        })

        # Prediction
        prediction = model.predict(input_data)[0]

        # Prediction probability
        probability = model.predict_proba(input_data)[0]

        if prediction == 1:

            st.success("🎉 Prediction: PLACED")

            st.write(
                f"Placement Probability: {probability[1] * 100:.2f}%"
            )
            st.info(
        "✨ Keep building your skills, gaining practical experience, "
        "and exploring opportunities. Your preparation can make a "
        "strong difference in your placement journey!"
    )

        else:

            st.warning("⚠️ Prediction: NOT PLACED")

            st.write(
                f"Placement Probability: {probability[1] * 100:.2f}%"
            )
            st.info(
        "🌱 Don't be discouraged! This prediction is only an estimate "
        "based on a synthetic dataset. Use it as motivation to identify "
        "areas for improvement, strengthen your skills, work on projects, "
        "and keep preparing. Every step forward brings you closer to "
        "your goal! 💪"
    )
