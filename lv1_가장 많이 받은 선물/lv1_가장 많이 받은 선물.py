def solution(friends, gifts):
    answer = 0
    hash=dict() # 준사람 받은사람 테이블
    score=dict() # 선물 지수 테이블
    get=dict() # 받는 개수 테이블
	
	#초기화
    for i in friends:
        score[i]=0
        get[i]=0
        for j in friends:
            if i==j:
                continue
            hash[(i,j)]=0
    
	#테이블 채우기
    for g in gifts:
        tmp=g.split(" ")
        hash[(tmp[0],tmp[1])]+=1
    
	#선물 지수 계산
    for h in hash:
        score[h[0]]+=hash[h]
        score[h[1]]-=hash[h]
    
    # 다음 달 받는 선물 계산
    for i in friends:
        for j in friends:
            if friends.index(i) >= friends.index(j):
                continue
            if hash[(i,j)] == hash[(j,i)] or (hash[(i,j)]== 0 and hash[(j,i)]==0):
                if score[i] > score[j]:
                    get[i]+=1
                elif score[i] < score[j]:
                    get[j]+=1
                else:
                    pass
            if hash[(i,j)] > hash[(j,i)]:
                get[i]+=1
            elif hash[(i,j)] < hash[(j,i)]:
                get[j]+=1
            else:
                pass
   
    
    answer=max(get.values())
    return answer