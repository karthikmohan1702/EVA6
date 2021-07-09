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



## Training Log
Showing only last **5 epochs accuracy**. To view the whole training log, you can navigate [here]() 




## Test Plot




## Misclassified Images





## References

- Learning rate finder - https://github.com/davidtvs/pytorch-lr-finder


  

