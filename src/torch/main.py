import torch


def main():
    print("Hello, world!")
    x = torch.rand(5, 3)
    print(x)

    dev_count = torch.cuda.device_count()
    print(f"Number of CUDA devices: {dev_count}")

if __name__ == "__main__":
    main()
