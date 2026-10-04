fn build_binary_heap(arr: &[i32]) -> Vec<i32> {
    let mut heap = Vec::new();
    for i in 0..arr.len() {
        insert_into_heap(&mut heap, arr[i]);
    }
    heap
}

fn insert_into_heap(heap: &mut Vec<i32>, value: i32) {
    heap.push(value);
    let mut index = heap.len() - 1;
    while index > 0 && heap[index] < heap[(index - 1) / 2] {
        heap.swap(index, (index - 1) / 2);
        index = (index - 1) / 2;
    }
}

fn remove_min_from_bheap(heap: &mut Vec<i32>) -> Option<i32> {
    if heap.is_empty() {
        return None;
    }

    let min_value = heap[0];
    heap[0] = heap[heap.len() - 1];
    heap.pop();
    let mut index = 0;
    let n = heap.len();
    while 2 * index + 1 < n {
        let left = 2 * index + 1;
        let right = 2 * index + 2;
        let mut smallest = left;

        if right < n && heap[right] < heap[left] {
            smallest = right;
        }

        if heap[index] <= heap[smallest] {
            break;
        }

        heap.swap(index, smallest);
        index = smallest;
    }
    Some(min_value)
}

fn heapsort(arr: &mut Vec<i32>) {
    let mut heap = build_binary_heap(arr);
    for i in 0..arr.len() {
        let item = remove_min_from_bheap(&mut heap);
        if let Some(value) = item {
            arr[i] = value;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_build_binary_heap() {
        let arr = [3, 1, 4, 1, 5, 9, 2, 6, 5];
        let heap = build_binary_heap(&arr);
        assert_eq!(heap[0], 1); // The smallest element should be at the root
        for i in 1..heap.len() {
            assert!(heap[i] >= heap[(i - 1) / 2]); // Each child should be greater than or equal to its parent
        }
        println!("Heap: {:?}", heap);

        let min = remove_min_from_bheap(&mut heap.clone());
        assert_eq!(min, Some(1)); // The smallest element should be removed

        let new_min = remove_min_from_bheap(&mut heap.clone());
        assert_eq!(new_min, Some(1)); // The next smallest element should be removed

        let mut arr_to_sort = vec![3, 1, 4, 1, 5, 9, 2, 6, 5];
        heapsort(&mut arr_to_sort);
        assert_eq!(arr_to_sort, vec![1, 1, 2, 3, 4, 5, 5, 6, 9]);
    }
}

