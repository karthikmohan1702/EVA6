## Contents

- [Visual Transformers on Cats and dogs dataset](#visual-transformers-on-cats-and-dogs-dataset)
- [Training logs](#training-log)
- [Visual Transformers](#visual-transformers)
- [References](#references) 



### Visual Transformers on Cats and dogs dataset

Implementing visual transformer on the Cat & Dog dataset as given in this [blog](https://analyticsindiamag.com/hands-on-vision-transformers-with-pytorch/). The dataset is obtained from [Kaggle](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data). 

- Dataset view

![image](https://user-images.githubusercontent.com/47082769/128538664-311c378d-66fa-4a99-ac0b-3003e7de0243.png)



### Training logs

Model is trained for 20 epochs & can be viewed here in the [jupyter_notebook]()

Showing last 5 training log 

### Visual Transformers

Transformers are a evolution in the computer vision. They are designed for text or NLP world, but vision transformer are designed to replace the CNN operations. In NLP we pass tokens as inputs to the transformer since these inputs will be in the sequence whereas in vision space, we pass patches from an image.

Positional information of the patches of the images is retained by providing this info to the network as a positional embedding along with the patch embedding. A learnable class parameter is also passed such that for each sequence & position of the image, the class is assigned which helps in prediction of the input image.

The transformer encoder module comprises 



### References

- https://analyticsindiamag.com/hands-on-vision-transformers-with-pytorch/
- https://www.kaggle.com/general/74235 
