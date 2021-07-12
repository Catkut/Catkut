def count_separators(chars):
    counts = 0
    for i in chars:
        if i in [" ", "_", "-"]:
            counts = counts + 1
        else:
            pass
    return(counts)
