def intTime2strTime(intTime):
    min=intTime//60
    sec=intTime%60
    
    if min<10:
        strmin="0"+str(min)
    else:
        strmin=str(min)
        
    if sec<10:
        strsec = "0" + str(sec)
    else:
        strsec = str(sec)
        
    return strmin+":"+strsec

def str2inttime(strTime):
    intlist=list(map(int, strTime.split(":")))
    return intlist[1] + 60*intlist[0]


def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    if (str2inttime(op_start) <= str2inttime(pos)) and (str2inttime(pos) <= str2inttime(op_end)):
        pos=op_end
    
    curTime=str2inttime(pos)
    endTime=str2inttime(video_len)
    opsttTime=str2inttime(op_start)
    opendTime=str2inttime(op_end)
    
    for i in range(len(commands)):
                          
        if (curTime >= opsttTime) and (curTime <= opendTime):
            curTime=opendTime
        
                          
        if commands[i]=="next":
            if (curTime+10>=endTime):
                curTime=endTime
            else:
                curTime+=10
        elif commands[i] == "prev":
            if(curTime-10 <=0):
                curTime=0
            else:
                curTime-=10
                
        if (curTime >= opsttTime) and (curTime <= opendTime):
            curTime=opendTime
    
    answer=intTime2strTime(curTime)
    
    return answer