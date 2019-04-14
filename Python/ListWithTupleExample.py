list=[('O’Hare International','ORD'),('Los Angeles International Airport','LAX'),('Dallas/Fort Worth International Airport','DFW'),('Denver International Airport','DEN')]

for values in list:
    (airportname,airportcode)=values
    print('The code for {} is {}'.format(airportname,airportcode))
