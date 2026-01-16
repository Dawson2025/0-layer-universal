# Data Science Operations

Utilities for aggregating assignment timing data either directly from Firestore or from local fixtures. The CLI lives in `assignment-timer/data_science_operations/data_science_operations.py`.

## Requirements
- Python 3.11+
- `firebase-admin` (only needed when hitting Firestore)
- Optional: `matplotlib` and `numpy` for plotting (`pip install matplotlib numpy`)

## CLI Usage
```bash
python assignment-timer/data_science_operations/data_science_operations.py \
  --project assignment-time \
  --group-by assignmentId \
  --export-json reports/timings.json \
  --plot reports/timings.png
```

### Key Flags
- `--project`: Firestore project to query (skipped if `--input-json` is provided).
- `--group-by`: `assignmentId` (default) or `courseAssignment`.
- `--collection`: Firestore collection name (defaults to `assignment_timings`).
- `--plot PATH`: Write a histogram + bell curve overlay to the given path (requires matplotlib).
- `--export-json PATH`: Persist raw records and per-group statistics to a JSON file.
- `--input-json PATH`: Load data from a local JSON file instead of querying Firestore. Useful for offline testing.

The printed summary table displays mean/median/std-dev/min/max in `hh:mm:ss` for readability, while JSON exports retain raw seconds for downstream calculations.

## Sample Data Quickstart
1. Run the bundled smoke-test script:
   ```bash
   python assignment-timer/data_science_operations/tests/test_data_science_operations.py
   ```
   This loads in-memory fixtures from `data_science_operations/sample_data/same_as_google_firebase/sample_data.py`, prints grouped summaries, and writes `data_science_operations/sample_data/json/analysis_output.json`.

2. Or invoke the CLI directly against the JSON sample (mirrors Firestore documents):
   ```bash
   python assignment-timer/data_science_operations/data_science_operations.py \
     --input-json assignment-timer/data_science_operations/sample_data/json/assignment_timings_sample.json \
     --group-by courseAssignment \
     --export-json assignment-timer/data_science_operations/sample_data/json/analysis_output.json
   ```

Both approaches simulate multiple Canvas users working on the same assignments so you can verify averages, medians, and distribution plots without touching live Firestore data.
