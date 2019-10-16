import itertools
import numpy as np
from typing import List, Iterator

def online_random_sampler(stream: Iterator[int], k: int) -> List[int]:
    # grab first k elements from stream
    sub = list(itertools.islice(stream, k))
    num_seen = k
    for s in stream:
        num_seen += 1
        v = np.random.randint(0, num_seen)
        if v < k:
            sub[v] = s
    return sub

if __name__ == "__main__":
    k = 2
    np.random.seed(0)
    x = iter(np.random.randint(0, 100, size=10))
    print(online_random_sampler(x, k), k)
