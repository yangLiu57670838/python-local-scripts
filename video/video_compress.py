import subprocess

input_file = "/Users/yangliu/Desktop/tmp/bike/result/final.mp4"
output_file = "/Users/yangliu/Desktop/tmp/bike/result/output_compressed.mp4"

subprocess.run([
    "ffmpeg",
    "-y",                     # overwrite output
    "-i", input_file,
    "-vcodec", "libx264",     # use codec to encode, compress video, supported in browser, phone, CapCut, etc.
    "-an",                    # remove audio!!! important!!!
    "-crf", "28",             # compression level (lower = better quality), 32 will be much smaller but quality will be worse
    "-preset", "fast",        # speed vs compression
    # "-acodec", "aac",         # audio codec, no need because -an is used
    # "-b:a", "128k",           # audio bitrate, 128k is the default bitrate, no need because -an is used
    output_file
], check=True)
