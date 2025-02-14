# Medi-Assist A Chatbot For Common Chronic Diseases Using DL 
Welcome to the Medi-Assist project! This repository contains the code for a chatbot that utilizes an LSTM (Long Short-Term Memory) neural network, a part of deep learning, for understanding and generating responses, integrated with a Flask web application for an interactive user interface.

Medi-Assist aims to create a conversational AI chatbot that can understand user input and generate appropriate responses using deep learning. The chatbot is trained using an LSTM model on predefined intents, which are sets of patterns and responses. The Flask web application serves as the frontend interface where users can interact with the chatbot. It takes symptoms as input and gives a chronic disease as output.
(note: For better accuracy give more symptoms as input)

# Features
•	LSTM Model: Utilizes an LSTM neural network for sequence learning and text classification.

•	Intent-Based Responses: Responds to user inputs based on predefined intents.

•	Interactive Web Interface: Flask web application for user interaction.

•	Team Information Page: Details about the project contributors.

•	Symptoms and FAQ Pages: Lists of symptoms and FAQs for user reference.


# Requirements
•	Python 3.6+

•	TensorFlow 2.x

•	Flask

•	NLTK

•	NumPy

•	scikit-learn


# Working of Chatbot



https://github.com/Rajat-Kiresur/107788748/d7aca39b-9580-448d-8c88-6c7f0fe899ab


#    

https://github.com/Rajat-Kiresur/107788748/25288ba6-f1aa-4897-80b8-dc4f0b588b5a




# Snapshots

# 1. Chatbot Training
![344393238-a45e460e-3315-4191-b503-4060d5f1809f](https://github.com/user-attachments/assets/33a634d3-13a2-400a-a47f-fea23f5a9757)

                    

# 2. Frequently asked questions
![344393278-66a17782-b433-471a-a0d0-65a75bfa006a](https://github.com/user-attachments/assets/aefba27b-fb5e-468c-bc95-c5580612f662)

                   
# 3. List of symptoms
![344393293-6504dc2a-3c4e-44b9-9935-401bed31688c](https://github.com/user-attachments/assets/93e8da69-62df-4922-9da8-5feb0685a769)


# 4. Navigating throughout
![344393330-fadc18b8-9829-476e-8875-bc476411e5d6](https://github.com/user-attachments/assets/bfc2285c-d5fc-404b-a90a-50d9f694b74f)

    
# 5. Output(predection of chronic disease)
![344393354-ada44074-7f20-46a1-8597-22c2e057fdf2](https://github.com/user-attachments/assets/cfcbbce6-d734-4793-924e-d385544cb460)




# Installation
1.	Clone the repository:
    git clone https://github.com/Rajat-Kiresur/MEDI---ASSIST-CHATBOT-FOR-COMMON-CHRONIC-DISEASES-USING-DL
3.	Install the required packages:
    pip install -r requirements.txt 
4.	Download NLTK data:
    import nltk nltk.download('punkt') nltk.download('wordnet') nltk.download('omw-1.4') 

# Usage
1.	Train the Model:
    python train_chatbot.py 
2.	Run the Flask Application:
    python app.py 
3.	Open your browser and go to interact with the chatbot.

# Project Structure

This image represents the directory structure of the Medi-Assist project, detailing the organization of files and folders including data, models, templates, static assets, and main Python scripts

![344394796-21f42c1c-2e49-48b7-8ed5-1675c8606db0](https://github.com/user-attachments/assets/9c4efc08-7ae0-481a-a7f3-015c3e4ebdd3)



# Model Training
The model is trained on a dataset of intents defined in intents.json. Each intent includes a tag, patterns, and responses. The LSTM model processes the text data, and after training, the model is saved as chatbot_model.h5.

# Training Script
The training script (train_chatbot.py) performs the following steps:
-> Loads and preprocesses the data.

-> Defines and compiles the LSTM model.

-> Trains the model on the preprocessed data.

-> Saves the trained model and necessary metadata.


# Flask Application
The Flask application (app.py) serves as the web interface for the chatbot. It includes routes for the homepage, team information, symptoms, and FAQs. The chatbot interaction is handled through the /get_response endpoint, which processes user input and returns a response from the trained model.

# License
This project is licensed under the MIT License. See the LICENSE file for more details.



