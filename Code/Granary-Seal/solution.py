import sys

def main():
    input_data = sys.stdin.buffer.read().decode()
    data = input_data.split()
    idx = 0
    def next_line():
        nonlocal idx
        line = data[idx]
        idx += 1
        return line.strip()

    C = int(next_line())
    clerks = set(next_line() for _ in range(C))

    CS = int(next_line())
    countersigners = set(next_line() for _ in range(CS))

    R = int(next_line())
    couriers = set(next_line() for _ in range(R))

    N = int(next_line())
    count = 0
    for _ in range(N):
        parts = next_line().split()
        clerk, countersigner, courier = parts[0], parts[1], parts[2]
        if clerk in clerks and countersigner in countersigners and courier in couriers:
            count += 1

    print(count)

if __name__ == "__main__":
    main()