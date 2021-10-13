import os
import sys
from abc import ABCMeta, abstractmethod  # 抽象类 abstract

'''
架构设计：
    在工程设计之初，搭建软件框架。搭建出各种类及类之间的关系。
    面向对象三大特性:
        封装
        继承
        多态
    接口: 隐藏类的内部实现
    
    1. 如何实现抽象接口
        1）抛出未实现的错误，来表示抽象接口
        2）采用抽象类和方法的包来定义抽象类(一般采用此种方式)    
        
    设计原则:solid原则
    1. 开放封闭原则：对扩展开放，对修改关闭
    2. 里氏替换原则: 所有引用父类的地方必须能透明的使用子类
    3. 依赖倒置原则：高层和底层之间利用接口抽象，不应直接依赖。面对接口编程。  
    
    工厂模式   
'''


# # 基类(抽象类实现方式1)
# class Payment:
#     def pay(self, money):
#         raise NotImplementedError  # 抛出一个未实现的错误，这就要求其继承者必须实现

# 基类(抽象类实现方式2)，一般采用第二种实现
class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod  # 表征方法是抽象方法，以约束子类必须实现这个方法  # 接口，对高层模块隐藏类接口的实现
    def pay(self, money):
        pass


class Alipay(Payment):  # 继承的实现方式
    def __init__(self, use_huabei=False):  # 初始化函数中的变量可以通过构造函数传入的方式进行初始化
        self.use_huabei = use_huabei

    # 继承抽象方法
    def pay(self, money):
        if self.use_huabei:
            print("花呗支付%d元" % money)
        else:
            print("支付宝支付%d元" % money)
        pass


class Wechatpay(Payment):
    # 继承抽象方法
    def pay(self, money):
        print("微信支付%d元" % money)
        pass


'''
    简单工厂模式: 好处是隐藏各种继承类的实现，客户端无需修改代码;
'''


# class PaymentFactory:
#     def create_payment(self, method):
#         if method == 'alipay':
#             return Alipay()
#         elif method == 'wechat':
#             return Wechatpay()
#         elif method == 'huabei':        # 缺点是违反开放封闭原则; 违反单一职责原则
#             return Alipay(use_huabei=True)
#         else:
#             return TypeError("No Such payment method - %s" % method)  # 抛出错误的打开方式
#
#
# pf = PaymentFactory()
# p = pf.create_payment('alipay')
# p.pay(1000)
# p = pf.create_payment('huabei')
# p.pay(100)


class PaymentFactory(metaclass=ABCMeta):
    """
    工厂抽象方法
    """

    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class WechatFactory(PaymentFactory):
    def create_payment(self):
        return Wechatpay()


class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)


pf = HuabeiFactory()    # 符合开放封闭原则。 # 符合单一设计原则
p = pf.create_payment()
p.pay(300)
