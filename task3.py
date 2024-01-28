import timeit


def boyer_moore_search(text, pattern):
    def build_last_occurrence_table(pattern):
        table = {}
        for i in range(len(pattern)):
            table[pattern[i]] = i
        return table

    last_occurrence = build_last_occurrence_table(pattern)
    m = len(pattern)
    n = len(text)
    i = m - 1

    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            return i - m + 1
        else:
            i += m - 1 - last_occurrence.get(text[i], -1)
    return -1


def kmp_search(text, pattern):
    def build_lps_array(pattern):
        length = 0
        lps = [0] * len(pattern)
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
        return lps

    lps = build_lps_array(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def rabin_karp_search(text, pattern, d=256, q=101):
    m = len(pattern)
    n = len(text)
    h = pow(d, m - 1) % q
    p = t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
    return -1


def measure_time(func, text, pattern):
    start_time = timeit.default_timer()
    func(text, pattern)
    return timeit.default_timer() - start_time


text1 = "приклад тексту для першого тексту"
pattern1 = "підрядок"

text2 = "інший текст для другого тесту"
pattern2 = "шукати"

# Вимірювання часу
bm_time_text1 = measure_time(boyer_moore_search, text1, pattern1)
kmp_time_text1 = measure_time(kmp_search, text1, pattern1)
rk_time_text1 = measure_time(rabin_karp_search, text1, pattern1)

bm_time_text2 = measure_time(boyer_moore_search, text2, pattern2)
kmp_time_text2 = measure_time(kmp_search, text2, pattern2)
rk_time_text2 = measure_time(rabin_karp_search, text2, pattern2)

# Створення Markdown звіту
markdown_report = f"""
# Висновки про швидкість алгоритмів пошуку підрядка

## Текст 1: "{text1}"
| Алгоритм | Час виконання |
|----------|---------------|
| Боєра-Мура | {bm_time_text1:.6f} сек |
| КМП | {kmp_time_text1:.6f} сек |
| Рабіна-Карпа | {rk_time_text1:.6f} сек |

## Текст 2: "{text2}"
| Алгоритм | Час виконання |
|----------|---------------|
| Боєра-Мура | {bm_time_text2:.6f} сек |
| КМП | {kmp_time_text2:.6f} сек |
| Рабіна-Карпа | {rk_time_text2:.6f} сек |
"""


print(markdown_report)