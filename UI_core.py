import streamlit as st
from core import analyze_movie_paragraph

st.set_page_config(page_title="CinSage", page_icon="🎬", layout="centered")

st.markdown(
    """
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"],
    [data-testid="stMain"], [data-testid="stMainBlockContainer"] {
        background: #ffffff !important;
        color: #111111 !important;
    }

    [data-testid="stAppViewContainer"] *,
    [data-testid="stMain"] * {
        color: #111111;
    }

    [data-testid="stHeader"] {
        background: #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="display:flex; align-items:center; gap:16px; margin:12px 0 4px;">
        <div style="display:flex; align-items:center; justify-content:center;
                    width:58px; height:58px; border:1px solid #dedede;
                    border-radius:16px; background:#fff; font-size:32px;">
            🎬
        </div>
        <h1 style="margin:0; color:#111;">CinSage</h1>
    </div>
    <p style="margin:4px 0 22px 74px; color:#444;">
        Movie insights, clearly presented
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("Paste a movie description to extract its key information.")

paragraph = st.text_area(
    "Movie paragraph",
    placeholder="Paste a movie paragraph here...",
    height=180,
)

with st.form("movie_analysis_form"):
    paragraph = st.text_area(
        "Movie paragraph",
        placeholder="Paste a movie paragraph here...",
        height=180,
    )
    submitted = st.form_submit_button("Analyze paragraph")

[data-testid="stTextArea"] textarea {
    background: #ffffff !important;
    color: #111111 !important;
    -webkit-text-fill-color: #111111 !important;
    border: 1px solid #b8b8b8 !important;
    border-radius: 12px !important;
    box-shadow: none !important;
}

[data-testid="stTextArea"] textarea::placeholder {
    color: #555555 !important;
    opacity: 1 !important;
}

div[data-testid="stFormSubmitButton"] button {
    background: #ffffff !important;
    color: #111111 !important;
    border: 1px solid #b8b8b8 !important;
    border-radius: 10px !important;
    box-shadow: none !important;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background: #f5f5f5 !important;
}

if submitted and not paragraph.strip():
    st.warning("Please enter a movie paragraph first.")

labels = (
    "Title",
    "Release year",
    "Director",
    "Main cast",
    "Genre",
    "Setting and premise",
    "Key themes",
    "Tone and style",
    "Notable strengths",
    "Reception details",
    "Quick summary",
    "Insights",
)

formatted_analysis = str(analysis).strip()

for label in labels:
    formatted_analysis = re.sub(
        rf"(?i)(?<!^)\s*({re.escape(label)}\s*:)",
        r"\n\n\1",
        formatted_analysis,
    )

st.markdown(
    f"""
    <div style="background:#fff; color:#111; border:1px solid #dedede;
                border-radius:14px; padding:22px 24px; line-height:1.75;
                white-space:pre-wrap;">
        {formatted_analysis}
    </div>
    """,
    unsafe_allow_html=True,
)

if submitted and paragraph.strip():
    with st.spinner("Analyzing the movie paragraph..."):
        analysis = analyze_movie_paragraph(paragraph.strip())
        st.write(analysis)