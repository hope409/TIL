# 데이터구조
## 1. Data Structure
  - 여러 데이터를 효과적으로 사용, 관리하기 위한 구조(str, list, dict등)
### 1) 자료 구조
---
  - 컴퓨터 공학에서는 '자료 구조'라고 함
  - 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것
### 2) 데이터 구조 활용
---
  - 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 메서드를 호출하여 다양한 기능을 활용하기
### 3) 메서드
---
  - 객체에 속한 함수
  - 객체의 상태를 조작하거나 동작을 수행
#### 메서드의 특징
---
  - 메서드는 클래스(class) 내부에 정의되는 함수
  - 클래스는 파이썬에서 '타입을 표현하는 방법'이며 이미 은연중에 사용해왔음
  - 예를 들어 help 함수를 통해 str을 호출해보면 class 였다는 것을 확인 가능
#### 지금 시점에 알아야 할 것
---
  - 메서드는 어딘가(클래스)에 속해 있는 함수이며, 각 데이터 타입별로 다양한 기능을 가진 메서드가 존재
#### 메서드 호출 방법
---
  - 데이터 타입 객체.메서드()
#### 메서드 호출 예시
``` python
# 문자열 메서드 예시
print('hello'.capitalize()) # Hello

# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)

print(numbers) # [1, 2, 3, 4]
```
## 2. 시퀀스 데이터 구조
### 문자열
#### 문자열 조회/탐색 및 검증 메서드
---
|메서드|설명|
|:---:|:---:|
|s.find(x)|x의 첫 번째 위치를 반환.없으면, -1을반환|
|s.index(x)|x의 첫 번째 위치를 반환. 없으면, 오류 발생|
|s.isupper()|대문자 여부|
|s.islower()|소문자 여부|
|s.isalpha()|알파벳 문자 여부 *단순 알파벳이 아닌 유니코드 상 Letter(한국어도 포함)|
#### 문자열 조작 메서드(새 문자열 반환)
---
|메서드|설명|
|:---:|:---:|
|s.replace(old, new[,count])||

### .replace(old, new[,count])
---
  - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
``` python
text = 'Hello, world!'
new_text = text.replace('world', 'Python)
print(new_text) # Hello, Python
```
### .strip([chars])
---
  - 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
``` python
text = '  Hello, world!  '
new_text = text.strip()
print(new_text)
```
### .split(sep=None, maxsplit=-1)
---
  - 지정한 문자를 구분자로 문자열을 분리하여 문자열의 리스트로 반환
``` python
text = 'Hello, world!'
words = text.split(',')
words2 = text.split()
print(words) # ['Hello', ' world!']
print(words2) # ['Hello,', 'world!']
```
### 'separator'.join(iterable)
---
  - iterable의 문자열을 연결한 문자열을 반환
``` python
words = ['Hello', 'world!']
new_text = '-'.join(words)
print(new_text) # Hello-world!
```
### 문자열 조작 메서드
---
``` python
# capitalize
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1) # Hello, world!

# title
new_text2 = text.title()
print(new_text2) # Hello, World!

# upper
new_text3 = text.upper()
print(new_text3) # HELLO, WORLD!

# lower
new_text4 = text.lower()
print(new_text4) # hello, world!

# swapcase
new_text5 = text.swapcase() # 대소문자를 서로 교체
print(new_text5) # HEllO, WOrLD!
```
### 리스트
#### 리스트 값 추가 및 삭제 메서드
---
|메서드|설명|
|:---:|:---:|

#### .append(x)
---
  - 리스트 마지막에 항목 x를 추가
``` python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # [1, 2, 3, 4]
print(my_list.append(4)) # None
```

#### .extend(iterable)
---
  - 리스트에 다른 반복 가능한 객체의 모든 항목을 추가
