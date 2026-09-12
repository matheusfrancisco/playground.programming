//! Given an array of integers sorted in increasing order and a target, find
//! the index of the first element in the array that is larger than or equal
//! to the target.
//!
//! Examples (from the study page):
//!   arr = [1, 3, 3, 5, 8, 8, 10], target = 2 → 1   (first ≥ 2 is 3 at index 1)
//!   arr = [2, 3, 5, 7, 11, 13, 17, 19], target = 6 → 3   (first ≥ 6 is 7)
//!
//! The page guarantees a satisfying element exists; here we generalize the
//! return type to ?usize and return null when EVERY element is smaller than
//! target (the boundary is "one past the end").
//!
//! Requirements
//! ------------
//! - O(log n) time, O(1) space.
//! - Duplicates allowed: must return the FIRST qualifying index.

const std = @import("std");

pub fn firstNotSmaller(nums: []const i32, target: i32) ?usize {
    var idx: ?usize = null;
    var lo: usize = 0;
    var hi: usize = nums.len;
    while (lo < hi) {
        const mid = lo + (hi - lo) / 2;
        if (nums[mid] >= target) {
            idx = mid;
            hi = mid; // search left half
        } else {
            lo = mid + 1; // search right half
        }
    }
    return idx;
}

/// Naive O(n) left-to-right scan.
fn naiveFirstNotSmaller(nums: []const i32, target: i32) ?usize {
    for (nums, 0..) |x, i| {
        if (x >= target) return i;
    }
    return null;
}

test "study page example 1" {
    const nums = [_]i32{ 1, 3, 3, 5, 8, 8, 10 };
    try std.testing.expectEqual(@as(?usize, 1), firstNotSmaller(&nums, 2));
}

test "study page example 2" {
    const nums = [_]i32{ 2, 3, 5, 7, 11, 13, 17, 19 };
    try std.testing.expectEqual(@as(?usize, 3), firstNotSmaller(&nums, 6));
}

test "duplicates: first of the equal run" {
    const nums = [_]i32{ 1, 3, 3, 3, 5 };
    try std.testing.expectEqual(@as(?usize, 1), firstNotSmaller(&nums, 3));
}

test "target below all elements: index 0" {
    const nums = [_]i32{ 4, 6, 8 };
    try std.testing.expectEqual(@as(?usize, 0), firstNotSmaller(&nums, -100));
}

test "target above all elements: null" {
    const nums = [_]i32{ 4, 6, 8 };
    try std.testing.expectEqual(@as(?usize, null), firstNotSmaller(&nums, 9));
}

test "empty array: null" {
    try std.testing.expectEqual(@as(?usize, null), firstNotSmaller(&[_]i32{}, 5));
}

test "stress: matches the linear-scan oracle" {
    var prng = std.Random.DefaultPrng.init(0xA1511);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 100) : (round += 1) {
        const n = r.intRangeAtMost(usize, 0, 150);
        const buf = try alloc.alloc(i32, n);
        defer alloc.free(buf);
        var v: i32 = r.intRangeAtMost(i32, -30, 0);
        for (buf) |*slot| {
            v += r.intRangeAtMost(i32, 0, 4); // nondecreasing, dups common
            slot.* = v;
        }
        const target = r.intRangeAtMost(i32, -40, v + 10);
        try std.testing.expectEqual(naiveFirstNotSmaller(buf, target), firstNotSmaller(buf, target));
    }
}
