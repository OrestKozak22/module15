import requests


class GitHub:
    def get_user_defunkt(self):
        r = requests.get(f"https://api.github.com/users/defunkt")
        body = r.json()

        return body
