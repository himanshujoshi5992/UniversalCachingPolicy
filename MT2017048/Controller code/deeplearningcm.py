#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from numpy import array
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

sc = StandardScaler()
classifier = Sequential()

class DLCM:
	

	# Importing the dataset:
	def training(self):
		dataset = pd.read_csv('Training_data_zipf.csv')
		X = dataset.iloc[:, 0:14].values
		y = dataset.iloc[:, 14].values
		y = array(y)
		y = to_categorical(y)
		y = y[:, 1:]
		# Encoding categorical data: It is used to get rid of the string data; converting it into some numerical value
		# Encoding the Independent Variable
		"""from sklearn.preprocessing import LabelEncoder, OneHotEncoder
		labelencoder_X_1 = LabelEncoder()
		X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
		labelencoder_X_2 = LabelEncoder()
		X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
		onehotencoder = OneHotEncoder(categorical_features = [1])
		X = onehotencoder.fit_transform(X).toarray()
		X = X[:, 1:]"""

		# Splitting the dataset into the Training set and Test set
		
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

		# Feature Scaling: It is used to suppress the dominance of one single variable
		
		
		X_train = sc.fit_transform(X_train)
		X_test = sc.transform(X_test)

		#Part 2 - Now let's make the ANN
		#Import the keras library and required packages
		#import keras


		#Initializing the ANN
		

		#Adding the input layer and first hidden layer
		#output_dim is the number of neurons in the hidden layer and input_dim is the number of neurons in the input layer.
		#The the number of neurons depends on the number of columns in the X-training set for input layer and for output layer the number of neurons depends on the number of columns in the Y_test data
		classifier.add(Dense(units = 8,kernel_initializer = 'uniform', activation = 'relu', input_dim = 14))
		#Adding the second hidden layer
		classifier.add(Dense(units = 8,kernel_initializer = 'uniform', activation = 'relu'))
		#Adding the output layer; We only change the units and activation. If we had more than one category we would have used softmax as the new activation function.
		classifier.add(Dense(activation="softmax", kernel_initializer="random_uniform", units=10))

		#Compiling the ANN: It simply means that we are going to apply the stochastic gradient descent method onto the ANN.
		classifier.compile(optimizer = 'adam',loss = 'binary_crossentropy',metrics = ['accuracy'])

		# Fitting ANN to the Training set
		classifier.fit(X_train, y_train, batch_size = 20, epochs = 20)

		# Create your classifier here

		# Predicting the Test set results
	def predict(self):
	    #data = float(data.replace(",", "."))
	    #data = repr(data)
	    dataset1 = pd.read_csv('predict.csv')
	    data = dataset1.iloc[:, 0:14].values
            #data = dataset1.iloc[0]
            #print data
	    data = sc.transform(data)
	    y_pred = classifier.predict(data)
	    print(y_pred)
            return y_pred
	# Making the Confusion Matrix
	"""
	from sklearn.metrics import confusion_matrix
	cm = confusion_matrix(y_test, y_pred)
	"""
