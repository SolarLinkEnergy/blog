# dependencies
# 1. nltk
# 2. pandas

# Import the required libraries
import nltk
import pandas as pd

# Define a function to categorize and label the information
def categorize_and_label(text):
    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text)

    # Label each sentence based on its content
    labeled_sentences = []
    for sentence in sentences:
        if 'plaintiff' in sentence.lower():
            labeled_sentences.append(('Party', sentence))
        elif 'defendant' in sentence.lower():
            labeled_sentences.append(('Party', sentence))
        elif 'claim' in sentence.lower():
            labeled_sentences.append(('Claim', sentence))
        else:
            labeled_sentences.append(('Fact', sentence))

    # Return the labeled sentences as a pandas DataFrame
    return pd.DataFrame(labeled_sentences, columns=['Label', 'Sentence'])

# Read the input text file
text = open('input.txt', 'r').read()

# Categorize and label the information
labeled_data = categorize_and_label(text)

# Write the labeled data to an output file
labeled_data.to_csv('output.csv', index=False)



#nltk
#pandas

