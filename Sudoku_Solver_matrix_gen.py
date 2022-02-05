# THis is a Sudoku solver using pre-defined Sudoku-Data

# import array as arr

Sudoku_len = 9
rows = Sudoku_len
cols = Sudoku_len

# Create a place holder for storing 'Sudoku matrix'
Sudoku_data_set_r_wise = list()

Row0 = [9, 4, 0, 8, 7, 0, 2, 5, 6]
Row1 = [5, 1, 2, 0, 0, 9, 7, 0, 3]
Row2 = [0, 8, 0, 2, 6, 5, 0, 9, 4]
Row3 = [6, 0, 9, 0, 5, 0, 8, 3, 0]
Row4 = [4, 0, 8, 3, 0, 2, 6, 0, 1]
Row5 = [0, 2, 3, 0, 8, 0, 5, 0, 9]
Row6 = [8, 7, 0, 9, 2, 6, 0, 1, 0]
Row7 = [2, 0, 5, 1, 0, 0, 9, 0, 8]
Row8 = [1, 9, 6, 0, 3, 8, 0, 2, 7]

Sudoku_data_set_c_wise = list()

Col0 = list()
Col1 = list()
Col2 = list()
Col3 = list()
Col4 = list()
Col5 = list()
Col6 = list()
Col7 = list()
Col8 = list()

Sudoku_data_set_c_wise = [Col0, Col1, Col2, Col3, Col4, Col5, Col6, Col7, Col8]
Sudoku_data_set_r_wise = [Row0, Row1, Row2, Row3, Row4, Row5, Row6, Row7, Row8]
Sudoku_data_set_r_wise_len = len(Sudoku_data_set_r_wise)
Sudoku_data_set_c_wise_len = len(Sudoku_data_set_c_wise)
Each_Row_len = len(Row1)
Each_Col_len = Each_Row_len
# print("Sudoku_data_set_r_wise = ...before loop execution")
# print(Sudoku_data_set_r_wise)


#value_and_pos_item_list = ["Sudoku_element", "Row_number", "Col_number"]
#value_and_pos_item_len = len(value_and_pos_item_list)
num_of_items_in_set = 3
value_and_pos_item_set = list()
value_and_pos_item_set_len = len(value_and_pos_item_set)
#value_and_pos_item_set = [0]*num_of_items_in_set
#value_and_pos_item_set = []
gen_matrix_row = list()
gen_matrix_r_wise = list()
gen_matrix_row_len = len(gen_matrix_row)
gen_matrix_r_wise_len = len(gen_matrix_r_wise)

gen_matrix_col = list()
gen_matrix_c_wise = list()
gen_matrix_col_len = len(gen_matrix_col)
gen_matrix_c_wise_len = len(gen_matrix_c_wise)


# _____________________________________________________________________________________________________


# Add the 'Sudoku problem' values mentioned in 'Sudoku_data_set_r_wise' matrix to the 'gen_matrix_r_wise' list()
# in the form of [number, i_pos, j_pos]
#                                                OR
# Print gen_matrix_r_wise = Matrix [ Row1[Set[value, value_row_pos, value_col_pos]], Row2[Set[value, value_row_pos, value_col_pos]], ....]
# print(gen_matrix_r_wise)


for row in range(0, Sudoku_data_set_r_wise_len):
#    print("gen_matrix_r_wise_len = ")
#    print(gen_matrix_r_wise_len)
#    print("Sudoku_data_set_r_wise_len = ")
#    print(Sudoku_data_set_r_wise_len)
    if gen_matrix_r_wise_len < Sudoku_data_set_r_wise_len:
        for element in range(0, Each_Row_len):
#            print("gen_matrix_row_len")
#            print(gen_matrix_row_len)
#            print("Each_Row_len =")
#            print(Each_Row_len)
            if gen_matrix_row_len < Each_Row_len:
                for item in range(0, num_of_items_in_set):
                    if len(value_and_pos_item_set) < num_of_items_in_set:
                        if len(value_and_pos_item_set) == 0:
                            value_and_pos_item_set.append(Sudoku_data_set_r_wise[row][element])
                        if len(value_and_pos_item_set) == 1:
                            value_and_pos_item_set.append(row)
                        if len(value_and_pos_item_set) == 2:
                            value_and_pos_item_set.append(element)

#                        print("value_and_pos_item_set is")
#                        print(value_and_pos_item_set)
#                        print("\n")
                gen_matrix_row.append(value_and_pos_item_set)
#                print("gen_matrix_row is ")
#                print(gen_matrix_row)
#                print("\n")
                gen_matrix_row_len = gen_matrix_row_len + 1
                value_and_pos_item_set = list()
        gen_matrix_r_wise.append(gen_matrix_row)
#        print("gen_matrix_r_wise is ")
#        print(gen_matrix_r_wise)
#        print("\n")
        gen_matrix_r_wise_len = gen_matrix_r_wise_len + 1
        gen_matrix_row = list()
        gen_matrix_row_len = 0


# _____________________________________________________________________________________________________


# Generate the Sudoku_data_set matrix in Column form - 'Sudoku_data_set_c_wise'
#                                       OR
# Sort the same Sudoku matrix 'Sudoku_data_set_r_wise' in the "Column form" as - 'Sudoku_data_set_c_wise'

