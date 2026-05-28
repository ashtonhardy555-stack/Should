import sys
import urllib.parse
from resources.lib.router import route

if __name__ == "__main__":
    plugin_url = sys.argv[0]
    handle = int(sys.argv[1])
    params = dict(urllib.parse.parse_qsl(sys.argv[2][1:]))
    route(plugin_url, handle, params)
