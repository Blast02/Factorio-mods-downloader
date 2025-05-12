import requests
import os
import time
import shutil
mods = [ #list des mods a dl
    "Krastorio2",
    "Krastorio2Assets",
    "krastorio-2-compat",
    "FluidMustFlow",
    "nach0_modpack_alienbiomes",
    "ArmouredBiters",]

baseURL = "https://mods-storage.re146.dev/"
versionURL = "https://re146.dev/factorio/mods/modinfo?id="
modspack_folder = "modspack"
version = []
if not os.path.exists(modspack_folder):
    os.makedirs(modspack_folder)
for i in mods:
    time.sleep(1)
    r = requests.get(versionURL + "/" + i)
    if r.status_code == 200:
        data = r.json()
        releases = data.get('releases', [])
        if releases:
            latest_release = releases[-1]
            mod_version = latest_release.get('version', 'Unknown')
            dl_rep = requests.get(baseURL + "/" + i + "/" + mod_version + ".zip", stream=True)
            if dl_rep.status_code == 200:
                file_path = os.path.join(modspack_folder, f"{i}_{mod_version}.zip")
                with open(file_path, 'wb') as f:
                    shutil.copyfileobj(dl_rep.raw, f)
                print(f"Downloaded {i} version {mod_version}")
            else:
                print(f"Failed to download {i} version {mod_version}")
        else:
            print(f"{i}: No releases found")
    else:
        print(f"Failed to get version for {i}")