## Contents

- [Objective](#objective)
- [Data Analysis](#data-analysis) 
- [Model Summary](#model-summary)
- [Training Log](#training-log)
- [Test Plot](#test-plot)
- [Misclassified Images](#misclassified-images)
- [References](#references) 



## Objective

1. Custom ResNet architecture for CIFAR10 that has the following architecture:
      1. **PrepLayer** - Conv 3x3 s1, p1) >> BN >> RELU [64k]

      2. **Layer1** 

         X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [128k]

         R1 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [128k] 

         Add(X, R1)
         
      3. **Layer 2** 

         Conv 3x3 [256k] >> MaxPooling2D >> BN >> ReLU

      4. **Layer 3**
         
         X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [512k]
         
         R2 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [512k]
         
         Add(X, R2)

      5. **MaxPooling with Kernel Size 4**
      
      6. **FC Layer**
      
      7. **SoftMax**

      8. **Use One Cycle Policy such that:**
         
         Total Epochs = 24
         
         Max at Epoch = 5
         
         LRMIN = FIND
         
         LRMAX = FIND
         
         NO Annihilation
      
      9. **Transformation**
         
         RandomCrop 32, 32 (after padding of 4) >> FlipLR >> Followed by CutOut(8, 8)
         
         Batch size = 512
         
         Target Accuracy: 90%


## Data Analysis


- **About Dataset** - The CIFAR-10 dataset ( Canadian Institute For Advanced Research) which contains 10 classes of images mainly ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck'] & there are 50000 training images and 10000 test images.

![image](https://user-images.githubusercontent.com/47082769/123464083-006b9680-d60a-11eb-8ad6-bf80d7b3cb0c.png)


- **Sample images in the dataset along with their labels**

![image](https://user-images.githubusercontent.com/47082769/123464209-28f39080-d60a-11eb-8acf-91f5028a923c.png)

- **Checking distribution of classes in Train & Test dataset**

![image](https://user-images.githubusercontent.com/47082769/123464595-a7503280-d60a-11eb-9d36-4a3cac351752.png)

- **Checking distribution of image sizes in Train & Test dataset**

![image](https://user-images.githubusercontent.com/47082769/123464717-cea6ff80-d60a-11eb-90fb-d7531eca3d11.png)

- **Mean**

[0.49138519167900085, 0.4821462035179138, 0.44650936126708984]

- **Standard deviation**

[0.2470356971025467, 0.24348768591880798, 0.26158225536346436]


## Model Summary


_Model is placed here_ [custom_resnet_model!](https://github.com/karthikmohan1702/vision_wrapper/blob/main/model/custom_resnet.py)

            ----------------------------------------------------------------
                    Layer (type)               Output Shape         Param #
            ================================================================
                        Conv2d-1           [-1, 64, 32, 32]           1,792
                   BatchNorm2d-2           [-1, 64, 32, 32]             128
                          ReLU-3           [-1, 64, 32, 32]               0
                        Conv2d-4          [-1, 128, 32, 32]          73,856
                     MaxPool2d-5          [-1, 128, 16, 16]               0
                   BatchNorm2d-6          [-1, 128, 16, 16]             256
                          ReLU-7          [-1, 128, 16, 16]               0
                        Conv2d-8          [-1, 128, 16, 16]         147,584
                   BatchNorm2d-9          [-1, 128, 16, 16]             256
                         ReLU-10          [-1, 128, 16, 16]               0
                       Conv2d-11          [-1, 128, 16, 16]         147,584
                  BatchNorm2d-12          [-1, 128, 16, 16]             256
                         ReLU-13          [-1, 128, 16, 16]               0
                       Conv2d-14          [-1, 256, 16, 16]         295,168
                    MaxPool2d-15            [-1, 256, 8, 8]               0
                  BatchNorm2d-16            [-1, 256, 8, 8]             512
                         ReLU-17            [-1, 256, 8, 8]               0
                       Conv2d-18            [-1, 512, 8, 8]       1,180,160
                    MaxPool2d-19            [-1, 512, 4, 4]               0
                  BatchNorm2d-20            [-1, 512, 4, 4]           1,024
                         ReLU-21            [-1, 512, 4, 4]               0
                       Conv2d-22            [-1, 512, 4, 4]       2,359,808
                  BatchNorm2d-23            [-1, 512, 4, 4]           1,024
                         ReLU-24            [-1, 512, 4, 4]               0
                       Conv2d-25            [-1, 512, 4, 4]       2,359,808
                  BatchNorm2d-26            [-1, 512, 4, 4]           1,024
                         ReLU-27            [-1, 512, 4, 4]               0
                    MaxPool2d-28            [-1, 512, 1, 1]               0
                       Linear-29                   [-1, 10]           5,130
            ================================================================
            Total params: 6,575,370
            Trainable params: 6,575,370
            Non-trainable params: 0
            ----------------------------------------------------------------
            Input size (MB): 0.01
            Forward/backward pass size (MB): 6.44
            Params size (MB): 25.08
            Estimated Total Size (MB): 31.54
----------------------------------------------------------------

## Training Log
Showing only last **5 epochs accuracy**. To view the whole training log, you can navigate [here](https://github.com/karthikmohan1702/EVA6/blob/main/S9_CustomResnet_CycleLR/S9_Resnet_LRFinder.ipynb) 

      EPOCH: 19
      Loss=0.4203657805919647 Batch_id=97 Accuracy=85.63: 100%|██████████| 98/98 [00:28<00:00,  3.42it/s]
        0%|          | 0/98 [00:00<?, ?it/s]
      Test set: Average loss: 0.0008, Accuracy: 8716/10000 (87.16%)

      EPOCH: 20
      Loss=0.457254558801651 Batch_id=97 Accuracy=86.08: 100%|██████████| 98/98 [00:28<00:00,  3.38it/s]
        0%|          | 0/98 [00:00<?, ?it/s]
      Test set: Average loss: 0.0008, Accuracy: 8751/10000 (87.51%)

      EPOCH: 21
      Loss=0.41286978125572205 Batch_id=97 Accuracy=86.06: 100%|██████████| 98/98 [00:28<00:00,  3.40it/s]
        0%|          | 0/98 [00:00<?, ?it/s]
      Test set: Average loss: 0.0008, Accuracy: 8722/10000 (87.22%)

      EPOCH: 22
      Loss=0.3912380635738373 Batch_id=97 Accuracy=86.43: 100%|██████████| 98/98 [00:29<00:00,  3.37it/s]
        0%|          | 0/98 [00:00<?, ?it/s]
      Test set: Average loss: 0.0008, Accuracy: 8701/10000 (87.01%)

      EPOCH: 23
      Loss=0.4123222827911377 Batch_id=97 Accuracy=86.81: 100%|██████████| 98/98 [00:28<00:00,  3.39it/s]

      Test set: Average loss: 0.0009, Accuracy: 8563/10000 (85.63%)


## Test Plot

![image](https://user-images.githubusercontent.com/47082769/125141530-eade8c80-e132-11eb-963e-860a18116c86.png)


## Misclassified Images

![image](https://user-images.githubusercontent.com/47082769/125141545-f5992180-e132-11eb-852a-252510bd9a33.png)



## References

- Learning rate finder - https://github.com/davidtvs/pytorch-lr-finder


  

