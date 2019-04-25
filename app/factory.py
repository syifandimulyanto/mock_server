from payment_log.service.bridge import PaymentService
from payment_log.repository.development import PaymentRepository

from helper import Attribute


class Factory:

    def __init__(self, db):
        self.db = db
        # self.session = session
        self.factory = None

    def __enter__(self):
        return self.start()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:# pragma: no cover
        return

    def start(self):
        self.factory = RepositoryFactory(self.db)
        return self

    @Attribute
    def payment(self):
        return PaymentService(self.factory)

    @Attribute
    def statuses(self):
        return StatusService(self.factory)

    @Attribute
    def register(self):
        return RegisterService(self.factory)


class RepositoryFactory:

    def __init__(self, db):
        self.db = db

    @Attribute
    def payment(self):
        return PaymentRepository(self.db)

    @Attribute
    def gateway(self):
        return Gateway()

    @Attribute
    def canopus_gateway(self):
        return CanopusGateway()

    @Attribute
    def statuses(self):
        return StatusRepository(self.db)

    @Attribute
    def register(self):
        return RegisterRepository(self.db)
