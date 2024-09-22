from rest_framework.permissions import BasePermission


class IsCoinEnough(BasePermission):
    message = "User doesn't have enough coins."

    def has_permission(self, request, view):
        user = request.user
        test_coin = view.get_object().coin
        return user.coin > test_coin
