#include <iostream>
#include <vector>

int main() {
  
  std::vector<int> data {1};

  for (auto number: data) {
    std::cout << number << std::endl;
  }
  return 0;
}
