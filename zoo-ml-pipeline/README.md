# zoo-ml-pipeline
Reproducible ML demo: synthetic dataset → features → baseline model → metrics.

## Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/train.py --seed 42 --out artifacts
python src/evaluate.py --artifacts artifacts
```
