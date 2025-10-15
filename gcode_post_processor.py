import sys
import re
import os

# Configuration for each machine type
CONFIGS = {
    "newer": {
        "allow_arcs": True,
        "allow_spindle_speed": True,
        "remove_commands": [],
        "replace_commands": [],
    },
    "older": {
        "allow_arcs": False,
        "allow_spindle_speed": False,
        "remove_commands": [r"^S\d+"],  # Remove spindle speed lines
        "replace_commands": [
            (r"^G0[23].*", "; Arc move removed, not supported")
        ],
    }
}

def process_gcode(input_path, config):
    output_path = os.path.splitext(input_path)[0] + "_processed.tap"
    with open(input_path, "r") as infile, open(output_path, "w") as outfile:
        for line in infile:
            # Remove unsupported commands
            if any(re.match(pattern, line) for pattern in config["remove_commands"]):
                continue
            # Replace unsupported commands
            replaced = False
            for pattern, repl in config["replace_commands"]:
                if re.match(pattern, line):
                    outfile.write(repl + "\n")
                    replaced = True
                    break
            if replaced:
                continue
            # Optionally, remove arcs if not allowed
            if not config["allow_arcs"] and re.match(r"^G0[23]", line):
                outfile.write("; Arc command removed: " + line)
                continue
            # Optionally, remove spindle speed if not allowed
            if not config["allow_spindle_speed"] and re.match(r"^S\d+", line):
                continue
            # Write line as is
            outfile.write(line)
    print(f"Processed file written to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python gcode_post_processor.py <input_file.tap> <newer|older>")
        sys.exit(1)
    input_file = sys.argv[1]
    machine_type = sys.argv[2]
    if machine_type not in CONFIGS:
        print("Unknown machine type. Use 'newer' or 'older'.")
        sys.exit(1)
    process_gcode(input_file, CONFIGS[machine_type])