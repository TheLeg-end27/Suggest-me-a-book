from pathlib import Path
from tkinter import Image
from fastai.vision.all import *
def search_images(term, max_images=30, folder_name="."):
    print(f"Searching for '{term}'")
    crawler = MyCrawler(
        prefix=term,
        storage={'root_dir': folder_name},
    )
    crawler.crawl(keyword=term, max_num=max_images)

search_images("cat", 1)
im = Image.open("cat000001.png")
im.to_thumb(256,256)

search_images("dog", 1)
im = Image.open("dog000001.png")
im.to_thumb(256,256)

#downloading multiple images 
no_of_photos = 20 

searches = 'cat','dog'
path = Path('cat_or_dog')
from time import sleep

for o in searches:
    dest = (path/o)
    dest.mkdir(exist_ok=True, parents=True)
    search_images(f"{o} photo", no_of_photos, dest)
    sleep(10)  
    search_images(f"{o} sun photo", no_of_photos, dest)
    sleep(10)
    search_images(f"{o} night photo", no_of_photos, dest)
    sleep(10)
    print(f"Photos of {o} completed!")

resize_images(path, max_size=400, dest=path, recurse=True)
print(f"Photos resized!")

failed = verify_images(get_image_files(path))
failed.map(Path.unlink)
len(failed)