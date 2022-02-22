import torch
state_dict = torch.load("/best.pth")
torch.save(state_dict, "/best.pth", _use_new_zipfile_serialization=False)
