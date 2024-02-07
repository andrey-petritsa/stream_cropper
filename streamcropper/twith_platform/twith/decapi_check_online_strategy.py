import utils

class DecapiCheckOnlineStrategy:
    def check_is_online(self, stream_reference):
        endpoint = f"http://decapi.me/twitch/uptime/{stream_reference}"
        response = utils.web_client.get(endpoint)
        is_online = True
        if 'offline' in response:
            is_online = False
        utils.logger.info(f'Decapi response {stream_reference} is_online {str(is_online)}')

        return is_online

