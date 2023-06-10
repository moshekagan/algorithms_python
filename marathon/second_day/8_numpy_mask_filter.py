import numpy as np

if __name__ == "__main__":
    x = np.linspace(-10, 10, 50)

    # masking
    mask = (0 < x) & (x < 3)  # [F, T, F, T ....]

    # filter values from x with mask
    x_filter = x[mask]
    print(x_filter)

    # get indexs of the filter
    print(np.where(mask)[0])
