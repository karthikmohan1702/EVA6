import torch
import torchvision
from torchvision import datasets


def get_mnist_dataset(train_transforms, test_transforms):
    train = datasets.MNIST(
        "./data", train=True, download=True, transform=train_transforms
    )
    test = datasets.MNIST(
        "./data", train=False, download=True, transform=test_transforms
    )
    return train, test


class get_cifar10_dataset(torchvision.datasets.CIFAR10):
    def __init__(
        self, root="~/data/cifar10", train=True, download=True, transform=None
    ):
        super().__init__(root=root, train=train, download=download, transform=transform)

    def __getitem__(self, index):
        image, label = self.data[index], self.targets[index]

        if self.transform is not None:
            augmentations = self.transform(image=image)
            image = augmentations["image"]

        return image, label


def train_test_loader(trainset, testset, batch_size):
    train_loader = torch.utils.data.DataLoader(
        trainset, batch_size=batch_size, shuffle=True, num_workers=2
    )

    test_loader = torch.utils.data.DataLoader(
        testset, batch_size=batch_size, shuffle=False, num_workers=2
    )

    return train_loader, test_loader


