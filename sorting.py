import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

numbers = random_numbers(5)

def selection_sort(numbers):
    numbers = numbers.copy()

    m = len(numbers)

    for idx_ukladany in range(m):
        idx_min = idx_ukladany

        for idx_hledany in range(idx_ukladany + 1, m):
            if numbers[idx_hledany] < numbers[idx_min]:
                idx_min = idx_hledany

        numbers[idx_ukladany], numbers[idx_min] = numbers[idx_min], numbers[idx_ukladany]

    return numbers



def main():
    print("Puvodni:", numbers)
    print("Serazeny:", selection_sort(numbers))


if __name__ == "__main__":
    main()


# def bubble_sort(numbers):







