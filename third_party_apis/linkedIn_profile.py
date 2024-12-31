import os
import requests

def scrape_linkedIn_profile(url):
    
    response = requests.get(url, timeout=10);
    data = response.json()
    data = {
        k: v
        for k,v  in data.items()
        if v not in ([], "", " ", None) and k not in ["people_also_viewed", "certifications" ]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    return data

if __name__ == "__main__":
    gist_endpoint = 'https://gist.githubusercontent.com/Ryngineering/f66d38df4bf875075fab1b0538159334/raw/50cdc1c9666a3f96d172fec061a5a314d9f5283a/linkedIn_profile.json'
    print(scrape_linkedIn_profile(gist_endpoint))