package main

type Pair struct {
	a, b int
}

func binarySearch(arr []int, target int) Pair {
	low, high := 0, len(arr)-1

	for low <= high {
		mid := low + (high-low)/2
		if arr[mid] == target {
			return  Pair{a: mid, b: arr[mid]}
		} else if arr[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return Pair{a: -1, b: -1}
}
