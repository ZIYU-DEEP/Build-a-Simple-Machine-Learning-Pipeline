# Build-a-Simple-Machine-Learning-Pipeline
The motivation of this project is to build a simple, modular, extensible, 
machine learning pipeline in Python.  

I recommend you to first view my [notebook](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/blob/master/notebook/Pipeline%20Implementation.ipynb)
to have a sense of the pipeline as a whole. (You can directly view it in github - 
if it cannot open (as it contains a lot of graph), just reload another time! Alternatively, 
you can also download it and use your own local Jupyter Notebook to view.) After
that, you can jump to my [code](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/tree/master/code) 
to see how I designed the functions used in the [notebook](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/blob/master/notebook/Pipeline%20Implementation.ipynb).


## 0. Introduction
The project build a complete machine learning pipeline. Specifically, it 
deploys the decision tree classifier, and uses the financial distress 
prediction as an example. The goal of the example is to predict if 
an individual will experience financial distress in the next two years.

The pipeline project is organized as follow:
* [code](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/tree/master/code):
The functions designed to build up the pipeline. It is composed by four python
files, which would be illustrated 
* [notebook](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/blob/master/notebook/Pipeline%20Implementation.ipynb):
An implementation of the pipeline.
* [data](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/tree/master/data):
The data from the financial distress example.

## 1. Data Preparation
* Please refer to [prep.py](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/blob/master/code/prep.py) and the corresponding part in the [notebook](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/blob/master/notebook/Pipeline%20Implementation.ipynb).

## 2. Data Exploration 
* Please refer to [explore.py](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/blob/master/code/feature.py) and the corresponding part in the [notebook](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/blob/master/notebook/Pipeline%20Implementation.ipynb).

## 3. Feature Engineering 
* Please refer to [feature.py](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/blob/master/code/feature.py) and the corresponding part in the [notebook](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/blob/master/notebook/Pipeline%20Implementation.ipynb).

## 4. Model Training, Testing and Evaluation 
* Please refer to [model.py](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/blob/master/code/model.py) and the corresponding part in the [notebook](https://github.com/ZIYU-DEEP/Build-a-Simple-Machine-Learning-Pipeline/blob/master/notebook/Pipeline%20Implementation.ipynb).


