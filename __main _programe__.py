from PyQt5 import QtWidgets, uic
import pickle
import numpy as np
import sys
import resources
from PyQt5.QtWidgets import QMessageBox

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('image/main.ui', self)
        self.btn.clicked.connect(lambda: self.button_click())
        self.show()

    def button_click(self):
        radius_mean=float(self.text1.text())
        texture_mean= self.text2.text()
        perimeter_mean  = float(self.text3.text())
        area_mean  = float(self.text4.text())
        smoothness_mean = float(self.text5.text())
        compactness_mean = float(self.text6.text())
        concavity_mean = float(self.text7.text())
        concave_points_mean = float(self.text8.text())
        symmetry_mean  = float(self.text9.text())
        fractal_dimension_mean = float(self.text10.text())

        radius_se=float(self.text11.text())
        texture_se= self.text12.text()
        perimeter_se  = float(self.text13.text())
        area_se  = float(self.text14.text())
        smoothness_se = float(self.text15.text())
        compactness_se = float(self.text16.text())
        concavity_se = float(self.text17.text())
        concave_points_se = float(self.text18.text())
        symmetry_se  = float(self.text19.text())
        fractal_dimension_se = float(self.text20.text())

        radius_worst=float(self.text21.text())
        texture_worst= self.text22.text()
        perimeter_worst  = float(self.text23.text())
        area_worst  = float(self.text24.text())
        smoothness_worst = float(self.text25.text())
        compactness_worst = float(self.text26.text())
        concavity_worst = float(self.text27.text())
        concave_points_worst = float(self.text28.text())
        symmetry_worst  = float(self.text29.text())
        fractal_dimension_worst = float(self.text30.text())

        clf = pickle.load(open(r"model/breast_cancer.pkl","rb"))
        test = np.array([[radius_mean,	texture_mean,	perimeter_mean,	area_mean,	smoothness_mean,	compactness_mean,	concavity_mean,	concave_points_mean,	symmetry_mean,	fractal_dimension_mean,	radius_se,	texture_se,	perimeter_se,	area_se	,smoothness_se,	compactness_se,	concavity_se,	concave_points_se,	symmetry_se,	fractal_dimension_se,	radius_worst,	texture_worst,	perimeter_worst,	area_worst,	smoothness_worst,	compactness_worst,	concavity_worst	,concave_points_worst,	symmetry_worst,	fractal_dimension_worst ]])
        predicition = clf.predict(test)

        if predicition == 0:
            QMessageBox.about(self, "Title", "the Diagnosis malignant")
           
        elif predicition==1:
            QMessageBox.about(self, "Title", "the Diagnosis benign")
            
            



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()        

