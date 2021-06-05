## Objective:
---------------
To write a MNIST recognition neural network model considering the below rules:
- 99.4% validation accuracy
- Have used parameters exactly between 12000 to 18000
- Have used exactly 19 epochs
- Have used BN, Dropout, a Fully connected layer, have used GAP.
- Dropout must have 0.069 as the dropout value
- Batch size must be exactly 128
- Must add random rotation to your images between -5 to +5 degrees


## Network Architecture & Params that achieved 99.4% accuracy:
----------------------------

![network_architecture](https://github.com/karthikmohan1702/EVA6/blob/a557784c9036c8e25da13fb2545e5c1e78175285/Session_4/Architectural_basics/images/network_architecture.JPG)

### Model charcteristics:
------------------------

1. Has **12,026** parameters
2. Droput set as **0.069**
3. Batch size is **128**
4. Random rotation to images between **-5 to +5 degrees**
5. Added GAP followed by a **1x1** layer (Since it's applied on 1D data)
6. Learning rate is **0.05** & momentum **0.9**
7. Achieved Test accuracy 99.4% at **13th Epoch & later gave consistently 99.4% throughout the end of the epoch.**

## Logs:
--------
0%|          | 0/469 [00:00<?, ?it/s]Epoch ===>  1
loss=0.0801708847284317 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.45it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0672, Accuracy: 9801/10000 (98.01%)

Epoch ===>  2
loss=0.05209269002079964 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.30it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0488, Accuracy: 9845/10000 (98.45%)

Epoch ===>  3
loss=0.030904844403266907 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.25it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0537, Accuracy: 9818/10000 (98.18%)

Epoch ===>  4
loss=0.018628625199198723 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.22it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0328, Accuracy: 9901/10000 (99.01%)

Epoch ===>  5
loss=0.06972938776016235 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.38it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0280, Accuracy: 9915/10000 (99.15%)

Epoch ===>  6
loss=0.028522558510303497 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.20it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0306, Accuracy: 9910/10000 (99.10%)

Epoch ===>  7
loss=0.08459246903657913 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.30it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0290, Accuracy: 9920/10000 (99.20%)

Epoch ===>  8
loss=0.020929912105202675 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.37it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0287, Accuracy: 9916/10000 (99.16%)

Epoch ===>  9
loss=0.019750045612454414 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.24it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0254, Accuracy: 9923/10000 (99.23%)

Epoch ===>  10
loss=0.008316735737025738 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.35it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0289, Accuracy: 9918/10000 (99.18%)

Epoch ===>  11
loss=0.009083679877221584 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.31it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0219, Accuracy: 9935/10000 (99.35%)

Epoch ===>  12
loss=0.029636325314641 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.36it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0206, Accuracy: 9939/10000 (99.39%)

Epoch ===>  13
loss=0.0028239365201443434 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.52it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0200, Accuracy: 9942/10000 (99.42%)

Epoch ===>  14
loss=0.0021510038059204817 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.61it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0197, Accuracy: 9942/10000 (99.42%)

Epoch ===>  15
loss=0.011636830866336823 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.46it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0193, Accuracy: 9943/10000 (99.43%)

Epoch ===>  16
loss=0.009641659446060658 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.71it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0193, Accuracy: 9945/10000 (99.45%)

Epoch ===>  17
loss=0.02697911113500595 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.59it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0192, Accuracy: 9946/10000 (99.46%)

Epoch ===>  18
loss=0.003246374661102891 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.72it/s]
  0%|          | 0/469 [00:00<?, ?it/s]
Test set: Average loss: 0.0191, Accuracy: 9945/10000 (99.45%)

Epoch ===>  19
loss=0.025792451575398445 batch_id=468: 100%|██████████| 469/469 [00:28<00:00, 16.73it/s]

Test set: Average loss: 0.0189, Accuracy: 9947/10000 (99.47%)


## Chart:
---------
Below chart depicts the Train & Validation accuracy across the epochs:

![train_val_acc](https://github.com/karthikmohan1702/EVA6/blob/798a20f1f6cf9c56017a5785893f00b696654ecf/Session_4/Architectural_basics/images/train_val_acc_chart.JPG)


## Learning:
------------
Performing different experimentation on the MNIST data to achieve 99.4% accuracy consistently for last couple of epochs has helped me to see how changing or adding hyperparameters can change the accuracy of the network. Having set of constraints like less than 20k params, 0.069 as dropout, has set me to focus keenly on how to utilize different hyper params & how it is having an impact on the accuracy.
