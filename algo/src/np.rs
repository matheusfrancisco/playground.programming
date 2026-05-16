// feasible(T, times, k)
// workers_used = 1;
// current_time = 0;
// for t in times:
//    if current_time + t >= T:
//      workers_used += 1;
//      current_time = 0;
//    else:
//      current_time += t;
// return workers_used <= k;

use core::num;

fn feasible(T: i32, times: &[i32], k: i32) -> bool {
    let mut workers_used = 1;
    let mut current_time = 0;

    for &t in times {
        if t > T {
            return false; // If any single task exceeds T, it's not feasible
        }
        if current_time + t > T {
            workers_used += 1;
            current_time = t; // Start a new worker with the current task
        } else {
            current_time += t; // Continue with the current worker
        }
    }

    workers_used <= k
}

fn newspapers_split(np: Vec<i32>, number_workers: i32) -> i32 {
    let mut lo = 0;
    let mut hi = np.iter().sum();

    while lo < hi {
        let mid = lo + (hi - lo) / 2;
        if feasible(mid, &np, number_workers) {
            hi = mid; // Try to find a smaller maximum
        } else {
            lo = mid + 1; // Increase the maximum
        }
    }

    lo
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_newspapers_split() {
        let np = vec![1, 2, 3, 4, 5];
        let times = 2;
        assert_eq!(newspapers_split(np, times), 9); // One worker takes [1,2,3] and the other takes [4,5]

        let np = vec![7, 2, 5, 10, 8];
        let times = 2;
        assert_eq!(newspapers_split(np, times), 18); // One worker takes [7,2,5] and the other takes [10,8]
        //
    }
}
