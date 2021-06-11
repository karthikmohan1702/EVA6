### Normalization

Image normalization is an important step in the processing the image. In simple terms, we can say that it changes the way we look at the data. For eg: we can consider distance 1km which is measured in different units 1000m or 100000cm or 0.62mile. Normalization aids a better training of an neural network. There are two areas where we implement normalization, initially we normalize the dataset when we get them & latter is for the channels in the network.

There are different normalization techniques that are performed in the network.

(a) **Batch normalization** - This is one of the most commonly used normalization technique in most architectures. It solves the internal covariate shift problem. Covariate means  input features, Covariate shift means that the distribution of the features is different in different parts of the training/test data. So what we mean by **covariant shift** is when you capture a photo of a dog in day & night light conditions, photos taken in bright light where most of the pixels are whitish, which means most of the pixels are nearer to 255 & same holds for dark color pixel value nearer to 0. Since, both photos are different & this type of difference is difficult for an kernel to handle & this is reason we have to make our data normalized in the network. BatchNorm reduces the covariate shift problem & aids in getting a better training model. BN relies on the mini-batch to compute params.

(b) **Layer Normalization** - is performed on the layers of the network instead of the batch size.

(c) **Group normalization** - is performed on the groups of channels in the layer of the network.
