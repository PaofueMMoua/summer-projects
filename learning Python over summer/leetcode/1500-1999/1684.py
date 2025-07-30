allowed_set = set(allowed)
        c = 0
        for word in words:
            if all(ch in allowed_set for ch in word):
                c += 1
        return c