def predict_single(customer, model):
    y_predict = model.predict(customer)
    return ((y_predict == 1)[0])