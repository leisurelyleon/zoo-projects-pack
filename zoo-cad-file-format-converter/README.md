# zoo-cad-file-format-converter
Parser/validator for a toy `.cadf` format, converters to JSON, and simple fuzzing.

## Python
```bash
python tools/cadf_to_json.py data/sample.cadf > data/sample.json
python tools/validate.py data/sample.cadf
python tools/fuzz.py --iters 50
```

## C++
```bash
mkdir build && cd build && cmake .. && cmake --build .
./cadf_to_json ../data/sample.cadf > ../data/sample.cpp.json
```
