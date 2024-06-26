## Lab 7: Clustering and Dimensionality Reduction

### Slides

The slides I showed this week can be found [here](https://ctsilva.github.io/2024-VisML-CDS/Labs/Lab_Week_7/VisML-Lab-Week7-slides). 

### Miscellaneous Notes 

* Homework 3 has been posted and is due next Friday (3/15) at 11:59pm
* Homework 2 is being graded, grades will likely be posted next week

### Topics Covered

* We discussed various dimensionality reduction techniques, which are used to project high-dimensional data into a low-dimensional space while preserving the clusters from the high-dimensional space. These included:
    * Principal Component Analysis (PCA)
    * Multidimensional Scaling (MDS)
    * Sparse Random Projection
    * Locally Linear Embedding
    * t-Distributed Stochastic Neighbor Embedding (t-SNE)
    * Uniform Manifold Approximation and Projection (UMAP)
* We also applied each of these methods to the [MNIST dataset](https://www.kaggle.com/datasets/hojjatk/mnist-dataset) of hand-drawn digits, projecting the 784-dimensional MNIST vectors into both 2 and 3 dimensions and visualizing the results. The code we used to create these visualizations can be found [here](https://ctsilva.github.io/2024-VisML-CDS/Labs/Lab_Week_7/VisML-Lab-Week7-slides). 
* We discussed common pitfalls that can lead to misreadings of t-SNE plots

### Further Reading 

* [This article](https://colah.github.io/posts/2014-10-Visualizing-MNIST/) contains an in-depth explanation of the interactive "MNIST Cube" visualization we discussed, as well as some animations of other clustering techniques 
* [This article](https://distill.pub/2016/misread-tsne/) breaks down the examples of common t-SNE plot pitfalls we looked at in more detail.
* [This article](https://pair-code.github.io/understanding-umap/) compares t-SNE and UMAP with interactive visualizations.