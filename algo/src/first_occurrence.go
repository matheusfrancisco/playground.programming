package main


// sorted arr with duplicates find the first occurrence of the target element
func findFirstOccurrence(arr []int, target int) int {
	low, high := 0, len(arr)-1

	f := -1
	for low <= high {
		mid := low + (high-low)/2
		if arr[mid] == target {
			f = mid
			high = mid - 1
		} else if arr[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return f
}
