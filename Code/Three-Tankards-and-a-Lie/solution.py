import sys

def main():
    input_data = sys.stdin.buffer.read().decode()
    data = input_data.split()
    idx = 0
    N, M, Q = int(data[idx]), int(data[idx+1]), int(data[idx+2])
    idx += 3

    item_at = list(range(N + 1))

    for _ in range(M):
        a, b = int(data[idx]), int(data[idx+1])
        idx += 2
        item_at[a], item_at[b] = item_at[b], item_at[a]

    final_pos = [0] * (N + 1)
    for p in range(1, N + 1):
        final_pos[item_at[p]] = p

    out = []
    for _ in range(Q):
        p = int(data[idx])
        idx += 1
        out.append(str(final_pos[p]))

    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()