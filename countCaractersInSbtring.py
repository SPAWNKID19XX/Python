import pprint
message = 'hdvervber cierh ueyrfgiefwue cieyyfgiwyehowiejdowimowuehiwe cwiefgwyegiwuncowenciwyefbiwyebiw ciwefgwiyehfoweniweiehfwuencwuenciwe'
       
count ={}
       
for car in message:
       count.setdefault(car, 0)
       count[car] += 1

print(pprint.pformat(count))