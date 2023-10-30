def find_largest_common_substring(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a table to store the lengths of the common substrings
    table = [[0] * (n + 1) for _ in range(m + 1)]

    # Variables to store the length and ending position of the longest common substring
    max_length = 0
    end_position = 0

    # Iterate through each character of str1 and str2
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > max_length:
                    max_length = table[i][j]
                    end_position = i

    # Extract the longest common substring
    longest_common_substring = str1[end_position - max_length: end_position]

    return longest_common_substring.strip()

