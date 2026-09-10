//! Given a string `original` and a string `check`, find the starting index
//! of all substrings in `original` that are anagrams of `check`. Return the
//! indices in ascending order.
//!
//! Examples (from the study page):
//!   original = "cbaebabacd", check = "abc" → [0, 6]
//!     ("cba" and "bac" contain exactly the letters of "abc")
//!   original = "abab", check = "ab" → [0, 1, 2]
//!     (every length-2 window of "abab" is an anagram of "ab")
//!
//! Constraints: 1 <= len(original), len(check) <= 10^5; lowercase a–z only.
//!
//! Requirements
//! - O(n) time: fixed window of len(check), update two [26] count tables
//!   (or one table + a matched-letters counter) incrementally. Do NOT
//!   re-count 26 letters per slide if you take the counter route — but a
//!   26-entry compare per slide is acceptable (26 is a constant).
//! - Caller owns and frees the returned slice.

const std = @import("std");

pub fn findAnagrams(alloc: std.mem.Allocator, s: []const u8, p: []const u8) ![]usize {
    const check_len = p.len;
    const s_len = s.len;
    if (check_len > s_len) return alloc.alloc(usize, 0);
    var out: std.ArrayList(usize) = .empty;
    errdefer out.deinit(alloc);
    var window: [26]i32 = @splat(0);
    var check: [26]i32 = @splat(0);

    // needs to add the zero
    for (p) |c| {
        check[c - 'a'] += 1;
        window[c - 'a'] += 1;
    }
    if (window == check) {
        try out.append(alloc, 0);
    }

    for (s_len - check_len) |i| {
        const out_char = s[i];
        const in_char = s[i + check_len];
        window[out_char - 'a'] -= 1;
        window[in_char - 'a'] += 1;
        if (window == check) {
            try out.append(alloc, i + 1);
        }
    }

    return out.toOwnedSlice(alloc);
}

/// True iff `a` and `b` are anagrams (lowercase a-z), by counting.
fn isAnagram(a: []const u8, b: []const u8) bool {
    if (a.len != b.len) return false;
    var counts: [26]i32 = @splat(0);
    for (a) |c| counts[c - 'a'] += 1;
    for (b) |c| counts[c - 'a'] -= 1;
    for (counts) |v| {
        if (v != 0) return false;
    }
    return true;
}

/// Naive O(n·m) oracle: test every window with a fresh count.
fn naiveFindAnagrams(alloc: std.mem.Allocator, s: []const u8, p: []const u8) ![]usize {
    var out: std.ArrayList(usize) = .empty;
    errdefer out.deinit(alloc);
    if (p.len <= s.len) {
        var i: usize = 0;
        while (i + p.len <= s.len) : (i += 1) {
            if (isAnagram(s[i .. i + p.len], p)) try out.append(alloc, i);
        }
    }
    return out.toOwnedSlice(alloc);
}

// ── Tests (the spec) ────────────────────────────────────────────────────────

test "study page example 1" {
    const alloc = std.testing.allocator;
    const got = try findAnagrams(alloc, "cbaebabacd", "abc");
    defer alloc.free(got);
    try std.testing.expectEqualSlices(usize, &[_]usize{ 0, 6 }, got);
}

test "study page example 2" {
    const alloc = std.testing.allocator;
    const got = try findAnagrams(alloc, "abab", "ab");
    defer alloc.free(got);
    try std.testing.expectEqualSlices(usize, &[_]usize{ 0, 1, 2 }, got);
}

test "no matches" {
    const alloc = std.testing.allocator;
    const got = try findAnagrams(alloc, "aaaa", "b");
    defer alloc.free(got);
    try std.testing.expectEqual(@as(usize, 0), got.len);
}

test "check longer than original: no windows" {
    const alloc = std.testing.allocator;
    const got = try findAnagrams(alloc, "ab", "abc");
    defer alloc.free(got);
    try std.testing.expectEqual(@as(usize, 0), got.len);
}

test "whole string is the single anagram" {
    const alloc = std.testing.allocator;
    const got = try findAnagrams(alloc, "bca", "abc");
    defer alloc.free(got);
    try std.testing.expectEqualSlices(usize, &[_]usize{0}, got);
}

test "stress: matches the naive per-window counting oracle" {
    var prng = std.Random.DefaultPrng.init(0xA1510);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 60) : (round += 1) {
        const n = r.intRangeAtMost(usize, 1, 80);
        const m = r.intRangeAtMost(usize, 1, 8);
        const s = try alloc.alloc(u8, n);
        defer alloc.free(s);
        const p = try alloc.alloc(u8, m);
        defer alloc.free(p);
        // 3-letter alphabet keeps anagram hits common.
        for (s) |*c| c.* = 'a' + r.intRangeLessThan(u8, 0, 3);
        for (p) |*c| c.* = 'a' + r.intRangeLessThan(u8, 0, 3);

        const expected = try naiveFindAnagrams(alloc, s, p);
        defer alloc.free(expected);
        const got = try findAnagrams(alloc, s, p);
        defer alloc.free(got);
        try std.testing.expectEqualSlices(usize, expected, got);
    }
}
