try:
    from src.backends.zvec_backend import ZvecANN, ZvecConfig
except Exception as e:
    print("zvec not available; skipping zvec smoke test")
    raise SystemExit(0)

def main():
    ann = ZvecANN(ZvecConfig(path="./.zvec_demo", dim=4))
    ann.insert(
        ids=[1, 2],
        vectors=[
            [0.1, 0.2, 0.3, 0.4],
            [0.2, 0.3, 0.4, 0.1],
        ],
        meta=[{"tag": "a"}, {"tag": "b"}],
    )
    print(ann.query([0.4, 0.3, 0.3, 0.1], r=0, k=2))

if __name__ == "__main__":
    main()
