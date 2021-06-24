from torchsummary import summary
import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from collections import Counter
from collections import OrderedDict


def get_device_info():
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    print(device)
    return device


def get_model_summary(model, input_size):
    device = get_device_info()
    model_to_device = model.to(device)
    return summary(model, input_size)


def get_mean_std(loader):
    channels_sum, channels_sqrd_sum, num_batches = 0, 0, 0

    for data, _ in tqdm(loader):
        channels_sum += torch.mean(data, dim=[0, 2, 3])
        channels_sqrd_sum += torch.mean(data ** 2, dim=[0, 2, 3])
        num_batches += 1

    mean = channels_sum / num_batches
    std = (channels_sqrd_sum / num_batches - mean ** 2) ** 0.5

    return mean, std


def get_class_dist(classes, dataset):
  ord_dict = OrderedDict()
  for id, cl in enumerate(classes):
    ord_dict[id] = cl  

  count_label = []
  count_img_size = []
  for img, label in dataset:
    label = ord_dict[label]
    count_label.append(label)
    count_img_size.append(img.numpy().shape)
  return Counter(count_label), Counter(count_img_size)

def print_dist_stats(train_set, test_set):
  print("Distribution of classes in Train Dataset")
  print("=="*30)
  display(get_class_dist(train_set.classes, train_set)[0])
  print("\n")

  print("Distribution of classes in Test Dataset")
  print("=="*30)
  display(get_class_dist(test_set.classes, test_set)[0])
  print("\n")

  print("Distribution of size of image in Train Dataset")
  print("=="*30)
  display(get_class_dist(train_set.classes, train_set)[1])
  print("\n")

  print("Distribution of size of image in Test Dataset")
  print("=="*30)
  display(get_class_dist(test_set.classes, test_set)[1])
  print("\n")