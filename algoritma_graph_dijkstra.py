import math
import heapq

def dijkstra_matrix(matrix, n, start, end):
    """
    Algoritma Dijkstra menggunakan Adjacency Matrix.
    matrix : list 2D berbobot, math.inf = tidak ada edge
    n      : jumlah node
    start  : node asal
    end    : node tujuan
    """
    M = math.inf

    Q = [M] * (n + 1)     # Q[i] = jarak terpendek dari start ke i
    R = [0] * (n + 1)     # R[i] = node sebelumnya (untuk rekonstruksi jalur)
    Q[start] = 0

    pq   = [(0, start)]   # priority queue: (jarak, node)
    done = [False] * (n + 1)

    print("=" * 55)
    print(f"ALGORITMA DIJKSTRA: Node {start} ke Node {end}")
    print("=" * 55)

    while pq:
        jarak_min, CN = heapq.heappop(pq)   # CN = Current Node

        if done[CN]:
            continue
        done[CN] = True
        print(f"\nProses Node {CN} | beban min dari asal = {jarak_min}")

        if CN == end:
            print("  → Node tujuan ditemukan, selesai!")
            break

        # Baca baris CN di adjacency matrix untuk temukan tetangga
        for i in range(1, n + 1):
            if matrix[CN][i] != M and not done[i]:
                jarak_baru = Q[CN] + matrix[CN][i]
                if jarak_baru < Q[i]:
                    Q[i] = jarak_baru
                    R[i] = CN                          # catat node sebelumnya
                    heapq.heappush(pq, (jarak_baru, i))
                    print(f"  Update Node {i}: beban min = {jarak_baru}, sebelumnya = {CN}")

    # Rekonstruksi jalur dari matriks R (backtrack dari end ke start)
    jalur = []
    node  = end
    while node != 0:
        jalur.append(node)
        node = R[node]
    jalur.reverse()

    print(f"\n{'=' * 55}")
    if Q[end] == M:
        print(f"Tidak ada jalur dari {start} ke {end}!")
    else:
        print(f"Rute terpendek : {' -> '.join(map(str, jalur))}")
        print(f"Beban minimal  : {int(Q[end])}")

    return Q, R, jalur

# ── Adjacency matrix berbobot — contoh dari slide ──────────────
M = math.inf
n = 5
matrix_dijkstra = [
    [M, M, M, M, M, M],   # baris 0 tidak dipakai
    [M, M, 1, 3, M, M],   # node 1 -> 2 (bobot 1), 1 -> 3 (bobot 3)
    [M, M, M, 1, M, 5],   # node 2 -> 3 (bobot 1), 2 -> 5 (bobot 5)
    [M, 3, M, M, 2, M],   # node 3 -> 1 (bobot 3), 3 -> 4 (bobot 2)
    [M, M, M, M, M, 1],   # node 4 -> 5 (bobot 1)
    [M, M, M, M, M, M],   # node 5 -> (tidak ada)
]

Q, R, jalur = dijkstra_matrix(matrix_dijkstra, n, 1, 5)
