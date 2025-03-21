import os
import requests

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

os.makedirs(PACKAGE_DIR, exist_ok=True)
def pakage(func, action, repo="https://raw.githubusercontent.com/berkaygldal/seaside/main/pakage/"):
# Repo link should have 'https://' at the front of the string and '/' at end of it.
    if func == "install":
        file = action + ".py"
        url = f"{repo}{file}"
        filepath = os.path.join(PACKAGE_DIR, file)
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            with open(filepath, "wb") as f:
                f.write(response.content)
            print(f"pakage : successfully installed {action}.")
        except requests.exceptions.RequestException as e:
            print(f"pakage : error while installing: {e}")
