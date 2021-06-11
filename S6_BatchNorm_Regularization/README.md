## Objective

1. Need to make 3 versions of  5th assignment's best model:

   1. Network with Group Normalization
   2. Network with Layer Normalization
   3. Network with L1 + BN
  
   
2. Write a single model.py file that includes GN/LN/BN and takes an argument to decide which normalization to include

3. Write a single notebook file to run all the 3 models above for 20 epochs each

4. Create these graphs:
   1. Graph 1: Test/Validation Loss for all 3 models together
   2. Graph 2: Test/Validation Accuracy for 3 models together
   3. graphs must have proper annotation

5. Find 10 misclassified images for each of the 3 models, and show them as a 5x2 image matrix in 3 separately annotated images.


### CODE

3 models was trained with different normalization techniques.

| Normalization/Regularization | Train_acc | Test_acc | L1    | num_groups |
| ---------------------------- | ----------| ---------| ------| -----------|
| BatchNorm + L1               |           |          | 0.001 |      -     |
| Group Norm                   |           |          |    -  |      4     |
| Layer Norm                   |           |          |    -  |      -     |


### Graphs









### Normalization Techniques
