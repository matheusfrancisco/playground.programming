//Problem: You have piles of bananas, e.g. [3, 6, 7, 11], and h hours total.
//Each hour you pick a pile and eat up to k bananas from it (if the pile has
//fewer, you eat all of them and the hour is still "spent").
//Find the minimum eating speed k that lets you finish all piles within h hours.

fn feasible(piles: &[i32], h: i32, k: i32) -> bool {
    let mut hours = 0;
    for &pile in piles {
        hours += (pile + k - 1) / k; // This is a common way to calculate the ceiling of pile/k
    }
    hours <= h
}

fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
    let mut l = 1;

    //let mut r = 0;
    //for &i in &piles {
    //    r = r.max(i);
    //}

    //let r = piles.iter().cloned().max().unwrap();
    let mut r = *piles.iter().max().unwrap();

    //    let &max = piles.iter().max().unwrap();
    //    let mut hi = max;
    //

    while l < r {
        let mid = l + (r - l) / 2;

        //for &pile in &piles {
        //    hours += (pile + mid - 1) / mid; // equivalent to ceil(pile / mid)
        //}
        if feasible(&piles, h, mid) {
            r = mid;
        } else {
            l = mid + 1;
        }
    }

    l
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_min() {
        let piles = vec![3, 6, 7, 11];
        let h = 8;
        assert_eq!(min_eating_speed(piles, h), 4);
    }
}
