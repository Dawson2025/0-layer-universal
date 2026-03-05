// resource_id: "3b6852a1-6be7-4fe4-8855-828b652b8000"
// resource_type: "document"
// resource_name: "dataScienceOperations"
// functions/dataScienceOperations.js

function calculateStatistics(times) {
  if (!times || times.length === 0) {
    return { mean: 0, median: 0, mode: 0 };
  }

  times = removeOutliers(times)

  // Mean
  const mean = times.reduce((a, b) => a + b, 0) / times.length;

  // Median
  const sorted = [...times].sort((a, b) => a - b);
  const mid = Math.floor(sorted.length / 2);
  const median =
    sorted.length % 2 !== 0
      ? sorted[mid]
      : (sorted[mid - 1] + sorted[mid]) / 2;

  // Mode
  const freq = {};
  let maxFreq = 0;
  let mode = null;
  for (const num of times) {
    freq[num] = (freq[num] || 0) + 1;
    if (freq[num] > maxFreq) {
      maxFreq = freq[num];
      mode = num;
    }
  }

  return { mean, median, mode };
}

function removeOutliers(values) {
  // Make a copy so we don’t modify the array while iterating
  let sorted = [...values].sort((a, b) => a - b);

  // Helper function to compute percentile
  function percentile(arr, p) {
    if (arr.length === 0) return 0;
    const index = (p / 100) * (arr.length - 1);
    const lower = Math.floor(index);
    const upper = Math.ceil(index);
    const weight = index - lower;
    if (upper >= arr.length) return arr[lower];
    return arr[lower] * (1 - weight) + arr[upper] * weight;
  }

  const q1 = percentile(sorted, 25);
  const q3 = percentile(sorted, 75);
  const iqr = q3 - q1;

  const lowerBound = q1 - 1.5 * iqr;
  const upperBound = q3 + 1.5 * iqr;

  // Return a filtered array without outliers
  return values.filter(v => v >= lowerBound && v <= upperBound);
}


module.exports = { calculateStatistics };
