from pytube import YouTube
from tqdm import tqdm
import argparse
import os

def download_video(url):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        total_size = video.filesize

        progress_bar = tqdm(total=total_size, unit="B", unit_scale=True)

        # Create the "videos" folder if it doesn't exist
        if not os.path.exists("videos"):
            os.makedirs("videos")

        # Download the video to the "videos" folder
        video.download(output_path="videos", filename=video.default_filename)

        progress_bar.update(total_size - progress_bar.n)

        progress_bar.close()
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", str(e))

def readFile(path):
    file = open(path, 'r')
    lines = file.readlines()
    file.close()
    return lines

# Parse given arguments
argParser = argparse.ArgumentParser(
            prog='getUrls',
            description='Get urls from file or direct url.',
            epilog='Current version only supports Youtube.')
argParser.add_argument('-u', '--url', help='Url from the video to download from.')
argParser.add_argument('-p', '--path', help='Path to a file containing urls to download from.')
args = argParser.parse_args()

# Check arguments
if args.url:
    download_video(args.url)
elif args.path:
    urls = readFile(args.path)
    for url in urls:
        download_video(url)
else:
    print("Arguments missing. Check -h for help.")