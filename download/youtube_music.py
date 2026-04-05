import subprocess
from pathlib import Path

url = "https://music.youtube.com/watch?v=KDlsH8MbDbs&list=OLAK5uy_k-NKMjAPoDEbQt4z6AAkMtA0Th3aGqAuY"
output_dir = Path("/Users/yangliu/Desktop/tmp/bike")

cmd = [
    "yt-dlp",
    "-x",                 # extract audio
    "--audio-format", "mp3",
    "-o", str(output_dir / "%(title)s.%(ext)s"),
    url,
]

subprocess.run(cmd, check=True)