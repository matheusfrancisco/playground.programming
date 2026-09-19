const std = @import("std");

pub const TreeNode = struct {
    val: i32,
    left: ?*TreeNode = null,
    right: ?*TreeNode = null,
};

fn sameTree(a: ?*const TreeNode, b: ?*const TreeNode) bool {
    if (a == null and b == null) return true;
    if (a == null or b == null) return false;
    if (a.?.val != b.?.val) return false;
    return sameTree(a.?.left, b.?.left) and sameTree(a.?.right, b.?.right);
}

/// Return true iff `sub` is a subtree of `root`: some node of `root` heads a
/// subtree with identical structure and values to `sub`. Empty `sub` → true
/// (even when `root` is empty); empty `root` with non-empty `sub` → false.
pub fn isSubtree(root: ?*const TreeNode, sub: ?*const TreeNode) bool {
    if (sub == null) return true;
    if (root == null) return false;
    if (sameTree(root, sub)) return true;
    return isSubtree(root.?.left, sub) or isSubtree(root.?.right, sub);
}

/// Build a tree from a level-order array where `null` marks a missing child.
/// Children slots are only consumed for nodes that exist (LeetCode-style).
fn buildTree(alloc: std.mem.Allocator, level: []const ?i32) !?*TreeNode {
    if (level.len == 0 or level[0] == null) return null;
    var nodes: std.ArrayList(*TreeNode) = .empty;
    defer nodes.deinit(alloc);
    const root = try alloc.create(TreeNode);
    root.* = .{ .val = level[0].? };
    try nodes.append(alloc, root);
    var head: usize = 0;
    var i: usize = 1;
    while (i < level.len and head < nodes.items.len) : (head += 1) {
        const parent = nodes.items[head];
        if (level[i]) |v| {
            const n = try alloc.create(TreeNode);
            n.* = .{ .val = v };
            parent.left = n;
            try nodes.append(alloc, n);
        }
        i += 1;
        if (i >= level.len) break;
        if (level[i]) |v| {
            const n = try alloc.create(TreeNode);
            n.* = .{ .val = v };
            parent.right = n;
            try nodes.append(alloc, n);
        }
        i += 1;
    }
    return root;
}

fn freeTree(alloc: std.mem.Allocator, node: ?*TreeNode) void {
    const n = node orelse return;
    freeTree(alloc, n.left);
    freeTree(alloc, n.right);
    alloc.destroy(n);
}

/// Insert n nodes at random positions — used by the stress test.
fn buildRandomTree(alloc: std.mem.Allocator, r: std.Random, n: usize) !?*TreeNode {
    var root: ?*TreeNode = null;
    var count: usize = 0;
    while (count < n) : (count += 1) {
        const node = try alloc.create(TreeNode);
        node.* = .{ .val = r.intRangeAtMost(i32, -50, 50) };
        if (root == null) {
            root = node;
            continue;
        }
        var cur = root.?;
        while (true) {
            if (r.boolean()) {
                if (cur.left) |l| cur = l else {
                    cur.left = node;
                    break;
                }
            } else {
                if (cur.right) |rt| cur = rt else {
                    cur.right = node;
                    break;
                }
            }
        }
    }
    return root;
}

/// Collect every node of the tree, preorder — used by the stress test to pick
/// a genuine subtree, and by the oracle below.
fn collectNodes(alloc: std.mem.Allocator, node: ?*TreeNode, out: *std.ArrayList(*TreeNode)) !void {
    const n = node orelse return;
    try out.append(alloc, n);
    try collectNodes(alloc, n.left, out);
    try collectNodes(alloc, n.right, out);
}

// Deliberately written differently from the intended solution: the equality
// check runs on an explicit stack of node pairs, not recursion, and the outer
// loop iterates a pre-collected node list. O(n·m), independent logic.

fn oracleSame(alloc: std.mem.Allocator, a0: ?*const TreeNode, b0: ?*const TreeNode) !bool {
    const Pair = struct { a: ?*const TreeNode, b: ?*const TreeNode };
    var stack: std.ArrayList(Pair) = .empty;
    defer stack.deinit(alloc);
    try stack.append(alloc, .{ .a = a0, .b = b0 });
    while (stack.pop()) |p| {
        const a = p.a orelse {
            if (p.b != null) return false;
            continue;
        };
        const b = p.b orelse return false;
        if (a.val != b.val) return false;
        try stack.append(alloc, .{ .a = a.left, .b = b.left });
        try stack.append(alloc, .{ .a = a.right, .b = b.right });
    }
    return true;
}

