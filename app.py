import os
from io import BytesIO

import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Imagine AI",
    page_icon="✨",
    layout="wide"
)


# --------------------------------------------------
# LOAD API KEY
# --------------------------------------------------

load_dotenv()

hf_token = os.getenv("HF_TOKEN")


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: #0b0c10;
    color: #f3f4f6;
}

/* Main container */

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* Title */

.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: 800;
    margin-bottom: 5px;
    letter-spacing: -1px;
}


/* Subtitle */

.subtitle {
    text-align: center;
    color: #a1a1aa;
    font-size: 18px;
    margin-bottom: 45px;
}


/* Section headings */

.section-title {
    font-size: 21px;
    font-weight: 650;
    margin-bottom: 12px;
}


/* Prompt box */

textarea {
    border-radius: 14px !important;
}


/* Buttons */

.stButton > button {
    width: 100%;
    height: 52px;
    border-radius: 12px;
    font-size: 17px;
    font-weight: 650;
}


/* Image card */

.image-card {
    background: #1f2128;
    border-radius: 18px;
    padding: 12px;
    min-height: 400px;
}


/* Feature cards */

.feature-card {
    background: #15171d;
    border: 1px solid #292c35;
    border-radius: 14px;
    padding: 18px;
    text-align: center;
    height: 100%;
}

.feature-icon {
    font-size: 28px;
}

.feature-title {
    font-weight: 650;
    margin-top: 8px;
}

.feature-text {
    color: #a1a1aa;
    font-size: 14px;
    margin-top: 5px;
}


/* Footer */

.footer {
    text-align: center;
    color: #71717a;
    margin-top: 55px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">✦ Imagine AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Turn your imagination into beautiful AI-generated images.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# MAIN SECTION
# --------------------------------------------------

left, right = st.columns([1, 1], gap="large")


# --------------------------------------------------
# LEFT SIDE
# --------------------------------------------------

with left:

    st.markdown(
        '<div class="section-title">Describe your image</div>',
        unsafe_allow_html=True
    )

    prompt = st.text_area(
        "Prompt",
        placeholder=(
            "Example: A futuristic city at night with "
            "neon lights and flying cars..."
        ),
        height=180,
        label_visibility="collapsed"
    )

    st.markdown("###")

    col1, col2 = st.columns(2)

    with col1:

        style = st.selectbox(
            "🎨 Style",
            [
                "Realistic",
                "Cinematic",
                "Digital Art",
                "Anime",
                "Fantasy",
                "3D Render"
            ]
        )

    with col2:

        aspect_ratio = st.selectbox(
            "📐 Aspect Ratio",
            [
                "Square (1:1)",
                "Portrait (2:3)",
                "Landscape (3:2)"
            ]
        )

    st.markdown("###")

    generate = st.button(
        "✨ Generate Image",
        type="primary"
    )


# --------------------------------------------------
# RIGHT SIDE
# --------------------------------------------------

with right:

    st.markdown(
        '<div class="section-title">Generated Image</div>',
        unsafe_allow_html=True
    )

    if "generated_image" not in st.session_state:

        st.markdown(
            """
            <div class="image-card">
                <br><br><br>
                <div style="text-align:center;">
                    <div style="font-size:55px;">🖼️</div>
                    <br>
                    <div style="color:#a1a1aa;">
                        Your generated image will appear here.
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.image(
            st.session_state.generated_image,
            use_container_width=True
        )

        st.download_button(
            label="⬇ Download Image",
            data=st.session_state.generated_image_bytes,
            file_name="imagine_ai.png",
            mime="image/png",
            use_container_width=True
        )


# --------------------------------------------------
# IMAGE GENERATION
# --------------------------------------------------

if generate:

    if not prompt.strip():

        st.warning("Please enter a description first.")

    elif not hf_token:

        st.error(
            "Hugging Face API key was not found. "
            "Please check your .env file."
        )

    else:

        style_prompt = f"""
        {prompt}

        Visual style: {style}

        Create a high-quality, detailed image.
        """

        with st.spinner("Creating your image... ✨"):

            try:

                client = InferenceClient(
                    api_key=hf_token
                )

                image = client.text_to_image(
                    prompt=style_prompt,
                    model="black-forest-labs/FLUX.1-schnell"
                )

                st.session_state.generated_image = image

                buffer = BytesIO()

                image.save(
                    buffer,
                    format="PNG"
                )

                st.session_state.generated_image_bytes = (
                    buffer.getvalue()
                )

                st.rerun()

            except Exception as e:

                st.error(
                    f"Something went wrong: {e}"
                )


# --------------------------------------------------
# FEATURES
# --------------------------------------------------

st.markdown("###")

feature1, feature2, feature3 = st.columns(3)

with feature1:

    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">AI Powered</div>
            <div class="feature-text">
                Generate images from simple text prompts.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with feature2:

    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🎨</div>
            <div class="feature-title">Multiple Styles</div>
            <div class="feature-text">
                Explore realistic, cinematic and creative styles.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with feature3:

    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">⬇️</div>
            <div class="feature-title">Easy Download</div>
            <div class="feature-text">
                Save your generated creations as PNG images.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    'Built with Python • Streamlit • Hugging Face'
    '</div>',
    unsafe_allow_html=True
)