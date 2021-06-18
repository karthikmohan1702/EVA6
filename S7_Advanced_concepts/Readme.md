### Objective

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


### Model Summary

![image](https://user-images.githubusercontent.com/47082769/122601973-b6c1ff80-d08f-11eb-9937-25036b919a8a.png)

**Model is placed here [cifar10_model!](https://github.com/karthikmohan1702/EVA6/blob/0b80085dd087748ac31d8168615c578923fd3eb7/S7_Advanced_concepts/src/model/cifar10_model.py)**


### Receptive Field

| Operation | Kernel | Padding | Stride | Dilation | Jin | Nin | Nout | Rin | Rout | Jout |
|-----------|--------|---------|--------|----------|-----|-----|------|-----| -----|------|
|  CONV1    |    3   |    1    |    1   |     0    |  1  |  32 |  32  |  1  |**3** |      |
|  CONV2    |        |         |        |          |  1  |  32 |  32  |  3  |**5** |      |
|  CONV3    |        |         |        |          |  1  |  32 |  32  |  5  |**5** |      |
|  CONV4    |        |         |        |          |  1  |  32 |  14  |  5  |**9** |      |
|  CONV5    |        |         |        |          |  2  |  14 |  12  |  9  |**17**|      |
|  CONV6    |        |         |        |          |  2  |  12 |  12  |  17 |**21**|      |
|  CONV7    |        |         |        |          |  2  |  12 |  12  |  21 |**21**|      |
|  CONV8    |        |         |        |          |  2  |  12 |  4   |  21 |**29**|      |
|  CONV9    |        |         |        |          |  4  |  4  |  4   |  29 |**37**|      |
|  CONV10   |        |         |        |          |  4  |  4  |  4   |  37 |**37**|      |
|  CONV11   |        |         |        |          |  4  |  4  |  4   |  37 |**45**|      |
|  CONV12   |        |         |        |          |  4  |  4  |  4   |  45 |**45**|      |
|  CONV13   |        |         |        |          |  4  |  4  |  4   |  45 |**53**|      |
|  CONV14   |        |         |        |          |  4  |  4  |  4   |  53 |**61**|      |


### Log

### Graph



