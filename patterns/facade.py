class Kitchen:
    def prepare_food(self) -> str:
        return "Kitchen: Food is prepared."


class PaymentSystem:
    def process_payment(self) -> str:
        return "PaymentSystem: Payment processed."


class DeliveryService:
    def deliver(self) -> str:
        return "DeliveryService: Order delivered."


class FoodOrderFacade:

    def __init__(self):
        self._kitchen = Kitchen()
        self._payment = PaymentSystem()
        self._delivery = DeliveryService()

    def place_order(self) -> str:
        results = []
        results.append("FoodOrderFacade: Starting order process...")
        results.append(self._payment.process_payment())
        results.append(self._kitchen.prepare_food())
        results.append(self._delivery.deliver())
        results.append("FoodOrderFacade: Order completed!")
        return "\n".join(results)


if __name__ == "__main__":
    facade = FoodOrderFacade()
    print(facade.place_order())