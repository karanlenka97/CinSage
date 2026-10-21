import streamlit as st

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