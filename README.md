# Intel Image Classification
Intel Image Classification using Convolutional Neural Network (CNN) is a method aimed at categorizing images based on their content, leveraging a dataset from Kaggle containing 25,000 images divided into six classes: buildings, forests, glaciers, mountains, seas, and streets. Through the utilization of CNNs, which are specialized neural networks for image processing tasks, the model is trained to recognize distinctive features within each image class. This involves multiple layers of neurons, including convolutional layers that extract low-level features like edges and curves, and subsequent layers that build upon these features to identify more abstract concepts. Dependencies for implementing this project include TensorFlow, Keras, scikit-learn, as well as standard libraries like pandas, numpy, and matplotlib.

# Input
![image](https://github.com/Aniket-Mahindrakar/Intel-Image-Classifications/assets/25640390/9de5f952-6646-4a1a-be2f-59d6e02bce57)

# Output
![image](https://github.com/Aniket-Mahindrakar/Intel-Image-Classifications/assets/25640390/2daf2280-7839-4d12-a493-1163c9c230d2)

# Key Highlights
- **Data Preparation:** Created augmented data generators using ImageDataGenerator from Keras, including rescaling, rotation, shifting, zooming, and horizontal flipping for training data, while only rescaling is applied for validation data, followed by loading data from directories and converting them into batches for training and testing.
- **Model Development:** Constructed a Convolutional Neural Network (CNN) model using Keras, comprising several layers including convolutional layers with ReLU activation, max-pooling layers, flattening layer, and dense layers with softmax activation. The model is compiled with categorical cross-entropy loss, Adam optimizer, and accuracy metrics.
- **Model Deployment:** Facilitated easy deployment of the models using Docker, Kubernetes, and GCP cloud deployment providing clear instructions for building and running a container.

# Deployment Instructions
### Kubernetes
- Apply the Kubernetes deployment YAML file:
  ```
  kubectl apply -f ./K8s/kubernetes_deployment.yml
  ```
- Apply the Kubernetes service YAML file:
  ```
  kubectl apply -f ./K8s/kubernetes_service.yml
  ```
- Check the status of the deployed service:
  ```
  kubectl get svc
  ```
### Docker
- Clean up any unused Docker resources
  ```
  docker system prune
  ```
- Build the Docker image
  ```
  docker build . -t aniketmm98/image_classifier
  ```
- Run the Docker container
  ```
  docker run --rm -it -p 8501:8501 --user=42420:42420 aniketmm98/image_classifier:latest
  ```
### Google Cloud Platform
- Create a Kubernetes cluster
  ```
  gcloud container clusters create mykube --zone "us-central1" --machine-type "n1-standard-1" --num-nodes "1" --project aniket-ai
  ```
