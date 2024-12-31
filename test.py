import requests

# headers = {'Authorization': 'Bearer ' + api_key}
# api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
gist_endpoint = 'https://gist.githubusercontent.com/Ryngineering/f66d38df4bf875075fab1b0538159334/raw/50cdc1c9666a3f96d172fec061a5a314d9f5283a/linkedIn_profile.json'
# params = {
#     'linkedin_profile_url': 'https://linkedin.com/in/ryanrodrigues/',
#     'extra': 'include',
#     'github_profile_id': 'include',
#     'facebook_profile_id': 'include',
#     'twitter_profile_id': 'include',
#     'personal_contact_number': 'include',
#     'personal_email': 'include',
#     'inferred_salary': 'include',
#     'skills': 'include',
#     'use_cache': 'if-present',
#     'fallback_to_cache': 'on-error',
# }
# response = requests.get(api_endpoint,
#                         params=params,
#                         headers=headers)
# print(response.json());



response = requests.get(gist_endpoint)
print(response.json())