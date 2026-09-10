//! Given an array `nums` consisting of ONLY non-negative integers, find the
//! largest sum among all subarrays of length `k` in `nums`.
//!
//! Example: nums = [1, 2, 3, 7, 4, 1], k = 3 → 14
//! (the largest length-3 subarray sum is [3, 7, 4] = 14).
//!
//! Requirements
//! ------------
//! - O(n) time, O(1) extra space: slide the window, do NOT re-sum it.
//!   (Recomputing each window is the O(n·k) trap the page warns about.)
//! - Assume 1 <= k <= nums.len. Return i64 to keep sums overflow-safe.
//!
//! Design questions (answer on paper BEFORE coding)
//! ------------------------------------------------
//! 1. State the window invariant in ONE sentence: when the window is
//!    [i, j], what does your running variable `sum` equal at all times?
//! 2. Sliding by one position changes the sum by exactly which two terms?
//!    Write the update as a single formula.
//! 3. Where is the window first FULL, and why does the answer update belong
//!    only from that point on?
//! 4. Would this exact code still be correct with negative numbers in the
//!    array? (Contrast with p08/p09 where it would not.)

const std = @import("std");

/// Largest sum among all subarrays of length exactly `k`.
/// Precondition: 1 <= k <= nums.len.
pub fn maxWindowSum(nums: []const i32, k: usize) i64 {
    if (k > nums.len) return 0;

    var sum: i64 = 0;
    var l: usize = 0;
    var r: usize = 0;
    var best: i64 = 0;

    while (r < nums.len) : (r += 1) {
        sum += nums[r];
        if (r - l + 1 == k) {
            best = @max(best, sum);
            sum -= nums[l];
            l += 1;
        }
    }

    return best;
}

/// Naive O(n·k) oracle: re-sum every window from scratch.
fn naiveMaxWindowSum(nums: []const i32, k: usize) i64 {
    var best: ?i64 = null;
    var start: usize = 0;
    while (start + k <= nums.len) : (start += 1) {
        var sum: i64 = 0;
        for (nums[start .. start + k]) |x| sum += x;
        if (best == null or sum > best.?) best = sum;
    }
    return best.?;
}

// ── Tests (the spec) ────────────────────────────────────────────────────────
test "example from the study page" {
    const nums = [_]i32{ 1, 2, 3, 7, 4, 1 };
    try std.testing.expectEqual(@as(i64, 14), maxWindowSum(&nums, 3));
}

test "k equals the whole array" {
    const nums = [_]i32{ 5, 1, 2 };
    try std.testing.expectEqual(@as(i64, 8), maxWindowSum(&nums, 3));
}

test "k = 1 picks the maximum element" {
    const nums = [_]i32{ 4, 9, 2, 9, 1 };
    try std.testing.expectEqual(@as(i64, 9), maxWindowSum(&nums, 1));
}

test "all zeros" {
    const nums = [_]i32{ 0, 0, 0, 0 };
    try std.testing.expectEqual(@as(i64, 0), maxWindowSum(&nums, 2));
}

test "stress: matches the re-summing oracle" {
    var prng = std.Random.DefaultPrng.init(0xA1506);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 50) : (round += 1) {
        const n = r.intRangeAtMost(usize, 1, 150);
        const buf = try alloc.alloc(i32, n);
        defer alloc.free(buf);
        for (buf) |*x| x.* = r.intRangeAtMost(i32, 0, 1000);
        const k = r.intRangeAtMost(usize, 1, n);
        try std.testing.expectEqual(naiveMaxWindowSum(buf, k), maxWindowSum(buf, k));
    }
}
