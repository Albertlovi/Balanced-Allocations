## Introduction

Consider a collection of m bins and n balls. We place each ball into one of the bins. To do so, we draw a certain 
number d of bins, uniformly at random, from the m total ones, and use some rule to choose in which of the d
bins we put the ball. The goal of this project is to find methods to allocate the balls in the bins in a balanced way.
We will look for strategies that minimize the gap between the load of the bin with maximum load and the average load of 
the bins. 

## Common functions

In the file functions.py we can find all the common functions between allocation methods. These are the functions 
concerning the random selection of the bins for the different methods, the function to calculate the gap, and the 
different functions to plot the experiments. 

## Allocation methods

In the rest of .py files we can find the different allocation methods. These are the one-choice method, the d-choice 
method, the partial information method and the probabilistic method. Each file is ready to run, we only need to set the 
values of the variables in the corresponding main funcitons. 
