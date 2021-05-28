### Objective: 
-----------------------
**==> Calculating the feed forward & backpropagation manually with a given set of inputs & weights for various learning rates 0.1, 0.2, 0.5, 0.8, 1, 2 in the excel.**


### Network Basics
--------------------------
The below network shows the interactions of the below layers:

![Image of neural_net](https://github.com/karthikmohan1702/EVA6/blob/f671eef55d80a6d9af3a416fbad2bbf8480c7e94/Session_4/Backpropagation/images/Neural_network.JPG) ![Image of legend](https://github.com/karthikmohan1702/EVA6/blob/f671eef55d80a6d9af3a416fbad2bbf8480c7e94/Session_4/Backpropagation/images/legend.JPG)



- Input layer — initial layer which constitutes the input data that needs to be fed to the neural network.
- Hidden layers — it’s the layer which is in between the input & output layer & majority of computations happen in these layers & are not visible such as input & output layer. Hence the name hidden layer. 
- Output layer — This is the layer which gives the output, can be in the form a single value or multiple values & situated at the end of the network


### Key terminologies
----------------------

(1)	**Feedforward network**: In simple terms, the input data is feed forwarded through the model from the input layer to the end of the layer (i.e, Output layer).

(2)	**Activation function**: Role of activation function is to capture the non-linearity in the neural network model & to decides whether neuron to be activated or not based on its value which is computed by different types of activation functions like (tanh, sigmoid, RELU, Leaky Relu, SELU, ELU) 

(3)	**Loss function**: Once the feed forward network completes its operation, then we compare our predicted value with actual value & the difference between them is the loss. So, we need a loss function which cumulates the total loss of the network & our goal is to minimize the loss as much as possible such that the predicted value is close to actual value & this can be done by backpropagation. 

(4)	**Backpropagation**: also, can be stated as "backward propagation of errors". Backprop is all about determining how changing the weight impact the overall cost in the neural network. It propagates error backwards in the neural network. On the way back it is finding how much each weight is contributing in the overall error. The weights that contribute more to the overall error will have larger derivation values, which means they will change more when computing gradient descent.

(5)	**Gradient descent**: It is an iterative optimization algorithm which is used to decrease the loss as minimum as possible or aids in finding the global minima.




### Forward Propagation
-----------------------

![Image of forward_prop](https://github.com/karthikmohan1702/EVA6/blob/16648a4cb0b3b15edd6ac6435a7f10d32786b8f3/Session_4/Backpropagation/images/Forward_prop.JPG)

Here from the above image, you can see how the forward propagation is carried out. Starting from the first equation, we have inputs **(i1 & i2)** that are connecting to hidden units **(h1 & h2)** by getting multiplied to the weights w1, w2 for i1 & w3, w4 for i2. 

Later the outputs from the hidden units are then passed to activation function **(a_h1 & a_h2)**, here we have used **sigmoid activation** function which is helping to capture the nonlinearity of the neural network model & allowing only selected neurons to pass through depending upon the activation function that we use. In our case we use sigmoid activation function which is S – shaped curve & has a **range between (0 to 1)**. So it allows only the neurons within that range to pass through the next layer.

Similar approach of computation is performed for **o1, o2 & a_o1, a_o2**

### Backpropagation
--------------------

![Image of back_prop](https://github.com/karthikmohan1702/EVA6/blob/16648a4cb0b3b15edd6ac6435a7f10d32786b8f3/Session_4/Backpropagation/images/Backprop.JPG)

Backpropagation can be encompassed into computing steps.
  1. Calculation of loss function
  2. Performing partial derivatives of total error w.r.t  each weight
  3. Using gradient descent approach to update the weights



#### 1. Calculation of Loss calculation
--------------------------------
We have to calculate the loss or error. The loss function which we are picking up is “MSE” or “mean squared error” .
- Error = (Predicted - Actual)^2 

We have two classes so we’ll have a total error which is below:  
- **E_total = E1 + E2**


#### 2. Performing partial derivatives of total error w.r.t  each weight
-----------------------------------
 
Above equations **(dE_total/dW5, dE_total/dW6, dE_total/dW7, dE_total/dW8, dE_total/dW1, dE_total/dW2, dE_total/dW3, dE_total/dW4)** we perform the core steps of backpropagation which is computing partial derivatives of the total error w.r.t each weight that’s there in the model.
And in equations shows how the partial derivative is performed w.r.t for eg w5. Here we can see that E2 is nowhere related to E1, so we are considering only the E1 & going back using the chain rule.


#### 3. Using gradient descent approach to update the weights
---------------------------------

Since we have all the partial derivatives ready. Now its time to perform the gradient descent approach & update the existing weights by subtracting these partial derivatives that we have calculated in the above steps with a learning rate.

    w1 = w1 - learning_rate * dE_total/dw1
    w2 = w2 - learning_rate * dE_total/dw2
    w3 = w3 - learning_rate * dE_total/dw3
    w4 = w4 - learning_rate * dE_total/dw4
    w5 = w5 - learning_rate * dE_total/dw5
    w8 = w6 - learning_rate * dE_total/dw6
    w7 = w7 - learning_rate * dE_total/dw7
    w8 = w8 - learning_rate * dE_total/dw8


**Learning rate** in the gradient descent tells us how much steps is needed to reach the global minima or less error. Here we have used learning rates like 0.1, 0.2, 0.5, 0.8, 1, 2, 8 & 20.

### Observation
----------
From the below Graph of error w.r.t to different learning rates tells us that lower the learning rate much slow is the progress or takes less time to converge to global minima, whereas higher learning rates are much faster in converging to global minima.

![Image_of_chart](https://github.com/karthikmohan1702/EVA6/blob/16648a4cb0b3b15edd6ac6435a7f10d32786b8f3/Session_4/Backpropagation/images/Chart.jpg)


### Learning 
--------------
Through this exercise we can conclude that learning rate can be an important factor to reduce the overall loss or helping in to converge faster. But still in the real world cases, we can’t solely depend on the learning rate, since higher and lower learning rate has its own de-merits like slow converging (eats up the computation resources) for lower LR & overshooting or missing the global minima for higher LR. It’s wise to consider other hyperparameters along with learning rate. 

