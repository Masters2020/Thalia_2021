# -*- coding: utf-8 -*-
"""BERT_CoNLL-2003.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19lQUANCxDzYcSuYu3kV4fMv4CVSZiJKu

Code for training BERT is from https://github.com/kamalkraj/BERT-NER.

Important: In order to generate NER-tags from the YouTube transcript dataset, the keyword lists need to be first compiled. These can be found in the Keyword list folder on GitHub, or you can compile them yourself in the svm_classification.py file.
"""

import pickle
from google.colab import drive

drive.mount('/content/drive')

"""This code is to load all the keyword lists once they are created:"""

import os
filepath = '/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1'
os.chdir(filepath)
import pickle

keyword = 10
with open(str(keyword) + 'keyword_list1.pickle', 'rb') as f:
    keyword_list1_10 = pickle.load(f)
with open(str(keyword) + 'keyword_list2.pickle', 'rb') as f:
    keyword_list2_10 = pickle.load(f)

import os
filepath = '/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1'
os.chdir(filepath)
import pickle

keyword = 15
with open(str(keyword) + 'keyword_list1.pickle', 'rb') as f:
    keyword_list1_15 = pickle.load(f)
with open(str(keyword) + 'keyword_list2.pickle', 'rb') as f:
    keyword_list2_15 = pickle.load(f)

import os
filepath = '/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1'
os.chdir(filepath)
import pickle

keyword = 20
with open(str(keyword) + 'keyword_list1.pickle', 'rb') as f:
    keyword_list1_20 = pickle.load(f)
with open(str(keyword) + 'keyword_list2.pickle', 'rb') as f:
    keyword_list2_20 = pickle.load(f)

import os
filepath = '/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1'
os.chdir(filepath)
import pickle

keyword = 50
with open(str(keyword) + 'keyword_list1.pickle', 'rb') as f:
    keyword_list1_50 = pickle.load(f)
with open(str(keyword) + 'keyword_list2.pickle', 'rb') as f:
    keyword_list2_50 = pickle.load(f)

import os
filepath = '/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1'
os.chdir(filepath)
import pickle

keyword = 100
with open(str(keyword) + 'keyword_list1.pickle', 'rb') as f:
    keyword_list1_100 = pickle.load(f)
with open(str(keyword) + 'keyword_list2.pickle', 'rb') as f:
    keyword_list2_100 = pickle.load(f)

import os
filepath = '/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1'
os.chdir(filepath)
import pickle

keyword = 200
with open(str(keyword) + 'keyword_list1.pickle', 'rb') as f:
    keyword_list1_200 = pickle.load(f)
with open(str(keyword) + 'keyword_list2.pickle', 'rb') as f:
    keyword_list2_200 = pickle.load(f)

import os
filepath = '/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1'
os.chdir(filepath)
import pickle

keyword = 500
with open(str(keyword) + 'keyword_list1.pickle', 'rb') as f:
    keyword_list1_500 = pickle.load(f)
with open(str(keyword) + 'keyword_list2.pickle', 'rb') as f:
    keyword_list2_500 = pickle.load(f)

import os
filepath = '/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1'
os.chdir(filepath)
import pickle

keyword = 750
with open(str(keyword) + 'keyword_list1.pickle', 'rb') as f:
    keyword_list1_750 = pickle.load(f)
with open(str(keyword) + 'keyword_list2.pickle', 'rb') as f:
    keyword_list2_750 = pickle.load(f)

import os
filepath = '/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1'
os.chdir(filepath)
import pickle

keyword = 1000
with open(str(keyword) + 'keyword_list1.pickle', 'rb') as f:
    keyword_list1_1000 = pickle.load(f)
with open(str(keyword) + 'keyword_list2.pickle', 'rb') as f:
    keyword_list2_1000 = pickle.load(f)



"""The next step is to load and train the BERT model. Once the model is pretrained on the NER-labeled dataset, BERT can predict NER tags on the keyword lists.

**Clone Repository:**
First Step is to clone KAMALKRAJ Github Repository. Below code is command to clone repository:
"""

