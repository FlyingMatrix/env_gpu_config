import torch

print("=============================================================")
print("PyTorch version: " + torch.__version__)
print("Is GPU support is available: " + str(torch.cuda.is_available()))
print("Current CUDA device: " + str(torch.cuda.device(torch.cuda.current_device())))
print("Current device name: " + torch.cuda.get_device_name(torch.cuda.current_device()))
print("=============================================================")