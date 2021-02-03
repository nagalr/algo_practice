def minimumLoss(price):
    i, j = 0, len(price) - 1
    min_loss = 100000  # inf-figure
    while i < j:
        if 0 < price[i] - price[j] < min_loss:
            min_loss = price[i] - price[j]

        if price[i] > price[j]:
            i += 1
        else:
            j -= 1

    return min_loss


l = [20, 7, 8, 2, 5]

print(minimumLoss(l))
