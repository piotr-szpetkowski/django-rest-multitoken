import swapper
Token = swapper.load_model('multitoken', 'Token')


def get_or_create_token(user, serializer_data=None):
    serializer_data = serializer_data or {}
    token_data = dict((k, v) for k, v in serializer_data.items() if k in Token.LOGIN_FIELDS)
    token, _ = Token.objects.get_or_create(user=user, **token_data)
    return token
