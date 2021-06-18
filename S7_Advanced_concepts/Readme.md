### Objective

1) Code must use device "GPU"
2) Architecture should be of C1C2C3C40 configuration (No MaxPooling, but 3 3x3 layers with stride of 2 instead)
3) Total RF must be more than 44
4) One of the layers must use Depthwise Separable Convolution
5) One of the layers must use Dilated Convolution
6) Use albumentation library and apply:
   - horizontal flip
   - shiftScaleRotate
   - coarseDropout (max_holes = 1, max_height=16px, max_width=1, min_holes = 1, min_height=16px, min_width=16px, fill_value=(mean of your dataset), mask_fill_value = None)
7) Achieve 85% accuracy, as many epochs as you want. Total Params to be less than 200k


