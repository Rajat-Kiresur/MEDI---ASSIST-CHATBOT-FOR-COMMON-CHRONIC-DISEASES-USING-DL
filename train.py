import random
import json
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

# Load intents
with open('intent.json') as json_file:
    intents = json.load(json_file)

# Extract data from intents
texts = []
labels = []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        texts.append(pattern)
        labels.append(intent['tag'])

# Tokenize texts
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
vocab_size = len(tokenizer.word_index) + 1

# Convert texts to sequences
sequences = tokenizer.texts_to_sequences(texts)

# Pad sequences
max_sequence_len = max([len(seq) for seq in sequences])
sequences = pad_sequences(sequences, maxlen=max_sequence_len, padding='post')

# One-hot encode labels
label_encoder = LabelEncoder()
label_encoder.fit(labels)
encoded_labels = label_encoder.transform(labels)

# Define the LSTM RNN model
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=64))
model.add(LSTM(128))
model.add(Dropout(0.5))
model.add(Dense(len(set(labels)), activation='softmax'))

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(sequences, encoded_labels, epochs=200, batch_size=5, verbose=1)

# Save the model
model.save('chatbot_model.h5.keras')

print('Training Done')
