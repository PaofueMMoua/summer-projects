cnt = {chr(i):0 for i in range(97, 123)}
        for ch in s:
            cnt[ch] += 1
        vow = {'a':cnt['a'], 'e':cnt['e'], 'o':cnt['o'], 'i':cnt['i'], 'u':cnt['u']}
        for v in vow:
            del cnt[v]
        return max(vow.values()) + max(cnt.values())