# Image-based-Calorie-Prediction 🍔😋

<p align="center">
  <a href="https://github.com/sivasai9398/Image-based-Calorie-Prediction">
    <img src="https://static.vecteezy.com/system/resources/previews/005/724/676/original/calorie-calculator-line-icon-count-calories-concept-linear-pictogram-calculate-kcal-for-healthy-nutrition-outline-icon-isolated-illustration-vector.jpg" alt="Logo" width="150" height="150">
  </a>

## 📌 Introduction

This Deep Learning Web Application utilizes Architecture from [Yolov5](https://github.com/ultralytics/yolov5) an Object detection model to process the Food Images and draw the bounding boxes around the food items which will give the count of each food items and atlast calories count is calculated.Calories values for a single food items are stored in the database and retrieved when it is useful.

## 🎯 Purpose of the Project

Now a days many diseases are coming to notice which are very different and new when compared to previous generations diseases with more calorie consumption related diseases or less calorie consumption related diseases. 
* High calorie intake effects:<br/>
The result is weightgain and higher body fat percentages. High calorie intake will cause stress on your body. High caloric foods are high in fats and sugars and extraordinary intake of these types of foods increase your risk factors for type 2 diabetes, heart disease and cancers.
* Low Calorie intake effects:
Regularly eating fewer calories than your body requires can cause fatigue and make it more challenging for you to meet your daily nutrient needs. For instance, calorie-restricted diets may not provide sufficient amounts of iron, folate or vitamin B12. This can lead to anemia and extreme fatigue (16, 17, 18).

 * To Overcome the above Problems there is a fundamental law of nutrition that goes like this: in order to maintain a constant weight, you have to balance the number of calories you eat with the number of calories you burn. To put it simply,


* If the equation is out of balance, you will either gain or lose weight, depending on which side of the equation is greater. You will not notice any weight change on a day-to-day basis, but you will if the equation remains unbalanced over a period of a week or more. The weight you might gain is stored primarily as fat.

* To Maintain the above equation, we had developed this solution which is helpful to track the calories intake by a user which is helpful to plan the diet accordingly and control their diet for the remaining whole day. If we follow this, we can get reduce chance for getting the diseases.

## Training Workflow
<a href="https://github.com/sivasai9398/Image-based-Calorie-Prediction"><img src="https://github.com/sivasai9398/Image-based-Calorie-Prediction/blob/main/image.png" alt="Logo" width="550" height="250"></a>
  * Images are collected using python web scrapper a piece of code which helps to collect images from web by giving keyword


## 🏁 Technology Stack

* [Flask](https://github.com/pallets/flask)
* [HTML](https://www.w3.org/TR/html52/)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Bootstrap](https://getbootstrap.com/)
* [Tensorflow](https://www.tensorflow.org/)
* [Keras](http://keras.io/)

## 🏃‍♂️ Local Installation

1. Drop a ⭐ on the Github Repository. 
2. Clone the Repo by going to your local Git Client and pushing in the command: 

```sh
https://github.com/sivasai9398/Image-based-Calorie-Prediction.git
```

3. Install the Packages: 
```sh
pip install -r requirements.txt
```

4. At last, push in the command:
```sh
python app.py
```

5. Go to ` http://127.0.0.1:5000/predict` and enjoy the application.

## 📋 Further Changes to be Done

- [ ] Deploying the Web Application on Cloud.
- [ ] Introducing weight estimation to get exact calories of each food.
- [ ] Enhance the User-Interface using HTML/CSS.
- [ ] Set the Application on Docker.

## 📜 LICENSE

[MIT](https://github.com/HarshCasper/Malaria-Detection/blob/master/LICENSE)