import os
path = '/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/BERT-CoNLL'
os.chdir(path)

!git clone https://github.com/kamalkraj/BERT-NER.git

"""Use "ls -l" command for verfying the repository cloned properly."""

ls -l

"""Now go to 'BERT-NER' directory by using below command:"""

cd BERT-NER/

"""**BERT-NER files:** Use 'ls -l' to check content inside BERT-NER folder. These below files and folders we will use for finetuning and prediction."""

ls -l

""""requirements.txt" contains all the pacakages that required for trainig and inference. By using below command install all the pacakages."""

!pip3 install -r requirements.txt

"""### **Fine-Tuning:**
For finetuning or training the **bert-base** model run the 'run_ner.py' as command given below.

In below command we have to pass different arguments:
   
*   '--data_dir' argument required to collect dataset. Pass 'data/' as argument which we can see as directory inside 'BERT-NER' folder for the previous comment and command for 'BERT-NER files' .
*   '--bert_model' used to download **pretrained bert base** model of Hugging Face transformers. There are different model-names as suggested by hugging face for argument, here we select 'bert-base-cased'.
*   '--task_name' argument used for task to perform. Enter 'ner' as we will train the model for Named Entity Recogintion(NER).
*   '--output_dir' argument is for where to store fine-tuned model. We give name 'out_base' for directory  where fine-tuned model stored.
*   Other arguments like '--max_seq_length', '--num_train_epochs' and '--warmup_proportion', just give values as suggested in repository.
*   For training pass argument '--do_train' and after that evaluating for results pass argument '--do_eval'.





    
"""

!python run_ner.py --data_dir=data/ --bert_model=bert-base-cased --task_name=ner --output_dir=out_ner --max_seq_length=128 --do_train --num_train_epochs 5 --do_eval --warmup_proportion=0.1

