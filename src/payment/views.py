from rest_framework import generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from paycomuz import Paycom
from clickuz import ClickUz
from paycomuz.views import MerchantAPIView
from clickuz.views import ClickUzMerchantAPIView
from rest_framework.response import Response

from paycomuz.models import Transaction
from .models import Order
from .serializers import OrderSerializer


class PaymeCheckPayment(Paycom):
    def check_order(self, amount, account, *args, **kwargs):
        print(account)
        order = Order.objects.filter(id=account['order_id']).first()
        print(order)
        if not order:
            print(self.ORDER_NOT_FOND)
            return self.ORDER_NOT_FOND
        if order.total != amount:
            return self.INVALID_AMOUNT
        return self.ORDER_FOUND

    def successfully_payment(self, account, transaction, *args, **kwargs):
        transaction = Transaction.objects.filter(_id=account['id']).first()
        order = Order.objects.filter(id=transaction.order_key).first()
        if not order:
            return self.ORDER_NOT_FOND

        if order.payment != "payme":
            return self.INVALID_AMOUNT

        user = order.user
        if order.type == "basic":
            user.coin += 57
        elif order.type == "pro":
            user.coin += 115
        elif order.type == "premium":
            user.coin += 230

        order.is_finished = True
        user.save()
        order.save()

    def cancel_payment(self, account, transaction, *args, **kwargs):
        print("Cancel payment")
        print("Account", account)
        print("transaction: ", transaction)
        print("args", args)
        print("kwargs", kwargs)


class PaymeView(MerchantAPIView):
    VALIDATE_CLASS = PaymeCheckPayment

    def order_found(self, validated_data):
        super().order_found(validated_data)

        order_id = validated_data['params']['account']['order_id']
        order = Order.objects.filter(id=order_id).first()

        self.reply['result']['detail'] = {
            'receipt_type': 0,
            'items': [{
                'title': 'unione.uz platformasida coin sotib olish',
                'price': order.total,
                'count': 1,
                'code': '10309999001000000',
                'package_code': '10306008001000000',
                'vat_percent': 10
            }]
        }

class ClickCheckPayment(ClickUz):
    def check_order(self, order_id: str, amount: str):
        order = Order.objects.filter(id=order_id).first()
        if not order:
            return self.ORDER_NOT_FOUND
        if order.total != amount:
            return self.INVALID_AMOUNT

        return self.ORDER_FOUND

    def successfully_payment(self, order_id: str, transaction):
        order = Order.objects.filter(id=order_id).first()
        if not order:
            return self.ORDER_NOT_FOUND

        if order.payment != "click":
            return self.INVALID_AMOUNT

        user = order.user
        if order.type == "basic":
            user.coin += 57
        elif order.type == "pro":
            user.coin += 115
        elif order.type == "premium":
            user.coin += 230

        order.is_finished = True
        user.save()
        order.save()


class ClickView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = ClickCheckPayment


class GeneratePaymentUrlView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        self.order = serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        order_id = str(self.order.id)
        amount = self.order.total
        response_data = {
            "order_id": order_id,
        }

        if self.order.payment == "click":
            from clickuz import ClickUz
            url = ClickUz.generate_url(
                order_id=order_id,
                amount=str(amount),
                return_url="http://univway.com/"
            )
            response_data["url"] = url
        elif self.order.payment == "payme":
            from paycomuz import Paycom
            paycom = Paycom()
            url = paycom.create_initialization(
                order_id=order_id,
                amount=float(amount),
                return_url="http://univway.com/"
            )
            response_data["url"] = url

        return Response(response_data, status=status.HTTP_201_CREATED)
