import json
import re
import pyhttpx
import time
import pandas as pd

def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",}
    session = pyhttpx.HttpSession()
    try:
        #发送get请求
        html = session.get(url,headers = headers)
        #配置编码
        if html.status_code == 200: 
            print("成功过获取源代码")
            
    except Exception as e:
        print("获取源代码失败:%s"% e)
    
    return html.text 
def save_comment_message_to_csv(file_path, input_string,i,flag):
    df = pd.DataFrame(input_string)
    if flag==1:
        df.to_csv(file_path, index=False)
    else:
        existing_df = pd.read_csv(file_path)
        # 将新数据添加到已有数据的末尾
        combined_df = pd.concat([existing_df, df], ignore_index=True)
        # 将合并后的DataFrame保存为CSV文件
        combined_df.to_csv(file_path, index=False)
    return 0


def time_change(timestamp):
    time_local = time.localtime(timestamp)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return dt

def get_com_message(url,i,reflag=0):
    com_message={}
    com_page=get_html(url)
    response_json = json.loads(com_page)
    comments = response_json["data"]["comments"]
    flag=0
    for comment in comments:
        com_message['content']=[comment['content']]
        com_message['uid']=[comment['userInfo']['uid']]
        com_message['uname']=[comment['userInfo']['uname']]
        addtime=time_change(comment['addTime'])
        com_message['addtime']=[addtime]
        com_message['likes']=[comment['likes']]
        flag+=1
        #print(com_message)
        
        if (reflag==1):
            filepath='./data/redata/comment/comment'+str(i)+'.csv'
        else:
            filepath='./data/comment/comment'+str(i)+'.csv'
        save_comment_message_to_csv(filepath,com_message,i,flag)
    #input()

    return 0

def get_comment(url1,i,reflag=0):
    if reflag==1:
        html=get_html(url1)
    else:
        html=get_html('https:'+url1)
    id=re.search(r'"tvid":([^,]+)', html)
    url='https://sns-comment.iqiyi.com/v3/comment/get_baseline_comments.action?agent_type=118&agent_version=9.11.5&authcookie=f5Fm16J5c7m2qG1ZHqQuMPw5KoZvCJM9QcTRZlxC5h2UxSVbfGBm1iarm3kNhm3g0kHPC5Ac5&business_type=17&channel_id=0&content_id='
    url+=id.group(1)
    url+='&last_id=&need_vote=1&page_size=10&qyid=4a144ccab1fdc3f0e7bed7219f1d9d09&sort=HOT&tail_num=1'
    get_com_message(url,i,reflag)

if __name__ == "__main__":
    html=get_html('https://www.iqiyi.com/v_f04zzeosk0.html?r_area=recent_popular&r_source=1002&bkt=hp_bkt_02&e=26a0edcd042193c613ec61d063dd9a78&stype=2&vfrm=pcw_home&vfrmblk=pcw_home_hot&vfrmrst=pcw_home_hot_float_video_area6')
    #a = soup.find_all('script', id='__NEXT_DATA__')
    id=re.search(r'"tvid":([^,]+)', html)
    url='https://sns-comment.iqiyi.com/v3/comment/get_baseline_comments.action?agent_type=118&agent_version=9.11.5&authcookie=f5Fm16J5c7m2qG1ZHqQuMPw5KoZvCJM9QcTRZlxC5h2UxSVbfGBm1iarm3kNhm3g0kHPC5Ac5&business_type=17&channel_id=0&content_id='
    url+=id.group(1)
    url+='&last_id=&need_vote=1&page_size=10&qyid=4a144ccab1fdc3f0e7bed7219f1d9d09&sort=HOT&tail_num=1'
    get_com_message(url,1)