for row in range(0, Sudoku_data_set_r_wise_len):
#    print(Sudoku_data_set_r_wise[row])
    for elem in range(0, Each_Row_len):
#        print(Sudoku_data_set_r_wise[row][elem])
        Sudoku_data_set_c_wise[elem].append(Sudoku_data_set_r_wise[row][elem])
#        print("Sudoku_data_set_c_wise")
#        print(Sudoku_data_set_c_wise)

# print("Sudoku matrix in column form is")
# print(Sudoku_data_set_c_wise)

# _____________________________________________________________________________________________________

# Add the 'Sudoku problem' values mentioned in 'Sudoku_data_set_c_wise' matrix to the 'gen_matrix_c_wise' list()
# in the form of [number, j_pos, i_pos]
#                                               OR
# Print gen_matrix_c_wise = Matrix [ Col1[Set[value, value_row_pos, value_col_pos]], Row2[Set[value, value_row_pos, value_col_pos]], ....]
# print(gen_matrix_c_wise)
#                                               OR
# Generate the "transpose of (gen_matrix_r_wise)" = gen_matrix_c_wise

for col in range(0, Sudoku_data_set_c_wise_len):
#    print("gen_matrix_c_wise_len = ")
#    print(gen_matrix_c_wise_len)
#    print("Sudoku_data_set_c_len = ")
#    print(Sudoku_data_set_c_len)
    if gen_matrix_c_wise_len < Sudoku_data_set_c_wise_len:
        for element in range(0, Each_Col_len):
#            print("gen_matrix_col_len")
#            print(gen_matrix_col_len)
#            print("Each_Col_len =")
#            print(Each_Col_len)
            if gen_matrix_col_len < Each_Col_len:
                for item in range(0, num_of_items_in_set):
                    if len(value_and_pos_item_set) < num_of_items_in_set:
                        if len(value_and_pos_item_set) == 0:
                            value_and_pos_item_set.append(Sudoku_data_set_c_wise[col][element])
                        if len(value_and_pos_item_set) == 1:
                            value_and_pos_item_set.append(element)
                        if len(value_and_pos_item_set) == 2:
                            value_and_pos_item_set.append(col)

#                        print("value_and_pos_item_set is")
#                        print(value_and_pos_item_set)
#                        print("\n")
                gen_matrix_col.append(value_and_pos_item_set)
#                print("gen_matrix_col is ")
#                print(gen_matrix_col)
#                print("\n")
                gen_matrix_col_len = gen_matrix_col_len + 1
                value_and_pos_item_set = list()
        gen_matrix_c_wise.append(gen_matrix_col)
#        print("gen_matrix_c_wise is ")
#        print(gen_matrix_c_wise)
#        print("\n")
        gen_matrix_c_wise_len = gen_matrix_c_wise_len + 1
        gen_matrix_col = list()
        gen_matrix_col_len = 0


#for row in Sudoku_data_set:
#    for elem_val in row:
#        Sudoku_data_row_index = Sudoku_data_set.index(row)
#        elem_index = row.index(elem_val)
##        print("\n")
##        print("Sudoku_data_row_index = ")
##        print(Sudoku_data_row_index)
##        print("elem_val_index = ")
##        print(elem_index)
##        print("matrix[Sudoku_data_row_index][elem_val_index][0]")
##        print(matrix[Sudoku_data_row_index][elem_index][0])
##        print("Sudoku_data_set[Sudoku_data_row_index][elem_val_index]")
##        print(Sudoku_data_set[Sudoku_data_row_index][elem_index])
##        matrix[Sudoku_data_row_index][elem_index][1] = Sudoku_data_set[Sudoku_data_row_index][elem_index]
#
##        print("matrix[Sudoku_data_row_index][elem_val_index][0]")
##        print(matrix[Sudoku_data_row_index][elem_val_index][0])
#
##        print("matrix[Sudoku_data_row_index][elem_index][0] ...before value assignment")
##        print(matrix[Sudoku_data_row_index][elem_index][0])
##        print("[Sudoku_data_set[Sudoku_data_row_index][elem_index]][Sudoku_data_row_index][elem_index] ...before value assignment")
##        print(Sudoku_data_set[Sudoku_data_row_index][elem_index])
##
##        matrix[Sudoku_data_row_index][elem_index][0] = Sudoku_data_set[Sudoku_data_row_index][elem_index]
##
##        print("matrix[Sudoku_data_row_index][elem_index][0] ...after value assignment")
##        print(matrix[Sudoku_data_row_index][elem_index][0])
##        print("[Sudoku_data_set[Sudoku_data_row_index][elem_index]][Sudoku_data_row_index][elem_index] ...after value assignment")
##        print(Sudoku_data_set[Sudoku_data_row_index][elem_index])
##
##        print("matrix = ...after value assignment")
##        print(matrix)
###
###        matrix[Sudoku_data_set_index][Row_index][2] = Row_index
###        print("Sudoku_data_set_index[Sudoku_data_set_index][Row_index][2]")
###        print(Sudoku_data_set[Sudoku_data_set_index][Row_index][2])
###        print("\n")
#
#print("matrix = ...after loop execution")
#print(matrix)
#print("Sudoku_data_set ...after loop execution")
#print(Sudoku_data_set)


