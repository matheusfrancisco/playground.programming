//! -------
//! A mountain array has at least 3 elements and a "peak" at index k:
//! A[0] < ... < A[k-1] < A[k] > A[k+1] > ... > A[n-1] — strictly increasing
//! up to the peak, then strictly decreasing. The peak is neither the first
//! nor the last index. Find the index k. Assume there is only one peak.
//!
//! Example (from the study page): [0, 1, 2, 3, 4, 2, 1, 0] → 3
//! (the largest element is 3, at index 3).
//!
//! Requirements
//! - O(log n) time, O(1) space — an O(n) max-scan misses the point.

const std = @import("std");

pub fn peakIndex(nums: []const i32) usize {
    var lo: usize = 0;
    var hi: usize = nums.len - 1;

    while (lo < hi) {
        const mid = lo + (hi - lo) / 2;

        if (nums[mid] < nums[mid + 1]) {
            lo = mid + 1; // search right half
        } else {
            hi = mid; // search left half
        }
    }
    return lo;
}

/// Naive O(n) oracle: index of the maximum element.
fn naivePeakIndex(nums: []const i32) usize {
    var best: usize = 0;
    for (nums, 0..) |x, i| {
        if (x > nums[best]) best = i;
    }
    return best;
}

/// Validity checker for generated inputs: strictly up to k, strictly down after.
fn isMountain(nums: []const i32, k: usize) bool {
    if (nums.len < 3 or k == 0 or k == nums.len - 1) return false;
    var i: usize = 0;
    while (i < k) : (i += 1) {
        if (nums[i] >= nums[i + 1]) return false;
    }
    while (i < nums.len - 1) : (i += 1) {
        if (nums[i] <= nums[i + 1]) return false;
    }
    return true;
}

// ── Tests (the spec) ────────────────────────────────────────────────────────

test "example from the study page" {
    const nums = [_]i32{ 0, 1, 2, 3, 2, 1, 0 };
    try std.testing.expectEqual(@as(usize, 3), peakIndex(&nums));
}

test "minimal mountain (3 elements)" {
    const nums = [_]i32{ 1, 5, 2 };
    try std.testing.expectEqual(@as(usize, 1), peakIndex(&nums));
}

test "peak next to the left edge" {
    const nums = [_]i32{ 1, 9, 8, 4, 2 };
    try std.testing.expectEqual(@as(usize, 1), peakIndex(&nums));
}

test "peak next to the right edge" {
    const nums = [_]i32{ 1, 2, 3, 9, 4 };
    try std.testing.expectEqual(@as(usize, 3), peakIndex(&nums));
}

test "stress: random mountains, checked against the max-scan oracle" {
    var prng = std.Random.DefaultPrng.init(0xA1513);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 100) : (round += 1) {
        const n = r.intRangeAtMost(usize, 3, 150);
        const buf = try alloc.alloc(i32, n);
        defer alloc.free(buf);
        const k = r.intRangeAtMost(usize, 1, n - 2);
        // Build strictly-increasing ascent then strictly-decreasing descent.
        var v: i32 = r.intRangeAtMost(i32, -50, 0);
        var i: usize = 0;
        while (i <= k) : (i += 1) {
            v += r.intRangeAtMost(i32, 1, 4);
            buf[i] = v;
        }
        while (i < n) : (i += 1) {
            v -= r.intRangeAtMost(i32, 1, 4);
            buf[i] = v;
        }
        try std.testing.expect(isMountain(buf, k));
        try std.testing.expectEqual(naivePeakIndex(buf), peakIndex(buf));
    }
}
