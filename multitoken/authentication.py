from rest_framework import authentication
import swapper
Token = swapper.load_model('multitoken', 'Token')


class TokenAuthentication(authentication.TokenAuthentication):
    model = Token
