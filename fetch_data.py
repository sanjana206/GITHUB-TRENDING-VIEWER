import requests
from bs4 import BeautifulSoup

def fetch_trending_repos():
    url = "https://github.com/trending"
    response = requests.get(url)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    repos = []

    for repo in soup.select("article.Box-row"):
        name = repo.h2.text.strip().replace("\n", "").replace(" ", "")
        star_tag = repo.select_one("a[href*='stargazers']")
        stars = star_tag.text.strip().replace(",", "") if star_tag else "0"

        repos.append({
            "Repository": name,
            "Stars": int(stars)
        })

    return repos
