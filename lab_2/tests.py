from math import sqrt, erfc
from scipy.special import gammainc
from consts import PI_I


def freq_bit_test(seq: str) -> float:
    """

    :return:
    """
    s_n = (seq.count("1") - seq.count("0")) / sqrt(len(seq))
    p_value = erfc(abs(s_n) / sqrt(2))
    return p_value


def test_for_identical_bits(seq: str) -> float:
    """

    :param seq:
    :return:
    """
    zeta = seq.count("1") / len(seq)
    if (abs(zeta) - 0.5) >= (2 / sqrt(len(seq))):
        return 0
    v_n = 0
    for bit in range(0, len(seq) - 1):
        if seq[bit] != seq[bit+1]:
            v_n += 1
    p_value = erfc(abs(v_n - 2 * len(seq) * zeta * (1-zeta)) / (2 * sqrt(2 * len(seq)) * zeta * (1 - zeta)))
    return p_value


def longest_sequence_test(seq: str) -> float:
    """

    :param seq:
    :return:
    """
    if len(seq) < 128:
        raise ValueError("128 bits required")

    v = [0, 0, 0, 0]

    for i in range(len(seq) // 8):
        block = seq[i * 8: (i + 1) * 8]
        max_run = 0
        current_run = 0

        for bit in block:
            if bit == '1':
                current_run += 1
                max_run = max(max_run, current_run)
            else:
                current_run = 0
        match max_run:
            case max_run if max_run <= 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case max_run if max_run >= 4:
                v[3] += 1

    x_2 = 0.0
    for i in range(len(v)):
        expected = 16 * PI_I[i]
        x_2 += (v[i] - expected) ** 2 / expected
    p_value = gammainc(3 / 2, x_2 / 2)
    return p_value
