from torchsummary import summary
import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np


def get_device_info():
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    print(device)
    return device

def get_model_summary(model, input_size):
    device = get_device_info()
    model_to_device = model.to(device)
    return summary(model, input_size)



