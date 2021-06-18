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



### Log

### Graph



