#Imports
import numpy as np 
import pandas as pd 
import sys
import json
import os
import re
import csv

# Importação dos dados
hdi = pd.read_csv('https://www.kaggle.com/datasets/neisse/scrapped-lyrics-from-6-genres?resource=download&select=lyrics-data.csv')

# Visualização inicial dos dados
display(hdi.shape)
display(hdi.head())
display(hdi.tail())