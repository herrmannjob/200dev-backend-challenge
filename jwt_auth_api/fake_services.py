import requests

def check_health():
    response = requests.get("https://api-onecloud.multicloud.tivit.com/fake/health")
    return response.json()

def get_admin_data():
    response = requests.get("https://api-onecloud.multicloud.tivit.com/fake/admin")
    return response.json()

def get_user_data():
    response = requests.get("https://api-onecloud.multicloud.tivit.com/fake/user")
    return response.json()
