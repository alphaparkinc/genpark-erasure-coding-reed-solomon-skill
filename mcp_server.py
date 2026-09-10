import sys
import json
from client import ReedSolomonGF256

rs = ReedSolomonGF256(3, 2)

def handle_call(name, arguments):
    if name == "encode":
        data = arguments["data"].encode("utf-8")
        shards = rs.encode(data)
        return {"total_shards": len(shards), "shard_length": len(shards[0])}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
