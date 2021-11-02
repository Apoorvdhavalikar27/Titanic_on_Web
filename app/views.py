from django.shortcuts import render
# from django.http import HttpResponse
import pickle


def home(request):

    return render(request, "app/index.html")


def predict(request):

    p_class = request.POST.get('P_class')
    age = request.POST.get("Age")
    sex = request.POST.get("Sex")
    parch = request.POST.get('Parch')
    embarked = request.POST.get('Embarked')

    data = [age, sex, p_class, parch, embarked]
    print(data)

    with open("model_pickle", 'rb') as f:
        my_model = pickle.load(f)

    prediction = my_model.predict([data])
    print(prediction)


    if prediction == [0]:
        survived = "Not Survived"
        params = {
            "result": survived
        }
        return render(request, "app/result2.html", params)

    elif prediction == [1]:
        survived = "Survived"
        params = {
            "result": survived
        }
        return render(request, "app/result1.html", params)
