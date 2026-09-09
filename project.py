
from pkgutil import get_data


Name = input("Enter your fuul name :")

clean_name = Name.strip()
formatted_name = clean_name .title()
list_name = formatted_name.split()
first_name = list_name [0]

scores = [45, 80, 90]

new_score =int(input("Enter a naw score :"))
scores.append(new_score)
total_score = sum(scores)
average_score = total_score / len(scores)


system_info = ("disha web school", 2027 )
My_skills = { "html","python","css"}
course_skills = {"python","c++","git"}
all_skills = My_skills.union(course_skills)
shared_skills = My_skills.intersection(course_skills)

user_data ={
    "full_name": formatted_name,
    "first_name":first_name,
     "scores":scores,
     "total": total_score,
     "average": average_score,
     "skills": all_skills
}
    
dict_keys_list = list(user_data.keys())
dict_values_list = list(user_data.values())

print("\n" + "=" * 40)
print(f"   STUDENT REPORT - {system_info[0]} ({system_info[1]})")
print("=" * 40)

print(f"Full Name   : {user_data['full_name']}")
print(f"First Name  : {user_data['first_name']}")
print("-" * 40)

print(f"Scores List : {user_data['scores']}")
print(f"Total Score : {user_data['total']}")
print(f"Average     : {user_data['average']}")
print("-" * 40)

print(f"All Skills  : {user_data['skills']}")
print(f"Shared Skills: {shared_skills}")
print("-" * 40)

print(f"Dictionary Keys Saved: {dict_keys_list}")
print(f"Dictionary values Saved: {dict_values_list}")
print("=" * 40)