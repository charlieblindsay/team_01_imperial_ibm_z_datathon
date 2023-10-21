
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io

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

# datatype = st.selectbox("", ["choose an option",
#                              "from this computer",
#                              "use camera"])

import streamlit as st
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np

# Load the model
model = keras.models.load_model('fire_detection_model.h5')  # Replace with your model's path

st.title("Image Classification App")
st.write("Upload an image to classify")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Preprocess the image
    image = image.resize((224, 224))
    image = np.array(image)
    image = image / 255.0  # Normalize the image

    # Make predictions
    image = np.expand_dims(image, axis=0)  # Add a batch dimension
    prediction = model.predict(image)

    # You may have a threshold to decide the class based on the prediction
    threshold = 0.5
    if prediction[0][0] >= threshold:
        st.write("Prediction: Fire")
    else:
        st.write("Prediction: Not Fire")


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