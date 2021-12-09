# Objective
This program processes a dataset of about 50,000 IMDB movie reviews and runs a Naive Bayes classification - **Positive** or **Negative** review - using user provided words.


# Implementation Details
This program is broken into 4 stages:
1. Input Parsing
2. Data Processing
3. Data Normalization 
4. Data Analysis

In the **Input Parsing** phase the program places each word provided as an argument into a dedicated model class. The `WordProbabilitiesModel` is the data structure used to hold basic information about each word.

The **Data Processing** stage opens the csv movie reviews dataset using pythons built in csv module. It then parses each row and keeps a tally of the number of times each word is used and if it falls under a positive or negative category. A simple one-liner counter regex pulled from stackoverflow is used to find matching words in each review. (https://stackoverflow.com/questions/17268958/finding-occurrences-of-a-word-in-a-string-in-python-3)

The **Data Normalization** phase is a necessary step for Naive Bayes classification to circumvent zero-value probability multiplications. A constant `ALPHA` of value 1 is used as the normalizing value but this can be set to whatever value we like. The `normalize_data` method checks for zeros in each word count and, if found, adds the alpha value to every count.

The **Data Analysis** phase runs the final Naive Bayes probability calculations:
```
P(Positive) * P(word1 | Positive) * P(word2 | Positive) * ...
P(Negative) * P(word1 | Negative) * P(word2 | Negative) * ...
```
Once this is calculated, we receive a breakdown of the probabilities and the likeliness classification of a positive or negative review given the words input.


# Running the Program
Below is an example of how to run this program.
For this example we will use the words 'great', 'awesome', 'ajshdfajhsd'.
Note that the last word is nonsense and is only meant to illustrate the data normalization capability, as there are no such word in this dataset.

In your terminal run:

```bash
python final_project.py great awesome ajshdfajhsd
```
(if your default version of python is not 3.x then replace **python** with **python3**)


You may access the help command by running:

```bash
python final_project.py help
```