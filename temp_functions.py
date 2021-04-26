#functions relate temperature calculation in problem 3

#define fahr_to_celsius
def fahr_to_celsius(temp_fahrenheit):
#input: temperature in fahrenheit
#output: temperature in celsius from fahrenheit by function
  converted_temp=(temp_fahrenheit-32)/1.8
  return converted_temp

#define temp_classifier
def temp_classifier(temp_celsius):
#input: temperatures in celsius
#output: number of class which is devided by given rules
  if(temp_celsius<-2):
   return 0
  elif((temp_celsius>=-2)and(temp_celsius<2)):
    return 1
  elif((temp_celsius>=2)and(temp_celsius<15)):
    return 2
  elif((temp_celsius>=15)):
    return 3