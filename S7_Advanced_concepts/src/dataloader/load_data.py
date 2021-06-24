import torch
import torchvision
from torchvision import datasets


def mnist_dataset(train_transforms, test_transforms):
    train = datasets.MNIST(
        "./data", train=True, download=True, transform=train_transforms
    )
    test = datasets.MNIST(
        "./data", train=False, download=True, transform=test_transforms
    )
    return train, test


class cifar10_dataset(torchvision.datasets.CIFAR10):
    def __init__(
        self, root="~/data/cifar10", train=True, download=True, transform=None
    ):
        super().__init__(root=root, train=train, download=download, transform=transform)

    def __getitem__(self, index):
        image, label = self.data[index], self.targets[index]

        if self.transform is not None:
            transformed = self.transform(image=image)
            image = transformed["image"]

        return image, label


def train_test_loader(trainset, testset, batch_size):
    train_loader = torch.utils.data.DataLoader(
        trainset, batch_size=batch_size, shuffle=True, num_workers=2
    )

    test_loader = torch.utils.data.DataLoader(
        testset, batch_size=batch_size, shuffle=False, num_workers=2
    )

    return train_loader, test_loader


def dummy_loader(sample_dataset, batch_size):
    data_loader = torch.utils.data.DataLoader(
        sample_dataset, batch_size=batch_size, shuffle=True, num_workers=2
    )

    return data_loader
