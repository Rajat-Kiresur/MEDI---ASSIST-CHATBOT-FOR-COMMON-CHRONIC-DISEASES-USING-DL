import os
import json
import csv
import random

# Get the current directory
current_directory = os.path.dirname(__file__)

# Load intents from intents.json
json_file_path = os.path.join(current_directory, 'intents.json')
with open(json_file_path, 'r') as file:
    intents_data = json.load(file)

# Phrases to be randomly selected
phrases = [
    "I am feeling",
    "I am experiencing",
    "I have a sense that",
    "It seems to me like",
    "I am sensing",
    "I have a feeling that",
    "I feel as though",
    "I am noticing",
    "I have a hunch that",
    "I get the impression that",
    "I am aware that"
]

# Write patterns to a CSV file
csv_file_path = os.path.join(current_directory, 'patterns.csv')
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Pattern'])  # Single header for the combined pattern line

    # Process each intent to include full patterns
    for intent in intents_data['intents']:
        patterns = intent['patterns']
        # Choose a random phrase
        phrase = random.choice(phrases)
        # Combine the phrase with the patterns
        combined_pattern = f'{phrase} {", ".join(patterns)}'
        writer.writerow([combined_pattern])

print(f"CSV file saved successfully to: {csv_file_path}")
