const std = @import("std");
const Io = std.Io;
const removeDuplicates = @import("duplicate.zig").removeDuplicates;
const twoSumSorted = @import("two.zig").twoSumSorted;
const isPalindrome = @import("palindrome.zig").isPalindrome;
const longestNoRepeat = @import("substring_nor.zig").longestNoRepeat;
const longestSubarraySumAtMost = @import("subarray_sum_long.zig").longestSubarraySumAtMost;
const countIslands = @import("number_of_islands.zig").countIslands;

const algozig = @import("algozig");

pub fn main(_: std.process.Init) !void {
    var gpa = std.heap.DebugAllocator(.{}){};
    defer _ = gpa.deinit();
    const alloc = gpa.allocator();
    //            0123456
    const grid = "1010101";
    //countIslands: cell = 1, start = 0, visited[start] = false
    //countIslands: found new island at start = 0
    //countIslands: visiting idx = 0, r = 0, c = 0
    //countIslands: cell = 0, start = 1, visited[start] = false
    //countIslands: cell = 1, start = 2, visited[start] = false
    //countIslands: found new island at start = 2
    //countIslands: visiting idx = 2, r = 0, c = 2
    //countIslands: cell = 0, start = 3, visited[start] = false
    //countIslands: cell = 1, start = 4, visited[start] = false
    //countIslands: found new island at start = 4
    //countIslands: visiting idx = 4, r = 0, c = 4
    //countIslands: cell = 0, start = 5, visited[start] = false
    //countIslands: cell = 1, start = 6, visited[start] = false
    //countIslands: found new island at start = 6
    //countIslands: visiting idx = 6, r = 0, c = 6
    //
    //countIslands: found new island at start = 0
    //countIslands: visiting idx = 0, r = 0, c = 0
    //countIslands: queue = { 0 }
    //countIslands: found new island at start = 2
    //countIslands: visiting idx = 2, r = 0, c = 2
    //countIslands: queue = { 2 }
    //countIslands: found new island at start = 4
    //countIslands: visiting idx = 4, r = 0, c = 4
    //countIslands: queue = { 4 }
    //countIslands: found new island at start = 6
    //countIslands: visiting idx = 6, r = 0, c = 6
    //countIslands: queue = { 6 }
    //expected 3, found 4
    try std.testing.expectEqual(@as(usize, 4), try countIslands(alloc, grid, 1, 7));
}
