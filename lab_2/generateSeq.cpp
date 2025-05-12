#include <fstream>
#include <iostream>
#include <random>
#include <string>

std::string genSequence() {
    std::random_device rand;
    std::mt19937 gen(rand());
    std::uniform_int_distribution<size_t> number(0, 1);

    std::string result;
    for (size_t i = 0; i < 128; ++i) {
        result += std::to_string(number(gen));
    }
    return result;
}

void save_string(const std::string& dir, const std::string& string2Save) {
    std::ofstream out;
    out.open(dir);
    out << string2Save << std::endl;
    out.close();
}

int main() {
    std::string s = genSequence();
    save_string("cppSeq.txt", s);
}