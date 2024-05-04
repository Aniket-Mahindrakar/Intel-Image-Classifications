import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import tensorflow as tf
import numpy as np
import streamlit as st
from PIL import Image
import requests
import sys
import path
from io import BytesIO

st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("Image Classifier for Location")
st.text("Please upload a picture of one of the places listed below:")
st.markdown("- Buildings")
st.markdown("- Forest")
st.markdown("- Glacier")
st.markdown("- Mountain")
st.markdown("- Sea")
st.markdown("- Street")

dir = path.Path(".").abspath()
sys.path.append(dir)

@st.cache_resource
def load_model():
  model = tf.keras.models.load_model(dir+'/app/models/')
  return model

with st.spinner('Loading Model Into Memory....'):
  model = load_model()

classes = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']

def decode_img(image):
  img = tf.image.decode_jpeg(image, channels=3)  
  img = tf.image.resize(img,[150,150])
  return np.expand_dims(img, axis=0)

# path = st.text_input('Enter Image URL to Classify.. ','https://storage.googleapis.com/image_classification_2021/Glacier-Argentina-South-America-blue-ice.JPEG')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    content = uploaded_file.read()

    st.write("Predicted Class :")
    with st.spinner('classifying.....'):
      label =np.argmax(model.predict(decode_img(content)),axis=1)
      st.write(classes[label[0]])    
    st.write("")
    image = Image.open(BytesIO(content))
    st.image(image, caption='Classifying Image', use_column_width=True)