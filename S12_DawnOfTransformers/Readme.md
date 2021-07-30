## Contents

- [Spatial Transformer](#spatial-transformer)
- [Model](#model)
- [Visualizing Spatial Transformer Network Results](#visualizing-spatial-transformer-network-results) 
- [References](#references) 


## Spatial Transformer

Architecture

![image](https://user-images.githubusercontent.com/47082769/127672712-d4eb0847-cb9c-478a-8278-084ef9649bb7.png)

Spatial transformer is a combination of 3 components:

1. Localization network
2. Grid generator
3. Sampler

## Model

The model architecture from [here](https://brsoff.github.io/tutorials/intermediate/spatial_transformer_tutorial.html) is based on the MNIST dataset & its modified to work with CIFAR10 dataset which has color images. 

      ----------------------------------------------------------------
              Layer (type)               Output Shape         Param #
      ================================================================
                  Conv2d-1            [-1, 8, 26, 26]           1,184
               MaxPool2d-2            [-1, 8, 13, 13]               0
                    ReLU-3            [-1, 8, 13, 13]               0
                  Conv2d-4             [-1, 10, 9, 9]           2,010
               MaxPool2d-5             [-1, 10, 4, 4]               0
                    ReLU-6             [-1, 10, 4, 4]               0
                  Linear-7                   [-1, 32]           5,152
                    ReLU-8                   [-1, 32]               0
                  Linear-9                    [-1, 6]             198
                 Conv2d-10           [-1, 10, 28, 28]             760
                 Conv2d-11           [-1, 20, 10, 10]           5,020
              Dropout2d-12           [-1, 20, 10, 10]               0
                 Linear-13                   [-1, 50]          25,050
                 Linear-14                   [-1, 10]             510
      ================================================================
      Total params: 39,884
      Trainable params: 39,884
      Non-trainable params: 0
      ----------------------------------------------------------------
      Input size (MB): 0.01
      Forward/backward pass size (MB): 0.16
      Params size (MB): 0.15
      Estimated Total Size (MB): 0.33

            

## Visualizing Spatial Transformer Network Results

![image](https://user-images.githubusercontent.com/47082769/127672255-e451803f-7c9e-4ac3-a77e-91ec981724d5.png)



## References

- https://brsoff.github.io/tutorials/intermediate/spatial_transformer_tutorial.html
- https://arxiv.org/pdf/1506.02025v3.pdf