"""**Overwrite 'bert.py' files:**
In 'bert.py' we have made changes for better representation and display of '**entity detected**' and their '**entity types**' for the given sentence to test or inference.
>Overwrite the 'bert.py' by using below command.
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile bert.py
# """BERT NER Inference."""
# 
# from __future__ import absolute_import, division, print_function
# 
# import json
# import os
# 
# import torch
# import torch.nn.functional as F
# from nltk import word_tokenize
# from pytorch_transformers import (BertConfig, BertForTokenClassification,
#                                   BertTokenizer)
# 
# 
# class BertNer(BertForTokenClassification):
# 
#     def forward(self, input_ids, token_type_ids=None, attention_mask=None, valid_ids=None):
#         sequence_output = self.bert(input_ids, token_type_ids, attention_mask, head_mask=None)[0]
#         batch_size,max_len,feat_dim = sequence_output.shape
#         valid_output = torch.zeros(batch_size,max_len,feat_dim,dtype=torch.float32,device='cuda' if torch.cuda.is_available() else 'cpu')
#         for i in range(batch_size):
#             jj = -1
#             for j in range(max_len):
#                     if valid_ids[i][j].item() == 1:
#                         jj += 1
#                         valid_output[i][jj] = sequence_output[i][j]
#         sequence_output = self.dropout(valid_output)
#         logits = self.classifier(sequence_output)
#         return logits
# 
# class Ner:
# 
#     def __init__(self,model_dir: str):
#         self.model , self.tokenizer, self.model_config = self.load_model(model_dir)
#         self.label_map = self.model_config["label_map"]
#         self.max_seq_length = self.model_config["max_seq_length"]
#         self.label_map = {int(k):v for k,v in self.label_map.items()}
#         self.device = "cuda" if torch.cuda.is_available() else "cpu"
#         self.model = self.model.to(self.device)
#         self.model.eval()
# 
#     def load_model(self, model_dir: str, model_config: str = "model_config.json"):
#         model_config = os.path.join(model_dir,model_config)
#         model_config = json.load(open(model_config))
#         model = BertNer.from_pretrained(model_dir)
#         tokenizer = BertTokenizer.from_pretrained(model_dir, do_lower_case=model_config["do_lower"])
#         return model, tokenizer, model_config
# 
#     def tokenize(self, text: str):
#         """ tokenize input"""
#         words = word_tokenize(text)
#         tokens = []
#         valid_positions = []
#         for i,word in enumerate(words):
#             token = self.tokenizer.tokenize(word)
#             tokens.extend(token)
#             for i in range(len(token)):
#                 if i == 0:
#                     valid_positions.append(1)
#                 else:
#                     valid_positions.append(0)
#         return tokens, valid_positions
# 
#     def preprocess(self, text: str):
#         """ preprocess """
#         tokens, valid_positions = self.tokenize(text)
#         ## insert "[CLS]"
#         tokens.insert(0,"[CLS]")
#         valid_positions.insert(0,1)
#         ## insert "[SEP]"
#         tokens.append("[SEP]")
#         valid_positions.append(1)
#         segment_ids = []
#         for i in range(len(tokens)):
#             segment_ids.append(0)
#         input_ids = self.tokenizer.convert_tokens_to_ids(tokens)
#         input_mask = [1] * len(input_ids)
#         while len(input_ids) < self.max_seq_length:
#             input_ids.append(0)
#             input_mask.append(0)
#             segment_ids.append(0)
#             valid_positions.append(0)
#         return input_ids,input_mask,segment_ids,valid_positions
# 
#     def predict(self, text: str):
#         input_ids,input_mask,segment_ids,valid_ids = self.preprocess(text)
#         input_ids = torch.tensor([input_ids],dtype=torch.long,device=self.device)
#         input_mask = torch.tensor([input_mask],dtype=torch.long,device=self.device)
#         segment_ids = torch.tensor([segment_ids],dtype=torch.long,device=self.device)
#         valid_ids = torch.tensor([valid_ids],dtype=torch.long,device=self.device)
#         with torch.no_grad():
#             logits = self.model(input_ids, segment_ids, input_mask,valid_ids)
#         logits = F.softmax(logits,dim=2)
#         logits_label = torch.argmax(logits,dim=2)
#         logits_label = logits_label.detach().cpu().numpy().tolist()[0]
# 
#         logits_confidence = [values[label].item() for values,label in zip(logits[0],logits_label)]
# 
#         logits = []
#         pos = 0
#         for index,mask in enumerate(valid_ids[0]):
#             if index == 0:
#                 continue
#             if mask == 1:
#                 logits.append((logits_label[index-pos],logits_confidence[index-pos]))
#             else:
#                 pos += 1
#         logits.pop()
# 
#         labels = [(self.label_map[label],confidence) for label,confidence in logits]
#         words = word_tokenize(text)
#         assert len(labels) == len(words)
# 
#         Person = []
#         Location = []
#         Organization = []
#         Miscelleneous = []
# 
#         for word, (label, confidence) in zip(words, labels):
#             if label=="B-PER" or label=="I-PER":
#                 Person.append(word)
#             elif label=="B-LOC" or label=="I-LOC":
#                 Location.append(word)
#             elif label=="B-ORG" or label=="I-ORG":
#                 Organization.append(word)
#             elif label=="B-MISC" or label=="I-MISC":
#                 Miscelleneous.append(word)
#             else:
#                 output = None
# 
#         output = []
#         for word, (label, confidence) in zip(words, labels):      
#             if label == "B-PER":
#                 output.append(' '.join(Person) + ": Person")
#             if label=="B-LOC":
#                 output.append(' '.join(Location) + ": Location")
#             if label=="B-MISC":
#                 output.append(' '.join(Miscelleneous) + ": Miscelleneous Entity")
#             if label=="B-ORG":
#                 output.append(' '.join(Organization) + ": Organization")
#                 
#         return output
# 
#

"""Put all the keyword lists into one list in order for BERT to make predictions on it. """

keyword_lists = [keyword_list1_10, keyword_list2_10, keyword_list1_15, keyword_list2_15, keyword_list1_20, keyword_list2_20, keyword_list1_50, keyword_list2_50, keyword_list1_100,
                 keyword_list2_100, keyword_list1_200, keyword_list2_200, keyword_list1_500, keyword_list2_500,
                 keyword_list1_750, keyword_list2_750, keyword_list1_1000, keyword_list2_1000]

"""Next is code to replace the first letter of a word with a captical letter, since NER gets a better performance with capital first letters for words referring to a person or organizations. Besides that, the keywords are also transformed to input that BERT can take. """

# Python program to convert a list
# to string using join() function
    
# Function to convert  
def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

k_list1_10 = listToString(keyword_list1_10)
k_list2_10 = listToString(keyword_list2_10)
k_list1_15 = listToString(keyword_list1_15)
k_list2_15 = listToString(keyword_list2_15)
k_list1_20 = listToString(keyword_list1_20)
k_list2_20 = listToString(keyword_list2_20)
k_list1_50 = listToString(keyword_list1_50)
k_list2_50 = listToString(keyword_list2_50)
k_list1_100 = listToString(keyword_list1_100)
k_list2_100 = listToString(keyword_list2_100)
k_list1_200 = listToString(keyword_list1_200)
k_list2_200 = listToString(keyword_list2_200)
k_list1_500 = listToString(keyword_list1_500)
k_list2_500 = listToString(keyword_list2_500)
k_list1_750 = listToString(keyword_list1_750)
k_list2_750 = listToString(keyword_list2_750)
k_list1_1000 = listToString(keyword_list1_1000)
k_list2_1000 = listToString(keyword_list2_1000)

k_list1_10 = k_list1_10.title().split()
k_list2_10 = k_list2_10.title().split()
k_list1_15 = k_list1_15.title().split()
k_list2_15 = k_list2_15.title().split()
k_list1_20 = k_list1_20.title().split()
k_list2_20 = k_list2_20.title().split()
k_list1_50 = k_list1_50.title().split()
k_list2_50 = k_list2_50.title().split()
k_list1_100 = k_list1_100.title().split()
k_list2_100 = k_list2_100.title().split()
k_list1_200 = k_list1_200.title().split()
k_list2_200 = k_list2_200.title().split()
k_list1_500 = k_list1_500.title().split()
k_list2_500 = k_list2_500.title().split()
k_list1_750 = k_list1_750.title().split()
k_list2_750 = k_list2_750.title().split()
k_list1_1000 = k_list1_1000.title().split()
k_list2_1000 = k_list2_1000.title().split()

"""Run the below cell for final output: 

