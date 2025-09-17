# zoo-cad-data-normalizer
Normalize heterogeneous CAD metadata to a single CSV (demo).

## Quickstart
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python src/normalize_cad.py --input data/raw --output data/processed/normalized.csv
```

## Schema
```part_id,assembly,version,updated_at,material,mass_kg,bbox_x,bbox_y,bbox_z,checksum,source_file```
