from prefect import flow, task


@task
def collect_order():
    print("Order received")
    return "Pizza Order"


@task
def prepare_order(order):
    print("Preparing:", order)
    return "Pizza Ready"


@task
def deliver_order(order):
    print("Delivering:", order)


@flow
def restaurant_workflow():

    order = collect_order()

    prepared_order = prepare_order(order)

    deliver_order(prepared_order)


if __name__ == "__main__":
    restaurant_workflow()