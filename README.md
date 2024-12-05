# Design Patterns Spec

## Task

We need to build a manufacturing facility for cars needs to accept orders and build the cars to specification if possible, otherwise the order should be rejected.

Designing and building engines are complicated, so we have partnered with a supplier who makes an excellent product, but are super secretive of their IP.
As such, we can't make any modifications to the engines they provide us.

We plan to offer 3 car chassis' of which each can be fitted with 2 different types of engines:
| Car Chassis      | Allowed Engines |
| ---------------- | --------------- |
| Sports           | V8, Electric    |
| Sedan/saloon     | V6, Electric    |
| Truck/ute        | V6, V8          |

After building each car, they should be tested, this involves turning on each car to ensure it is working.
If the test passes, we have a warehouse company named "BestQL" who will store the finished car before shipping to our customers.
Cars are stored using their Vehicle Identification Numbers (VIN) to ensure they don't get lost.

Once an order is complete, we mark the status on the order to notify the customer.

## Constraints

* Files in `bestql` and `engines` cannot be modified
* `order.py` should not be modified
* Orders which are completed should be marked as such and those not completable should be rejected
* `vin_service.py` should be used to get a VIN for each car

## Running
```sh
python3 main.py
```

## Extras

* We are expanding, so we want to open additional manufacturing plants, but we will still use the same warehouse company for all orders
* We want to start offering additional chassis, such as the `SUV`
* We sign up with a new engine supplier, which offers `DIESEL` engine type, which can be installed in a truck/ute chassis
