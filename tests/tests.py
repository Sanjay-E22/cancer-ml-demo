from app.main import cancer_prediction

def test_cancer_prediction():
    # Expected to be 'Malignant'
    assert cancer_prediction(6, 7) == "Malignant"
    # Expected to be 'Benign'
    assert cancer_prediction(3, 4) == "Benign"
