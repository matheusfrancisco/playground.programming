use std::cmp::Ordering;

fn binary_search<T: Ord>(arr: &[T], val: &T) -> usize {
    let mut left = 0;
    let mut right = arr.len();

    while left < right {
        let mid = left + (right - left) / 2;

        match &arr[mid] {
            x if x == val => return mid,
            x if x < val => left = mid + 1,
            _ => right = mid,
        }
    }
    usize::MAX // Not found
}

fn binary_search_<T: Ord>(arr: &[T], val: &T) -> Option<usize> {
    let mut left = 0;
    let mut right = arr.len();

    while left < right {
        let mid = left + (right - left) / 2;
        match arr[mid].cmp(val) {
            Ordering::Equal => return Some(mid),
            Ordering::Less => left = mid + 1,
            Ordering::Greater => right = mid,
        }
    }
    None
}


fn search_2d_matrix_(matrix: &[Vec<i32>], target: i32) -> bool {

    let rows = matrix.len();
    if rows == 0 {
        return false;
    }
    let cols = matrix[0].len();
    let mut left = 0;
    let mut right = rows * cols;
    while left < right {

        let mid = left + (right - left) / 2;
        let row = mid / cols;
        let col = mid - (row * cols);
        let mid_value = matrix[row][col];

        match mid_value.cmp(&target) {
            Ordering::Equal => return true,
            Ordering::Less => left = mid + 1,
            Ordering::Greater => right = mid,
        }
    }

    false

}
fn search_2d_matrix(matrix: &[Vec<i32>], target: i32) -> bool {
    if matrix.is_empty() {
        return false;
    }

    let rows = matrix.len();
    let cols = matrix[0].len();
    let mut left = 0;
    let mut right = rows * cols;

    while left < right {
        let mid = left + (right - left) / 2;
        let mid_value = matrix[mid / cols][mid % cols];

        match mid_value.cmp(&target) {
            Ordering::Equal => return true,
            Ordering::Less => left = mid + 1,
            Ordering::Greater => right = mid,
        }
    }
    false

}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_binary_search() {
        let arr = [1, 2, 3, 4, 5];
        assert_eq!(binary_search(&arr, &3), 2);
        assert_eq!(binary_search(&arr, &4), 3);
        assert_eq!(binary_search_(&arr, &4),Some(3));
        assert_eq!(binary_search(&arr, &6), usize::MAX); // Not found
    }


    #[test]
    fn search_2d_matrix_test() {
        let matrix = vec![
            vec![1, 3, 5, 7],
            vec![10, 11, 16, 20],
            vec![23, 30, 34, 60],
        ];
        assert_eq!(search_2d_matrix(&matrix, 3), true);
        assert_eq!(search_2d_matrix(&matrix, 13), false);
    }
}
