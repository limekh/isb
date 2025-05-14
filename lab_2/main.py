from consts import *
from reedsave import *
from tests import *


def all_tests(seq: str, name: str, out: str):
    """
    Run all tests for seq
    :param seq: sequence for tests
    :param name: name of prog lang
    :param out: path to save
    :return:
    """
    result = {
        f"{name} sequence": seq,
        f"Frequency bit test (P-value)": freq_bit_test(seq),
        f"Test for identical consecutive bits (P-value)": test_for_identical_bits(seq),
        f"Test for the longest sequence of ones in a block (P-value)": longest_sequence_test(seq)
    }
    save_json(out, result)


def main():
    cpp_seq = get_text(cpp_seq_txt)
    java_seq = get_text(java_seq_txt)

    all_tests(cpp_seq, "C++", test_results_cpp)
    all_tests(java_seq, "Java", test_results_java)


if __name__ == "__main__":
    main()
