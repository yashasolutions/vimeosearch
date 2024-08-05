import argparse
import json
import os
import vimeo
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Vimeo API credentials from environment variables

CLIENT_ID = os.getenv('VIMEO_CLIENT_ID')
CLIENT_SECRET = os.getenv('VIMEO_CLIENT_SECRET')
ACCESS_TOKEN = os.getenv('VIMEO_ACCESS_TOKEN')

def get_client():
    # Initialize Vimeo client with client ID and client secret
    client = vimeo.VimeoClient(
        key=CLIENT_ID,
        secret=CLIENT_SECRET,
        token=ACCESS_TOKEN
    )
    response = client

def search_videos(search_string, max_results=50):
    # Initialize Vimeo client with access token only (OAuth2 Bearer Token)
    client = vimeo.VimeoClient(
        token=ACCESS_TOKEN
    )

    videos = []
    page = 1
    per_page = 50  # Maximum allowed per page is 50
    total_fetched = 0

    while total_fetched < max_results:
        response = client.get('/me/videos', params={
            'query': search_string,
            'page': page,
            'per_page': per_page
        })

        if response.status_code != 200:
            raise Exception(f"Failed to fetch videos: {response.json()}")

        data = response.json()
        videos.extend(data.get('data', []))
        total_fetched += len(data.get('data', []))

        # Check if there are more pages
        if not data.get('paging', {}).get('next'):
            break

        page += 1

    return videos[:max_results]

def parse_search_results(videos):
    # Parse video data from Vimeo to extract relevant information
    # - name
    # - url
    # - duration
    # - created_time
    # - video files (links for different resolutions)

    parsed_videos = []
    for video in videos:
        video_id = video.get('uri', '').split('/')[-1]
        name = video.get('name', '')
        url = video.get('link', '')
        duration = video.get('duration', 0)
        created_time = video.get('created_time', '')
        video_files = video.get('files', [])
        link_360 = get_video_files(video_files, '360p')
        link_240 = get_video_files(video_files, '240p')
        link_720 = get_video_files(video_files, '720p')
        link_1080 = get_video_files(video_files, '1080p')

        parsed_videos.append({
            'id': video_id,
            'name': name,
            'url': url,
            'duration': duration,
            'created_time': created_time,
            'link_240': link_240,
            'link_360': link_360,
            'link_720': link_720,
            'link_1080': link_1080
        })
    return parsed_videos

def get_video_files(video_files, rendition='240p'):
    # Get video file URL for the specified rendition
    for video_file in video_files:
        if video_file.get('rendition') == rendition:
            return video_file.get('link', '')
    return None


def main():
    parser = argparse.ArgumentParser(description='Search for videos on Vimeo using a search string.')
    parser.add_argument('search_string', type=str, help='The search string to query for videos.')
    parser.add_argument('--max_results', type=int, default=50, help='Maximum number of results to fetch.')
    args = parser.parse_args()

    try:
        videos = search_videos(args.search_string, max_results=args.max_results)
        videos_list = parse_search_results(videos)
        print(json.dumps(videos_list, indent=2))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
