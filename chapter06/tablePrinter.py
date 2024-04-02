def print_table(table_data):
    # Find the maximum length of each column
    col_widths = [max(len(item) for item in col) for col in table_data]
    num_cols = len(table_data)

    # Transpose the table data
    for y in range(len(table_data[0])):
        for x in range(num_cols):
            print(table_data[x][y].rjust(col_widths[x]), end=' ')
        print()

# Example usage:
table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
