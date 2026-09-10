//! Problem
//! -------
//! Find the length of the longest substring of a given string without
//! repeating characters.
//!
//! Examples (from the study page):
//!   "abccabcabcc" → 3   (longest are "abc" and "cab", both length 3)
//!   "aaaabaaa"    → 2   ("ab" is the longest, length 2)
//!
//! Requirements
//! ------------
//! - O(n) time, O(1) space: input is ASCII, so a [128]bool seen-table (or
//!   [128]usize counts) replaces a hash map.
//! - Each pointer moves forward only  no restarting the left pointer.

const std = @import("std");

/// Length of the longest substring of ASCII string `s` with all-distinct
/// characters.
pub fn longestNoRepeat(s: []const u8) usize {
    var seen: [128]bool = @splat(false);
    var best: usize = 0;
    var left: usize = 0;
    for (s, 0..) |c, right| {
        // Shrink from the left until `c` is no longer in the window.
        // std.debug.print("c: {c} -> {}, \n", .{ c, c });

        while (seen[c]) : (left += 1) seen[s[left]] = false;
        seen[c] = true;
        best = @max(best, right - left + 1);
    }
    return best;
}

/// Naive O(n²) oracle: for every start, extend until a repeat.
fn naiveLongestNoRepeat(s: []const u8) usize {
    var best: usize = 0;
    for (0..s.len) |start| {
        var seen: [128]bool = @splat(false);
        var j = start;
        while (j < s.len and !seen[s[j]]) : (j += 1) seen[s[j]] = true;
        best = @max(best, j - start);
    }
    return best;
}

test "sample 1 from the study page" {
    try std.testing.expectEqual(@as(usize, 3), longestNoRepeat("abccabcabcc"));
}

test "sample 2 from the study page" {
    try std.testing.expectEqual(@as(usize, 2), longestNoRepeat("aaaabaaa"));
}

test "empty string" {
    try std.testing.expectEqual(@as(usize, 0), longestNoRepeat(""));
}

test "all distinct characters" {
    try std.testing.expectEqual(@as(usize, 6), longestNoRepeat("abcdef"));
}

test "all identical characters" {
    try std.testing.expectEqual(@as(usize, 1), longestNoRepeat("zzzzzz"));
}

test "stress: matches the O(n^2) oracle on a small alphabet" {
    var prng = std.Random.DefaultPrng.init(0xA1507);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 100) : (round += 1) {
        const n = r.intRangeAtMost(usize, 0, 80);
        const buf = try alloc.alloc(u8, n);
        defer alloc.free(buf);
        // Small alphabet keeps repeats common.
        for (buf) |*c| c.* = 'a' + r.intRangeLessThan(u8, 0, 5);
        try std.testing.expectEqual(naiveLongestNoRepeat(buf), longestNoRepeat(buf));
    }
}
