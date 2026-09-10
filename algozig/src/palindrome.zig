//! Determine whether a string is a palindrome, ignoring non-alphanumeric
//! characters and case.
//!
//! Examples (from the study page):
//!   "Do geese see God?"          → true
//!   "Was it a car or a cat I saw?" → true
//!   "A brown fox jumping over"   → false
//!
//! Requirements
//! - O(n) time, O(1) extra space. No allocation, no filtered copy.
//! - Use std.ascii for classification (isAlphanumeric / toLower).
//!

const std = @import("std");

pub fn isPalindrome(s: []const u8) bool {
    if (s.len == 0 or s.len == 1) return true;

    var lo: usize = 0;
    var hi: usize = s.len - 1;

    while (lo < hi) {
        const loChar = s[lo];
        if (!std.ascii.isAlphanumeric(loChar)) {
            lo += 1;
            continue;
        }
        const hiChar = s[hi];
        if (!std.ascii.isAlphanumeric(hiChar)) {
            hi -= 1;
            continue;
        }
        if (std.ascii.toLower(loChar) != std.ascii.toLower(hiChar)) {
            return false;
        }
        lo += 1;
        hi -= 1;
    }

    return true;
}

/// Naive O(n) time / O(n) space oracle: filter to lowercase alphanumerics,
/// then compare the copy against its reverse.
fn naiveIsPalindrome(alloc: std.mem.Allocator, s: []const u8) !bool {
    var filtered: std.ArrayList(u8) = .empty;
    defer filtered.deinit(alloc);
    for (s) |c| {
        if (std.ascii.isAlphanumeric(c)) {
            try filtered.append(alloc, std.ascii.toLower(c));
        }
    }
    const f = filtered.items;
    var i: usize = 0;
    while (i < f.len / 2) : (i += 1) {
        if (f[i] != f[f.len - 1 - i]) return false;
    }
    return true;
}

test "examples from the study page" {
    try std.testing.expect(isPalindrome("Do geese see God?"));
    try std.testing.expect(isPalindrome("Was it a car or a cat I saw?"));
    try std.testing.expect(!isPalindrome("A brown fox jumping over"));
}

test "empty and punctuation-only strings are palindromes" {
    try std.testing.expect(isPalindrome(""));
    try std.testing.expect(isPalindrome("?!, ,"));
}

test "single character and case-insensitivity" {
    try std.testing.expect(isPalindrome("x"));
    try std.testing.expect(isPalindrome("Aa"));
    try std.testing.expect(!isPalindrome("ab"));
}

test "digits count as alphanumeric" {
    try std.testing.expect(isPalindrome("1 racecar 1"));
    try std.testing.expect(!isPalindrome("12a21b"));
}

test "stress: agrees with the filter-and-reverse oracle" {
    var prng = std.Random.DefaultPrng.init(0xA1503);
    const r = prng.random();
    const alloc = std.testing.allocator;
    const pool = "aAbB1 ,?xY";

    var round: usize = 0;
    while (round < 100) : (round += 1) {
        const n = r.intRangeAtMost(usize, 0, 40);
        const buf = try alloc.alloc(u8, n);
        defer alloc.free(buf);
        for (buf) |*c| c.* = pool[r.intRangeLessThan(usize, 0, pool.len)];
        // Half the rounds: force a palindrome by mirroring the letters.
        if (round % 2 == 0 and n > 0) {
            var i: usize = 0;
            var j: usize = n - 1;
            while (i < j) : ({
                i += 1;
                j -= 1;
            }) buf[j] = buf[i];
        }
        const expected = try naiveIsPalindrome(alloc, buf);
        try std.testing.expectEqual(expected, isPalindrome(buf));
    }
}
