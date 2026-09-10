from client import ReedSolomonGF256

def main():
    print("=== Testing Reed-Solomon Erasure Coding ===")
    rs = ReedSolomonGF256(k=3, m=2)
    payload = b"Production Distributed Object Store Payload 2026"

    encoded = rs.encode(payload)
    print(f"Input payload ({len(payload)} bytes) encoded into {len(encoded)} shards (3 data + 2 parity).")
    assert len(encoded) == 5
    assert len(encoded[0]) == len(encoded[3])
    print("Shard 0 (data):", encoded[0][:10])
    print("Shard 3 (parity 1):", encoded[3][:10])
    print("Shard 4 (parity 2):", encoded[4][:10])
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
