# K nearest neighbours

## Introduction
A commonly used algorithm in clustering and machine learning it basically works by finding the k nearest neighbours to a point and then using the average of those points to predict the value of the point.

## Math
The algorithm we are trying to implement is the following:
$$\hat{Y}(x) = \frac{1}{k} \sum_{x_i \in N_k(x)}y_i $$
Here $N_k(x)$ is the neighbourhood that we will be looking in. For this project we will be using the euclidean distance to find the nearest neighbours. The euclidean distance is defined as:
$$d(x,y) = \sqrt{\sum_{i=1}^{n}(x_i - y_i)^2}$$

## Implementation
The implementation is fairly simple, we will be using the sklearn library to do the heavy lifting for us. We will be using the iris dataset to test our algorithm. The iris dataset is a dataset that contains 3 different types of iris flowers and 4 different features of the flowers. We will be using the first 2 features to predict the type of flower.

The biggest problem with this algorithm is that it is very slow. This is because it has to calculate the distance between every point in the dataset and the point that we are trying to predict. This means that the algorithm has to calculate the distance between the point we are trying to predict and every other point in the dataset.

The Big(O) notation for this algorithm is $O(n^2)$ where n is the number of points in the dataset. This means that the algorithm will take a very long time to run if the dataset is large.

## Results
The results are as follows:
