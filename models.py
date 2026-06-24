from dataclasses import dataclass

@dataclass
class Order:
    id: str
    store_id: str
    provider_id: str
    order_store_id: str
    order_provider_id: str
    status: str
    status_description: str
    tracking_code: str
