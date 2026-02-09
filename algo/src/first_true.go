package main


func firstTrue(arr []bool) int {
	low, high := 0, len(arr)-1
	for low <= high {
		mid := low + (high-low)/2
		if arr[mid] {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	if low < len(arr) && arr[low] {
		return low
	}
	return -1
}

func firstTrueBounded(arr []bool) int {
	low, high := 0, len(arr)-1
	bound := -1
	for low <= high {
		mid := low + (high-low)/2
		if arr[mid] {
			bound = mid
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	return bound
}
