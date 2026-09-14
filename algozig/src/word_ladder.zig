//! Given a start word, an end word, and a dictionary of words (all the same
//! length, lowercase a–z), find the minimum number of STEPS to go from start
//! to end, where each step changes exactly one letter and every intermediate
//! word (and the end word) must be in the dictionary. Return 0 if the end
//! word is unreachable.
//!
//! Example (study page):
//!   start = "cold", end = "warm"
//!   words = ["cold","gold","cord","sold","card","ward","warm","tard"]
//!   Output: 4   (cold → cord → card → ward → warm is 4 steps/edges)
//!
//! Convention: begin == end → 0. The step count is the number of EDGES on
//! the shortest chain.
//!
//! Requirements
//! - BFS from the start word; O(n · L · 26) neighbor generation or O(n² · L)
//!   pairwise comparison — either is fine at study scale, but know which
//!   you're writing.
//! - Use `alloc` for the queue / visited set; free everything (tests run
//!   under the leak-checking allocator).

const std = @import("std");

/// Minimum number of one-letter steps from `begin` to `end` using only
/// dictionary `words` for intermediates and the end. 0 if unreachable.
/// All words have the same length and are lowercase a–z.
pub fn ladderLength(
    alloc: std.mem.Allocator,
    begin: []const u8,
    end: []const u8,
    words: []const []const u8,
) !usize {
    _ = alloc;
    _ = begin;
    _ = end;
    _ = words;
    @panic("TODO: implement");
}

/// True if a and b have equal length and differ in exactly one position.
fn differByOne(a: []const u8, b: []const u8) bool {
    if (a.len != b.len) return false;
    var diff: usize = 0;
    for (a, b) |x, y| {
        if (x != y) diff += 1;
        if (diff > 1) return false;
    }
    return diff == 1;
}

/// Independent oracle: plain BFS over pairwise differ-by-one edges.
fn oracleLadder(
    alloc: std.mem.Allocator,
    begin: []const u8,
    end: []const u8,
    words: []const []const u8,
) !usize {
    if (std.mem.eql(u8, begin, end)) return 0;

    var dist: std.StringHashMap(usize) = .init(alloc);
    defer dist.deinit();
    var queue: std.ArrayList([]const u8) = .empty;
    defer queue.deinit(alloc);

    try dist.put(begin, 0);
    try queue.append(alloc, begin);
    var head: usize = 0;
    while (head < queue.items.len) : (head += 1) {
        const cur = queue.items[head];
        const d = dist.get(cur).?;
        for (words) |w| {
            if (!differByOne(cur, w)) continue;
            if (dist.contains(w)) continue;
            if (std.mem.eql(u8, w, end)) return d + 1;
            try dist.put(w, d + 1);
            try queue.append(alloc, w);
        }
    }
    return 0;
}

test "example from the study page: cold → warm in 4 steps" {
    const alloc = std.testing.allocator;
    const words = [_][]const u8{ "cold", "gold", "cord", "sold", "card", "ward", "warm", "tard" };
    const got = try ladderLength(alloc, "cold", "warm", &words);
    try std.testing.expectEqual(@as(usize, 4), got);
}

test "unreachable end word → 0" {
    const alloc = std.testing.allocator;
    const words = [_][]const u8{ "hot", "dot", "dog" };
    try std.testing.expectEqual(@as(usize, 0), try ladderLength(alloc, "hit", "cog", &words));
}

test "begin equals end → 0 steps" {
    const alloc = std.testing.allocator;
    const words = [_][]const u8{"abc"};
    try std.testing.expectEqual(@as(usize, 0), try ladderLength(alloc, "abc", "abc", &words));
}

test "direct neighbor in dictionary → 1 step" {
    const alloc = std.testing.allocator;
    const words = [_][]const u8{"cat"};
    try std.testing.expectEqual(@as(usize, 1), try ladderLength(alloc, "bat", "cat", &words));
}

test "stress: random small dictionaries match BFS oracle" {
    var prng = std.Random.DefaultPrng.init(0x1ADDE220);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 30) : (round += 1) {
        // Words of length 3 over {a, b, c}: dense enough for real ladders.
        const word_len = 3;
        const n_words = r.intRangeAtMost(usize, 1, 15);
        var storage = try alloc.alloc(u8, n_words * word_len);
        defer alloc.free(storage);
        var words = try alloc.alloc([]const u8, n_words);
        defer alloc.free(words);
        for (0..n_words) |i| {
            const w = storage[i * word_len ..][0..word_len];
            for (w) |*ch| ch.* = 'a' + r.intRangeAtMost(u8, 0, 2);
            words[i] = w;
        }
        var begin: [word_len]u8 = undefined;
        var end: [word_len]u8 = undefined;
        for (&begin) |*ch| ch.* = 'a' + r.intRangeAtMost(u8, 0, 2);
        for (&end) |*ch| ch.* = 'a' + r.intRangeAtMost(u8, 0, 2);

        const want = try oracleLadder(alloc, &begin, &end, words);
        const got = try ladderLength(alloc, &begin, &end, words);
        try std.testing.expectEqual(want, got);
        // Relationship: a chain uses at most all dictionary words.
        try std.testing.expect(got <= n_words + 1);
    }
}
