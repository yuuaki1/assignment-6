def pascal_triangle(n):
    # create an empty list to store the current row
    current_row = [1]
    # print the first row
    print(current_row)
    # loop through the remaining rows
    for i in range(1, n):
        # create a new row with the previous row
        previous_row = current_row
        current_row = [1]
        for j in range(1, i):
            current_row.append(previous_row[j-1] + previous_row[j])
        current_row.append(1)
        # print the current row
        print(current_row)

# test the function
pascal_triangle(6)
