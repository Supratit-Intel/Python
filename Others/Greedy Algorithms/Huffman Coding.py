import heapq

def huffman_encode(freq):
    heap = [[w, [sym, '']] for sym, w in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        l = heapq.heappop(heap)
        r = heapq.heappop(heap)
        for pair in l[1:]:
            pair[1] = '0' + pair[1]
        for pair in r[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [l[0]+r[0]] + l[1:] + r[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

if __name__ == '__main__':
    freq = {'a':5,'b':2,'c':1}
    print(huffman_encode(freq))