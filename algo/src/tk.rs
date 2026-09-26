use std::{cmp::Reverse, collections::{BinaryHeap, HashMap}};

fn tpk(arr: Vec<i32>, k: usize) -> Vec<i32> {
    let k = k as usize;
    let mut count = HashMap::new();
    for &num in &arr {
        *count.entry(num).or_insert(0i32) += 1;
    }

    let mut heap = BinaryHeap::new();
    for (&num, &freq) in &count {
        heap.push(Reverse((freq, num)));
        if heap.len() > k {
            heap.pop();
        }
    }

    heap.into_iter().map(|Reverse((_, num))| num).collect()

}

fn min_heapfy(arr: &mut Vec<i32>, n: usize, i: usize) {
    let mut smallest = i;
    let left = 2 * i + 1;
    let right = 2 * i + 2;

    if left < n && arr[left] < arr[smallest] {
        smallest = left;
    }

    if right < n && arr[right] < arr[smallest] {
        smallest = right;
    }

    if smallest != i {
        arr.swap(i, smallest);
        min_heapfy(arr, n, smallest);
    }
}
//get an arr of unsorted items and build a max heap
// [2 8 5 3 9 1]
//  0 1 2 3 4 5
// i = floor(n/2) - 1
//
fn max_heapfy(arr: &mut Vec<(i32, i32)>, n: usize, i: usize) {
    let mut largest = i;
    let left = 2 * i + 1;
    let right = 2 * i + 2;

    if left < n && arr[left].1 > arr[largest].1 {
        largest = left;
    }

    if right < n && arr[right].1 > arr[largest].1 {
        largest = right;
    }

    if largest != i {
        arr.swap(i, largest);
        max_heapfy(arr, n, largest);
    }
}

fn max_heap(mut arr: Vec<(i32, i32)>) -> Vec<(i32, i32)> {
    let n = arr.len();

    for i in (0..n / 2).rev() {
        max_heapfy(&mut arr, n, i);
    }

    arr
}

fn topk_distinct(arr: Vec<i32>, k: usize) -> Vec<i32> {
    let mut freq_map: HashMap<i32, i32> = HashMap::new();
    for a in &arr {
        freq_map.entry(*a).and_modify(|e| *e += 1).or_insert(1);
    }

    let mut items = Vec::new();
    for i in freq_map {
        items.push((i.0, i.1));
    }

    let n = items.len();
    for i in (0..items.len() / 2).rev() {
        max_heapfy(&mut items, n, i);
    }

    let mut out = vec![];
    let mut heap_size = items.len();
    for i in 0..k {
        if heap_size == 0 {
            break;
        }
        out.push(items[0].0);
        items.swap(0, heap_size - 1); // move root to the end
        heap_size -= 1; // shrink logical heap
        max_heapfy(&mut items, heap_size, 0);
    }
    out
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_max_heap() {
        let mut arr = vec![(2, 1), (8, 2), (5, 1), (3, 1), (9, 9), (1, 1)];
        arr = max_heap(arr);
        assert_eq!(arr, vec![(9, 9), (8, 2), (5, 1), (3, 1), (2, 1), (1, 1)]);
    }

    #[test]
    fn test_topk() {
        let arr = vec![1, 2, 2, 3, 3, 3];
        let result = topk_distinct(arr, 2);
        assert_eq!(result, vec![3, 2]);
    }

    #[test]
    fn test_tk() {
        let arr = vec![1, 8, 8];
        let r = topk_distinct(arr, 1);
        assert_eq!(r, vec![8]);
    }
}
