import sys

def main():
    input_data = sys.stdin.buffer.read().decode()
    data = input_data.split()
    idx = 0
    N = int(data[idx])
    idx += 1
    G = int(data[idx])
    idx += 1

    arrivals = [int(data[idx + i]) for i in range(N)]
    idx += N
    clearances = [int(data[idx + i]) for i in range(G)]
    idx += G

    MAX_T = 221
    count = [0] * (MAX_T + 1)
    for c in clearances:
        count[c] += 1

    arrivals.sort()

    total_wait = 0
    for a in arrivals:
        t = a
        while count[t] == 0:
            t += 1
        count[t] -= 1
        total_wait += t - a

    print(total_wait)

if __name__ == "__main__":
    main()