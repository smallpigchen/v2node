import random


class RadomUA:
    def process_request(self, request, spider):
        ua = random.choice(spider.settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers.setdefault('User-Agent', ua)


class checkUA:
    def process_response(self, request, response, spider):
        user_agent = request.headers.get('User-Agent')
        print('\nUser-Agent:\n', user_agent)
        return response
