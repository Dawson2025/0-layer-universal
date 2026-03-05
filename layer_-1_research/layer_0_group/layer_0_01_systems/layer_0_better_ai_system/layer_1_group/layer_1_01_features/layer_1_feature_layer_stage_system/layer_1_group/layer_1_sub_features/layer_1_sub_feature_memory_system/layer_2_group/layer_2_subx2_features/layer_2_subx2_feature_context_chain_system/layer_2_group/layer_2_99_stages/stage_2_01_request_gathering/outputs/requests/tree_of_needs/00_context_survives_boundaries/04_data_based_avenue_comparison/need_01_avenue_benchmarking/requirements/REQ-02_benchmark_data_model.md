---
resource_id: "02c1e14f-2dad-4b6a-af34-d491b7ec432f"
resource_type: "output"
resource_name: "REQ-02_benchmark_data_model"
---
# Benchmark Data Model

**Need**: [Avenue Benchmarking](../README.md)

---

- MUST store raw benchmark values with their original units
- MUST store normalized scores (0-100) alongside raw values
- MUST record measurement date and source for traceability
- MUST support both lower-is-better (cost, latency) and higher-is-better (coverage, readability) metrics
- MUST use documented normalization formula: `score = (raw - min) / (max - min) * 100`
