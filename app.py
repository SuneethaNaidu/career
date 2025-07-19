import streamlit as st
import base64
from career_data import career_data  # Import your career dataset

st.set_page_config(page_title="Career Companion", page_icon="🎯")
st.title("🎯 Career Companion")
st.write("An AI-powered skill-based career guidance platform.")

# User Inputs
user_name = st.text_input("👤 Enter your name:", key="user_name")
skills_input = st.text_input("🛠️ Enter your skills (comma-separated):")

if user_name and skills_input:
    user_skills = [skill.strip().lower() for skill in skills_input.split(",")]

    # Match logic
    matched = [(role, len(set(user_skills) & set(info["skills"])))
               for role, info in career_data.items()]
    matched.sort(key=lambda x: x[1], reverse=True)

    if matched[0][1] == 0:
        st.warning("⚠️ No matching career path found. Please check your skill inputs or try different ones.")
    else:
        best_match = matched[0][0]
        matched_score = matched[0][1]

        # 🎯 Best Match and Score
        st.success(f"🎯 Best Match: **{best_match}**")
        st.info(f"🎯 Match Score: {matched_score} skill(s) matched")

        # 💬 Matched Skills
        st.markdown("**Your Matched Skills:**")
        for skill in set(user_skills) & set(career_data[best_match]["skills"]):
            st.code(skill.strip())

        # 📘 Recommended Skills
        st.subheader("📘 Recommended Skills")
        for skill in career_data[best_match]["skills"]:
            st.write(f"- {skill}")

        # 💡 Project Suggestions (Two Columns)
        st.subheader("💡 Project Suggestions")
        cols = st.columns(2)
        for i, proj in enumerate(career_data[best_match]["projects"]):
            cols[i % 2].success(f"📁 {proj}")

        # 📚 Learning Resources (Two Columns)
        st.subheader("📚 Learning Resources")
        cols = st.columns(2)
        for i, link in enumerate(career_data[best_match]["resources"]):
            cols[i % 2].markdown(f"[🔗 {link}]({link})")

        # 📊 Track Progress
        st.subheader("📊 Track Your Progress")
        progress_key = f"{user_name}_{best_match}_progress"

        if progress_key not in st.session_state:
            st.session_state[progress_key] = {}

        for skill in career_data[best_match]["skills"]:
            if skill not in st.session_state[progress_key]:
                st.session_state[progress_key][skill] = False

            st.session_state[progress_key][skill] = st.checkbox(
                f"✔️ Completed: {skill.title()}",
                value=st.session_state[progress_key][skill]
            )

        completed_skills = [
            skill for skill, done in st.session_state[progress_key].items() if done
        ]
        total_skills = len(career_data[best_match]["skills"])
        progress_percent = (len(completed_skills) / total_skills) * 100

        st.markdown(
            f"**✅ Progress: {len(completed_skills)} / {total_skills} skills completed ({progress_percent:.0f}%)**"
        )

        # 📥 Download Roadmap
        st.subheader("📥 Download Roadmap")
        roadmap_text = "\n".join(
            [f"- {skill.title()}" for skill in career_data[best_match]["skills"]]
        )

        if st.button("📄 Download as Text File"):
            b64 = base64.b64encode(roadmap_text.encode()).decode()
            href = f'<a href="data:file/txt;base64,{b64}" download="Career_Roadmap.txt">📄 Click here to download your roadmap</a>'
            st.markdown(href, unsafe_allow_html=True)

# 📘 Browse All Career Paths
with st.expander("📘 Browse All Career Paths"):
    for role in career_data:
        st.markdown(f"### {role}")
        st.markdown(f"**Skills**: {', '.join(career_data[role]['skills'])}")
        st.markdown(f"**Projects**: {', '.join(career_data[role]['projects'])}")
        st.markdown(f"**Resources**:")
        for link in career_data[role]["resources"]:
            st.markdown(f"- [🔗 {link}]({link})")
        st.markdown("---")
