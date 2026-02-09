package main

import "testing"

func Test_firstTrue(t *testing.T) {
	type args struct {
		arr []bool
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			name: "test1",
			args: args{
				arr: []bool{false, false, true, true, true},
			},
			want: 2,
		},
		{
			name: "test2",
			args: args{
				arr: []bool{false, false, false, false, false},
			},
			want: -1,
		},
		{
			name: "test3",
			args: args{
				arr: []bool{true, true, true, true, true},
			},
			want: 0,
		},
		{
			name: "test4",
			args: args{
				arr: []bool{false, false, false, false, true, true},
			},
			want: 4,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := firstTrue(tt.args.arr); got != tt.want {
				t.Errorf("firstTrue() = %v, want %v", got, tt.want)
			}

			if got := firstTrueBounded(tt.args.arr); got != tt.want {
				t.Errorf("firstTrueBounded() = %v, want %v", got, tt.want)
			}
		})
	}
}
