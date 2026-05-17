pub fn move_zeroes(arr: &mut Vec<i32>) {
    let mut slow = 0;

    for f in 0..arr.len() {
        if arr[f] != 0 {
            // swap
            let aux = arr[f];
            arr[f] = arr[slow];
            arr[slow] = aux;
            // or arr.swap(f, slow);
            slow += 1;
        }
    }
}

#[cfg(test)]
mod tests {

    #[test]
    fn test_move_zeroes() {
        let mut arr = vec![0, 1, 0, 3, 12];
        let expected = vec![1, 3, 12, 0, 0];
        super::move_zeroes(&mut arr);
        assert_eq!(arr, expected);

        let mut arr = vec![0];
        let expected = vec![0];
        super::move_zeroes(&mut arr);
        assert_eq!(arr, expected);

        let mut arr = vec![1];
        let expected = vec![1];
        super::move_zeroes(&mut arr);
        assert_eq!(arr, expected);

        let mut arr = vec![0, 0, 0];
        let expected = vec![0, 0, 0];
        super::move_zeroes(&mut arr);
        assert_eq!(arr, expected);

        let mut arr = vec![1, 2, 3];
        let expected = vec![1, 2, 3];
        super::move_zeroes(&mut arr);
        assert_eq!(arr, expected);
    }
}
