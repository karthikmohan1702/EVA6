import albumentations as A
from albumentations.pytorch import ToTensorV2
import torchvision
import torchvision.transforms as transforms


def albumentaion_transform():
    train_transform = A.Compose(
        [
            A.HorizontalFlip(p=0.2),
            A.augmentations.geometric.transforms.ShiftScaleRotate(
                shift_limit=0.0625,
                scale_limit=0.1,
                rotate_limit=10,
            ),
            A.CoarseDropout(
                max_holes=1,
                max_height=16,
                max_width=16,
                min_holes=1,
                min_height=16,
                min_width=1,
                fill_value=[0.4914, 0.4822, 0.4465],
                mask_fill_value=None,
            ),
            A.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)),
            ToTensorV2(),
        ]
    )

    test_transform = A.Compose(
        [A.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010)), ToTensorV2()]
    )

    return train_transform, test_transform


def mnist_transform():
    # Train Phase transformations
    train_transforms = transforms.Compose(
        [
            #  transforms.Resize((28, 28)),
            #  transforms.ColorJitter(brightness=0.10, contrast=0.1, saturation=0.10, hue=0.1),
            transforms.RandomRotation((-6.0, 6.0), fill=(1,)),
            transforms.ToTensor(),
            transforms.Normalize(
                (0.1307,), (0.3081,)
            )  # The mean and std have to be sequences (e.g., tuples), therefore you should add a comma after the values.
            # Note the difference between (0.1307) and (0.1307,)
        ]
    )

    # Test Phase transformations
    test_transforms = transforms.Compose(
        [
            #  transforms.Resize((28, 28)),
            #  transforms.ColorJitter(brightness=0.10, contrast=0.1, saturation=0.10, hue=0.1),
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,)),
        ]
    )
    return train_transforms, test_transforms
