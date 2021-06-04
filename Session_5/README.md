## Objective

This assignment objective was to achieve test accuracy as 99.4% consistently in the last 4-5 epochs, with less than 10k params & under 15 epochs. It was said, to mention it in 4 steps(or models). 4 jupyter files are placed and the 4 steps are explained below along with their Receptive field.

1_Setup_&_Basic_Skeleton
-----------------------------
    Target
    ======
    1) Setting up a basic skeleton of the model
    2) Setting transforms, dataloads & training & test loops
    3) Set it as working code.

    Results
    ======
    1) Parameters: 2,02,724
    2) Best Train Accuracy: 99.49
    3) Best Test Accuracy: 99.14
    
    Analysis
    ========
    1. Huge model with overload of params
    2. Can see the model is overfitting
    3. Training is working fine & can see consistent increase in the training accuracy as we progress through epochs
    4. Will need to make the model lighter in the next step.
    
#### Receptive field calculation

![receptive_field_1](https://user-images.githubusercontent.com/47082769/120853343-18b33d00-c599-11eb-859a-41e07ebd6feb.JPG)

 
     Nin   : number of input features
     Nout  : number of output features
     k     : convolution kernel size
     p     : convolution padding size
     s     : convolution stride size

     Rin   : 
     Rout  :
     Jin   :
     Jout  :
 
 
| Operation | Kernel | Padding | Stride | Jin | Nin | Nout | Rin| Rout | Jout |
|-----------|--------|---------|--------|-----|-----|------|----|----- | -----|
| CONV1     |   3    |    0    |    1   |  1  |  28 |  26  |  1 |  3   |   1  |
| CONV2     |   3    |    0    |    1   |  1  |  26 |  24  |  3 |  5   |   1  |
| CONV3     |   3    |    0    |    1   |  1  |  24 |  22  |  5 |  7   |   1  |
| MAX       |   2    |    0    |    2   |  1  |  22 |  11  |  7 |  8   |   2  |
| CONV4     |   1    |    0    |    1   |  2  |  11 |  11  |  8 |  8   |   2  |
| CONV5     |   3    |    0    |    1   |  2  |  11 |  9   |  8 |  12  |   2  |
| CONV6     |   3    |    0    |    1   |  2  |  9  |  7   | 12 |  16  |   2  |
| CONV7     |   5    |    0    |    1   |  2  |  7  |  3   | 16 |  24  |   2  |


2_Lighter_model_&_batch_norm
----------------------------

    Target
    ======
    1) Make the model lighter (by reducing the channels)
    2) Adding batch norm to the model to increase the model efficiency

    Results
    ======
    1) Parameters: 11,364
    2) Best Train Accuracy: 99.76
    3) Best Test Accuracy: 99.30

    Analysis
    ========
    1) Before applying Batch norm - Made the model lighter by reducing channels but accuracy was dropped for 
       both the train & test due to less number of parameters. And also can see no overfitting. 
       The train_acc = 98.89 & test_acc = 98.91, gap seems to be less between them.
    2) After adding Batch norm – Could see a significant increase in both the accuracies test & train. 
       This tells how much powerful batch norm is & now it has accentuated the features by uplifting them.
       The train_acc = 99.76 & test_acc = 99.30. Seems to be large gap between train & test accuracy which states 
       the model is overfitting & in the next steps we can use regularization to penalize.
   









