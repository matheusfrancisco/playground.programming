//! A sorted array of UNIQUE integers was rotated at an unknown pivot.
//! For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20].
//! Find the index of the minimum element in this array.
//!
//! Examples (from the study page):
//!   [30, 40, 50, 10, 20]          → 3   (min is 10 at index 3)
//!   [3, 5, 7, 11, 13, 17, 19, 2]  → 7   (min is 2 at index 7)
//!
//! Requirements
//! ------------
//! - O(log n) time, O(1) space. Values are distinct (no equal-to-pivot
//!   ambiguity). Rotation by 0 (already sorted) must also work.
//! - Assume nums.len >= 1.

const std = @import("std");

pub fn findMinIndex(nums: []const i32) usize {
    var lo: usize = 0;
    var hi: usize = nums.len - 1;

    while (lo < hi) {
        const mid = lo + (hi - lo) / 2;

        if (nums[mid] > nums[hi]) {
            lo = mid + 1; // search right half
        } else {
            hi = mid; // search left half
        }
    }
    return lo;
}

/// Naive O(n) scan for the smallest element's index.
fn naiveMinIndex(nums: []const i32) usize {
    var best: usize = 0;
    for (nums, 0..) |x, i| {
        if (x < nums[best]) best = i;
    }
    return best;
}

// ── Tests (the spec) ────────────────────────────────────────────────────────

test "study page example 1" {
    const nums = [_]i32{ 30, 40, 50, 10, 20 };
    try std.testing.expectEqual(@as(usize, 3), findMinIndex(&nums));
}

test "study page example 2" {
    const nums = [_]i32{ 3, 5, 7, 11, 13, 17, 19, 2 };
    try std.testing.expectEqual(@as(usize, 7), findMinIndex(&nums));
}

test "rotation by zero: already sorted" {
    const nums = [_]i32{ 10, 20, 30, 40, 50 };
    try std.testing.expectEqual(@as(usize, 0), findMinIndex(&nums));
}

test "rotation by one: min at the last index" {
    const nums = [_]i32{ 2, 3, 4, 5, 1 };
    try std.testing.expectEqual(@as(usize, 4), findMinIndex(&nums));
}

test "single element and pair" {
    const one = [_]i32{7};
    try std.testing.expectEqual(@as(usize, 0), findMinIndex(&one));
    const pair = [_]i32{ 9, 4 };
    try std.testing.expectEqual(@as(usize, 1), findMinIndex(&pair));
}

test "stress: random strictly-increasing array, random rotation" {
    var prng = std.Random.DefaultPrng.init(0xA1512);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 100) : (round += 1) {
        const n = r.intRangeAtMost(usize, 1, 150);
        const buf = try alloc.alloc(i32, n);
        defer alloc.free(buf);
        // Strictly increasing values, then rotate by rot.
        const rot = r.intRangeLessThan(usize, 0, n);
        var v: i32 = r.intRangeAtMost(i32, -100, 0);
        var i: usize = 0;
        while (i < n) : (i += 1) {
            v += r.intRangeAtMost(i32, 1, 5);
            buf[(i + rot) % n] = v;
        }
        const idx = findMinIndex(buf);
        try std.testing.expectEqual(naiveMinIndex(buf), idx);
    }
}
