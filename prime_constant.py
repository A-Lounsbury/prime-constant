# prime_constant.py
# Andrew Lounsbury
# 19/3/23
# Purpose: Compute the constant discussed in this (https://www.youtube.com/watch?v=_gCKX6VMvmU) video
import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def prime(n):
    if n == 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def generate(n):
    sequence = []
    while len(sequence) < n:
        for m in range(1, n):
            # loop through the numbers less than m
            for i in range(2, m):
                # if prime and doesn't divide m, add it to the sequence and move to the next number 
                if prime(i) and m % i != 0 and len(sequence) < n:
                    sequence.append(i)
                    break
    return sequence

sequence = generate(20)
print(sequence)

# Plots of Averages
n = 10
sequence = generate(n)

average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)
print(len(average_sequence))

average_df = pd.DataFrame(average_sequence, columns=["Average"])
average_df['index'] = [i for i in range(len(average_sequence))]
sns.scatterplot(x="index", y="Average", data=average_df)
plt.show()

n = 100
sequence = generate(n)

average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)
print(len(average_sequence))

average_df = pd.DataFrame(average_sequence, columns=["Average"])
average_df['index'] = [i for i in range(len(average_sequence))]
sns.scatterplot(x="index", y="Average", data=average_df)
plt.show()

n = 1000
sequence = generate(n)

average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)
print(len(average_sequence))

average_df = pd.DataFrame(average_sequence, columns=["Average"])
average_df['index'] = [i for i in range(len(average_sequence))]
sns.scatterplot(x="index", y="Average", data=average_df)
plt.show()

n = 10000
sequence = generate(n)

average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)
print(len(average_sequence))

average_df = pd.DataFrame(average_sequence, columns=["Average"])
average_df['index'] = [i for i in range(len(average_sequence))]
sns.scatterplot(x="index", y="Average", data=average_df)
plt.show()

n = 100000
sequence = generate(n)

average_sequence = []
total = 0
for i, s in enumerate(sequence):
    total += s
    average = total / (i + 1)
    average_sequence.append(average)
print(len(average_sequence))

average_df = pd.DataFrame(average_sequence, columns=["Average"])
average_df['index'] = [i for i in range(len(average_sequence))]
sns.scatterplot(x="index", y="Average", data=average_df)
plt.show()