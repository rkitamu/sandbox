"""Bedrock InvokeModel で2つのテキストの cosine similarity を出す。

uv run scripts/bedrock_similarity.py "犬が好き" "猫が好き"
"""
import json
import math
import sys

import boto3

MODEL_ID = "amazon.titan-embed-text-v2:0"


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b, strict=True))
    return dot / (math.hypot(*a) * math.hypot(*b))


def embed(client, text):
    res = client.invoke_model(modelId=MODEL_ID, body=json.dumps({"inputText": text}))
    return json.loads(res["body"].read())["embedding"]


if __name__ == "__main__":
    assert math.isclose(cosine([1, 2], [2, 4]), 1) and cosine([1, 0], [0, 1]) == 0
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    client = boto3.client("bedrock-runtime")
    a, b = (embed(client, t) for t in sys.argv[1:])
    print(f"{cosine(a, b):.4f}")
