import streamlit as st
import numpy as np
from PIL import Image
from tensorflow import keras
import tempfile
import cv2
import math 




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
# Load the model
model = keras.models.load_model('fire_detection_model.h5')  

st.title("Image Classification App")
st.write("Upload an image to classify")


datatype = st.selectbox("", ["choose an option",
                             "upload image",
                             "use camera", 
                             "upload video"])

video_file = None
image = None
image_placeholder = st.empty()

if datatype == "upload image":
    image = st.file_uploader("upload a file")
elif datatype == "use camera":
    image = st.camera_input("take a photo")
elif datatype == "upload video":
    video_file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])

if (datatype == "upload image" or datatype == "use camera") and image is not None:
    image = Image.open(image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess the image
    image = image.resize((224, 224))
    image = np.array(image)
    image = image / 255.0  # Normalize the image

    # Make predictions
    image = np.expand_dims(image, axis=0)  # Add a batch dimension
    prediction = model.predict(image)

    # threshold to decide the class based on the prediction
    threshold = 0.5
    if prediction[0][0] >= threshold:
        st.write("Prediction: Fire")
    else:
        st.write("Prediction: Not Fire")

if video_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(video_file.read())

    cap = cv2.VideoCapture(tfile.name)

    frame_rate = cap.get(5)  
    while(cap.isOpened()):
        frame_id = cap.get(1)  
        ret, frame = cap.read()
        if (ret != True):
            break
        if (frame_id % math.floor(frame_rate) == 0):
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
            image = Image.fromarray(frame)  
            image = image.resize((224, 224))  
            image = np.array(image) 
            image = image / 255.0  
            image = np.expand_dims(image, axis=0) 
            prediction = model.predict(image)  

            threshold = 0.5
            if prediction[0][0] >= threshold:
                result_text = "Prediction: Fire"
            else:
                result_text = "Prediction: Not Fire"

            image_placeholder.image(frame, caption=result_text, use_column_width=True)
            
            #st.image(frame, caption=result_text, use_column_width=True)

    cap.release()


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
