def decomposition(x): # 분해합 구하는 함수
  de=x
  for i in range(len(str(x))):
    de+=x%10
    x=x//10
  return de

num=int(input())  # 숫자 입력

temp=num-num%10-1 # 일의자리가 9로 끝나는 num보다 작은 수 중, 제일 큰 수
while decomposition(temp)>=num:
  temp-=10

while True:
  if decomposition(temp)==num:
    print(temp)
    break
  else:
    temp+=1