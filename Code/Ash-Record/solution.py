import sys
import bisect
from collections import defaultdict

def main():
    input_data = sys.stdin.buffer.read().decode()
    data = input_data.split()
    idx = 0
    N = int(data[idx]); idx += 1
    P = int(data[idx]); idx += 1
    min_gap = int(data[idx]); idx += 1
    sequence = [data[idx + i] for i in range(P)]; idx += P

    residues_by_type = defaultdict(list)

    for _ in range(N):
        t = int(data[idx]); idx += 1
        mat = data[idx]; idx += 1
        residues_by_type[mat].append(t)

    for mat in residues_by_type:
        residues_by_type[mat].sort()

    confirmed = 0
    last_time = None

    for step_type in sequence:
        timestamps = residues_by_type.get(step_type)
        if not timestamps:
            break

        if last_time is None:
            chosen = timestamps[0]
        else:
            target = last_time + min_gap
            pos = bisect.bisect_left(timestamps, target)
            if pos == len(timestamps):
                break
            chosen = timestamps[pos]

        last_time = chosen
        confirmed += 1

    print(confirmed)

if __name__ == "__main__":
    main()