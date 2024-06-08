import argparse
import os
import tools.log
import amedia.Amedia


# Start main program
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Amedia',
        description='Downloader for amedia.site')

    parser.add_argument('link', help="origin link")
    parser.add_argument('-D', '--destination', help="destination filename (filename, absolute/relative path)", default=".")
    parser.add_argument('--overwrite', '-O', action='store_true', help="if file already exists overwrites it if provided")
    parser.add_argument('--multiple', '-M', action='store_true', help="downloads multiple videos if provided")
    parser.add_argument('--first', '-f', help="specifies a first episode to download if -M is provided")
    parser.add_argument('--last', '-l', help="specifies a last episode to download if -M is provided")

    args = parser.parse_args()

    tools.info("Script launched")
    
    tools.warn("Directory {} doesn't exist".format(args.destination))
    if not os.path.exists(args.destination):
        os.makedirs(args.destination)
        tools.info("Created directory: " + args.destination)
    
    amedia = amedia.Amedia(args.link, args.overwrite)
    if args.multiple:
        amedia.download_multiple(args.destination, args.first, args.last)
    else:
        amedia.download_one(args.destination)
    tools.info("Script stopped")