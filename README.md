# AmediaDownloader
Downloader for amedia.site

usage: Amedia [-h] [-D DESTINATION] [--overwrite] [--multiple] [--first FIRST] [--last LAST] link

Downloader for amedia.site

positional arguments:
  link                  origin link

options:
  -h, --help            show this help message and exit
  -D DESTINATION, --destination DESTINATION
                        destination filename (filename, absolute/relative path)
  --overwrite, -O       if file already exists overwrites it if provided
  --multiple, -M        downloads multiple videos if provided
  --first FIRST, -f FIRST
                        specifies a first episode to download if -M is provided
  --last LAST, -l LAST  specifies a last episode to download if -M is provided