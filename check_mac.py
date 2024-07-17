import torch
print(torch.backends.mps.is_available())

a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print(a)

b = a.to("mps")
print(b)

