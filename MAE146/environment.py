import sys
import numpy as np
import matplotlib as plt
import scipy
import tqdm
import sklearn
import torch

if __name__ == "__main__":
    print("python executable:", sys.executable)
    print("python version:", sys.version)
    print("numpy version:", np.__version__)
    print("matplotlib version:", plt.__version__)
    print("scipy version:", scipy.__version__)
    print("tqdm version:", tqdm.__version__)
    print("sklearn version:", sklearn.__version__)
    print("torch version:", torch.__version__)
    print("cuda available:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("device:", "cuda")
        print("gpu count:", torch.cuda.device_count())
        print("current gpu:", torch.cuda.current_device())
        print("gpu name:", torch.cuda.get_device_name(0))
    else:
        print("device:", "cpu")
        print("running on CPU")

    print("All modules have been successfully installed.")

