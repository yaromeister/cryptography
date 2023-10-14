import numpy as np

def normalize_word_length(word:str, length:int):
    if length < 0:
        raise ValueError("Length should be a non-negative integer.")

    if length == 0:
        return ""

    if len(word) < length:
        # Duplicate the word until it reaches the desired length
        return (word * (length // len(word))) + word[:length % len(word)]
    elif len(word) > length:
        # Truncate the word to the desired length
        return word[:length]
    else:
        return word

def get_sorted_indexes(key:str):
    return [i for i, _ in sorted(enumerate(key), key=lambda x: x[1].lower())]

def encrypt(text:str, col_key:str, row_key:str):
    #text = text.replace(' ', '')
    hardcoded_col_num = 6
    rows = round(len(text) / hardcoded_col_num)
    matrix = np.array([[' ' for _ in range(hardcoded_col_num)] for _ in range(rows)])
    # Fill the matrix with characters from the text
    row, col = 0, 0
    for char in text:
        if col == hardcoded_col_num:
            row += 1
            col = 0
        if row == rows:
            break
        matrix[row][col] = char
        col += 1

    norm_col_key = normalize_word_length(col_key,hardcoded_col_num)
    norm_row_key = normalize_word_length(row_key,rows)
    column_permute = matrix[:, get_sorted_indexes(norm_col_key)]
    row_permute = column_permute[get_sorted_indexes(norm_row_key),:]

    result = ''
    for j in range(len(row_permute[0])):
        for i in range(len(row_permute)):
            result += row_permute[i][j]

    return result

def decrypt(encoded_text: str, col_key: str, row_key: str):
    hardcoded_col_num = 6

    # Calculate the number of rows based on the encoded text length
    rows = len(encoded_text) // hardcoded_col_num

    # Initialize the matrix
    matrix = [[' ' for _ in range(hardcoded_col_num)] for _ in range(rows)]

    # Reverse the permutation of row and column keys
    norm_col_key = normalize_word_length(col_key, hardcoded_col_num)
    norm_row_key = normalize_word_length(row_key, rows)
    reversed_col_permute = get_sorted_indexes(norm_col_key)
    reversed_row_permute = get_sorted_indexes(norm_row_key)

    # Fill the matrix based on the reversed permutation
    for j in range(len(reversed_row_permute)):
        for i in range(len(reversed_col_permute)):
            matrix[reversed_row_permute[j]][reversed_col_permute[i]] = encoded_text[i * len(reversed_row_permute) + j]

    # Reconstruct the original text from the matrix
    original_text = ''.join(''.join(row) for row in matrix)
    return original_text
