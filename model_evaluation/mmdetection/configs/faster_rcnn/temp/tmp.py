for i in [200, 1000, 5000, 25000]:
    for j in ["0.0", "0.2", "0.4", "0.6", "0.8", "1.0"]:
        with open("faster-rcnn_my_tmp.py", 'r', encoding='utf-8') as file:
            original_content = file.readlines()
        lines_to_add = [
            "REPLACE1 = 'yuxing/dataset/NIPS_dataset/annotations/mixed_annotations/merged_size"+str(i)+"_prop_realworld_"+j+".json'\n",
            "REPLACE2 = "+str(int(100000/i))+"\n"
            "REPLACE3 = "+str(max(1, int(10000/i)))+"\n"
        ]
        new_content = lines_to_add + original_content

        # 将新内容写回文件
        with open("faster-rcnn_my_"+str(i)+"_"+j+".py", 'w', encoding='utf-8') as file:
            file.writelines(new_content)