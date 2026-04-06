import streamlit as st
from backend.difficulty import detect_difficulty
from backend.simplifier import simplify_text

st.set_page_config(
    page_title="Adaptive NLP v2",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧠 Adaptive NLP v2")
st.markdown("**Smart text analysis with adaptive difficulty detection and instant simplification.**")
st.markdown("---")

st.sidebar.header("About")
st.sidebar.markdown("""
This app analyzes text for reading difficulty and provides simplified versions.

**Features:**
- Difficulty scoring (Easy/Medium/Hard)
- Intelligent text simplification
- Real-time processing
""")

st.header("📝 Text Analysis")

text_input = st.text_area(
    "Enter your text here:",
    height=150,
    placeholder="Paste or type the text you want to analyze..."
)

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 Analyze Text", type="primary", use_container_width=True):
        if text_input.strip():
            with st.spinner("Analyzing..."):
                difficulty = detect_difficulty(text_input)
                simplified = simplify_text(text_input)

            st.success("Analysis complete!")

            st.subheader("📊 Difficulty Level")
            if difficulty == "Easy":
                st.info(f"**{difficulty}** - This text is easy to read.")
            elif difficulty == "Medium":
                st.warning(f"**{difficulty}** - This text has moderate complexity.")
            else:
                st.error(f"**{difficulty}** - This text is difficult to read.")

            st.subheader("✨ Simplified Text")
            st.text_area(
                "Simplified version:",
                value=simplified,
                height=150,
                disabled=True,
                key="simplified"
            )
        else:
            st.error("Please enter some text to analyze.")

with col2:
    st.subheader("💡 How it works")
    st.markdown("""
    1. **Difficulty Detection**: Uses Flesch Reading Ease score
    2. **Text Simplification**: Replaces complex words with simpler synonyms
    3. **Real-time Processing**: Instant results with no server setup needed
    """)

    st.subheader("📈 Score Ranges")
    st.markdown("""
    - **Easy**: Score > 60
    - **Medium**: Score 30-60
    - **Hard**: Score < 30
    """)

st.markdown("---")
st.markdown("Built with ❤️ using Streamlit, NLTK, and TextStat")

if __name__ == "__main__":
    st.write("Run with: `streamlit run streamlit_app.py`")