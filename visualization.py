import matplotlib.pyplot as plt
import numpy as np
import torchvision
from dataloader import load_data
from utils import misc
import torch


def plot_sample_img(loader, classes):
    dataiter = iter(loader)
    images, labels = dataiter.next()
    grid = torchvision.utils.make_grid(images)
    plt.axis("off")
    print(" ".join("%7s" % classes[labels[j]] for j in range(5)))
    _ = plt.imshow(grid.permute(1, 2, 0))


def plot_acc_loss(train_losses, train_acc, test_losses, test_acc):
    fig, axs = plt.subplots(2, 2, figsize=(15, 10))
    axs[0, 0].plot(train_losses)
    axs[0, 0].set_title("Training Loss")
    axs[1, 0].plot(train_acc)
    axs[1, 0].set_title("Training Accuracy")
    axs[0, 1].plot(test_losses)
    axs[0, 1].set_title("Test Loss")
    axs[1, 1].plot(test_acc)
    axs[1, 1].set_title("Test Accuracy")


def misclassified_images(model, classes, test_transform, trainset, testset, batch_size):
    testset = load_data.get_cifar10_dataset(train=False, transform=test_transform)
    batch_size = len(testset)
    train_loader, test_loader = load_data.train_test_loader(
        trainset, testset, batch_size
    )
    mean, std = misc.get_mean_std(train_loader)
    device = misc.get_device_info()
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            pred = output.argmax(dim=1, keepdim=True)
            indexes = (
                pred.view(
                    -1,
                )
                != target.view(
                    -1,
                )
            ).nonzero()
            fig = plt.figure(figsize=(10, 9))
            for i, idx in enumerate(indexes[:15]):
                ax = fig.add_subplot(3, 5, i + 1)
                mean_norm = torch.tensor(mean).reshape(1, 3, 1, 1)
                std_norm = torch.tensor(std).reshape(1, 3, 1, 1)
                img = data.cpu() * std_norm + mean_norm
                ax.imshow(img[idx].squeeze().permute(1, 2, 0).clamp(0, 1))
                ax.set_title(
                    f"Target = {classes[target[idx].item()]} \n Predicted = {classes[pred[idx].item()]}"
                )

            plt.show()
