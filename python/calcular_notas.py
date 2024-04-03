if __name__ == '__main__':

    value = int(input())

    print(value)

    notes = [100, 50, 20, 10, 5, 2, 1]
    count_notes = [0, 0, 0, 0, 0, 0, 0]

    for i in range(len(notes)):
        count_notes[i] = value // notes[i]
        value %= notes[i]

    for i in range(len(notes)):
        print(f"{count_notes[i]} nota(s) de R$ {notes[i]:.2f}")