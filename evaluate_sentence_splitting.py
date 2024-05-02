import nltk
from nltk.tokenize import sent_tokenize
import stanza
import spacy

# Download necessary data for NLTK
nltk.download('punkt')

# Norwegian text
text = "Ta f.eks. dette eksempelet: Er jeg dr. Per E. Kummervold? Prøv f.eks. også: å ta deg sammen!!"

# Testing with NLTK
print("NLTK Sentence Splitting:")
nltk_sentences = sent_tokenize(text, language='norwegian')
for i, sentence in enumerate(nltk_sentences):
    print(f"NLTK Sentence {i+1}: {sentence}")

# Setup Stanza for Norwegian
stanza.download('no')  # Download Norwegian models
nlp_no = stanza.Pipeline(lang='no')  # Setup the Norwegian pipeline

# Testing with Stanza
print("\nStanza Sentence Splitting:")
doc_no = nlp_no(text)
for i, sentence in enumerate(doc_no.sentences):
    print(f"Stanza Sentence {i+1}: {sentence.text}")

# Setup spaCy with the multilingual model
nlp_spacy = spacy.load('xx_ent_wiki_sm')

# Testing with spaCy
print("\nspaCy Sentence Splitting:")
doc_spacy = nlp_spacy(text)
spacy_sentences = [sent.text for sent in doc_spacy.sents]
for i, sentence in enumerate(spacy_sentences):
    print(f"spaCy Sentence {i+1}: {sentence}")

