#https://cpquery.cponline.cnipa.gov.cn/chinesepatent/index
#由于爬虫没跑通，从上面的网站手动搜索，手动复制页面内容到txt

import  pandas  as pd



leixing=['发明专利','外观设计','实用新型']



cols=[
"申请号",
'发明名称',
'申请人',
'专利类型',
'申请日',
'发明专利申请公布号',
'法律状态',
'案件状态',
'授权公告号',
'主分类号'
]
def process_copy_string(path):
    output_string=''
    with open(path, encoding="utf8") as f:
        data = f.readlines()
        print(f'行数:{len(data)}')


        input_string=''.join(data)
        patent_strings = input_string.replace("\n申请号/专利号","申请号/专利号")

        # Remove any empty strings from the list
        data =patent_strings.split('\n')
        # print(data)
        sep='手动分隔符'

    # 申请号/专利号： 
        for i in range(len(data)):
            line = data[i]
            for c in leixing:
                if f'{c} ' in line:
                    line = line.replace(f'{c} ',f'\n{c} ')
                line = line.replace(f'{c} ', f'{c}:')

            for e in cols:
                if e in line:
                    line = line.replace(e, sep + e)
            # print(line)

            data[i] = line

        print(f'行数:{len(data)}')
        max_columns = max(len(s.split(sep)) for s in data)
        df = pd.DataFrame([s.split(sep) + [''] * (max_columns - len(s.split(sep))) for s in data if s!=''], columns=['字段'+str(i) for i in range(max_columns)])
        # Save the DataFrame as an Excel file
        excel_path = path.replace('.txt','.xlsx')
        df.to_excel(excel_path, index=False)    

# keyword=['智能手表','智能戒指']
# path='PPG/发明专利 智能手表.txt'
# for c in leixing:
#     for k in keyword:
#         path=f'PPG/{c} {k}.txt'

#         process_copy_string(path)

# process_copy_string('PPG/发明专利 PPG.txt')
# process_copy_string('PPG/发明专利 脉搏波.txt')
process_copy_string('PPG/发明专利 辟谷.txt')
