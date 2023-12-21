from collections import Counter
import heapq


def encode(input_str):
    heap = []
    for char, count in Counter(s).items():
        heap.append([count, [char, ""]])

    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        for pair in lo[1:]:
            pair[1] = '0' + pair[1]

        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    codes = heap[0][1:]

    for char, code in codes:
        input_str = input_str.replace(char, code)

    return input_str, codes


s = input()

s_encoded, s_codes = encode(s)

for code in s_codes:
    print(f"{code[0]}: {code[1]}")

print(s_encoded)