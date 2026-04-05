import subprocess

ranges = [
    ("00:05:10", "00:05:25"),
    ("00:08:05", "00:08:15"),
]

input_file = '/Users/yangliu/Desktop/tmp/bike/3.MP4'
output_dir = "/Users/yangliu/Desktop/tmp/bike"

for i, (start, end) in enumerate(ranges):
    output = f"{output_dir}/output_{i}.mp4"

    try:
        subprocess.run([
            "ffmpeg",
            "-y",                   # overwrite output file if exists
            "-ss", start,
            "-to", end,
            "-i", input_file,
            "-c:v", "libx264",  # re-encode video → accurate cut, or use "-c", "copy" fast (no re-encode)
            "-c:a", "copy",     # keep audio unchanged, or use "-c", "copy" fast (no re-encode)
            output
        ], check=True)

        print(f"✅ Created: {output}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Failed on segment {i}: {e}")


