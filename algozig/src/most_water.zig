//! Problem
//! -------
//! You are given an array `height` where height[i] is the height of a
//! vertical bar at position i. All bars are spaced one unit apart. Two bars
//! and the x-axis form a container; the amount of water it holds is
//! (j - i) × min(height[i], height[j]) — width times the shorter bar,
//! since water spills over the shorter side.
//! Find the pair of bars that holds the most water; return that area.
//!
//! Example: [1, 8, 6, 2, 5, 4, 8, 3, 7] → 49
//! (bars at index 1 and 8: width 7, shorter height 7, area 49).
//!
//! Requirements
//! ------------
//! - O(n) time, O(1) extra space.
//! - Heights are non-negative; fewer than 2 bars → area 0.
//! - Return i64 (width × height can exceed i32 for large inputs).
//!
//! Design questions (answer on paper BEFORE coding)
//! ------------------------------------------------
//! 1. State the loop invariant in ONE sentence: what claim holds about
//!    every pair already ELIMINATED when left/right have moved inward?
//! 2. When you move the SHORTER side inward, prove no discarded pair could
//!    have beaten the current best. Why does moving the taller side lose
//!    that guarantee?
//! 3. If both sides are equal height, does it matter which one you move?
//! 4. Why is greedy-by-height correct here but the same idea fails for
//!    Trapping Rain Water? What differs about the objective?
//!
//! Ritual: invariant sentence on paper → code → run `zig build p04` →
//! if stuck >45 min, write down WHERE it breaks, then open the source page.

const std = @import("std");

pub fn maxArea(height: []const i32) i64 {
    if (height.len < 2) return 0;
    var max: i64 = 0;
    var i: usize = 0;
    var j: usize = height.len - 1;
    while (i < j) {
        const shorter: i64 = @min(height[i], height[j]);
        const width: i64 = @intCast(j - i);
        max = @max(max, width * shorter);
        if (height[i] < height[j]) {
            i += 1;
        } else {
            j -= 1;
        }
    }
    return max;
}

/// Naive O(n²) all-pairs oracle.
fn naiveMaxArea(height: []const i32) i64 {
    var best: i64 = 0;
    for (height, 0..) |hi, i| {
        var j: usize = i + 1;
        while (j < height.len) : (j += 1) {
            const shorter: i64 = @min(hi, height[j]);
            const width: i64 = @intCast(j - i);
            best = @max(best, width * shorter);
        }
    }
    return best;
}

// ── Tests (the spec) ────────────────────────────────────────────────────────
test "example from the study page" {
    const height = [_]i32{ 1, 8, 6, 2, 5, 4, 8, 3, 7 };
    try std.testing.expectEqual(@as(i64, 49), maxArea(&height));
}

test "two bars only" {
    const height = [_]i32{ 5, 9 };
    try std.testing.expectEqual(@as(i64, 5), maxArea(&height));
}

test "degenerate: fewer than two bars holds nothing" {
    try std.testing.expectEqual(@as(i64, 0), maxArea(&[_]i32{}));
    try std.testing.expectEqual(@as(i64, 0), maxArea(&[_]i32{7}));
}

test "all zero heights" {
    const height = [_]i32{ 0, 0, 0, 0 };
    try std.testing.expectEqual(@as(i64, 0), maxArea(&height));
}

test "monotonic ramp: best pair is not always the extremes" {
    const height = [_]i32{ 1, 2, 3, 4, 5 };
    try std.testing.expectEqual(naiveMaxArea(&height), maxArea(&height));
}

test "stress: matches the O(n^2) all-pairs oracle" {
    var prng = std.Random.DefaultPrng.init(0xA1504);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 50) : (round += 1) {
        const n = r.intRangeAtMost(usize, 0, 120);
        const buf = try alloc.alloc(i32, n);
        defer alloc.free(buf);
        for (buf) |*h| h.* = r.intRangeAtMost(i32, 0, 1000);
        try std.testing.expectEqual(naiveMaxArea(buf), maxArea(buf));
    }
}
