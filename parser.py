import re

def parse_range(ref_range):
    match = re.findall(r"[\d.]+", ref_range)
    if len(match) == 2:
        return float(match[0]), float(match[1])
    return None, None

def parse_lab_tests(text):
    lab_tests = []
    lines = text.split("\n")

    for line in lines:
        # Example line: HB ESTIMATION 9.4 g/dl 12.0-15.0
        match = re.match(r"(.+?)\s+([\d.]+)\s*(\S+)\s+([\d.]+\s*-\s*[\d.]+)", line)
        if match:
            test_name = match.group(1).strip()
            test_value = match.group(2).strip()
            test_unit = match.group(3).strip()
            ref_range = match.group(4).strip()

            low, high = parse_range(ref_range)
            value = float(test_value)
            out_of_range = value < low or value > high if low is not None else None

            lab_tests.append({
                "test_name": test_name,
                "test_value": test_value,
                "bio_reference_range": ref_range,
                "test_unit": test_unit,
                "lab_test_out_of_range": out_of_range
            })

    return lab_tests
