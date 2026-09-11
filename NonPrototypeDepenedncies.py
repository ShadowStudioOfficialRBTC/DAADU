import os
import streamlit as st
from PIL import Image
import numpy as np
import pywhatkit

address = "116 Girish Ghosgh Road Liluah, Hawrah -711204"
pft =   False

tod =""
def pathfromengine(txt):
    if txt == 'img':
        path = "C:/Users/ADITYA/OneDrive/Documents/DAADU/Images/images.jpg"
        return path
    else :
        path =" C:/Users/ADITYA/OneDrive/Documents/DAADU/Images/"
        return path

def save(uploaded_file):
    if uploaded_file is not None:
        save_dir = "C:/Users/ADITYA/OneDrive/Documents/DAADU/Images"
        os.makedirs(save_dir, exist_ok=True)  
        
        save_path = os.path.join(save_dir, "images.jpg")
        with open(save_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return save_path
    return None

def readandput():
    st.title("Input the image")
    tab1, = st.tabs(["Upload an Image"])

    with tab1:
        st.header("Welcome to Damage Assessment And Dispatchment Unit")
        
        # Accept only jpg format
        uploaded_file = st.file_uploader(
            "Choose an image file...", 
            type=["jpg"]
        )
        
        if uploaded_file is not None:
            saved_path = save(uploaded_file)
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            if pft == True:
                st.text(tod)
            

def safet_gauge():
    import sys
    print("This is a prototype judges i am not joking")
    sys.exit()


def call_firefighters(Prototype):
    if Prototype:
        print("model was calling firefighters but was stopped as it was an oprototype")
        return "model was calling firefighters but was stopped as it was an oprototype"
    else:
            return "works till here"


def call_medics(Prototype):
    if Prototype:
        print("model was calling medics but was stopped as it was an oprototype")
        return "model was calling medics but was stopped as it was an oprototype"
    else:
        return "works till here"


def call_rescue_team(Prototype):
    if Prototype:
        print("model was calling the rescue team but was stopped as it was an oprototype")
        return "model was calling the rescue team but was stopped as it was an oprototype"
    else:
        return "works till here"


def call_water_rescue(Prototype):
    if Prototype:
        print("model was calling water rescue but was stopped as it was an oprototype")
        return "model was calling water rescue but was stopped as it was an oprototype"
    else:
        return "works till here"