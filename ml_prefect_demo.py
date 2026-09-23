from prefect import flow, task
import time


@task
def load_data():
    print("Loading dataset...")
    return [65, 72, 80, 90, 55]


@task
def preprocess_data(data):
    print("Preprocessing dataset...")
    return [value / 100 for value in data]


@task
def train_model(data):
    print("Training model...")
    time.sleep(2)

    model = "Trained_Model"

    return model


@task
def evaluate_model(model):
    print("Evaluating model...")

    accuracy = 0.87

    return accuracy


@flow(name="ML Training Workflow")
def ml_workflow():

    data = load_data()

    processed_data = preprocess_data(data)

    model = train_model(processed_data)

    accuracy = evaluate_model(model)

    print("Final Accuracy:", accuracy)


if __name__ == "__main__":
    ml_workflow()