#include <iostream>
#include <string>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::vector<long long> heap;
    std::string command;
    while (std::cin >> command) {
        if (command == "CLEAR") {
            heap.clear();
        } else if (command == "ADD") {
            long long x;
            std::cin >> x;
            heap.push_back(x);
            std::size_t i = heap.size() - 1;
            while (i > 0 && heap[(i - 1) / 2] > x) {
                std::size_t p = (i - 1) / 2;
                heap[i] = heap[p];
                i = p;
            }
            heap[i] = x;
        } else if (command == "EXTRACT") {
            if (heap.empty()) {
                std::cout << "CANNOT\n";
                continue;
            }
            std::cout << heap[0] << '\n';
            long long x = heap.back();
            heap.pop_back();
            if (heap.empty()) continue;
            std::size_t i = 0;
            while (2 * i + 1 < heap.size()) {
                std::size_t j = 2 * i + 1;
                if (j + 1 < heap.size() && heap[j + 1] < heap[j]) ++j;
                if (heap[j] >= x) break;
                heap[i] = heap[j];
                i = j;
            }
            heap[i] = x;
        }
    }
}
