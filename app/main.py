def cancer_prediction(cell_size, cell_shape):
    """
    Simple function that simulates a model prediction.
    Returns 'Malignant' if both values > 5, else 'Benign'.
    """
    if cell_size > 5 and cell_shape > 5:
        return "Malignant"
    else:
        return "Benign"


if __name__ == "__main__":
    result = cancer_prediction(6, 7)
    print("Prediction:", result)
