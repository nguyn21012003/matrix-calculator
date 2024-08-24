from tabulate import tabulate
import csv
import os


def open_file_csv(file):
    with open(file, "r") as file:
        reader = csv.DictReader(file)
        rows = []
        for row in reader:
            rows.append(row)
        return tabulate(rows, headers="keys", tablefmt="rounded_grid")


def read_file_matrix(file):
    matrix = []
    with open(file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            row_data = []
            for element in row:
                row_data.append((element))
            matrix.append(row_data)
        return matrix


def print_file_matrix(file):
    matrix = []
    with open(file, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            row_data = []
            for element in row:
                row_data.append(f"{element}")
            matrix.append(row_data)
        return tabulate(matrix, tablefmt="rounded_grid")


def create_matrix(row, col):
    matrix = []
    for i in range(row):
        a = []
        for j in range(col):
            print(f"Input the matrix element ROW {i+1}, COL {j+1}")
            a.append(str(input()))
        matrix.append(a)

    print("The matrix is: ")

    for row in range(row):
        for column in range(col):
            print(matrix[row][column], end=" ")
        print()

    return matrix


def save_matrix(name):
    matrix = create_matrix(int(input("Rows?: ")), int(input("Cols?: ")))
    with open(name, "w", newline="") as writefile:
        writer = csv.writer(writefile)
        writer.writerows(matrix)


def show_file():
    files = os.listdir()
    list_files = []
    for file in files:
        if file.startswith("matrix"):
            file = file.replace(".csv", "")
            file = list_files.append(file)

        with open("memory.csv", "w", newline="") as writefile:
            writer = csv.DictWriter(writefile, fieldnames=["ID", "Name"])
            writer.writeheader()
            for i in range(len(list_files)):
                writer.writerow({"ID": f"{i+1}", "Name": f"{list_files[i]}"})


def check_matrix_element(file):
    matrix_A = read_file_matrix(file)
    for i in range(len(matrix_A)):
        for j in range(len(matrix_A[i])):
            return f"Note chua ktra thanh phan ma tran"


def additional(operation):
    operation = operation.replace(" ", "")
    matrix_A, matrix_B = operation.split("+")
    name_matrix_A = "matrix " + matrix_A + ".csv"
    name_matrix_B = "matrix " + matrix_B + ".csv"
    # print dang ma tran nhin cho dep
    matrix_A_pretty = print_file_matrix(name_matrix_A)
    matrix_B_pretty = print_file_matrix(name_matrix_B)
    rowth_A = len(read_file_matrix(name_matrix_A))
    colth_A = len(read_file_matrix(name_matrix_A)[0])
    rowth_B = len(read_file_matrix(name_matrix_B))
    colth_B = len(read_file_matrix(name_matrix_B)[0])
    print(f"A is a matrix {rowth_A}x{colth_A}, and B is a matrix {rowth_B}x{colth_B}")
    new_matrix = []
    if colth_A == rowth_B:
        print(matrix_A_pretty)
        print("+")
        print(matrix_B_pretty)
        print("=")

        for i in range(rowth_A):
            rowth_C = []
            for j in range(colth_A):
                A_element = read_file_matrix(name_matrix_A)[i][j]
                B_element = read_file_matrix(name_matrix_B)[i][j]
                if not (A_element.isdigit() and B_element.isdigit()):
                    if str(A_element) == str(B_element):
                        len_char = len(str(A_element)) + len(str(B_element))
                        rowth_C.append(str(len_char) + str(A_element))
                    else:
                        rowth_C.append(str(A_element) + "+" + str(B_element))
                else:
                    rowth_C.append(float(A_element) + float(B_element))

            new_matrix.append(rowth_C)

        with open("new matrix.csv", "w", newline="") as writefile:
            writer = csv.writer(writefile)
            writer.writerows(new_matrix)
    else:
        print("The number of columns in the first matrix should be equal to the number of rows in the second.")


def get_minor_matrix(name, i, j):
    matrix = read_file_matrix(name)
    rows = len(matrix)
    cols = len(matrix[0])
    minor_matrix = []

    for row in range(rows):
        if row == i:
            continue

        new_row = []

        for col in range(cols):
            if col == j:
                continue

            new_row.append(matrix[row][col])

        minor_matrix.append(new_row)

    return minor_matrix


def det_2x2_matrix(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][1]
    d = matrix[1][0]
    det = int(a) * int(c) - int(d) * int(b)
    return det


def det_matrix(name):
    matrix = read_file_matrix(name)
    print(print_file_matrix(name))
    row = len(matrix)
    col = len(matrix[0])
    if row == col:
        if row == 2:
            det = det_2x2_matrix(matrix)
            return f"Det of {name.replace('.csv', '')} is {det}"
        elif row == 3:
            a = matrix[0][0]
            b = matrix[0][1]
            c = matrix[0][2]
            detA = det_2x2_matrix(get_minor_matrix(name, 0, 0))
            detB = det_2x2_matrix(get_minor_matrix(name, 0, 1))
            detC = det_2x2_matrix(get_minor_matrix(name, 0, 2))
            det = int(a) * detA - int(b) * detB + int(c) * detC
            return f"Det of {name.replace('.csv', '')} is {int(det)}"


def matrix_calculator(operator):
    if "+" in operator:
        additional(operator)
        print(print_file_matrix("new matrix.csv"))
    elif "-" in operator:
        pass


def promt_user(id):
    if id == 1:
        while True:
            try:
                name = str("matrix ") + str(input("Matrix name from A to Z: ")).upper() + str(".csv")
                save_matrix(name)
                show_file()
                print("ctrl + Z and Enter to stop")
            except ValueError:
                print("Value Error")
                break
            except KeyboardInterrupt:
                print("Stop promt")
                break
            except EOFError:
                print("Stop create matrix")
                break
    elif id == 2:
        print(open_file_csv(str("memory.csv")))
        operator = str(input("Input matrix (eg: A*C or A+C...): "))
        matrix_calculator(operator)
    elif id == 3:
        print("Coming soon")
    elif id == 4:
        show_file()
        print(open_file_csv(str("memory.csv")))
    elif id == 5:
        print(open_file_csv(str("memory.csv")))
        name = str("matrix " + input("Input (eg: A,C,... ): ").upper().strip() + ".csv")
        print(det_matrix(name))
    else:
        return False


def main():
    print(open_file_csv(str("menu.csv")))
    promt_user(int(input()))


if __name__ == "__main__":
    main()
