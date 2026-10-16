import subprocess
import os

output_files = [
    "/Users/yangliu/Desktop/temporary/1.mp4",
    "/Users/yangliu/Desktop/temporary/2.mp4",
]

output_dir = "/Users/yangliu/Desktop/temporary/"
list_file = os.path.join(output_dir, "list.txt")
final_output = os.path.join(output_dir, "final.mp4")

# 🧩 Step 1: generate list.txt
with open(list_file, "w") as f:
    for file in output_files:
        f.write(f"file '{file}'\n")

print("📄 list.txt created")

# 🧩 Step 2: merge videos
subprocess.run([
    "ffmpeg",
    "-y",
    "-f", "concat",
    "-safe", "0",
    "-i", list_file,
    "-c", "copy",
    final_output
], check=True)

print(f"🎬 Final video created: {final_output}")