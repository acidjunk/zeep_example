import logging.config

import sys

import os

from zeep import Client


logging.config.dictConfig({
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "%(name)s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "zeep.transports": {
            "level": "INFO",
            "propagate": True,
            "handlers": ["console"],
        },
        "ims_client": {
            "level": "INFO",
            "propagate": False,
            "handlers": ["console"],
        },
    }
})
logger = logging.getLogger("example_client")

client = Client('wsdl/login.wsdl')
result = client.service.Login({"Username": os.getenv("USER"), "Password": os.getenv("PASS")})
token = result['LoginResult']

client = Client('wsdl/inventory.wsdl', strict=False)
### Wrong search
# Construct filter and pager for Name == 'LP'
array_of_filter_field = [{"FilterField": {"Name": "Name", "SelectedOperator": "OperationEquals", "Value": "LP"}}]
filter = {"Filters": array_of_filter_field}
pager = {"StartElement": 0, "Descending": False, "NumberOfElements": 10,
         "OrderByProperty": None}
wrong = client.service.GetAllProductsFiltered(pager=pager, filter=filter, sessionToken=token)
print(f'WRONG: {wrong}')
sys.exit()

### Correct search
# Construct filter and pager for Name == 'LP'
array_of_filter_field = [{"FilterField": {"Name": "CircuitId", "SelectedOperator": "OperationEquals", "Value": 1}}]
filter = {"Filters": array_of_filter_field}
pager = {"StartElement": 0, "Descending": False, "NumberOfElements": 2,
         "OrderByProperty": None}
correct = client.service.GetAllPortsFiltered(pager=pager, filter=filter, sessionToken=token)
print(f'CORRECT: {correct}')
