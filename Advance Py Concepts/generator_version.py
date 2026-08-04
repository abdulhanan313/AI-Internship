import tracemalloc
import resource

def get_severe_lines_gen(filepath):
    """Generator: reads ONE line at a time, yields matches ONE at a time.
    Nothing is ever fully materialized in memory."""
    with open(filepath, "r") as f:
        for line in f:
            if "ERROR" in line or "CRITICAL" in line:
                yield line

tracemalloc.start()

count = 0
for line in get_severe_lines_gen("app.log"):
    count += 1  # we process one at a time; we never hold them all at once

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

peak_rss_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024

print(f"[GEN] Matched lines: {count}")
print(f"[GEN] Peak traced memory: {peak / 1024 / 1024:.2f} MB")
print(f"[GEN] Peak process RSS:   {peak_rss_mb:.2f} MB")
