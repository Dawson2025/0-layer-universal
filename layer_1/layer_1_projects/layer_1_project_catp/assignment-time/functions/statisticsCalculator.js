/**
 * Statistical calculation functions for assignment timing data
 */

/**
 * Calculate mean (average) of an array of numbers
 */
function calculateMean(values) {
    if (!values || values.length === 0) return 0;
    const sum = values.reduce((acc, val) => acc + val, 0);
    return sum / values.length;
}

/**
 * Calculate median of an array of numbers
 */
function calculateMedian(values) {
    if (!values || values.length === 0) return 0;
    
    const sorted = [...values].sort((a, b) => a - b);
    const middle = Math.floor(sorted.length / 2);
    
    if (sorted.length % 2 === 0) {
        // Even number of elements - average the two middle values
        return (sorted[middle - 1] + sorted[middle]) / 2;
    } else {
        // Odd number of elements - return the middle value
        return sorted[middle];
    }
}

/**
 * Calculate mode (most frequent value) of an array of numbers
 * If there's a tie, returns the smallest value
 */
function calculateMode(values) {
    if (!values || values.length === 0) return 0;
    
    // Create frequency map
    const frequency = {};
    values.forEach(val => {
        frequency[val] = (frequency[val] || 0) + 1;
    });
    
    // Find the maximum frequency
    let maxFreq = 0;
    let mode = values[0];
    
    for (const [value, freq] of Object.entries(frequency)) {
        const numValue = parseFloat(value);
        if (freq > maxFreq || (freq === maxFreq && numValue < mode)) {
            maxFreq = freq;
            mode = numValue;
        }
    }
    
    return mode;
}

/**
 * Calculate all statistics for an array of time values
 */
function calculateStatistics(timeValues) {
    if (!timeValues || timeValues.length === 0) {
        return {
            mean: 0,
            median: 0,
            mode: 0,
            count: 0,
            min: 0,
            max: 0
        };
    }
    
    return {
        mean: Math.round(calculateMean(timeValues)),
        median: Math.round(calculateMedian(timeValues)),
        mode: Math.round(calculateMode(timeValues)),
        count: timeValues.length,
        min: Math.min(...timeValues),
        max: Math.max(...timeValues)
    };
}

module.exports = {
    calculateMean,
    calculateMedian,
    calculateMode,
    calculateStatistics
};

