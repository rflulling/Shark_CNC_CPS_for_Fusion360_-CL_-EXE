import re

# Configuration: Define patterns to remove/replace and rules
REMOVE_PATTERNS = [
    r'^M6',  # Removes tool change commands (example)
    r'^T\d+',  # Removes tool selection lines
]

REPLACE_RULES = [
    (r'^G21', 'G20'),  # Example: Convert mm to inch (dangerous, only if you know the output units!)
    # Add more tuple pairs: (pattern, replacement)
]

def should_remove(line):
    for pattern in REMOVE_PATTERNS:
        if re.match(pattern, line):
            return True
    return False

def apply_replacements(line):
    for pattern, replacement in REPLACE_RULES:
        if re.match(pattern, line):
            return re.sub(pattern, replacement, line)
    return line

def process_gcode(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
        for line in infile:
            stripped = line.strip()
            if should_remove(stripped):
                continue  # Skip this line
            new_line = apply_replacements(stripped)
            outfile.write(new_line + '\n')

if __name__ == "__main__":
    # Example usage
    process_gcode('input.nc', 'output.nc')