package arrays

import "fmt"

func Arrays() {
	fmt.Println("Arrays in Go!")
	// this is arrays study
	var arr = [5]int{1, 2, 3, 4, 5}
	var i int
	for i = 0; i < len(arr); i++ {
		fmt.Printf("%v \n", arr[i])
	}
}
