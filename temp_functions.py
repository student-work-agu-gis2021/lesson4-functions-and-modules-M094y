def fahr_to_celsius(temp_fahrenheit):
  converted_temp = (temp_fahrenheit-32) / 1.8
  return converted_temp


def temp_classifier(temp_celsius):
  if (temp_celsius <-2):
   return 0
  if (temp_celsius >=-2) and (temp_celsius <2):
   return 1
  if (temp_celsius >=2) and (temp_celsius <15):
   return 2
  if (temp_celsius >=15):
   return 3
