import torch
import torch.nn as nn
import torch.nn.functional as F
from tqdm import tqdm


def l1_regularization(model, loss, lambda_l1):
    l1 = 0
    for p in model.parameters():
        l1 = l1 + p.abs().sum()
    loss = loss + lambda_l1 * l1
    return loss


def set_train(
    model,
    device,
    train_loader,
    optimizer,
    epoch,
    train_losses,
    train_acc,
    lambda_l1=0,
):
    model.train()
    pbar = tqdm(train_loader)
    correct = 0
    processed = 0
    for batch_idx, (data, target) in enumerate(pbar):
        # get samples
        data, target = data.to(device), target.to(device)

        # Init
        optimizer.zero_grad()

        # Predict
        y_pred = model(data)

        # Calculate loss
        loss_func = nn.CrossEntropyLoss()
        loss = loss_func(y_pred, target)

        # L1 regularization
        if lambda_l1 > 0:
            loss = l1_regularization(loss, lambda_l1)

        train_losses.append(loss.data.cpu().numpy().item())

        # Backpropagation
        loss.backward()
        optimizer.step()

        # Update pbar-tqdm

        pred = y_pred.argmax(
            dim=1, keepdim=True
        )  # get the index of the max log-probability
        correct += pred.eq(target.view_as(pred)).sum().item()
        processed += len(data)

        pbar.set_description(
            desc=f"Loss={loss.item()} Batch_id={batch_idx} Accuracy={100*correct/processed:0.2f}"
        )
        train_acc.append(100 * correct / processed)


