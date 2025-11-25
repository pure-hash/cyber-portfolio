#!/usr/bin/env python3
import json, os, collections

LOG = os.path.join(os.path.dirname(__file__), "../logs/ssh_honeypot.jsonl")
counts = collections.Counter()

# Check if log file exists
if not os.path.exists(LOG):
    print("No log file found.")
    exit(0)

# Read the log file and count occurrences of src_ip
with open(LOG, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            obj = json.loads(line)
            counts[obj.get("src_ip", "<unknown>")] += 1
        except json.JSONDecodeError:
            # If the line isn't valid JSON, skip it
            continue

# Print the top source IPs in a formatted manner
print("Top Source IPs:")
print(f"{'Source IP Address':<20} {'Count'}")
print("=" * 40)

for ip, c in counts.most_common(20):
    print(f"{ip:<20} {c}")

# Optionally, save the output to a file (uncomment if needed)
# output_file = "top_ips.txt"
# with open(output_file, 'w', encoding='utf-8') as out:
#     out.write(f"{'Source IP Address':<20} {'Count'}\n")
#     out.write("=" * 40 + "\n")
#     for ip, c in counts.most_common(20):
#         out.write(f"{ip:<20} {c}\n")
# print(f"Results saved to {output_file}")

