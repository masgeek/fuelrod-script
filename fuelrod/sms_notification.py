import requests


class SmsNotification:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def send_sms(self, sms_message, end_point):
        _url = self.base_url + "/v1/sms/fee-notification"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }
        with requests.Session() as session:
            _response = session.post(url=_url, headers=headers, json=sms_message)
            _response.raise_for_status()
        return {
            "id": sms_message["id"],
            "username": sms_message["username"],
            "endpoint": end_point,
        }
