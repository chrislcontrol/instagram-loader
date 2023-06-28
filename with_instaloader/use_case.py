import re

from instaloader import instaloader

url = 'https://www.instagram.com/p/B4frbgtA5JJ/'
download_dir = 'downloads'

loader = instaloader.Instaloader(
    download_pictures=True,
    download_videos=False,
    download_video_thumbnails=False,
    download_geotags=False,
    download_comments=False,
    save_metadata=True,
    compress_json=False,
    filename_pattern='{profile}_{mediaid}',

)
expr = r'\/p\/([^\/]*)/'
found = re.search(expr, url)
if not found:
    raise Exception('Picture not found.')

print("Downloading ", found.group(1), "...")

post = instaloader.Post.from_shortcode(loader.context, found.group(1))
loader.download_post(post, download_dir)
