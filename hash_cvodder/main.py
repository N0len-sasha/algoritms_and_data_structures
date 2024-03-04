import random
import string


class MarsURLEncoder:

    def __init__(self):
        self.urls = {}

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        letters = string.ascii_uppercase
        hash_code = ''.join(random.choice(letters) for i in range(10))
        if hash_code not in self.urls.keys():
            self.urls[hash_code] = long_url
        else:
            self.encode(long_url)
        return f'https://ma.rs/{hash_code}'

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        codes = short_url.split("/")
        hash_code = codes[len(codes) - 1]
        return self.urls[hash_code]
