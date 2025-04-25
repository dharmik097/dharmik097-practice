import requests
import heapq
import time
import os

# === UI Utilities ===
def loading_animation(message="Processing exchange data"):
    print(f"\n{message}... ", end="", flush=True)
    for _ in range(10):
        print("⏳", end="", flush=True)
        time.sleep(0.1)
    print(" ✅")

def print_bar_graph(results):
    print("\n-------------------------------")
    print("Exchange Path Comparison:")
    max_rate = max([r[1] for r in results])
    for name, rate in results:
        bar = '█' * int((rate / max_rate) * 20)
        print(f"{name:<15} {bar} {rate:.6f}")

def get_exchange_rates(base_currency):
    url = f'https://open.er-api.com/v6/latest/{base_currency}'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch exchange rates for {base_currency}")
    return response.json()['rates']

# === Strategies ===
def normal_strategy(from_currency, to_currency):
    rates = get_exchange_rates(from_currency)
    direct_rate = rates.get(to_currency, None)

    best_rate = direct_rate if direct_rate else float('-inf')
    best_path = (from_currency, to_currency)

    for mid_currency in rates:
        if mid_currency == from_currency or mid_currency == to_currency:
            continue
        try:
            mid_to_target = get_exchange_rates(mid_currency)[to_currency]
            total = rates[mid_currency] * mid_to_target
            if total > best_rate:
                best_rate = total
                best_path = (from_currency, mid_currency, to_currency)
        except:
            continue

    print("\n[Normal Strategy]")
    print(f"Best path: {' -> '.join(best_path)} = {best_rate:.6f}")
    return ("Normal", best_rate, best_path)

def dijkstra_strategy(from_currency, to_currency):
    currencies = get_exchange_rates(from_currency).keys()
    graph = {}

    for currency in currencies:
        try:
            rates = get_exchange_rates(currency)
            graph[currency] = {k: -1 * (1 / v) for k, v in rates.items()}  # inverse for cost
        except:
            continue

    queue = [(0, from_currency, [])]
    visited = set()

    while queue:
        cost, curr, path = heapq.heappop(queue)
        if curr in visited:
            continue
        visited.add(curr)
        path = path + [curr]
        if curr == to_currency:
            effective_rate = round(-1 / cost, 6) if cost != 0 else 0
            print("\n[Dijkstra Strategy]")
            print(f"Best path: {' -> '.join(path)}")
            print(f"Effective rate: {effective_rate}")
            return ("Dijkstra", effective_rate, path)
        for neighbor, weight in graph.get(curr, {}).items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    print("[Dijkstra Strategy] No path found.")
    return ("Dijkstra", 0.0, [])

def bellman_ford_strategy(start, end):
    currencies = list(get_exchange_rates(start).keys())
    rates_map = {c: get_exchange_rates(c) for c in currencies if c != start}
    graph = []
    for u in rates_map:
        for v in rates_map[u]:
            try:
                cost = -1 * (1 / rates_map[u][v])
                graph.append((u, v, cost))
            except:
                continue

    distance = {c: float('inf') for c in currencies}
    predecessor = {}
    distance[start] = 0

    for _ in range(len(currencies) - 1):
        for u, v, cost in graph:
            if distance[u] + cost < distance[v]:
                distance[v] = distance[u] + cost
                predecessor[v] = u

    # Reconstruct path
    path = []
    current = end
    while current in predecessor:
        path.insert(0, current)
        current = predecessor[current]
    if current == start:
        path.insert(0, start)
    if not path or path[0] != start:
        print("[Bellman-Ford Strategy] No path found.")
        return ("Bellman-Ford", 0.0, [])

    final_cost = distance[end]
    rate = round(-1 / final_cost, 6)
    print("\n[Bellman-Ford Strategy]")
    print(f"Path: {' -> '.join(path)}")
    print(f"Effective rate: {rate}")
    return ("Bellman-Ford", rate, path)

# === MAIN ===
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("💱 Currency Conversion Optimizer 💱\n")
    from_currency = input("🔹 From Currency (e.g., INR): ").upper()
    to_currency = input("🔹 To Currency (e.g., EUR): ").upper()

    loading_animation()

    results = []
    results.append(normal_strategy(from_currency, to_currency))
    results.append(dijkstra_strategy(from_currency, to_currency))
    results.append(bellman_ford_strategy(from_currency, to_currency))

    print_bar_graph([(r[0], r[1]) for r in results])
    best = max(results, key=lambda x: x[1])
    print(f"\n✅ Recommended Strategy: {best[0]}")
    print(f"➡️  Path: {' -> '.join(best[2])}")
    print(f"💰 Best Rate: {best[1]:.6f}\n")

if __name__ == "__main__":
    main()
