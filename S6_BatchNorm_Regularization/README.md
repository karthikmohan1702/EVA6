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


### CODE

3 models was trained with different normalization techniques.

| Normalization/Regularization | Train_acc | Test_acc | L1    | num_groups |
| ---------------------------- | ----------| ---------| ------| -----------|
| BatchNorm + L1               |   98.46   |   98.99  | 0.001 |      -     |
| Group Norm                   |   98.84   |   99.34  |    -  |      4     |
| Layer Norm                   |   98.83   |   99.35  |    -  |      -     |


### Graphs


![image](https://user-images.githubusercontent.com/47082769/121750089-5ed44780-cb29-11eb-89f6-78c79369ebdf.png)



### Normalization Techniques

Image normalization is an important step in the processing the image. In simple terms, we can say that it changes the way we look at the data. For eg: we can consider distance 1km which is measured in different units 1000m or 100000cm or 0.62mile. Normalization aids a better training of an neural network. There are two areas where we implement normalization, initially we normalize the dataset when we get them & latter is for the channels in the network.

There are different normalization techniques that are performed in the network.

![normalization_types](https://user-images.githubusercontent.com/47082769/121749188-dd2fea00-cb27-11eb-97d3-568044b1aa7d.png)


(a) **Batch normalization** - This is one of the most commonly used normalization technique in most architectures. It solves the internal covariate shift problem. Covariate means  input features, Covariate shift means that the distribution of the features is different in different parts of the training/test data. So what we mean by **covariant shift** is when you capture a photo of a dog in day & night light conditions, photos taken in bright light where most of the pixels are whitish, which means most of the pixels are nearer to 255 & same holds for dark color pixel value nearer to 0. Since, both photos are different & this type of difference is difficult for an kernel to handle & this is reason we have to make our data normalized in the network. BatchNorm reduces the covariate shift problem & aids in getting a better training model. BN relies on the mini-batch to compute params. Here mean and standard deviation is based on the number of channels for batchnorm, so here we have 4 mean & 4 standard deviation for 3 images.

![image](https://user-images.githubusercontent.com/47082769/121749858-000ece00-cb29-11eb-966e-3b70a7528444.png)

(b) **Layer Normalization** - is performed on the layers of the network instead of the batch size. Total number of mean & standard deviationis dependent on the images we have

![image](https://user-images.githubusercontent.com/47082769/121749930-17e65200-cb29-11eb-8bd6-125f6a62d27d.png)
![image](https://user-images.githubusercontent.com/47082769/121749965-1f0d6000-cb29-11eb-9235-ba703890134c.png)


(c) **Group normalization** - is performed on the groups of channels in the layer of the network.

![image](https://user-images.githubusercontent.com/47082769/121749997-2a608b80-cb29-11eb-9dce-9b460a488b8c.png)
![image](https://user-images.githubusercontent.com/47082769/121750011-32203000-cb29-11eb-959b-65e7cad41440.png)



