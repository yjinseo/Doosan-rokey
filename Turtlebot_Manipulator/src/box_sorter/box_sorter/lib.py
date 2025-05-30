import json, os
from std_msgs.msg import String

# def flatten(lst):
#     single = False
#     if not isinstance(lst[0], list):
#         yield lst
#         single = True
#         #return lst
    
#     if not single:
#         for item in lst:
#             if isinstance(item, list) and isinstance(item[0], list):
#                 yield from flatten(item)
#             else:
#                 yield item


# def create_json_msg_test(command, data) -> String:
#     json_msg = String()

#     dict_ = []
#     for i, c in enumerate(flatten(command[::-1])):
#         header = True
#         data = data if isinstance(data[0], list) else [data]
#         for d in data:
#             dict_.append(dict(zip(c, d)))
#             header = False
#         if header:
#             dict_ = {c : [dict_]}

#     json_msg.data = json.dumps(dict_)

#     return json_msg

def create_json_msg(command:list, data:list) -> String:
    '''
    ex) create_json_msg(['red', 'blue', 'goal], [0, 1, 1])
    '''
    json_msg = String()

    json_msg.data = json.dumps(dict(zip(command, data)))

    return json_msg

def get_offset_params(file_path = 'offset_values.txt'):
    offsets = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                # 각 줄을 "변수명 : 값" 형식으로 분리하여 변수에 값을 넣음
                parts = line.strip().split(":")
                if len(parts) == 2:
                    var_name, value = parts
                    try:
                        # 값을 float로 변환하여 변수에 할당
                        value = float(value.strip())
                        if var_name == "right_low_x_offset ":
                            right_low_x_offset = value
                        elif var_name == "right_low_y_offset ":
                            right_low_y_offset = value
                        elif var_name == "right_high_x_offset ":
                            right_high_x_offset = value
                        elif var_name == "right_high_y_offset ":
                            right_high_y_offset = value
                        elif var_name == "left_low_x_offset ":
                            left_low_x_offset = value
                        elif var_name == "left_low_y_offset ":
                            left_low_y_offset = value
                        elif var_name == "left_high_x_offset ":
                            left_high_x_offset = value
                        elif var_name == "left_high_y_offset ":
                            left_high_y_offset = value
                    except ValueError:
                        pass
        return right_low_x_offset, right_low_y_offset, right_high_x_offset, right_high_y_offset, left_low_x_offset, left_low_y_offset, left_high_x_offset, left_high_y_offset



def count_yolo_classes(result:list, classes) -> dict:
    '''
    count yolo red, blue 검출 결과 
    '''
    cls_num = dict()
    for res in result:
        cls_num[classes[res]] = cls_num.get(classes[res], 0) + 1

    return cls_num

def get_yolo_cxcy_red_blue(result:list, goal_cls:str, classes:list = ['red', 'blue']):
    '''
    yolo 데이터에서 red, blue 중심점
    result : yolo_info data
    goal_cls : red, blue
    '''
    ret = False
    for res in result:
        cls = classes[res[0]]
        # 있으면 return
        if cls == goal_cls:
            ret = True
            return ret, res[1], res[2]
        print(f'cls = {cls},x = {res[1]}, y , {res[2]},')
    
    return None

if __name__ == '__main__':
    print('?')