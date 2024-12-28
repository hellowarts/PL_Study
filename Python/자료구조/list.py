# 1. 리스트 생성
empty_list = []
another_empty_list = list()
weekdays = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday"]

# 2. 리스트 사용
print(weekdays[2]) # Wednesday
print(weekdays[0:2]) # ['Monday', "Tuesday"]
print(weekdays[::2]) # ['Monday', "Wednesday", "Friday"]
print(weekdays[::-1]) # 역 : ['Friday', 'Thursday', 'Wednesday', 'Tuesday', 'Monday']
print(weekdays.index("Wednesday")) # 2
print("Tuesday" in weekdays) # True
print(weekdays.count('Tuesday')) # 1 
print(len(weekdays)) # 5

# 3. 리스트 추가
marxes = []
others = ["Gummo", "karl"]
marxes.append('Zeppo')

# 리스트 병합
marxes += others
print(marxes)

# 특정 위치에 값 추가
marxes.insert(2, "Harpo")
print(marxes)

# 4. 리스트 삭제
del marxes[1]
marxes.remove("karl")
print(marxes.pop(1))

# 5. 기타 사용법
## 리스트 문자열로 병합
marxes = ["Groucho", "Chico", "Harpo"]
print(', '.join(marxes)) 

## 리스트 정렬
marxes.sort() # 리스트 자체를 내부적으로 정렬'
print(marxes) 
print(sorted(marxes)) # 리스트의 정렬된 복사본을 반환 

## 리스트 복사
### 얕은 복사
a = [1, 2, 3]
print(a)
b = a
print(b)
a[0] = 'surpise'
print(a)
print(b) # a값만 변경했는데 b의 값도 변경되어 있다.

### 깊은 복사 3가지 방법
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = "integer lists are boring"
print(a, b, c, d)