In the below cell first line we call the '**Ner**' class from the 'bert.py' file. '**Ner**' class intialize our fine-tuned model.

Store the model in any variable. In below cell we store our fine-tuned model into 'model' variable.

Pass any text as a string for entity detection. 

Use '**predict**' function of class '**Ner**' for detecting entities for the 'text' and stored it into 'output'. In 'output' variable we have a detected entities of list.

Run 'for loop' for list formed 'output'. Print the 'prediction' of 'for loop'.
"""

import nltk
nltk.download('punkt')

from bert import Ner
model = Ner("out_ner/")

"""Example:"""

text= "The U.S. President Donald Trump came to visit Ahmedabad first time at Motera Stadium with our Prime Minister Narendra Modi in February 2020."
print("Text to predict Entity:", text)

output = model.predict(text)
for prediction in output:
    print(prediction)

new_k_list1_10 = []
for t in k_list1_10:
  output = model.predict(t)
  for p in output:
    new_k_list1_10.append(p)

new_k_list2_10 = []
for t in k_list2_10:
  output = model.predict(t)
  for p in output:
    new_k_list2_10.append(p)

new_k_list1_15 = []
for t in k_list1_15:
  output = model.predict(t)
  for p in output:
    new_k_list1_15.append(p)

new_k_list2_15 = []
for t in k_list2_15:
  output = model.predict(t)
  for p in output:
    new_k_list2_15.append(p)

new_k_list1_20 = []
for t in k_list1_20:
  output = model.predict(t)
  for p in output:
    new_k_list1_20.append(p)

new_k_list2_20 = []
for t in k_list2_20:
  output = model.predict(t)
  for p in output:
    new_k_list2_20.append(p)

new_k_list1_50 = []
for t in k_list1_50:
  output = model.predict(t)
  for p in output:
    new_k_list1_50.append(p)

new_k_list2_50 = []
for t in k_list2_50:
  output = model.predict(t)
  for p in output:
    new_k_list2_50.append(p)

new_k_list1_100 = []
for t in k_list1_100:
  output = model.predict(t)
  for p in output:
    new_k_list1_100.append(p)

new_k_list2_100 = []
for t in k_list2_100:
  output = model.predict(t)
  for p in output:
    new_k_list2_100.append(p)

new_k_list1_200 = []
for t in k_list1_200:
  output = model.predict(t)
  for p in output:
    new_k_list1_200.append(p)

new_k_list2_200 = []
for t in k_list2_200:
  output = model.predict(t)
  for p in output:
    new_k_list2_200.append(p)

new_k_list1_500 = []
for t in k_list1_500:
  output = model.predict(t)
  for p in output:
    new_k_list1_500.append(p)

new_k_list2_500 = []
for t in k_list2_500:
  output = model.predict(t)
  for p in output:
    new_k_list2_500.append(p)

new_k_list1_750 = []
for t in k_list1_750:
  output = model.predict(t)
  for p in output:
    new_k_list1_750.append(p)

new_k_list2_750 = []
for t in k_list2_750:
  output = model.predict(t)
  for p in output:
    new_k_list2_750.append(p)

new_k_list1_1000 = []
for t in k_list1_1000:
  output = model.predict(t)
  for p in output:
    new_k_list1_1000.append(p)

new_k_list2_1000 = []
for t in k_list2_1000:
  output = model.predict(t)
  for p in output:
    new_k_list2_1000.append(p)

"""The NER-tags are now extracted on the keyword lists. Only the person and organization tags will be used in the current research. The following code makes sure the NER-keyword lists have the same format again as the regular keyword lists and the person-and organization NER tags are merged into one list. """

person_keywords_1_10 = []
organization_keywords_1_10 = []

for match in new_k_list1_10:
    if "Person" in match:
      person_keywords_1_10.append(match)
    if "Organization" in match:
      organization_keywords_1_10.append(match)

print(person_keywords_1_10)
print(organization_keywords_1_10)

person_keywords_2_10 = []
organization_keywords_2_10 = []

for match in new_k_list2_10:
    if "Person" in match:
      person_keywords_2_10.append(match)
    if "Organization" in match:
      organization_keywords_2_10.append(match)

print(person_keywords_2_10)
print(organization_keywords_2_10)

person_keywords_1_15 = []
organization_keywords_1_15 = []

for match in new_k_list1_15:
    if "Person" in match:
      person_keywords_1_15.append(match)
    if "Organization" in match:
      organization_keywords_1_15.append(match)

print(person_keywords_1_15)
print(organization_keywords_1_15)

person_keywords_2_15 = []
organization_keywords_2_15 = []

for match in new_k_list2_15:
    if "Person" in match:
      person_keywords_2_15.append(match)
    if "Organization" in match:
      organization_keywords_2_15.append(match)

print(person_keywords_2_15)
print(organization_keywords_2_15)

person_keywords_1_20 = []
organization_keywords_1_20 = []

for match in new_k_list1_20:
    if "Person" in match:
      person_keywords_1_20.append(match)
    if "Organization" in match:
      organization_keywords_1_20.append(match)

print(person_keywords_1_20)
print(organization_keywords_1_20)

person_keywords_2_20 = []
organization_keywords_2_20 = []

for match in new_k_list2_20:
    if "Person" in match:
      person_keywords_2_20.append(match)
    if "Organization" in match:
      organization_keywords_2_20.append(match)

print(person_keywords_2_20)
print(organization_keywords_2_20)

person_keywords_1_50 = []
organization_keywords_1_50 = []

for match in new_k_list1_50:
    if "Person" in match:
      person_keywords_1_50.append(match)
    if "Organization" in match:
      organization_keywords_1_50.append(match)

print(person_keywords_1_50)
print(organization_keywords_1_50)

person_keywords_2_50 = []
organization_keywords_2_50 = []

for match in new_k_list2_50:
    if "Person" in match:
      person_keywords_2_50.append(match)
    if "Organization" in match:
      organization_keywords_2_50.append(match)

print(person_keywords_2_50)
print(organization_keywords_2_50)

person_keywords_1_100 = []
organization_keywords_1_100 = []

for match in new_k_list1_100:
    if "Person" in match:
      person_keywords_1_100.append(match)
    if "Organization" in match:
      organization_keywords_1_100.append(match)

print(person_keywords_1_100)
print(organization_keywords_1_100)

person_keywords_2_100 = []
organization_keywords_2_100 = []

for match in new_k_list2_100:
    if "Person" in match:
      person_keywords_2_100.append(match)
    if "Organization" in match:
      organization_keywords_2_100.append(match)

print(person_keywords_2_100)
print(organization_keywords_2_100)

person_keywords_1_200 = []
organization_keywords_1_200 = []

for match in new_k_list1_200:
    if "Person" in match:
      person_keywords_1_200.append(match)
    if "Organization" in match:
      organization_keywords_1_200.append(match)

print(person_keywords_1_200)
print(organization_keywords_1_200)

person_keywords_2_200 = []
organization_keywords_2_200 = []

for match in new_k_list2_200:
    if "Person" in match:
      person_keywords_2_200.append(match)
    if "Organization" in match:
      organization_keywords_2_200.append(match)

print(person_keywords_2_200)
print(organization_keywords_2_200)

person_keywords_1_500 = []
organization_keywords_1_500 = []

for match in new_k_list1_500:
    if "Person" in match:
      person_keywords_1_500.append(match)
    if "Organization" in match:
      organization_keywords_1_500.append(match)

print(person_keywords_1_500)
print(organization_keywords_1_500)

person_keywords_2_500 = []
organization_keywords_2_500 = []

for match in new_k_list2_500:
    if "Person" in match:
      person_keywords_2_500.append(match)
    if "Organization" in match:
      organization_keywords_2_500.append(match)

print(person_keywords_2_500)
print(organization_keywords_2_500)

person_keywords_1_750 = []
organization_keywords_1_750 = []

for match in new_k_list1_750:
    if "Person" in match:
      person_keywords_1_750.append(match)
    if "Organization" in match:
      organization_keywords_1_750.append(match)

print(person_keywords_1_750)
print(organization_keywords_1_750)

person_keywords_2_750 = []
organization_keywords_2_750 = []

for match in new_k_list2_750:
    if "Person" in match:
      person_keywords_2_750.append(match)
    if "Organization" in match:
      organization_keywords_2_750.append(match)

print(person_keywords_2_750)
print(organization_keywords_2_750)

person_keywords_1_1000 = []
organization_keywords_1_1000 = []

for match in new_k_list1_1000:
    if "Person" in match:
      person_keywords_1_1000.append(match)
    if "Organization" in match:
      organization_keywords_1_1000.append(match)

print(person_keywords_1_1000)
print(organization_keywords_1_1000)

person_keywords_2_1000 = []
organization_keywords_2_1000 = []

for match in new_k_list2_1000:
    if "Person" in match:
      person_keywords_2_1000.append(match)
    if "Organization" in match:
      organization_keywords_2_1000.append(match)

print(person_keywords_2_1000)
print(organization_keywords_2_1000)



person_1_10 = []
for p in person_keywords_1_10:
  p = str(p)
  person_1_10.append(p[:p.index(":")])

organization_1_10 = []
for o in organization_keywords_1_10:
  o = str(o)
  organization_1_10.append(o[:o.index(":")])

person_2_10 = []
for p in person_keywords_2_10:
  p = str(p)
  person_2_10.append(p[:p.index(":")])

organization_2_10 = []
for o in organization_keywords_2_10:
  o = str(o)
  organization_2_10.append(o[:o.index(":")])

person_1_15 = []
for p in person_keywords_1_15:
  p = str(p)
  person_1_15.append(p[:p.index(":")])

organization_1_15 = []
for o in organization_keywords_1_15:
  o = str(o)
  organization_1_15.append(o[:o.index(":")])

person_2_15 = []
for p in person_keywords_2_15:
  p = str(p)
  person_2_15.append(p[:p.index(":")])

organization_2_15 = []
for o in organization_keywords_2_15:
  o = str(o)
  organization_2_15.append(o[:o.index(":")])

person_1_20 = []
for p in person_keywords_1_20:
  p = str(p)
  person_1_20.append(p[:p.index(":")])

organization_1_20 = []
for o in organization_keywords_1_20:
  o = str(o)
  organization_1_20.append(o[:o.index(":")])

person_2_20 = []
for p in person_keywords_2_20:
  p = str(p)
  person_2_20.append(p[:p.index(":")])

organization_2_20 = []
for o in organization_keywords_2_20:
  o = str(o)
  organization_2_20.append(o[:o.index(":")])

person_1_50 = []
for p in person_keywords_1_50:
  p = str(p)
  person_1_50.append(p[:p.index(":")])

organization_1_50 = []
for o in organization_keywords_1_50:
  o = str(o)
  organization_1_50.append(o[:o.index(":")])

person_2_50 = []
for p in person_keywords_2_50:
  p = str(p)
  person_2_50.append(p[:p.index(":")])

organization_2_50 = []
for o in organization_keywords_2_50:
  o = str(o)
  organization_2_50.append(o[:o.index(":")])

person_1_100 = []
for p in person_keywords_1_100:
  p = str(p)
  person_1_100.append(p[:p.index(":")])

organization_1_100 = []
for o in organization_keywords_1_100:
  o = str(o)
  organization_1_100.append(o[:o.index(":")])

person_2_100 = []
for p in person_keywords_2_100:
  p = str(p)
  person_2_100.append(p[:p.index(":")])

organization_2_100 = []
for o in organization_keywords_2_100:
  o = str(o)
  organization_2_100.append(o[:o.index(":")])

person_1_200 = []
for p in person_keywords_1_200:
  p = str(p)
  person_1_200.append(p[:p.index(":")])

organization_1_200 = []
for o in organization_keywords_1_200:
  o = str(o)
  organization_1_200.append(o[:o.index(":")])

person_2_200 = []
for p in person_keywords_2_200:
  p = str(p)
  person_2_200.append(p[:p.index(":")])

organization_2_200 = []
for o in organization_keywords_2_200:
  o = str(o)
  organization_2_200.append(o[:o.index(":")])

person_1_500 = []
for p in person_keywords_1_500:
  p = str(p)
  person_1_500.append(p[:p.index(":")])

organization_1_500 = []
for o in organization_keywords_1_500:
  o = str(o)
  organization_1_500.append(o[:o.index(":")])

person_2_500 = []
for p in person_keywords_2_500:
  p = str(p)
  person_2_500.append(p[:p.index(":")])

organization_2_500 = []
for o in organization_keywords_2_500:
  o = str(o)
  organization_2_500.append(o[:o.index(":")])

person_1_750 = []
for p in person_keywords_1_750:
  p = str(p)
  person_1_750.append(p[:p.index(":")])

organization_1_750 = []
for o in organization_keywords_1_750:
  o = str(o)
  organization_1_750.append(o[:o.index(":")])

person_2_750 = []
for p in person_keywords_2_750:
  p = str(p)
  person_2_750.append(p[:p.index(":")])

organization_2_750 = []
for o in organization_keywords_2_750:
  o = str(o)
  organization_2_750.append(o[:o.index(":")])

person_1_1000 = []
for p in person_keywords_1_1000:
  p = str(p)
  person_1_1000.append(p[:p.index(":")])

organization_1_1000 = []
for o in organization_keywords_1_1000:
  o = str(o)
  organization_1_1000.append(o[:o.index(":")])

person_2_1000 = []
for p in person_keywords_2_1000:
  p = str(p)
  person_2_1000.append(p[:p.index(":")])

organization_2_1000 = []
for o in organization_keywords_2_1000:
  o = str(o)
  organization_2_1000.append(o[:o.index(":")])

"""The following code is to save the NER-keyword lists. """

ner_key_list1_10 = person_1_10 + organization_1_10

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list1_10.pickle', 'wb') as f:
  pickle.dump(ner_key_list1_10, f)

ner_key_list2_10 = person_2_10 + organization_2_10

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list2_10.pickle', 'wb') as f:
  pickle.dump(ner_key_list2_10, f)

ner_key_list1_15 = person_1_15 + organization_1_15

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list1_15.pickle', 'wb') as f:
  pickle.dump(ner_key_list1_15, f)

ner_key_list2_15 = person_2_15 + organization_2_15

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list2_15.pickle', 'wb') as f:
  pickle.dump(ner_key_list2_15, f)

ner_key_list1_20 = person_1_20 + organization_1_20

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list1_20.pickle', 'wb') as f:
  pickle.dump(ner_key_list1_20, f)

ner_key_list2_20 = person_2_20 + organization_2_20

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list2_20.pickle', 'wb') as f:
  pickle.dump(ner_key_list2_20, f)

ner_key_list1_50 = person_1_50 + organization_1_50

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list1_50.pickle', 'wb') as f:
  pickle.dump(ner_key_list1_50, f)

ner_key_list2_50 = person_2_50 + organization_2_50

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list2_50.pickle', 'wb') as f:
  pickle.dump(ner_key_list2_50, f)

ner_key_list1_100 = person_1_100 + organization_1_100

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list1_100.pickle', 'wb') as f:
  pickle.dump(ner_key_list1_100, f)

ner_key_list2_100 = person_2_100 + organization_2_100

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list2_100.pickle', 'wb') as f:
  pickle.dump(ner_key_list2_100, f)

ner_key_list1_200 = person_1_200 + organization_1_200

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list1_200.pickle', 'wb') as f:
  pickle.dump(ner_key_list1_200, f)

ner_key_list2_200 = person_2_200 + organization_2_200

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list2_200.pickle', 'wb') as f:
  pickle.dump(ner_key_list2_200, f)

ner_key_list1_500 = person_1_500 + organization_1_500

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list1_500.pickle', 'wb') as f:
  pickle.dump(ner_key_list1_500, f)

ner_key_list2_500 = person_2_500 + organization_2_500

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list2_500.pickle', 'wb') as f:
  pickle.dump(ner_key_list2_500, f)

ner_key_list1_750 = person_1_750 + organization_1_750

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list1_750.pickle', 'wb') as f:
  pickle.dump(ner_key_list1_750, f)

ner_key_list2_750 = person_2_750 + organization_2_750

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list2_750.pickle', 'wb') as f:
  pickle.dump(ner_key_list2_750, f)

ner_key_list1_1000 = person_1_1000 + organization_1_1000

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list1_1000.pickle', 'wb') as f:
  pickle.dump(ner_key_list1_1000, f)

ner_key_list2_1000 = person_2_1000 + organization_2_1000

os.chdir("/content/drive/My Drive/Colab Notebooks/Thesis Project/Code/CoNLL-2003 code/Keywords 1 NER CONLL2003")
with open('ner_key_list2_1000.pickle', 'wb') as f:
  pickle.dump(ner_key_list2_1000, f)

