const std = @import("std");
const Io = std.Io;
const removeDuplicates = @import("duplicate.zig").removeDuplicates;
const twoSumSorted = @import("two.zig").twoSumSorted;
const isPalindrome = @import("palindrome.zig").isPalindrome;
const longestNoRepeat = @import("substring_nor.zig").longestNoRepeat;
const longestSubarraySumAtMost = @import("subarray_sum_long.zig").longestSubarraySumAtMost;

const algozig = @import("algozig");

pub fn main(_: std.process.Init) !void {
    const nums = [_]u32{ 5, 9, 7 };
    try std.testing.expectEqual(@as(usize, 0), longestSubarraySumAtMost(&nums, 4));
}
