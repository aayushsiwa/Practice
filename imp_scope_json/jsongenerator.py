import json
from employee import details, age, title, employee_name

def create_dict(name, age, title):
    dict={"first_name":name,"age":age,"title":title}
    return dict
    raise NotImplementedError()

def write_json_to_file(json_obj, output_file):
    with open(output_file,"w") as f:
        f.write(json_obj)
        f.close()
    return None
    raise NotImplementedError()

def main():
    details()
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))
    json_object = json.dumps(employee_dict)
    print("json_object: " + str(json_object))
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()