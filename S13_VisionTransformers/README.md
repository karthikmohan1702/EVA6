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

Model is trained for 20 epochs & can be viewed here in the [jupyter_notebook](https://github.com/karthikmohan1702/EVA6/blob/main/S13_VisionTransformers%20/S13_VIT_Dog_Cat.ipynb)

Showing last 5 training log 

    Epoch : 15 - loss : 0.6071 - acc: 0.6598 - val_loss : 0.6114 - val_acc: 0.6559

    100%
    313/313 [02:14<00:00, 2.33it/s]

    Epoch : 16 - loss : 0.6025 - acc: 0.6694 - val_loss : 0.6060 - val_acc: 0.6659

    100%
    313/313 [01:50<00:00, 2.84it/s]

    Epoch : 17 - loss : 0.5951 - acc: 0.6750 - val_loss : 0.6011 - val_acc: 0.6669

    100%
    313/313 [04:30<00:00, 1.16it/s]

    Epoch : 18 - loss : 0.5968 - acc: 0.6723 - val_loss : 0.6048 - val_acc: 0.6644

    100%
    313/313 [02:15<00:00, 2.31it/s]

    Epoch : 19 - loss : 0.5915 - acc: 0.6792 - val_loss : 0.5947 - val_acc: 0.6826

    100%
    313/313 [01:48<00:00, 2.88it/s]

    Epoch : 20 - loss : 0.5937 - acc: 0.6739 - val_loss : 0.5924 - val_acc: 0.6839

### Visual Transformers

Transformers are a evolution in the computer vision. They are designed for text or NLP world, but vision transformer are designed to replace the CNN operations. In NLP we pass tokens as inputs to the transformer since these inputs will be in the sequence whereas in vision space, we pass patches from an image.

Positional information of the patches of the images is retained by providing this info to the network as a positional embedding along with the patch embedding. A learnable class parameter is also passed such that for each sequence & position of the image, the class is assigned which helps in prediction of the input image.

The transformer encoder module comprises 



### References

- https://analyticsindiamag.com/hands-on-vision-transformers-with-pytorch/
- https://www.kaggle.com/general/74235 
