import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract

"""
    Python中的适配器模式: 
        将一个类的接口转换成客户希望的接口。使得原本由于接口不兼容而不能一起工作的类可以一起进行工作 
        
    两种实现思路:
    1. 类适配器。使用多继承
    2. 对象适配器。使用组合    
"""


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self):
        pass


class AliPay(Payment):
    def pay(self, money):
        print("支付宝支付%d元" % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)


class BankPay:
    def cost(self, money):  # BankPay的接口和其他pay的接口不一致，在使用方使用时会出现问题
        print("银联支付%d元" % money)


# 适配器模式1: 通过类继承的方式实现
class NewBankPay(Payment, BankPay):
    def pay(self, money):
        self.cost(money)


# 适配器模式1: 通过类组合(在一个类中继承另一个类的对象)的方式实现
class PaymentAdapter:
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p = NewBankPay()  # 从调用方的角度看，接口不应该有差异，但实际上，接口是有差异的，这时候就应该用适配器模式
p.pay(100)

p = PaymentAdapter(BankPay())   # 适配不同的接口。
p.pay(1000)
