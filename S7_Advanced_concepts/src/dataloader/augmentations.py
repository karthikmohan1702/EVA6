import albumentations as A
from albumentations.pytorch import ToTensorV2
import torchvision
import torchvision.transforms as transforms



def albumentaion_transform(mean:list, std:list):
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
                fill_value=mean,
                mask_fill_value=None,
            ),
            A.Normalize(mean, std),
            ToTensorV2(),
        ]
    )

    test_transform = A.Compose(
        [A.Normalize(mean, std), ToTensorV2()]
    )

    return train_transform, test_transform