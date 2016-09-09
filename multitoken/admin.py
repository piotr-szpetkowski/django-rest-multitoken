from django.contrib import admin

import swapper
Token = swapper.load_model('multitoken', 'Token')


class TokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'client', 'created')
    fields = ('user', 'client', 'created')
    ordering = ('-created',)
    readonly_fields = ('created',)


admin.site.register(Token, TokenAdmin)
