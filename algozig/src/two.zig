//! Given an array of integers sorted in ascending order, find two numbers
//! that add up to a given target. Return the indices of the two numbers in
//! ascending order. You can assume elements in the array are unique and
//! there is only one solution.
//!
//! Sample Input:  [2, 3, 4, 5, 8, 11, 18], target = 8
//! Sample Output: indices 1 and 3   (3 + 5 == 8)

const std = @import("std");
pub fn twoSumSorted(nums: []const i32, target: i32) [2]usize {
    var lo: usize = 0;
    var ro: usize = nums.len - 1;
    while (lo < ro) {
        const sum = nums[lo] + nums[ro];
        if (sum == target) {
            return [2]usize{ lo, ro };
        } else if (sum < target) {
            lo += 1;
        } else {
            ro -= 1;
        }
    }
    return [2]usize{ 0, 0 };
}

fn checkAnswer(nums: []const i32, target: i32, idx: [2]usize) bool {
    if (idx[0] >= idx[1]) return false;
    if (idx[1] >= nums.len) return false;
    return nums[idx[0]] + nums[idx[1]] == target;
}

test "example from the study page" {
    const nums = [_]i32{ 2, 3, 4, 5, 8, 11, 18 };
    const idx = twoSumSorted(&nums, 8);
    try std.testing.expectEqual(@as(usize, 1), idx[0]);
    try std.testing.expectEqual(@as(usize, 3), idx[1]);
}

test "pair at the extremes" {
    const nums = [_]i32{ -5, 1, 4, 9, 20 };
    const idx = twoSumSorted(&nums, 15);
    try std.testing.expectEqual(@as(usize, 0), idx[0]);
    try std.testing.expectEqual(@as(usize, 4), idx[1]);
}

test "two-element array" {
    const nums = [_]i32{ 3, 7 };
    const idx = twoSumSorted(&nums, 10);
    try std.testing.expectEqual(@as(usize, 0), idx[0]);
    try std.testing.expectEqual(@as(usize, 1), idx[1]);
}

test "negative values" {
    const nums = [_]i32{ -8, -3, 0, 2, 6 };
    const idx = twoSumSorted(&nums, -1);
    try std.testing.expect(checkAnswer(&nums, -1, idx));
}

test "stress: planted pair is found and answer checks out" {
    var prng = std.Random.DefaultPrng.init(0xA1502);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 50) : (round += 1) {
        const n = r.intRangeAtMost(usize, 2, 100);
        const buf = try alloc.alloc(i32, n);
        defer alloc.free(buf);
        // Strictly increasing values (uniqueness required by the problem).
        var v: i32 = r.intRangeAtMost(i32, -50, 0);
        for (buf) |*slot| {
            v += r.intRangeAtMost(i32, 1, 5);
            slot.* = v;
        }
        // Plant a target from a random pair.
        const a = r.intRangeLessThan(usize, 0, n - 1);
        const b = r.intRangeAtMost(usize, a + 1, n - 1);
        const target = buf[a] + buf[b];

        // Multiple pairs may hit `target`; assert the relationship, not the
        // planted indices themselves.
        const idx = twoSumSorted(buf, target);
        try std.testing.expect(checkAnswer(buf, target, idx));
    }
}
