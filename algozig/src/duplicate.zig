const std = @import("std");
const Io = std.Io;

pub fn removeDuplicates(nums: []i32) usize {
    if (nums.len == 0) return 0;

    var slow: usize = 0;
    for (0..nums.len) |fast| {
        //std.debug.print("fast: {any}, slow: {any}, nums: {any}\n", .{ fast, slow, nums });
        if (nums[fast] != nums[slow]) {
            slow += 1;
            nums[slow] = nums[fast];
        }
    }

    return slow + 1;
}

fn checkPrefixStrictlyIncreasing(nums: []const i32, k: usize) bool {
    if (k == 0) return true;
    var i: usize = 1;
    while (i < k) : (i += 1) {
        if (nums[i - 1] >= nums[i]) return false;
    }
    return true;
}

test "example from the study page" {
    var nums = [_]i32{ 0, 0, 1, 1, 1, 2, 2 };
    const k = removeDuplicates(&nums);
    try std.testing.expectEqual(@as(usize, 3), k);
    try std.testing.expectEqualSlices(i32, &[_]i32{ 0, 1, 2 }, nums[0..k]);
}

test "no duplicates: slice unchanged" {
    var nums = [_]i32{ 1, 2, 3, 4 };
    const k = removeDuplicates(&nums);
    try std.testing.expectEqual(@as(usize, 4), k);
    try std.testing.expectEqualSlices(i32, &[_]i32{ 1, 2, 3, 4 }, nums[0..k]);
}

test "all elements equal" {
    var nums = [_]i32{ 7, 7, 7, 7, 7 };
    const k = removeDuplicates(&nums);
    try std.testing.expectEqual(@as(usize, 1), k);
    try std.testing.expectEqual(@as(i32, 7), nums[0]);
}

test "empty and single-element slices" {
    var empty = [_]i32{};
    try std.testing.expectEqual(@as(usize, 0), removeDuplicates(&empty));
    var one = [_]i32{42};
    try std.testing.expectEqual(@as(usize, 1), removeDuplicates(&one));
}

test "stress: prefix invariant + count matches a hash-set oracle" {
    var prng = std.Random.DefaultPrng.init(0xA1503);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 50) : (round += 1) {
        const n = r.intRangeAtMost(usize, 0, 200);
        const buf = try alloc.alloc(i32, n);
        defer alloc.free(buf);
        // Sorted input with duplicates: nondecreasing random steps.
        var v: i32 = r.intRangeAtMost(i32, -20, 0);
        for (buf) |*slot| {
            v += r.intRangeAtMost(i32, 0, 2); // step 0 keeps duplicates common
            slot.* = v;
        }

        // Oracle: count distinct values before mutation.
        var seen = std.AutoHashMap(i32, void).init(alloc);
        defer seen.deinit();
        for (buf) |x| try seen.put(x, {});
        const distinct = seen.count();

        const k = removeDuplicates(buf);
        try std.testing.expectEqual(@as(usize, distinct), k);
        try std.testing.expect(checkPrefixStrictlyIncreasing(buf, k));
    }
}
