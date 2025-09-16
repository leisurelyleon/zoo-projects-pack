# Zoo Projects Pack

Four compact, buildable demos that map 1:1 to Zoo’s roles. Each folder is self-contained with runnable code and a short README. Screenshots live in `images/`.

> Tip: In applications, paste a link to the specific subfolder (e.g., `.../tree/main/zoo-cad-data-normalizer`) so reviewers land exactly where the code is.

---

## Index (projects → roles)

1. **zoo-cad-data-normalizer** — Python tool to normalize heterogeneous CAD metadata → a clean CSV with checksums.  
   **What I did (1-liner):** Built a Python normalizer that validates/merges CAD metadata and emits a versioned CSV with per-file SHA256 checksums.  
   **Maps to:** *Software Engineer, CAD Data*

2. **zoo-graphics-engine-prototype** — C++17 mesh + transforms + AABB with a micro-benchmark.  
   **What I did (1-liner):** Wrote a clean C++ mesh playground with translate/scale/rotate ops, AABB, and a timing harness to profile hot paths.  
   **Maps to:** *Graphics Engine Software Engineer*

3. **zoo-cad-file-format-converter** — Toy `.cadf` parser/validator with JSON converter and fuzz checks (Python + C++ emitter).  
   **What I did (1-liner):** Implemented a minimal CADF parser/converter, checksum validation, and a fuzz harness to harden error handling.  
   **Maps to:** *Software Engineer, CAD File Format*

4. **zoo-ml-pipeline** — Reproducible pipeline: synthetic dataset → features → baseline model → metrics.  
   **What I did (1-liner):** Assembled a reproducible ML pipeline with feature engineering, a baseline classifier, and logged metrics/artifacts.  
   **Maps to:** *Machine Learning Software Engineer*

---

### 1) CAD Data Normalizer

**TL;DR:** Ingest JSON/CSV, validate, compute per-file checksums, and emit a normalized CSV ready for warehousing.  
**Run**
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/normalize_cad.py --input data/raw --output data/processed/normalized.csv

### 2) Graphics Engine Prototype

**TL;DR:** Minimal C++17 mesh (indexed tris) with translate/scale/rotate ops and AABB; includes a micro-benchmark.
**Build & Run**
```bash
mkdir build && cd build
cmake .. && cmake --build .
./engine_bench

### 3) CAD File Format Converter

**TL;DR:** Parser/validator for a toy .cadf format plus JSON converter; includes fuzzing to harden edge cases.
**Run**
```bash
python tools/cadf_to_json.py data/sample.cadf > data/sample.json
python tools/validate.py data/sample.cadf
python tools/fuzz.py --iters 50

# C++ JSON emitter
mkdir build && cd build && cmake .. && cmake --build .
./cadf_to_json ../data/sample.cadf > ../data/sample.cpp.json

### 4) ML Pipeline
**TL;DR:** Reproducible ML demo that creates features, trains a baseline, and logs metrics/artifacts.
**Run**
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/train.py --seed 42 --out artifacts
python src/evaluate.py --artifacts artifacts

## Outputs `artifacts/features.parquet, model.pkl, metrics.json, eval_summary.json`

# Quick-start (repo-level)
```bash
# from repo root:
cd zoo-cad-data-normalizer     # or another folder
# then follow that folder's README
