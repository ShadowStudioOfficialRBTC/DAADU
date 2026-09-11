from pathlib import Path
from uuid import uuid4
import shutil
import time
import streamlit as st
import NonPrototypeDepenedncies as imp
import ClassifyAgent as Classifyer


BASE_DIR = Path(__file__).resolve().parent
IMAGES_DIR = BASE_DIR / "Images"
DONE_DIR = BASE_DIR / "done"




#DONOT turn this flase judges as this is a prototype  False  will cause it to actuallt call them 

Prototype = True








@st.cache_resource
def load_agent():
    agent = Classifyer.disasterclassifyer()
    agent.initalize()
    return agent


def save_upload(uploaded_file):
    IMAGES_DIR.mkdir(exist_ok=True)
    DONE_DIR.mkdir(exist_ok=True)
    suffix = Path(uploaded_file.name).suffix.lower() or ".jpg"
    input_path = IMAGES_DIR / f"upload_{uuid4().hex}{suffix}"
    input_path.write_bytes(uploaded_file.getbuffer())
    return input_path


def classify_and_archive(input_path):
    classification = load_agent().classify(str(input_path))
    output_path = DONE_DIR / input_path.name
    shutil.move(str(input_path), str(output_path))
    return classification, output_path


def show_styles():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@500;600;700&display=swap');
        :root { --ink: #f4f7fb; --muted: #b8c2cc; --mint: #b9f2d0; --blue: #78a2ff; }
        .stApp { background: #000; color: var(--ink); }
        .block-container { max-width: 980px; padding: 3.5rem 2rem 4rem; }
        h1, h2, h3 { font-family: 'Space Grotesk', sans-serif; color: var(--ink); }
        p, label, .stMarkdown { font-family: 'DM Sans', sans-serif; }
        .eyebrow { color: var(--blue); font: 700 0.78rem 'DM Sans', sans-serif; letter-spacing: 0.12em; text-transform: uppercase; }
        .hero { border-bottom: 1px solid #293039; padding-bottom: 2rem; margin-bottom: 2rem; }
        .hero h1 { font-size: clamp(2.5rem, 7vw, 5.4rem); line-height: .95; margin: .6rem 0 1rem; max-width: 720px; }
        .hero p { color: var(--muted); font-size: 1.05rem; line-height: 1.6; max-width: 620px; }
        .upload-card { background: #111; border: 1px solid #293039; border-radius: 8px; padding: 1.5rem; box-shadow: 0 18px 55px rgba(0, 0, 0, .35); }
        .upload-heading { margin: 0 0 .35rem; font: 700 1.15rem 'Space Grotesk', sans-serif; color: var(--ink); }
        .upload-copy { margin: 0 0 1rem; color: var(--muted); line-height: 1.5; }
        [data-testid='stFileUploader'] label { color: var(--ink); font-weight: 700; }
        [data-testid='stFileUploaderDropzone'] { min-height: 8rem; align-items: center; }
        [data-testid='stFileUploader'] { background: #171717; border: 1px dashed #607080; border-radius: 8px; padding: .5rem; }
        .result { background: #151a20; border-radius: 8px; color: var(--ink); padding: 1.4rem 1.6rem; margin-top: 1.4rem; }
        .result-label { color: var(--mint); font: 700 .76rem 'DM Sans', sans-serif; letter-spacing: .1em; text-transform: uppercase; }
        .result-value { font: 700 2.1rem 'Space Grotesk', sans-serif; margin-top: .35rem; }
        .result-meta { color: #c5d0d6; line-height: 1.5; margin: .55rem 0 0; }
        .dispatch-card { background: #111; border: 1px solid #293039; border-radius: 8px; padding: 1rem 1.15rem; margin-top: .8rem; }
        .dispatch-title { color: var(--ink); font: 700 1rem 'Space Grotesk', sans-serif; margin: 0; }
        .dispatch-copy { color: var(--muted); line-height: 1.45; margin: .3rem 0 0; }
        .dispatch-status { color: var(--mint); font-weight: 700; margin: .65rem 0 0; }
        .dispatch-status.declined { color: #ffb4ab; }
        .section-heading { color: var(--ink); font: 700 1.35rem 'Space Grotesk', sans-serif; margin: 1.8rem 0 .25rem; }
        .section-copy { color: var(--muted); margin: 0; }
        </style>
        """,
        unsafe_allow_html=True,
    )
if Prototype == False:
    imp.safet_gauge()
    
def call_firefighters():
    if Prototype:
        print("model was calling firefighters but was stopped as it was an oprototype")
        return "model was calling firefighters but was stopped as it was an oprototype"
    else:
            return "works till here"


def call_medics():
    if Prototype:
        print("model was calling medics but was stopped as it was an oprototype")
        return "model was calling medics but was stopped as it was an oprototype"
    else:
        return "works till here"


def call_rescue_team():
    if Prototype:
        print("model was calling the rescue team but was stopped as it was an oprototype")
        return "model was calling the rescue team but was stopped as it was an oprototype"
    else:
        return "works till here"


def call_water_rescue():
    if Prototype:
        print("model was calling water rescue but was stopped as it was an oprototype")
        return "model was calling water rescue but was stopped as it was an oprototype"
    else:
        return "works till here"


def call_police():
    if Prototype:
        print("model was calling police but was stopped as it was an oprototype")
        return "model was calling police but was stopped as it was an oprototype"
    else:
        return "works till here"


def call_utility_team():
    if Prototype:
        print("model was calling the utility team but was stopped as it was an oprototype")
        return "model was calling the utility team but was stopped as it was an oprototype"
    else:
        return "works till here"


def wanna_call_firefighters():
    return "Model wants to call the firefighters."


def wanna_call_medics():
    return "Model wants to call the medics."


def wanna_call_rescue_team():
    return "Model wants to call the rescue team."


def wanna_call_water_rescue():
    return "Model wants to call water rescue."


def wanna_call_police():
    return "Model wants to call the police."


def wanna_call_utility_team():
    return "Model wants to call the utility team."


RESPONSE_TEAMS = {
    "Cyclone": [call_medics, call_firefighters],
    "Earthquake": [call_rescue_team, call_medics, call_firefighters],
    "Flood": [call_water_rescue, call_medics, call_rescue_team],
    "Wildfire": [call_firefighters, call_medics, call_police],
}

TEAM_ACTIONS = {
    "call_firefighters": call_firefighters,
    "call_medics": call_medics,
    "call_rescue_team": call_rescue_team,
    "call_water_rescue": call_water_rescue,
    "call_police": call_police,
    "call_utility_team": call_utility_team,
}

WANTS_TO_CALL = {
    "call_firefighters": wanna_call_firefighters,
    "call_medics": wanna_call_medics,
    "call_rescue_team": wanna_call_rescue_team,
    "call_water_rescue": wanna_call_water_rescue,
    "call_police": wanna_call_police,
    "call_utility_team": wanna_call_utility_team,
}


def clear_app_state():
    for key in (
        "last_result",
        "processed_upload",
        "pending_dispatch",
        "dispatch_decisions",
        "dispatch_mode",
        "image_uploader",
    ):
        st.session_state.pop(key, None)


def show_dispatch_requests():
    pending_dispatch = st.session_state.get("pending_dispatch", [])
    dispatch_decisions = st.session_state.setdefault("dispatch_decisions", {})
    dispatch_mode = st.session_state.get("dispatch_mode", "approval")
    if not pending_dispatch:
        return

    if dispatch_mode == "direct":
        heading = "Dispatch complete"
        copy = "The recommended response teams were called automatically."
    else:
        heading = "Dispatch requests"
        copy = "Review each recommended response before it is called."
    st.markdown(f'<h2 class="section-heading">{heading}</h2><p class="section-copy">{copy}</p>', unsafe_allow_html=True)
    for index, team_function in enumerate(pending_dispatch):
        decision = dispatch_decisions.get(index)
        team_name = team_function if isinstance(team_function, str) else team_function.__name__
        team_action = TEAM_ACTIONS[team_name]
        wants_to_call = WANTS_TO_CALL[team_name]

        if dispatch_mode == "approval":
            st.markdown(
                f'<div class="dispatch-card"><p class="dispatch-title">{wants_to_call()}</p>'
                '<p class="dispatch-copy">Allow this response team to be contacted?</p></div>',
                unsafe_allow_html=True,
            )

        if decision is None and dispatch_mode == "approval":
            accept_column, decline_column = st.columns(2)
            with accept_column:
                if st.button("Allow", key=f"allow_dispatch_{index}", use_container_width=True):
                    dispatch_decisions[index] = team_action()
                    st.rerun()
            with decline_column:
                if st.button("Decline", key=f"decline_dispatch_{index}", use_container_width=True):
                    dispatch_decisions[index] = "Dispatch declined."
                    st.rerun()
        elif decision == "Dispatch declined.":
            st.markdown('<p class="dispatch-status declined">Dispatch declined.</p>', unsafe_allow_html=True)
        elif decision is not None:
            st.markdown(
                f'<div class="dispatch-card"><p class="dispatch-status">{decision}</p></div>',
                unsafe_allow_html=True,
            )
        elif dispatch_mode == "direct":
            st.markdown(
                '<div class="dispatch-card"><p class="dispatch-status">Dispatch completed.</p></div>',
                unsafe_allow_html=True,
            )



def main():
    st.set_page_config(page_title="DAADU | Disaster image assessment", page_icon="D", layout="centered")
    show_styles()
    if st.button("Clear", key="clear_app", help="Remove the current image, result, and dispatch requests."):
        clear_app_state()
        st.rerun()

    st.markdown(
        """
        <div class="hero">
            <div class="eyebrow">DAADU / rapid visual assessment</div>
            <h1>See the signal.<br>Move with purpose.</h1>
            <p>Upload a disaster image and the assessment engine will classify it, then archive the processed original for review.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <section class="upload-card" aria-labelledby="upload-heading">
            <h2 id="upload-heading" class="upload-heading">Upload a disaster image</h2>
            <p class="upload-copy">Add a clear image to begin the assessment.</p>
        """,
        unsafe_allow_html=True,
    )
    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png", "webp"],
        help="Supported formats: JPG, JPEG, PNG, and WEBP.",
        key="image_uploader",
    )
    if uploaded_file is not None:
        st.image(uploaded_file, caption=uploaded_file.name, use_container_width=True)
        upload_key = f"{uploaded_file.name}:{uploaded_file.size}"
        assess_column, dispatch_column = st.columns(2)
        with assess_column:
            assess_clicked = st.button("Assess", key="assess_button", use_container_width=True)
        with dispatch_column:
            dispatch_clicked = st.button(
                "Assess & Dispatch",
                key="assess_dispatch_button",
                use_container_width=True,
            )

        if assess_clicked or dispatch_clicked:
            input_path = save_upload(uploaded_file)
            try:
                with st.spinner("Assessing image..."):
                    classification, archived_path = classify_and_archive(input_path)
                st.session_state.last_result = (classification, archived_path.name)
                st.session_state.processed_upload = upload_key
                disaster = classification
                team_names = [
                    team_function.__name__ for team_function in RESPONSE_TEAMS[disaster]
                ]
                st.session_state.pending_dispatch = team_names
                st.session_state.dispatch_mode = "direct" if dispatch_clicked else "approval"
                if dispatch_clicked:
                    st.session_state.dispatch_decisions = {
                        index: TEAM_ACTIONS[team_name]()
                        for index, team_name in enumerate(team_names)
                    }
                else:
                    st.session_state.dispatch_decisions = {}
                st.rerun()
            except Exception as error:
                input_path.unlink(missing_ok=True)
                st.error(f"The image could not be classified: {error}")
    st.markdown('</section>', unsafe_allow_html=True)

    if "last_result" in st.session_state:
        classification, archived_name = st.session_state.last_result
        st.markdown(
            f"""
            <section class="result" aria-labelledby="result-heading">
                <div class="result-label">Assessment complete</div>
                <h2 id="result-heading" class="result-value">{classification}</h2>
                <p class="result-meta">Original archived as {archived_name}</p>
            </section>
            """,
            unsafe_allow_html=True,
        )
        show_dispatch_requests()


if __name__ == "__main__":
    main()