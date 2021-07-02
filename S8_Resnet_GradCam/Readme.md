## Contents

- [Objective](#objective)
- [Data Analysis](#data-analysis) 
- [Model Summary](#model-summary)
- [Training Log](#training-log)
- [Test Plot](#test-plot)
- [Misclassified Images](#misclassified-images)
- [References](#references) 



## Objective

1. Train resnet18 for 20 epochs on the CIFAR10 dataset.
2. Show loss curves for test and train datasets.
3. Show a gallery of 10 misclassified images.
4. Show gradcam output on 10 images.
5. Apply these transforms while training:
    - RandomCrop(32, padding=4) 
    - CutOut(16x16)


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


_Model is placed here_ [resnet_models!](https://github.com/karthikmohan1702/vision_wrapper/blob/main/model/resnet_models.py)

        ----------------------------------------------------------------
                Layer (type)               Output Shape         Param #
        ================================================================
                    Conv2d-1           [-1, 64, 32, 32]           1,728
               BatchNorm2d-2           [-1, 64, 32, 32]             128
                    Conv2d-3           [-1, 64, 32, 32]          36,864
               BatchNorm2d-4           [-1, 64, 32, 32]             128
                    Conv2d-5           [-1, 64, 32, 32]          36,864
               BatchNorm2d-6           [-1, 64, 32, 32]             128
                BasicBlock-7           [-1, 64, 32, 32]               0
                    Conv2d-8           [-1, 64, 32, 32]          36,864
               BatchNorm2d-9           [-1, 64, 32, 32]             128
                   Conv2d-10           [-1, 64, 32, 32]          36,864
              BatchNorm2d-11           [-1, 64, 32, 32]             128
               BasicBlock-12           [-1, 64, 32, 32]               0
                   Conv2d-13          [-1, 128, 16, 16]          73,728
              BatchNorm2d-14          [-1, 128, 16, 16]             256
                   Conv2d-15          [-1, 128, 16, 16]         147,456
              BatchNorm2d-16          [-1, 128, 16, 16]             256
                   Conv2d-17          [-1, 128, 16, 16]           8,192
              BatchNorm2d-18          [-1, 128, 16, 16]             256
               BasicBlock-19          [-1, 128, 16, 16]               0
                   Conv2d-20          [-1, 128, 16, 16]         147,456
              BatchNorm2d-21          [-1, 128, 16, 16]             256
                   Conv2d-22          [-1, 128, 16, 16]         147,456
              BatchNorm2d-23          [-1, 128, 16, 16]             256
               BasicBlock-24          [-1, 128, 16, 16]               0
                   Conv2d-25            [-1, 256, 8, 8]         294,912
              BatchNorm2d-26            [-1, 256, 8, 8]             512
                   Conv2d-27            [-1, 256, 8, 8]         589,824
              BatchNorm2d-28            [-1, 256, 8, 8]             512
                   Conv2d-29            [-1, 256, 8, 8]          32,768
              BatchNorm2d-30            [-1, 256, 8, 8]             512
               BasicBlock-31            [-1, 256, 8, 8]               0
                   Conv2d-32            [-1, 256, 8, 8]         589,824
              BatchNorm2d-33            [-1, 256, 8, 8]             512
                   Conv2d-34            [-1, 256, 8, 8]         589,824
              BatchNorm2d-35            [-1, 256, 8, 8]             512
               BasicBlock-36            [-1, 256, 8, 8]               0
                   Conv2d-37            [-1, 512, 8, 8]       1,179,648
              BatchNorm2d-38            [-1, 512, 8, 8]           1,024
                   Conv2d-39            [-1, 512, 8, 8]       2,359,296
              BatchNorm2d-40            [-1, 512, 8, 8]           1,024
                   Conv2d-41            [-1, 512, 8, 8]         131,072
              BatchNorm2d-42            [-1, 512, 8, 8]           1,024
               BasicBlock-43            [-1, 512, 8, 8]               0
                   Conv2d-44            [-1, 512, 8, 8]       2,359,296
              BatchNorm2d-45            [-1, 512, 8, 8]           1,024
                   Conv2d-46            [-1, 512, 8, 8]       2,359,296
              BatchNorm2d-47            [-1, 512, 8, 8]           1,024
               BasicBlock-48            [-1, 512, 8, 8]               0
                   Linear-49                   [-1, 10]          20,490
        ================================================================
        Total params: 11,189,322
        Trainable params: 11,189,322
        Non-trainable params: 0
        ----------------------------------------------------------------
        Input size (MB): 0.01
        Forward/backward pass size (MB): 13.50
        Params size (MB): 42.68
        Estimated Total Size (MB): 56.20
        ----------------------------------------------------------------

## Training Log
Showing only last **5 epochs accuracy**. To view the whole training log, you can navigate [here](https://github.com/karthikmohan1702/EVA6/blob/main/S8_Resnet_GradCam/Resnet_Grad_CAM.ipynb) 

EPOCH: 15
Loss=0.25836020708084106 Batch_id=390 Accuracy=87.60: 100%|██████████| 391/391 [01:05<00:00,  5.97it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0032, Accuracy: 8716/10000 (87.16%)

EPOCH: 16
Loss=0.2927214801311493 Batch_id=390 Accuracy=88.46: 100%|██████████| 391/391 [01:05<00:00,  5.97it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0032, Accuracy: 8740/10000 (87.40%)

EPOCH: 17
Loss=0.40868210792541504 Batch_id=390 Accuracy=88.90: 100%|██████████| 391/391 [01:05<00:00,  5.97it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0033, Accuracy: 8767/10000 (87.67%)

EPOCH: 18
Loss=0.3036760985851288 Batch_id=390 Accuracy=89.32: 100%|██████████| 391/391 [01:05<00:00,  5.97it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0030, Accuracy: 8806/10000 (88.06%)

EPOCH: 19
Loss=0.3504355549812317 Batch_id=390 Accuracy=89.71: 100%|██████████| 391/391 [01:05<00:00,  5.96it/s]

Test set: Average loss: 0.0029, Accuracy: 8842/10000 (88.42%)


## Test Plot

![image](https://user-images.githubusercontent.com/47082769/124327988-675af380-dba6-11eb-914d-ca1a706bfeda.png)





## Misclassified Images





## References

- Resnet model - https://github.com/kuangliu/pytorch-cifar/blob/master/models/resnet.py 


  
