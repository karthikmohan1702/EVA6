## Objective

1. Need to make 3 versions of  5th assignment's best model:

   1. Network with Group Normalization
   2. Network with Layer Normalization
   3. Network with L1 + BN
  
   
2. Write a single model.py file that includes GN/LN/BN and takes an argument to decide which normalization to include

3. Write a single notebook file to run all the 3 models above for 20 epochs each

4. Create these graphs:
   1. Graph 1: Test/Validation Loss for all 3 models together
   2. Graph 2: Test/Validation Accuracy for 3 models together
   3. graphs must have proper annotation

5. Find 10 misclassified images for each of the 3 models, and show them as a 5x2 image matrix in 3 separately annotated images.


### CODE

3 models was trained with different normalization techniques.

| Normalization/Regularization | Train_acc | Test_acc | L1    | num_groups |
| ---------------------------- | ----------| ---------| ------| -----------|
| BatchNorm + L1               |           |          | 0.001 |      -     |
| Group Norm                   |           |          |    -  |      4     |
| Layer Norm                   |           |          |    -  |      -     |


### Graphs









### Normalization Techniques

Image normalization is an important step in the processing the image. In simple terms, we can say that it changes the way we look at the data. For eg: we can consider distance 1km which is measured in different units 1000m or 100000cm or 0.62mile. Normalization aids a better training of an neural network. There are two areas where we implement normalization, initially we normalize the dataset when we get them & latter is for the channels in the network.

There are different normalization techniques that are performed in the network.

![normalization_types](https://user-images.githubusercontent.com/47082769/121749188-dd2fea00-cb27-11eb-97d3-568044b1aa7d.png)


(a) **Batch normalization** - This is one of the most commonly used normalization technique in most architectures. It solves the internal covariate shift problem. Covariate means  input features, Covariate shift means that the distribution of the features is different in different parts of the training/test data. So what we mean by **covariant shift** is when you capture a photo of a dog in day & night light conditions, photos taken in bright light where most of the pixels are whitish, which means most of the pixels are nearer to 255 & same holds for dark color pixel value nearer to 0. Since, both photos are different & this type of difference is difficult for an kernel to handle & this is reason we have to make our data normalized in the network. BatchNorm reduces the covariate shift problem & aids in getting a better training model. BN relies on the mini-batch to compute params. Here mean and standard deviation is based on the number of channels for batchnorm, so here we have 4 mean & 4 standard deviation for 3 images.

(b) **Layer Normalization** - is performed on the layers of the network instead of the batch size. Total number of mean & standard deviationis dependent on the images we have

(c) **Group normalization** - is performed on the groups of channels in the layer of the network.



