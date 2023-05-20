from pytube import YouTube
import argparse

def download_video(url):
    try:
        print("Starting download...")
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download()
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error:", str(e))

def readFile(path):
    file = open(path, 'r')
    lines = file.readlines()
    file.close()
    return lines

#parsing given arguments
argParser = argparse.ArgumentParser(
            prog='getUrls',
            description='Get urls from file or direct url.',
            epilog='Current version only supports Youtube.')
argParser.add_argument('-u', '--url', help='Url from the video to download from.')
argParser.add_argument('-p', '--path', help='Path to a file containing urls to download from.')
args = argParser.parse_args()

#check args
if args.url:
    download_video(args.url)
elif args.path:
    urls = readFile(args.path)
    for url in urls:
        download_video(url)
else:
    print("Arguments missing. Check -h for help.")