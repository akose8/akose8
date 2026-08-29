import numpy as np
import csv
import random
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import seaborn as sns

genes = []
data = []

with open("Data/GSE150910_gene-level_count_file.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        
        genes.append(row[0])
        data.append(row[1:])

samples = data[0]
data = data[1:]
genes = genes[1:]
