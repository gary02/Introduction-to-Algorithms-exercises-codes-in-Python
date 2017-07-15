def choose_sort(list_):
    working_index = 0
    tmp_smallest_value_index = 0
    for i in list_:
        tmp_smallest_value_index = working_index
        for index,item in enumerate(list_):
            if index < working_index:
                continue
            if item < list_[tmp_smallest_value_index]:
                tmp_smallest_value_index = index
        print tmp_smallest_value_index
        list_[tmp_smallest_value_index],list_[working_index] = list_[working_index], list_[tmp_smallest_value_index]
        working_index+=1

    return list_

if __name__ == "__main__":
    print choose_sort([3,4,5,1,3,5,7,9,0,-9,5])