fn oracleIsSubtree(alloc: std.mem.Allocator, root: ?*TreeNode, sub: ?*const TreeNode) !bool {
    if (sub == null) return true;
    var nodes: std.ArrayList(*TreeNode) = .empty;
    defer nodes.deinit(alloc);
    try collectNodes(alloc, root, &nodes);
    for (nodes.items) |n| {
        if (try oracleSame(alloc, n, sub)) return true;
    }
    return false;
}

test "example from the study page: [3,4,5,1,2] contains [4,1,2]" {
    const alloc = std.testing.allocator;
    const root = try buildTree(alloc, &[_]?i32{ 3, 4, 5, 1, 2 });
    defer freeTree(alloc, root);
    const sub = try buildTree(alloc, &[_]?i32{ 4, 1, 2 });
    defer freeTree(alloc, sub);
    try std.testing.expect(isSubtree(root, sub));

    // A tree that appears nowhere in root.
    const absent = try buildTree(alloc, &[_]?i32{ 4, 2, 1 });
    defer freeTree(alloc, absent);
    try std.testing.expect(!isSubtree(root, absent));
}

test "empty-sub convention: empty tree is a subtree of anything" {
    const alloc = std.testing.allocator;
    const root = try buildTree(alloc, &[_]?i32{ 1, 2, 3 });
    defer freeTree(alloc, root);
    try std.testing.expect(isSubtree(root, null));
    try std.testing.expect(isSubtree(null, null));
    // ...but a non-empty sub is never inside an empty root.
    const sub = try buildTree(alloc, &[_]?i32{7});
    defer freeTree(alloc, sub);
    try std.testing.expect(!isSubtree(null, sub));
}

test "values match but structure differs: extra leaf under a candidate" {
    const alloc = std.testing.allocator;
    // Node 4 matches sub's root value and has children 1 and 2 — but 2 grew
    // an extra leaf 0, so no node of root heads an exact copy of sub.
    const root = try buildTree(alloc, &[_]?i32{ 3, 4, 5, 1, 2, null, null, null, null, 0 });
    defer freeTree(alloc, root);
    const sub = try buildTree(alloc, &[_]?i32{ 4, 1, 2 });
    defer freeTree(alloc, sub);
    try std.testing.expect(!isSubtree(root, sub));
}

test "duplicate values: first sameTree failure must not stop the search" {
    const alloc = std.testing.allocator;
    // Root is 4 → (left) 4 → children 1, 2. The TOP node matches sub's root
    // value yet fails sameTree; the real match sits one level below.
    const root = try buildTree(alloc, &[_]?i32{ 4, 4, null, 1, 2 });
    defer freeTree(alloc, root);
    const sub = try buildTree(alloc, &[_]?i32{ 4, 1, 2 });
    defer freeTree(alloc, sub);
    try std.testing.expect(isSubtree(root, sub));

    // Degenerate left chain 5 → 4 → 3: its suffix is a subtree, the mirrored
    // right chain is not.
    const chain = try buildTree(alloc, &[_]?i32{ 5, 4, null, 3, null });
    defer freeTree(alloc, chain);
    const suffix = try buildTree(alloc, &[_]?i32{ 4, 3, null });
    defer freeTree(alloc, suffix);
    try std.testing.expect(isSubtree(chain, suffix));
    const mirrored = try buildTree(alloc, &[_]?i32{ 4, null, 3 });
    defer freeTree(alloc, mirrored);
    try std.testing.expect(!isSubtree(chain, mirrored));
}

test "stress: matches try-from-every-node oracle on random trees" {
    var prng = std.Random.DefaultPrng.init(0x516B0416);
    const r = prng.random();
    const alloc = std.testing.allocator;

    var round: usize = 0;
    while (round < 60) : (round += 1) {
        const n = r.intRangeAtMost(usize, 0, 40);
        const root = try buildRandomTree(alloc, r, n);
        defer freeTree(alloc, root);
        if (n > 0 and r.boolean()) {
            // A node picked from root itself heads a genuine subtree → true.
            var nodes: std.ArrayList(*TreeNode) = .empty;
            defer nodes.deinit(alloc);
            try collectNodes(alloc, root, &nodes);
            const pick = nodes.items[r.intRangeAtMost(usize, 0, nodes.items.len - 1)];
            try std.testing.expect(isSubtree(root, pick));
        } else {
            const m = r.intRangeAtMost(usize, 0, 6);
            const sub = try buildRandomTree(alloc, r, m);
            defer freeTree(alloc, sub);
            const want = try oracleIsSubtree(alloc, root, sub);
            try std.testing.expectEqual(want, isSubtree(root, sub));
        }
    }
}
