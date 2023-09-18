import os as os


BAR_LENGTH = int(os.get_terminal_size().columns * 0.75)


def ft_tqdm(lst: range) -> None:
    """
    Function that simulates a progress bar.

    @param lst: range of values
    @return None
    """
    end = lst.stop - lst.start
    for x in range(end + 1):
        ratio = x / end
        filled = int(BAR_LENGTH * ratio)
        empty = BAR_LENGTH - filled
        loading_bar = '█' * filled + ' ' * empty
        yield print(f"{ratio * 100:.0f}%|{loading_bar}| {x}/{end}", end="\r")
