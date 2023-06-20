items = ['A', 'B', 'C', 'D', 'E']

step = 1/2

times = [int(el / step) for el in [1/2, 1/2, 1, 2, 1/2]]

ratings = [7, 6, 9, 9, 8]

# 0 time to maximum times.
cols = int(2/step+1)

# Given the durations of activites , and ratings of activities, find the
# maximum total rating that can be obtained in the limited amount of time


def opt_tra_iti(items, times, ratings):

    # Table keeps the current rating value and set of items for the cell,
    # also the items that are added for this cell. Each cell represents
    # a state (a subproblem)
    # table[][0] is always (0, set()). It is only stored for ease of coding
    table = [[[0, set()] for j in range(cols)] for i in range(len(items))]

    # For the first item (item 0)
    for j in range(1, cols):
        # If the item fits to the current duration of time
        if j >= times[0]:
            # Add the item to the cell set
            table[0][j][0] = ratings[0]
            table[0][j][1].add(items[0])

    # Iterate over other items
    for i in range(1, len(items)):
        # Iterate over times
        for j in range(1, cols):
            # If current item cannot be added for the time duration
            if j < times[i]:
                # The state is the same as the state for the previous
                # item with the same amount of time
                table[i][j][0] = table[i-1][j][0]
                table[i][j][1] = table[i-1][j][1].copy()

            # Item can fit
            elif j >= times[i]:
                # State pre addition
                pre_add_sta = table[i-1][j-times[i]]

                # The situation the item is added
                if pre_add_sta[0] + ratings[i] > table[i-1][j][0]:
                    # Add the item
                    table[i][j][0] = pre_add_sta[0] + ratings[i]
                    table[i][j][1] = pre_add_sta[1].copy() | {items[i]}
                else:
                    table[i][j][0] = table[i-1][j][0]
                    table[i][j][1] = table[i-1][j][1].copy()

    print("Table is: ")

    for row in table:
        print(row)

    return table[-1][-1]

# Compare to words and return the maximum number of same characters in
# corresponding positions. Returns the comparison table and longest common
# subsequence between words
def word_compare(word_1, word_2):
    table = [[0 for j in range(len(word_1))] for i in range(len(word_2))]

    maxim = 0

    for i in range(len(word_2)):
        for j in range(len(word_1)):
            if word_1[j] == word_2[i]:
                # One more than upper left.
                if i >0 and j > 0:
                    table[i][j] = table[i-1][j-1] + 1
                else:
                    table[i][j] = 1

                maxim = max(maxim, table[i][j])
            else:
                if i >0 and j > 0:
                    table[i][j] = table[i-1][j-1]

    return (maxim, table)


if __name__ == "__main__":
    # res = opt_tra_iti(items, times, ratings)

    # print("result is", res)

    word_1 = "blue"
    word_2 = "clues"

    (longest_substr, table) = word_compare(word_1, word_2)

    print("Longest substring is", longest_substr)
    print("Table is")

    for row in table:
        print(row)
