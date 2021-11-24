# THis is a Sudoku solver using pre-defined Sudoku-Data

# import array as arr

Sudoku_len = 9
rows = Sudoku_len
cols = Sudoku_len

Row1 = list()
Row2 = list()
Row3 = list()
Row4 = list()
Row5 = list()
Row6 = list()
Row7 = list()
Row8 = list()
Row9 = list()

#Col1 = [0]*Sudoku_len
#Col2 = [0]*Sudoku_len
#Col3 = [0]*Sudoku_len
#Col4 = [0]*Sudoku_len
#Col5 = [0]*Sudoku_len
#Col6 = [0]*Sudoku_len
#Col7 = [0]*Sudoku_len
#Col8 = [0]*Sudoku_len
#Col9 = [0]*Sudoku_len



# Create a place holder for storing 'Sudoku matrix'
Sudoku_data_rows = list()

Row1 = [9, 4, 2, 8, 7, 3, 2, 5, 6]
Row2 = [5, 1, 2, 0, 0, 9, 7, 0, 3]
Row3 = [0, 8, 0, 2, 6, 5, 0, 9, 4]
Row4 = [6, 0, 9, 0, 5, 0, 8, 3, 0]
Row5 = [4, 0, 8, 3, 0, 2, 6, 0, 1]
Row6 = [0, 2, 3, 0, 8, 0, 5, 0, 9]
Row7 = [8, 7, 0, 9, 2, 6, 0, 1, 0]
Row8 = [2, 0, 5, 1, 0, 0, 9, 0, 8]
Row9 = [1, 9, 6, 0, 3, 8, 0, 2, 7]

Sudoku_data_rows = [Row1, Row2, Row3, Row4, Row5, Row6, Row7, Row8, Row9]
Sudoku_data_rows_len = len(Sudoku_data_rows)
Each_Row_len = len(Row1)
print("Sudoku_data_rows = ...before loop execution")
print(Sudoku_data_rows)


# Create an place holder for storing [Sudoku_value, Sudoku_value_position_i, Sudoku_value_position_j]
# Create a place holder of Zeros for the a 3 x 9 x 9 "matrix"

#value_and_pos_item_list = ["Sudoku_element", "Row_number", "Col_number"]
#value_and_pos_item_len = len(value_and_pos_item_list)
num_of_items_in_set = 3
value_and_pos_item_set = list()
value_and_pos_item_set_len = len(value_and_pos_item_set)
#value_and_pos_item_set = [0]*num_of_items_in_set
#value_and_pos_item_set = []
gen_matrix_row = list()
gen_matrix = list()
gen_matrix_row_len = len(gen_matrix_row)
gen_matrix_len = len(gen_matrix)


# Store a list of [0, 0, 0] in 'matrix'
# for each position of Sudoku_data_element
# matrix = [[value_and_pos_item_set for i in range(cols)] for j in range(rows)]
# print("3D Matrix of Zeros = matrix = ...before loop execution")
# print(matrix)


for row in range(0, Sudoku_data_rows_len):
    print("gen_matrix_len = ")
    print(gen_matrix_len)
    print("Sudoku_data_rows_len = ")
    print(Sudoku_data_rows_len)
    if gen_matrix_len < Sudoku_data_rows_len:
        for element in range(0, Each_Row_len):
            print("gen_matrix_row_len")
            print(gen_matrix_row_len)
            print("Each_Row_len =")
            print(Each_Row_len)
            if gen_matrix_row_len < Each_Row_len:
                for item in range(0, num_of_items_in_set):
                    if len(value_and_pos_item_set) < num_of_items_in_set:
#                        value_and_pos_item_set.append(0)
                        if len(value_and_pos_item_set) == 0:
                            value_and_pos_item_set.append(Sudoku_data_rows[row][element])
                        if len(value_and_pos_item_set) == 1:
                            value_and_pos_item_set.append(row)
                        if len(value_and_pos_item_set) == 2:
                            value_and_pos_item_set.append(element)

                        print("value_and_pos_item_set is")
                        print(value_and_pos_item_set)
                        print("\n")
                gen_matrix_row.append(value_and_pos_item_set)
                print("gen_matrix_row is ")
                print(gen_matrix_row)
                print("\n")
                gen_matrix_row_len = gen_matrix_row_len + 1
                value_and_pos_item_set = list()
#            gen_matrix_row_len = 0
        gen_matrix.append(gen_matrix_row)
        print("gen_matrix is ")
        print(gen_matrix)
        print("\n")
        gen_matrix_len = gen_matrix_len + 1


# Add the Sudoku problem values in the
# 'matrix' in the form of [number, i_pos, j_pos]


for row in Sudoku_data_rows:
    for elem_val in row:
        Sudoku_data_row_index = Sudoku_data_rows.index(row)
        elem_index = row.index(elem_val)
#        print("\n")
#        print("Sudoku_data_row_index = ")
#        print(Sudoku_data_row_index)
#        print("elem_val_index = ")
#        print(elem_index)
#        print("matrix[Sudoku_data_row_index][elem_val_index][0]")
#        print(matrix[Sudoku_data_row_index][elem_index][0])
#        print("Sudoku_data_rows[Sudoku_data_row_index][elem_val_index]")
#        print(Sudoku_data_rows[Sudoku_data_row_index][elem_index])
#        matrix[Sudoku_data_row_index][elem_index][1] = Sudoku_data_rows[Sudoku_data_row_index][elem_index]

#        print("matrix[Sudoku_data_row_index][elem_val_index][0]")
#        print(matrix[Sudoku_data_row_index][elem_val_index][0])

        print("matrix[Sudoku_data_row_index][elem_index][0] ...before value assignment")
        print(matrix[Sudoku_data_row_index][elem_index][0])
        print("[Sudoku_data_rows[Sudoku_data_row_index][elem_index]][Sudoku_data_row_index][elem_index] ...before value assignment")
        print(Sudoku_data_rows[Sudoku_data_row_index][elem_index])

        matrix[Sudoku_data_row_index][elem_index][0] = Sudoku_data_rows[Sudoku_data_row_index][elem_index]

        print("matrix[Sudoku_data_row_index][elem_index][0] ...after value assignment")
        print(matrix[Sudoku_data_row_index][elem_index][0])
        print("[Sudoku_data_rows[Sudoku_data_row_index][elem_index]][Sudoku_data_row_index][elem_index] ...after value assignment")
        print(Sudoku_data_rows[Sudoku_data_row_index][elem_index])

        print("matrix = ...after value assignment")
        print(matrix)
#
#        matrix[Sudoku_data_rows_index][Row_index][2] = Row_index
#        print("Sudoku_data_rows_index[Sudoku_data_rows_index][Row_index][2]")
#        print(Sudoku_data_rows[Sudoku_data_rows_index][Row_index][2])
#        print("\n")

print("matrix = ...after loop execution")
print(matrix)
print("Sudoku_data_rows ...after loop execution")
print(Sudoku_data_rows)




