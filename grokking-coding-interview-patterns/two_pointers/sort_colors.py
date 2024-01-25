
def sort_colors(colors):
    "O(n) time | O(1) space)"
    red, white, blue =0, 0, len(colors) - 1
    while white <= blue:
        if colors[white] == 0:
            if colors[red] != 0:
                print(f"swapping white: {colors[white]} with blue: {colors[red]}")
                colors[white], colors[red] = colors[red], colors[white]
            white += 1
            red += 1
        elif colors[white] == 1:
            white += 1
        else:
            if colors[blue] != 2:
                print(f"swapping blue: {colors[white]} with blue: {colors[blue]}")
                colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1
        print(colors)
    return colors


arr = sort_colors([1, 0, 2, 1, 0])
print(arr == [0, 0, 1, 1, 2])
print(arr)

"""
Solution summary
To recap, the solution to this problem can be divided into five main parts:

We traverse the array using three pointers, red, white, and blue.
If the element pointed to by the white pointer is 0 , we swap it with the 
element pointed to by the red pointer if it’s not pointing to 0 , and 
increment both the red and white pointers.
If the element pointed to by the white pointer is 1 , we increment the 
white pointer.
If the element pointed to by the white pointer is 2
, we swap it with the element pointed to by the blue
pointer if it’s not pointing to 2 and decrement the blue pointer.
The array is sorted when the blue pointer becomes less than the white pointer.
"""
