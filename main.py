total_people=1000
strep=200
no_strep=800
positive_strep=int(0.85*strep)
negative_strep=strep-positive_strep
positive_no_strep=int(0.02*no_strep)
negative_no_strep=no_strep-positive_no_strep
total_positive=positive_strep+positive_no_strep
result=f"{positive_strep}out of {total_positive}"
print("People with strep",strep)
print("People without strep",no_strep)
print("Positive tests from strep group",positive_strep)
print("Positive tests from no strep group",positive_no_strep)
print("Total positive tests",total_positive)
print("-> If test is positive,chance of real strep",result)