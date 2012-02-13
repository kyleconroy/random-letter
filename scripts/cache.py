import os
from datetime import datetime 

with open("src/letter.appcache", "w") as f:
    f.write("CACHE MANIFEST\n")
    f.write("#" + str(datetime.now()) + "\n")

    for path in os.listdir("src"):
        if path.startswith(".") or path.endswith("appcache") or path.endswith("html"):
            continue
        f.write(path + "\n")

