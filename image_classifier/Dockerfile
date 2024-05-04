# lightweight python
FROM python:3.7-slim

RUN apt-get update

# Copy local code to the container image.
RUN mkdir /image_classifier && chown -R 42420:42420 /image_classifier
ENV APP_HOME /image_classifier
WORKDIR $APP_HOME
COPY . ./

RUN ls -la $APP_HOME/

# Install dependencies
RUN pip install -r requirements.txt

# Run the streamlit on container startup
CMD [ "streamlit", "run", "myapp.py", "--server.address=0.0.0.0"]

