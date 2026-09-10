//! Given an array of NON-NEGATIVE integers `nums`, find the length of the
//! longest subarray whose sum is smaller than or equal to `target`.
//!
//! Example: nums = [1, 6, 3, 1, 2, 4, 5], target = 10 → 4
//! (the longest subarray not exceeding 10 is [3, 1, 2, 4]).
//!
//! Requirements
//! - O(n) time, O(1) extra space. Grow right each step; shrink left only
//!   while the window sum exceeds target.
//! - Return 0 when no non-empty subarray qualifies (e.g. every single
//!   element already exceeds target).
//!

const std = @import("std");

/// Length of the longest subarray of non-negative `nums` with sum <= target.
/// Returns 0 if no non-empty subarray qualifies.
pub fn longestSubarraySumAtMost(nums: []const u32, target: u64) usize {
    if (nums.len == 0) return 0;
    var r: usize = 0;
    var l: usize = 0;
    var sum: i64 = 0;
    var best: usize = 0;

    while (r < nums.len) : (r += 1) {
        //std.debug.print("r: {d}, l: {d}, sum: {d}\n", .{ r, l, sum });
        sum += nums[r];
        while (sum > target) : (l += 1) sum -= nums[l];
        // std.debug.print("r: {d}, l: {d}, sum: {d}\n", .{ r, l, sum });
        best = @max(best, r + 1 - l);
        //std.debug.print("r: {d}, l: {d}, sum: {d}\n", .{ r, l, sum });
    }

    //std.debug.print("best: {d}\n", .{best});
    return best;
}

/// Naive O(n²) oracle: try every start, extend while the sum stays in budget.
fn naiveLongest(nums: []const u32, target: u64) usize {
    var best: usize = 0;
    for (0..nums.len) |start| {
        var sum: u64 = 0;
        var j = start;
        while (j < nums.len) : (j += 1) {
            sum += nums[j];
            if (sum > target) break;
            best = @max(best, j - start + 1);
        }
    }
    return best;
}

pub fn shortestSubarraySumAtLeast(nums: []const u32, target: u64) usize {
    if (nums.len == 0) return 0;
    var r: usize = 0;
    var l: usize = 0;
    var sum: i64 = 0;
    var best: usize = 0;

    while (r < nums.len) : (r += 1) {
        sum += nums[r];
        while (sum >= target) : (l += 1) {
            best = if (best == 0) r + 1 - l else @min(best, r + 1 - l);
            sum -= nums[l];
        }
    }

    //std.debug.print("best: {d}\n", .{best});
    return best;
}

/// Naive O(n²) oracle: for every start, extend until the sum reaches target.
fn naiveShortest(nums: []const u32, target: u64) usize {
    var best: ?usize = null;
    for (0..nums.len) |start| {
        var sum: u64 = 0;
        var j = start;
        while (j < nums.len) : (j += 1) {
            sum += nums[j];
            if (sum >= target) {
                const len = j - start + 1;
                if (best == null or len < best.?) best = len;
                break;
            }
        }
    }
    return best orelse 0;
}

test "example from the study page" {
    const nums = [_]u32{ 1, 6, 3, 1, 2, 4, 5 };
    try std.testing.expectEqual(@as(usize, 4), longestSubarraySumAtMost(&nums, 10));
}

test "whole array fits" {
    const nums = [_]u32{ 1, 2, 3 };
    try std.testing.expectEqual(@as(usize, 3), longestSubarraySumAtMost(&nums, 100));
}

test "nothing fits: every element exceeds target" {
    const nums = [_]u32{ 5, 9, 7 };
    try std.testing.expectEqual(@as(usize, 0), longestSubarraySumAtMost(&nums, 4));
}

test "zeros stretch a window for free" {
    const nums = [_]u32{ 0, 0, 5, 0, 0 };
    try std.testing.expectEqual(@as(usize, 5), longestSubarraySumAtMost(&nums, 5));
}

test "empty array" {
    try std.testing.expectEqual(@as(usize, 0), longestSubarraySumAtMost(&[_]u32{}, 3));
}

test "stress: matches the O(n^2) oracle" {
    var prng = std.Random.DefaultPrng.init(0xA1508);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 60) : (round += 1) {
        const n = r.intRangeAtMost(usize, 0, 120);
        const buf = try alloc.alloc(u32, n);
        defer alloc.free(buf);
        for (buf) |*x| x.* = r.intRangeAtMost(u32, 0, 20);
        const target = r.intRangeAtMost(u64, 0, 100);
        try std.testing.expectEqual(naiveLongest(buf, target), longestSubarraySumAtMost(buf, target));
    }
}

test "example from the study page2" {
    const nums = [_]u32{ 1, 4, 1, 7, 3, 0, 2, 5 };
    try std.testing.expectEqual(@as(usize, 2), shortestSubarraySumAtLeast(&nums, 10));
}

test "single element already reaches target" {
    const nums = [_]u32{ 1, 2, 50, 3 };
    try std.testing.expectEqual(@as(usize, 1), shortestSubarraySumAtLeast(&nums, 40));
}

test "whole array needed" {
    const nums = [_]u32{ 2, 2, 2 };
    try std.testing.expectEqual(@as(usize, 3), shortestSubarraySumAtLeast(&nums, 6));
}

test "impossible: total sum below target returns 0" {
    const nums = [_]u32{ 1, 1, 1 };
    try std.testing.expectEqual(@as(usize, 0), shortestSubarraySumAtLeast(&nums, 100));
}

test "target zero: empty-threshold degenerate, any single element works" {
    const nums = [_]u32{ 3, 1 };
    try std.testing.expectEqual(@as(usize, 1), shortestSubarraySumAtLeast(&nums, 0));
}

test "stress: matches the O(n^2) oracle2" {
    var prng = std.Random.DefaultPrng.init(0xA1509);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 60) : (round += 1) {
        const n = r.intRangeAtMost(usize, 0, 120);
        const buf = try alloc.alloc(u32, n);
        defer alloc.free(buf);
        for (buf) |*x| x.* = r.intRangeAtMost(u32, 0, 20);
        const target = r.intRangeAtMost(u64, 1, 120);
        try std.testing.expectEqual(naiveShortest(buf, target), shortestSubarraySumAtLeast(buf, target));
    }
}