``` python
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6]
# my_list.extend(5) # 에러 iterable이 아니어서
my_list.extend([5]) # iterable이어서 가능
print(my_list) # [1, 2, 3, 4, 5, 6, 5]
my_list.append([9, 9, 9])
print(my_list) # [1, 2, 3, 4, 5, 6, 5, [9, 9, 9]]
```
#### .insert(i, x)
---
  - 리스트의 지정한 인덱스 i 위치에 항목 x를 삽입
``` python
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list) # [1, 5, 2, 3]
```
#### .remove(x)
---
  - 리스트에서 첫 번째로 일치하는 항목을 삭제
``` python
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list) # [1, 3, 2, 2, 2]
```
#### .pop(i)
---
  - 리스트에서 지정한 인덱스의 항목을 제거하고 반환
  - 작성하지 않을 경우 마지막 항목을 제거
``` python
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0)

print(item1) # 5
print(item2) # 1
print(my_list) # [2, 3, 4]
```
#### .clear
---
  - 리스트의 모든 항목을 삭제
``` python
my_list = [1, 2, 3]
my_list.clear()
print(my_list) # []
```
#### 리스트 탐색 및 정렬 메서드
---
|문법|설명|
|:---:|:---:|

#### .index(x)
---
  - 리스트에서 첫 번째로 일치하는 항목 x의 인덱스를 반환
``` python
my_list = [1, 2, 3]
index = my_list.index(2)
print(index) # 1
```
#### .count(x)
---
  - 리스트에서 항목 x의 개수를 반환
``` python
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number) # 3
```
#### .reverse()
---
  - 리스트의 순서를 역순으로 변경(정렬 X)
``` python
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list.reverse()) # None
print(my_list) # [9, 1, 8, 2, 3, 1]
```
#### .sort()
---
  - 원본 리스트를 오름차순으로 정렬
``` python
# sort(오름차순 정렬)
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list) # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list) # [100, 3, 2, 1]
```
### 참고 문서
---
- [5.1 리스트 더 보기 참고](https://docs.python.org/ko/3.9/tutorial/datastructures.html#more-on-lists)

## 3. 복사
### 데이터 타입과 복사
---
  - 파이썬에서는 데이터에 분류에 따라 복사가 달라짐
  - "변경 가능한 데이터 타입"과 "변경 불가능한 데이터 타입"을 다르게 다룸

#### 할당
---
  - 할당을 할 시 주소가 들어감
  - b = a라고 하면 복사가 아닌 할당임
#### 리스트 복사 예시
---
  - 할당 연산자 (=)를 통한 복사는 해당 객체에 대한 객체 참조를 복사
``` python
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a) # [100, 2, 3, 4]
print(b) # [100, 2, 3, 4]

a = 20
b = a
b = 10
print(a) # 20
print(b) # 10
```
#### 복사 유형
---
- 1. 얕은 복사
- 2. 깊은 복사

#### 2. 얕은 복사
``` python
a = [1, 2, 3]
b = a[:]
c = a.copy()

b[0] = 100
c[0] = 999

print(a) # [1, 2, 3]
print(b) # [100, 2, 3]
print(c) # [999, 2, 3]
```
#### 얕은 복사의 한계
---
  - 2차원 리스트와 같이 한단계 더 들어가면 복사가 안된다.
``` python
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
b[2][1] = 100
print(a) # [1, 2, [3, 100, 5]]
print(b) # [1, 2, [3, 100, 5]]
```
#### 깊은 복사
---
``` python
import copy
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)
b[2][1] = 100
print(a) # [1, 2, [3, 4, 5]]
print(b) # [1, 2, [3, 100, 5]]
```

#### 문자열에 포함된 문자들의 유형을 판별하는 메서드
---
  - isdecimal()
    - 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
  - isdigit()
    - isdecimal()과 비슷하지만,유니코드 숫자도 인식
  - isnumeric()
    - isdigit()과 유사하지만, 몇 가지 추가적인 유니코드 문자들을 인식
    - (분수, 지수, 루트 기호도 숫자로 인식)