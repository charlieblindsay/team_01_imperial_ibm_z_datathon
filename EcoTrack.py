import streamlit as st
import detection

css = """
<style>

    .stApp {


    }

    .text-center {
        text-align: center;
        padding: 0px;
        border: 0px;
        margin: 0px 0px 0px 0px;
    }

</style>
"""

st.markdown(css, unsafe_allow_html=True)

st.info("""
    # 🌿
    # EcoTrack
    ###### Enviromental Protection and Sustainability Monitoring

    Welcome to EcoTrack! 👋 Our vision for a safer,
    more proactive world. In the era of unprecedented environmental
    changes, we're leveraging cutting-edge technology to predict, 
    monitor, and assess natural disasters, turning data into
    actionable insights.
    """)

st.info("""
    ## The Urgency of Now

    Every year, natural disasters claim lives, devastate communities
    , and disrupt ecosystems. With climate change, we're facing an
    increase in both the frequency and severity of these events. The
    need for advanced, accurate monitoring and response mechanisms has
    never been more critical.
    """)

st.info(
    """
    ## How it works

    EcoTrack has been designed to be light weight, easy to use, and
    adaptive to your needs. From live drone footage, to image files: EcoTrack
    will be able to help. Try it out below:
    """
)

datatype = st.selectbox("", ["choose an option",
                             "from this computer",
                             "use camera"])

image = None
if datatype == "from this computer":
    image = st.file_uploader("upload a file")
elif datatype == "use camera":
    image = st.camera_input("take a photo")

if image:
    st.image(detection.detection(image))


st.info(
    """
    ## Proven to Work

    EcoTrack has already been tried and tested on various datasets,
    proving that it is an adaptive, flexible model.
    """
)

st.info(
    """
    ## Vision 

    Our mission with EcoTrack is to make it quick and easy to provide real time
    safety monitoring of wildfires, in the areas that need it most. It will be
    an affordable but effective tool, useful for both local authorities, and
    government organisations.
    """
)