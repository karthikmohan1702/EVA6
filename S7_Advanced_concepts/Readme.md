# Contents

- [Objective](#objective)

- [Data Analysis](data-analysis) 

- [Model Summary](#model-summary)

- [Receptive Field Calculation](#receptive-field-calculation)

- [Training Log](#training-log)

- [Test Plot](#test-plot)

- [Misclassified Images](#misclassified-images)

- [References](#references) 



Objective
=========

1) Code must use device "GPU"
2) Architecture should be of C1C2C3C40 configuration (No MaxPooling, but 3 3x3 layers with stride of 2 instead)
3) Total RF must be more than 44
4) One of the layers must use Depthwise Separable Convolution
5) One of the layers must use Dilated Convolution
6) Use albumentation library and apply:
   - horizontal flip
   - shiftScaleRotate
   - coarseDropout (max_holes = 1, max_height=16px, max_width=1, min_holes = 1, min_height=16px, min_width=16px, fill_value=(mean of the dataset), mask_fill_value = None)
7) Achieve 85% accuracy, as many epochs as you want. Total Params to be less than 200k


Data Analysis
=============



Model Summary
=============

_Model is placed here_ [cifar10_model!](https://github.com/karthikmohan1702/EVA6/blob/0b80085dd087748ac31d8168615c578923fd3eb7/S7_Advanced_concepts/src/model/cifar10_model.py)

![image](https://user-images.githubusercontent.com/47082769/122601973-b6c1ff80-d08f-11eb-9937-25036b919a8a.png)



Receptive Field Calculation
===========================

| Operation | Kernel | Padding | Stride | Dilation | Jin | Nin | Nout | Rin | Rout | Jout |
|-----------|--------|---------|--------|----------|-----|-----|------|-----| -----|------|
|  CONV1    |    3   |    1    |    1   |     1    |  1  |  32 |  32  |  1  |**3** |  1   |
|  CONV2    |    3   |    1    |    1   |     1    |  1  |  32 |  32  |  3  |**5** |  1   |
|  CONV3    |    1   |    0    |    1   |     1    |  1  |  32 |  32  |  5  |**5** |  1   |
|  CONV4    |    3   |    0    |    2   |     2    |  1  |  32 |  14  |  5  |**9** |  2   |
|  CONV5    |    3   |    1    |    1   |     2    |  2  |  14 |  12  |  9  |**17**|  2   |
|  CONV6    |    3   |    1    |    1   |     1    |  2  |  12 |  12  |  17 |**21**|  2   |
|  CONV7    |    1   |    0    |    1   |     1    |  2  |  12 |  12  |  21 |**21**|  2   |
|  CONV8    |    3   |    0    |    2   |     2    |  2  |  12 |  4   |  21 |**29**|  4   |
|  CONV9    |    3   |    1    |    1   |     1    |  4  |  4  |  4   |  29 |**37**|  4   |
|  CONV10   |    1   |    0    |    1   |     1    |  4  |  4  |  4   |  37 |**37**|  4   |
|  CONV11   |    3   |    1    |    1   |     1    |  4  |  4  |  4   |  37 |**45**|  4   |
|  CONV12   |    1   |    0    |    1   |     1    |  4  |  4  |  4   |  45 |**45**|  4   |
|  CONV13   |    3   |    1    |    1   |     1    |  4  |  4  |  4   |  45 |**53**|  4   |
|  CONV14   |    3   |    1    |    1   |     1    |  4  |  4  |  4   |  53 |**61**|  4   |


Training Log
============
Showing only last **20 epochs accuracy**. To view the whole training log, you can navigate [here](https://github.com/karthikmohan1702/EVA6/blob/main/S7_Advanced_concepts/S7_Dilated_Depthwise.ipynb) 

      EPOCH: 80
      Loss=0.46172434091567993 Batch_id=390 Accuracy=83.67: 100%|██████████| 391/391 [00:12<00:00, 30.92it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0038, Accuracy: 8445/10000 (84.45%)

      EPOCH: 81
      Loss=0.3917255997657776 Batch_id=390 Accuracy=83.73: 100%|██████████| 391/391 [00:12<00:00, 30.99it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0038, Accuracy: 8409/10000 (84.09%)

      EPOCH: 82
      Loss=0.372040718793869 Batch_id=390 Accuracy=83.83: 100%|██████████| 391/391 [00:12<00:00, 30.89it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0037, Accuracy: 8434/10000 (84.34%)

      EPOCH: 83
      Loss=0.4561113715171814 Batch_id=390 Accuracy=83.90: 100%|██████████| 391/391 [00:12<00:00, 30.20it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0036, Accuracy: 8476/10000 (84.76%)

      EPOCH: 84
      Loss=0.5162553191184998 Batch_id=390 Accuracy=83.98: 100%|██████████| 391/391 [00:12<00:00, 30.90it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0036, Accuracy: 8485/10000 (84.85%)

      EPOCH: 85
      Loss=0.5636851191520691 Batch_id=390 Accuracy=84.21: 100%|██████████| 391/391 [00:12<00:00, 31.09it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0036, Accuracy: 8484/10000 (84.84%)

      EPOCH: 86
      Loss=0.39641308784484863 Batch_id=390 Accuracy=84.11: 100%|██████████| 391/391 [00:12<00:00, 31.16it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0036, Accuracy: 8500/10000 (85.00%)

      EPOCH: 87
      Loss=0.543121337890625 Batch_id=390 Accuracy=83.91: 100%|██████████| 391/391 [00:12<00:00, 30.90it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0036, Accuracy: 8511/10000 (85.11%)

      EPOCH: 88
      Loss=0.7345693111419678 Batch_id=390 Accuracy=84.15: 100%|██████████| 391/391 [00:12<00:00, 31.19it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0036, Accuracy: 8474/10000 (84.74%)

      EPOCH: 89
      Loss=0.5152137875556946 Batch_id=390 Accuracy=84.24: 100%|██████████| 391/391 [00:12<00:00, 30.79it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0035, Accuracy: 8513/10000 (85.13%)

      EPOCH: 90
      Loss=0.7191966772079468 Batch_id=390 Accuracy=84.24: 100%|██████████| 391/391 [00:12<00:00, 30.81it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0035, Accuracy: 8504/10000 (85.04%)

      EPOCH: 91
      Loss=0.48198479413986206 Batch_id=390 Accuracy=84.44: 100%|██████████| 391/391 [00:12<00:00, 30.71it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0036, Accuracy: 8481/10000 (84.81%)

      EPOCH: 92
      Loss=0.47975096106529236 Batch_id=390 Accuracy=84.45: 100%|██████████| 391/391 [00:12<00:00, 30.72it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0036, Accuracy: 8424/10000 (84.24%)

      EPOCH: 93
      Loss=0.40960758924484253 Batch_id=390 Accuracy=84.57: 100%|██████████| 391/391 [00:12<00:00, 30.88it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0035, Accuracy: 8567/10000 (85.67%)

      EPOCH: 94
      Loss=0.6805081367492676 Batch_id=390 Accuracy=84.65: 100%|██████████| 391/391 [00:12<00:00, 30.43it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0036, Accuracy: 8550/10000 (85.50%)

      EPOCH: 95
      Loss=0.39049187302589417 Batch_id=390 Accuracy=84.58: 100%|██████████| 391/391 [00:12<00:00, 30.81it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0036, Accuracy: 8512/10000 (85.12%)

      EPOCH: 96
      Loss=0.4927293360233307 Batch_id=390 Accuracy=84.90: 100%|██████████| 391/391 [00:12<00:00, 30.81it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0036, Accuracy: 8485/10000 (84.85%)

      EPOCH: 97
      Loss=0.37856730818748474 Batch_id=390 Accuracy=84.58: 100%|██████████| 391/391 [00:12<00:00, 30.87it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0035, Accuracy: 8511/10000 (85.11%)

      EPOCH: 98
      Loss=0.32023921608924866 Batch_id=390 Accuracy=84.74: 100%|██████████| 391/391 [00:12<00:00, 31.13it/s]
        0%|          | 0/391 [00:00<?, ?it/s]
      Test set: Average loss: 0.0037, Accuracy: 8511/10000 (85.11%)

      EPOCH: 99
      Loss=0.45082154870033264 Batch_id=390 Accuracy=84.44: 100%|██████████| 391/391 [00:12<00:00, 30.64it/s]

      Test set: Average loss: 0.0035, Accuracy: 8533/10000 (85.33%)





Test Plot
=========

![image](https://user-images.githubusercontent.com/47082769/122605432-0fe06200-d095-11eb-87eb-890b61c051de.png)



Misclassified Images
====================

![image](https://user-images.githubusercontent.com/47082769/123330930-41a56d00-d55c-11eb-8f24-54d91a6765ac.png)


References
==========
- https://github.com/aladdinpersson/Machine-Learning-Collection/blob/master/ML/Pytorch/Basics/pytorch_std_mean.py

