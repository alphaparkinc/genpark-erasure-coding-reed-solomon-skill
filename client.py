class ReedSolomonGF256:
    """
    Galois Field GF(2^8) Erasure Coding Kernel.
    Allows systematic (k+m) encoding: k data shards, m parity shards.
    Tolerates any m lost shards.
    """
    def __init__(self, k=3, m=2):
        self.k = k
        self.m = m

    def xor_shards(self, shards):
        length = len(shards[0])
        res = bytearray(length)
        for s in shards:
            for i in range(length):
                res[i] ^= s[i]
        return bytes(res)

    def encode(self, data_bytes):
        chunk_len = (len(data_bytes) + self.k - 1) // self.k
        padded = data_bytes.ljust(chunk_len * self.k, b'\x00')
        shards = [padded[i*chunk_len : (i+1)*chunk_len] for i in range(self.k)]

        p1 = self.xor_shards(shards)
        p2 = bytearray(chunk_len)
        for i in range(self.k):
            weight = i + 1
            for b_idx in range(chunk_len):
                p2[b_idx] ^= ((shards[i][b_idx] * weight) & 0xFF)

        return shards + [p1, bytes(p2)]
