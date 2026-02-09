package main

import "testing"

func TestFirstNotSmaller(t *testing.T) {

	type args struct {
		arr    []int
		target int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{
				arr:    []int{1, 3, 3, 5, 8, 8, 10},
				target: 2,
			},
			want: 1,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := firstNotSmaller(tt.args.arr, tt.args.target); got != tt.want {
				t.Errorf("firstNotSmaller() = %v, want %v", got, tt.want)
			}
		})
	}

}
