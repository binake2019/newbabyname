import pickle
import os
import random
import datetime

now = datetime.datetime.now().strftime('%m%d%H%M')
print(now)
def load_dict(name):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
os.chdir('d:\\起名字')
dict_shijing = load_dict('name_shi')
dict_tangshi = load_dict('name_tangshi')
dict_songci = load_dict('name_ci')

dict_all = dict()
for i in dict_shijing.keys():
    dict_all[i] = dict_shijing[i]

for i in dict_tangshi.keys():
    dict_all[i] = dict_tangshi[i]

for i in dict_songci.keys():
    dict_all[i] = dict_songci[i]

print(len(dict_all))
f = open('d:\\起名字\\name'+now+'.txt', 'a')
for p in range(10000):
    num1 = random.randint(0, len(dict_all) - 1)  # 随机选一首诗歌
    ls_name = []
    for i in dict_all.keys():
        ls_name.append(i)
    shi_name = ls_name[num1]
    num2 = random.randint(0, len(dict_all[shi_name]) - 1)
    ls_sentens = dict_all[shi_name][num2]

    num3 = random.randint(0, len(ls_sentens) - 1)
    num4 = random.randint(0, len(ls_sentens) - 1)

    l1 = ['，', '；', '。', '！', '？', '、', '《', '》', '[', ']', '□', ',', '］', '　', '：'
        , '不', '薨', '死', '贱', '凄', '惨', '魂', '悔', '病', '屠', '残', '瘴', '歇', '阴', '愁', '难', '怕', '侵', '虫'
        , '贫', '穷', '杀', '误', '藟', '催', '衢', '男', '役', '妻', '刀', '苦', '卒', '妇', '亡', '歼', '婚', '灭', '夭'
          , '雄']
    l2 = '123465789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' \
         '”）)(）?/<>;:？、' \
         '.!矣昏泪窠禁寤丁黑［我你他她氵悲嗟断老恨萋性惊搔舅怨螽窥蠋鬵欲乱旧而古' \
         '寘瘏吠禽反噬障人佛神倡把冥伤短漏骚盬之头弓逝'
    for i in l2:
        l1.append(i)
    try:
        while ls_sentens[num3] in l1 or ls_sentens[num4] in l1:
            num3 = random.randint(0, len(ls_sentens) - 1)
            num4 = random.randint(0, len(ls_sentens) - 1)
        xing = '唐'
        ls1 = ''.join(dict_all[shi_name])
        print('【' + xing + ls_sentens[num3] + ls_sentens[num4] + '】', shi_name[3:].strip(),
               file=f)
        print('-', ls_sentens, file=f)
    except Exception as e:
        print(e)
f.close()