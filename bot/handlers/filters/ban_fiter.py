from aiogram.dispatcher.filters.filters import BoundFilter

class BanFilter(BoundFilter):
    key = 'rethrow'
    required = True
    default = True

    def __init__(self, rethrow: bool,):
        self.rethrow = rethrow

    async def check(self, obj):
        if obj.conf['is_banned']:
            return False
        return True