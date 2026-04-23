import random
import matplotlib.pyplot as plt



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

def bubble_sort(numbers):
    numbers = numbers.copy()

    m = len(numbers)

    plt.ion()
    plt.show()

    for cislo_pruchodu in range(m):
        for j in range(0, m - cislo_pruchodu - 1):

            index_highlight1 = j
            index_highlight2 = j + 1

            colors = ["steelblue"] * len(numbers)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"

            plt.clf()
            plt.bar(range(len(numbers)), numbers, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)


            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    plt.ioff()
    plt.show()

    return numbers



def main():
    print("Puvodni:", numbers)
    print("Serazeny:", selection_sort(numbers))

    print(bubble_sort(numbers))


if __name__ == "__main__":
    main()







