def fahr_to_celsius(temp_fahrenheit):
  converted_temp = (temp_fahrenheit-32) / 1.8
  return converted_temp
"""
 parameter:temp_fahrenheit
 convert the input temperature from degrees Fahrenheit to degrees Celsius
 """


def temp_classifier(temp_celsius):
  if (temp_celsius <-2):
   return 0
  if (temp_celsius >=-2) and (temp_celsius <2):
   return 1
  if (temp_celsius >=2) and (temp_celsius <15):
   return 2
  if (temp_celsius >=15):
   return 3

 """
  parameter:temp_celsius
  classify 4 classes from 0 to 3
    If temp_celsius <-2　, then temp_classifier=0
    If temp_celsius >=-2 and temp_celsius <2　, then temp_classifier=1
    If temp_celsius >=2 and temp_celsius <15　, then temp_classifier=2
    If temp_celsius >=15　, then temp_classifier=3
  """
