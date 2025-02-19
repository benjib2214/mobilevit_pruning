import torch
from torchvision import datasets, transforms

standard_transform = transforms.Compose([
                            transforms.Resize(64),
                            transforms.RandomHorizontalFlip(0.5),
                            transforms.ToTensor(),
                            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                 std=[0.229, 0.224, 0.225])
                            ])

test_transform = transforms.Compose([
                            transforms.Resize(64),
                            transforms.ToTensor(),
                            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                                 std=[0.229, 0.224, 0.225])
                            ])