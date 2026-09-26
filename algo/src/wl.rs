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

use std::collections::{HashMap, HashSet, VecDeque};

/// Minimum number of one-letter steps from `begin` to `end` using only
/// dictionary `words` for intermediates and the end. 0 if unreachable.
/// All words have the same length and are lowercase a–z.
pub fn ladder_length(begin: &str, end: &str, words: &[&str]) -> usize {
    if begin == end {
        return 0;
    }
    let mut path =
        HashMap::<String, Vec<&str>>::from_iter(words.iter().map(|&w| (w.to_string(), Vec::new())));

    for &w in words {
        for i in 0..w.len() {
            let mut b = w.as_bytes().to_vec();
            b[i] = b'*';
            path.entry(String::from_utf8(b).unwrap())
                .or_default()
                .push(w);
        }
    }
    println!("path: {:#?}", path);
    let mut visited: HashSet<&str> = HashSet::new();
    visited.insert(begin);
    let mut queue: VecDeque<(&str, usize)> = VecDeque::new();
    queue.push_back((begin, 0));

    while let Some((cur, d)) = queue.pop_front() {
        for i in 0..cur.len() {
            let mut b = cur.as_bytes().to_vec();
            b[i] = b'*';
            let key = String::from_utf8(b).unwrap();
            let Some(bucket) = path.get(&key) else {
                continue;
            };
            for &w in bucket {
                if w == end {
                    return d + 1;
                }
                if visited.insert(w) {
                    queue.push_back((w, d + 1));
                }
            }
        }
    }

    0
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::prng::Rng;
    use std::collections::HashMap;

    /// True if a and b have equal length and differ in exactly one position.
    fn differ_by_one(a: &str, b: &str) -> bool {
        if a.len() != b.len() {
            return false;
        }
        let mut diff = 0;
        for (x, y) in a.bytes().zip(b.bytes()) {
            if x != y {
                diff += 1;
            }
            if diff > 1 {
                return false;
            }
        }
        diff == 1
    }

    /// Independent oracle: plain BFS over pairwise differ-by-one edges.
    fn oracle_ladder(begin: &str, end: &str, words: &[&str]) -> usize {
        if begin == end {
            return 0;
        }

        let mut dist: HashMap<&str, usize> = HashMap::new();
        let mut queue: Vec<&str> = Vec::new();

        dist.insert(begin, 0);
        queue.push(begin);
        let mut head = 0;
        while head < queue.len() {
            let cur = queue[head];
            head += 1;
            let d = dist[cur];
            for &w in words {
                if !differ_by_one(cur, w) {
                    continue;
                }
                if dist.contains_key(w) {
                    continue;
                }
                if w == end {
                    return d + 1;
                }
                dist.insert(w, d + 1);
                queue.push(w);
            }
        }
        0
    }

    #[test]
    fn example_from_the_study_page_cold_warm_in_4_steps() {
        let words = [
            "cold", "gold", "cord", "sold", "card", "ward", "warm", "tard",
        ];
        let got = ladder_length("cold", "warm", &words);
        assert_eq!(got, 4);
    }

    #[test]
    fn unreachable_end_word_0() {
        let words = ["hot", "dot", "dog"];
        assert_eq!(ladder_length("hit", "cog", &words), 0);
    }

    #[test]
    fn begin_equals_end_0_steps() {
        let words = ["abc"];
        assert_eq!(ladder_length("abc", "abc", &words), 0);
    }

    #[test]
    fn direct_neighbor_in_dictionary_1_step() {
        let words = ["cat"];
        assert_eq!(ladder_length("bat", "cat", &words), 1);
    }

    #[test]
    fn stress_random_small_dictionaries_match_bfs_oracle() {
        let mut r = Rng::new(0x1ADDE220);

        // Words of length 3 over {a, b, c}: dense enough for real ladders.
        const WORD_LEN: usize = 3;
        fn random_word(r: &mut Rng) -> String {
            (0..WORD_LEN)
                .map(|_| (b'a' + r.range_i32(0, 2) as u8) as char)
                .collect()
        }

        for _ in 0..30 {
            let n_words = r.range_usize(1, 15);
            let storage: Vec<String> = (0..n_words).map(|_| random_word(&mut r)).collect();
            let words: Vec<&str> = storage.iter().map(String::as_str).collect();
            let begin = random_word(&mut r);
            let end = random_word(&mut r);

            let want = oracle_ladder(&begin, &end, &words);
            let got = ladder_length(&begin, &end, &words);
            assert_eq!(got, want);
            // Relationship: a chain uses at most all dictionary words.
            assert!(got <= n_words + 1);
        }
    }
}
