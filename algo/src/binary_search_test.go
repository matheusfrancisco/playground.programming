package main

import "testing"

func TestBinarySearch(t *testing.T) {
	type args struct {
		arr    []int
		target int
	}
	tests := []struct {
		name string
		args args
		want Pair
	}{
		{
			name: "test1",
			args: args{
				arr:    []int{1, 2, 3, 4, 5},
				target: 3,
			},
			want: Pair{a: 2, b: 3},
		},
		{
			name: "test2",
			args: args{
				arr:    []int{1, 2, 3, 4, 5},
				target: 6,
			},
			want: Pair{a: -1, b: -1},
		},
		{
			name: "test3",
			args: args{
				arr:    []int{1, 3, 5, 7, 8},
				target: 5,
			},
			want: Pair{a: 2, b: 5},
		},
		{
			name: "test4",
			args: args{
				arr:    []int{1, 2,3,4,5,6,7},
				target: 0,
			},
			want: Pair{a: -1, b: -1},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := binarySearch(tt.args.arr, tt.args.target); got != tt.want {
				t.Errorf("binarySearch() = %v, want %v", got, tt.want)
			}
		})
	}
}
