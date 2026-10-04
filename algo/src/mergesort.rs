fn merge(a: &[usize], b: &[usize]) -> Vec<usize> {
    let mut result = Vec::with_capacity(a.len() + b.len());
    let mut i = 0;
    let mut j = 0;

    while i < a.len() && j < b.len() {
        if a[i] <= b[j] {
            result.push(a[i]);
            i += 1;
        } else {
            result.push(b[j]);
            j += 1;
        }
    }

    while i < a.len() {
        result.push(a[i]);
        i += 1;
    }

    while j < b.len() {
        result.push(b[j]);
        j += 1;
    }

    result
}

fn mergesort(arr: &[usize]) -> Vec<usize> {
    let n = arr.len();
    if n <= 1 {
        return arr.to_vec();
    }

    let a = mergesort(&arr[..n / 2]);
    let b = mergesort(&arr[n / 2..]);
    merge(&a, &b)
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::prng::Rng;

    #[test]
    fn test_mergesort() {
        let arr = [38, 27, 43, 3, 9, 82, 10];
        let arr = mergesort(&arr);

        assert_eq!(arr, [3, 9, 10, 27, 38, 43, 82]);
    }
}
