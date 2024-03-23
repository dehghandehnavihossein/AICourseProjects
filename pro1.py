import time
from collections import deque
import heapq


def create_data():
    """Stores the data for the problem."""
    distance_matrix = [
        [0, 2451, 713, 1018, 1631, 1374, 2408, 213, 2571, 875, 1420, 2145, 1972],
        [2451, 0, 1745, 1524, 831, 1240, 959, 2596, 403, 1589, 1374, 357, 579],
        [713, 1745, 0, 355, 920, 803, 1737, 851, 1858, 262, 940, 1453, 1260],
        [1018, 1524, 355, 0, 700, 862, 1395, 1123, 1584, 466, 1056, 1280, 987],
        [1631, 831, 920, 700, 0, 663, 1021, 1769, 949, 796, 879, 586, 371],
        [1374, 1240, 803, 862, 663, 0, 1681, 1551, 1765, 547, 225, 887, 999],
        [2408, 959, 1737, 1395, 1021, 1681, 0, 2493, 678, 1724, 1891, 1114, 701],
        [213, 2596, 851, 1123, 1769, 1551, 2493, 0, 2699, 1038, 1605, 2300, 2099],
        [2571, 403, 1858, 1584, 949, 1765, 678, 2699, 0, 1744, 1645, 653, 600],
        [875, 1589, 262, 466, 796, 547, 1724, 1038, 1744, 0, 679, 1272, 1162],
        [1420, 1374, 940, 1056, 879, 225, 1891, 1605, 1645, 679, 0, 1017, 1200],
        [2145, 357, 1453, 1280, 586, 887, 1114, 2300, 653, 1272, 1017, 0, 504],
        [1972, 579, 1260, 987, 371, 999, 701, 2099, 600, 1162, 1200, 504, 0],
    ]
    city_index = [
        "New York",
        "Los Angeles",
        "Chicago",
        "Minneapolis",
        "Denver",
        "Dallas",
        "Seattle",
        "Boston",
        "San Francisco",
        "St. Louis",
        "Houston",
        "Phoenix",
        "Salt Lake City"
    ]

    return distance_matrix, city_index


def find_cost(start, end):
    return distance_matrix[city_index.index(start)][city_index.index(end)]


def calu_cost(path):
    cost = 0
    for i, city in enumerate(path[:-1]):
        cost += find_cost(city, path[i + 1])
    return cost


def printInfo(N_nodes, N_nodes_m, _time, path):
    print(f"- Cost: {calu_cost(path)}\n"
          f"- Path: {' -> '.join(path)}\n"
          f"- Number of Nodes: {N_nodes}\n"
          f"- Number of Nodes in Memory: {N_nodes_m}\n"
          f"- Time: {_time:.0f}ms\n")


def bfs(start, end):
    # تعداد nodeهای حافظه
    N_nodes_m = 0

    # مجموعه ای برای نگه داشتن گره های بازدید شده
    visited = set()

    # صف برای نگه داشتن گره هایی که باید بررسی بشن
    queue = deque([(start, [start])])

    # تا زمانی که صف خالی نشده
    while queue:
        # اولین گره را از صف خارج می کنیم
        city, path = queue.popleft()

        # اگر گره هدف پیدا شد، جستجو را متوقف می کنیم
        if city == end:
            return path, len(visited), N_nodes_m

        # گره را به مجموعه بازدید شده اضافه می کنیم
        visited.add(city)

        # گره های مجاور را بررسی می کنیم
        for neighbor in city_index:
            # اگر گره مجاور قبلا بازدید نشده، آن را در صف قرار می دهیم
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))

        # محاسبه nodeهای درون صف
        N_nodes_m = max(len(queue), N_nodes_m)

    return None, 0, 0, 0


def bfs_main(start, end):
    print("BFS:")
    start_time = time.perf_counter_ns()
    path, N_nodes, N_nodes_m = bfs(start, end)
    bfs_time = (time.perf_counter_ns() - start_time) / 1e6
    printInfo(N_nodes, N_nodes_m, bfs_time, path)


def dfs(start, end):
    # تعداد nodeهای حافظه
    N_nodes_m = 0

    # مجموعه ای برای نگه داشتن گره های بازدید شده
    visited = set()

    # پشته برای نگه داشتن گره هایی که باید بررسی بشن
    stack = [(start, [start])]

    # تا زمانی که پشته خالی نشده
    while stack:
        # محاسبه nodeهای درون صف
        N_nodes_m = max(len(stack), N_nodes_m)

        # اولین گره را از پشته خارج می کنیم
        city, path = stack.pop()

        # اگر گره هدف پیدا شد، جستجو را متوقف می کنیم
        if city == end:
            return path, len(visited), N_nodes_m

        # گره را به مجموعه بازدید شده اضافه می کنیم
        visited.add(city)

        # گره های مجاور را بررسی می کنیم
        for neighbor in city_index[::-1]:
            # اگر گره مجاور قبلا بازدید نشده، آن را در پشته قرار می دهیم
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

    return None, 0, 0, 0


def dfs_main(start, end):
    print("\nDFS:")
    start_time = time.perf_counter_ns()
    path, N_nodes, N_nodes_m = dfs(start, end)
    dfs_time = (time.perf_counter_ns() - start_time) / 1e6
    printInfo(N_nodes, N_nodes_m, dfs_time, path)


def uniform_cost(start, end):
    # تعداد nodeهای حافظه
    N_nodes_m = 0

    # ایجاد یک صف الویت برای ذخیره و رتبه‌بندی گره‌ها بر اساس هزینه تاکنون
    priority_queue = [(0, start, [start])]  # هزینه تاکنون، گره، مسیر
    visited = set()  # مجموعه‌ای برای نگهداری گره‌هایی که قبلاً بازدید شده‌اند

    while priority_queue:
        # محاسبه nodeهای درون صف
        N_nodes_m = max(len(priority_queue), N_nodes_m)

        # اولین گره را از صف اولویت خارج می کنیم
        cost, city, path = heapq.heappop(priority_queue)

        # اگر گره هدف پیدا شد، جستجو را متوقف می کنیم
        if city == end:
            return path, len(visited), N_nodes_m, cost

        # گره را به مجموعه بازدید شده اضافه می کنیم
        visited.add(city)

        # گره های مجاور را بررسی می کنیم
        for neighbor in city_index:
            # اگر گره مجاور قبلا بازدید نشده، هزینه را محاسبه کرده و آن را در صف اولویت قرار می دهیم
            if neighbor not in path:
                new_cost = cost + find_cost(city, neighbor)
                heapq.heappush(priority_queue, (new_cost, neighbor, path + [neighbor]))

    return None, 0, 0, 0  # در صورتی که به گره هدف نرسیده باشیم


def ucs_main(start, end):
    print("\nUCS:")
    start_time = time.perf_counter_ns()
    path, N_nodes, N_nodes_m, cost = uniform_cost(start, end)
    ucs_time = (time.perf_counter_ns() - start_time) / 1e6
    printInfo(N_nodes, N_nodes_m, ucs_time, path)


distance_matrix, city_index = create_data()


def main():
    while True:
        start, end = input(), input()

        if start not in city_index:
            print(f"{start} is not in the list of cities.")
            print("The cities are:", city_index)

        if end not in city_index:
            print(f"{end} is not in the list of cities.")
            print("The cities are:", city_index)

        if end in city_index and end in city_index:
            print("Both cities entered correctly!")
            break

    bfs_main(start, end)
    dfs_main(start, end)
    ucs_main(start, end)


if __name__ == "__main__":
    main()
