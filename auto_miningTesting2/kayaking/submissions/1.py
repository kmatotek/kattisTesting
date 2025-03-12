def max_kayak_speed(b, n, e, sb, sn, se, cs):
    cs.sort()
    strengths = [sb]*b + [sn]*n + [se]*e
    strengths.sort()
    result = []

    while strengths:
        if len(strengths) == 1:
            result.append(cs.pop() * strengths.pop())
        else:
            max_strength = strengths.pop()
            min_strength = strengths.pop(0)
            result.append(cs.pop() * (max_strength + min_strength))

    return min(result)


# Testing the function
print(max_kayak_speed(2, 3, 2, 1, 2, 3, [1, 1, 2, 2, 3]))