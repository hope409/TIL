## 복습
### data Types
---
  - 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성
### 데이터 타입 분류
---
  - Numeric
  - Text Sequence
  - Sequence
  - Non-sequence
  - 기타(Boolean, None, Functions)
#### 데이터 타입이 필요한 이유
  - 값들을 구분하고, 어떻게 다뤄야 하는지를 알 수 있음
  - 요리 재료마다 특정한 도구가 필요하듯이 각 데이터 타입 값들도 각자에게 적합한 도구를 가짐
  - 타입을 명시적으로 지정하면 코드를 읽는 사람이 변수의 의도를 더 쉽게 이해할 수 있고, 잘못된 데이터 타입으로 인한 오류를 미리 예방

#### int
  - 정수를 표현하는 자료형
#### float
  - 실수를 표현하는 자료형
  - 프로그래밍 언어에서는 float는 실수에 대한 근삿값
### Sequence Types 특징
  - 순서
  - 인덱싱
  - 슬라이싱
  - 길이
  - 반복
### str
---
  - 문자열은 단일 문자나 여러 문자의 조합으로 이루어짐
  - 작은따옴표(') 또는 큰따옴표(")로 감싸서 표현

### Escape sequence
---
  - 역슬래시(\\) 뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
  - 파이썬의 일반적인 문법 규칙을 잠시 탈출한다는 의미

|예약문자|내용(의미)|
|:---:|:---:|
|\n|줄 바꿈|
|\t|탭|
|\ \ |백슬래시|
|\'|작은 따옴표|
|\"|큰 따옴표|

### String Interpolation
---
  - 문자열 내에 변수나 표현식을 삽입하는 방법
  - f-string

### 인덱스
---
- 시퀀스 내의 값들에 대한 고유한 번호로, 각값의 위치를 식별하는 데 사용되는 숫자

### 슬라이싱
---
  - 시퀀스의 일부분을 선택하여 추출하는 작업
  - 시작 인덱스와 끝 인덱스를 지정하여 해당 범위의 값을 포함하는 새로운 시퀀스를 생성

## 1. Sequence Types
### 1) list
---
  - 여러 개의 값을 순서대로 저장하는 변경 가능한 시퀀스 자료형
#### 리스트 표현
---
  - 0개 이상의 객체를 포함하며 데이터 목록을 저장
  - 대괄호([])로 표기
  - 데이터는 어떤 자료형도 저장할 수 있음
``` python
my_list_1 = []
my_list_2 = [1, 'a', 3, 'b', 5]
my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
```
#### 중첩된 리스트
---
  - 리스트는 안에다가 리스트를 하나 더 만들 수 있다.
  - 왜냐하면 리스트는 어떤 자료형도 저장할 수 있기 때문
``` python
my_list = [1, 2, 3, ['python', 'hello', 100]]

print(len(my_list)) # 4
print(my_list[3][1]) # hello
print(my_list[3][1][-1]) # o
```

#### 리스트는 가변이다.
---
  - 리스트의 내용은 변경이 가능하다.
``` python
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)
```

### 2) tuple
---
  - 여러 개의 값을 순서대로 저장하는 변경 불가능한 시퀀스 자료형
#### 튜플의 표현
  - 0개 이상의 객체를 포함하며 데이터 목록을 저장
  - 소괄호 () 로 표기
  - 데이터는 어떤 자료형도 저장할 수 있음
``` python
my_tuple_1 = ()
my_tuple_2 = (1, ) # 요소가 하나인 튜플은 꼭 ,를 입력해줘야 함
my_tuple_3 = (1, 'a', 3, 'b', 5)
```
#### 튜플은 어디에 쓰일까?
---
  - 튜플의 불변 특성을 사용한 안전하게 여러 개의 값을 전달, 그룹화, 다중 할당 등
  - 개발자가 직접 사용하기 보다 '파이썬 내부동작'에서 주로 사용됨
``` python
x, y = (10, 20)

print(x) # 10
print(y) # 20

# 파이썬은 쉼표(,)를 튜플 생성자로 사용하니 괄호는 생략 가능
x, y = 10, 20
```

### 3) range
---
  - 연속된 정수 시퀀스를 생성하는 변경 불가능한 자료형
#### range의 표현
---
  - range(시작 값, 끝 값, 증가 값)
  - range(n)
    - 0부터 n-1까지의 숫자의 시퀀스
  - range(n, m)
    - n부터 m-1까지의 숫자 시퀀스
#### range의 특징
---
  - 증가 값이 없으면 1씩 증가
  - 증가 값이 음수이면 감소 / 증가 값이 양수이면 증가
  - 증가 값이 0이면 에러
  - 증가 값이 음수이면 시작 값이 끝 값보다 커야 함
  - 증가 값이 양수이면 시작 값이 끝 값보다 작아야 함
``` python
my_range_1 = range(5)
my_range_2 = range(1, 10)

print(my_range_1)  # range(0, 5)
print(my_range_2)  # range(1, 10)

# 리스트로 형 변환 시 데이터 확인 가능
print(list(my_range_1)) # [0, 1, 2, 3, 4]
print(list(my_range_2)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 주로 반복문과 함께 활용
for i in range(5): # 0 1 2 3 4 순으로 출력
    print(i)
```

## 2. Non-sequence Types
### 1) dict
---
  - key - value 쌍으로 이루어진
  - 순서와 중복이 없는 변경 가능한 자료형
#### 딕셔너리의 표현
---
  - key는 변경 불가능한 자료형만 사용 가능(str, int, float, tuple, range, ...)
  - value는 모든 자료형 사용 가능
  - 중괄호 {}로 표기
``` python
my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict_1)  # {}
print(my_dict_2)  # {'key': 'value'}
print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}
```

### 2) set
---
  - 순서와 중복이 없는 변경 가능한 자료형
#### 세트 표현
---
  - 수학에서의 집합과 동일한 연산 처리 가능
  - 중괄호 {}로 표기
``` python
my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}

print(my_set_1)  # set()
print(my_set_2)  # {1, 2, 3}
print(my_set_3)  # {1} 세트는 중복이 없어서 1개만 남음
```

#### 세트의 집합 연산
``` python
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2)  # {1, 2}

# 교집합
print(my_set_1 & my_set_2)  # {3}
```

## 3. 기타
### 1) None
---
  - 파이썬에서 '값이 없음'을 표현하는 자료형
``` python
# None
variable = None
print(variable)  # None
```

### 2) Boolean
---
  - 참(True)과 거짓(False)을 표현하는 자료형
``` python
# Boolean
bool_1 = True
bool_2 = False
print(bool_1)  # True
print(bool_2)  # False
print(3 > 1)  # True
print('3' != 3)  # True
```
## 4. 컬렉션
  - 여러 개의 항목 또는 요소를 담는 자료 구조
  - str, list, tuple, set, dict

|컬렉션|변경 가능 여부|순서 여부|
|:---:|:---:|:---:|
|str|X|O|
|list|O|O|
|tuple|X|O|
|dict|O|X|
|set|O|X|

## 5. 형변환
  - 한 데이터 타입을 다른 데이터 타입으로 변환하는 과정
  - 암시적 형변환 / 명시적 형변환

### 1) 암시적 형변환
---
  - 파이썬이 자동으로 수행하는 형변환
#### 암시적 형변환 예시
---
  - 정수와 실수의 연산에서 정수가 실수로 변환됨
  - Boolean과 Numeric Type에서만 가능
``` python
print(3 + 5.0) # 8.0

print(True + 3) # 4

print(True + False) # 1
```

### 2) 명시적 형변환
---
  - 프로그래머가 직접 지정하는 형변환
  - 암시적 형변환이 아닌 경우를 모두 포함
#### 명시적 형변환 예시
---
  - str -> int : 형식에 맞는 숫자만 가능
``` python
print(int('1')) # 1

# ValueError: invalid literal for int() with base 10: '3.5'
print(int('3.5'))

print(int(3.5)) # 3

print(float('3.5')) # 3.5
```
  - int -> str : 모두 가능
``` python
print(str(1) + '등') # 1등
```

#### 컬렉션 간 형변환 정리

||str|list|tuple|range|set|dict|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|str||O|O|X|O|X|
|list|O||O|X|O|X|
|tuple|O|O||X|O|X|
|range|O|O|O||O|X|
|set|O|O|O|X||X|
|dict|O|O|O|X|O||
  - 이때 dict는 key만 형변환이 가능하다.


## 6. 연산자
### 1) 산술연산자
|기호|연산자|
|:---:|:---:|
|-|음수부호|
|+|덧셈|
|-|뺼셈|
|*|곱셈|
|/|나눗셈|
|//|몫|
|%|나머지|
|**|지수|

### 2) 복합 연산자
---
  - 연산과 할당이 함께 이뤄짐

|기호|예시|의미|
|:---:|:---:|:---:|
|+=|a += b|a = a + b|
|-=|a -= b|a = a - b|
|*=|a *= b|a = a * b|
|/=|a /= b|a = a / b|
|//=|a //=b|a = a // b|
|%=|a %= b|a = a % b|
|**=|a **= b|a = a ** b|


``` python
# 복합 연산자
y = 10
y -= 4
# y = y - 4
print(y)  # 6

z = 7
z *= 2
print(z)  # 14

w = 15
w /= 4
print(w)  # 3.75

q = 20
q //= 3
print(q)  # 6
```

### 3) 비교 연산자
|기호|내용|
|:---:|:---:|
|<|미만|
|<=|이하|
|>|초과|
|>=|이상|
|==|같음|
|!=|같지 않음|
|is|같음|
|is not|같지 않음|

#### is 비교 연산자
---
  - 메모리 내에서 같은 객체를 참조하는지 확인
  - == 는 동등성(equality) is는 식별성(identity)
  - 값을 비교하는 ==와 다름
  - 표그려넣기
#### 비교 연산자 예시
``` python
# 비교 연산자
print(3 > 6)  # False
print(2.0 == 2)  # True
print(2 != 2)  # False
print('HI' == 'hi')  # False
print(1 == True)  # True

# SyntaxWarning: "is" with a literal. Did you mean "=="?
# ==은 값(데이터)을 비교하는 것이지만 is는 레퍼런스(주소)를 비교하기 때문
# 아래 조건은 항상 False이기 때문에 is 대신 ==를 사용해야 한다는 것을 알림
print(1 is True)  # False
print(2 is 2.0)  # False
print(1 == True)  # True
print(2 == 2.0)  # True
```

### 4) 논리 연산자
  - 표그리기

#### 논리 연산자 예시
``` python
# 논리 연산자
print(True and False)  # False

print(True or False)  # True

print(not True)  # False

print(not 0)  # True
```
  - 비교 연산자와 함께 사용 가능
``` python
# 논리 연산자 & 비교 연산자
num = 15
result = (num > 10) and (num % 2 == 0)
print(result)  # False

name = 'Alice'
age = 25
result = (name == 'Alice') or (age == 30)
print(result)  # True
```

## 7. 단축평가
  - 논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작

#### 단축평가 예시 문제
```python
# 단축 평가

vowels = 'aeiou'
# ('a' and 'b')의 연산결과는 b임
# 왜냐면 값이 있다면 True로 평가하여 and연산을 이어서함
print(('a' and 'b') in vowels)  # False
print(('b' and 'a') in vowels)  # True

print(3 and 5)  # 5
# 3 and 0에서 3이 값이 있어서 True 이고 and연산을 시작 0을 만나서 False 이고 0
print(3 and 0)  # 0
# 0 and 3에서 0이 False이므로 and 연산을 하지 않음
print(0 and 3)  # 0
print(0 and 0)  # 0

# 5 or 3에서 5가 이미 값이 있기 때문에 True여서 or연산을 진행 안함
print(5 or 3)  # 5
print(3 or 0)  # 3
print(0 or 3)  # 3
print(0 or 0)  # 0
```

#### 단축평가 이유
---
  - 코드 실행을 최적화하고, 불필요한 연산을 피할 수 있도록 함
### 1) 멤버십 연산자
---
  - 특정 값이 시퀀스나 다른 컬렉션에 속하는지 여부를 확인
  - 표 그리기
#### 멤버십 연산자 예시
``` python
# 멤버십 연산자

word = 'hello'
numbers = [1, 2, 3, 4, 5]

print('h' in word)  # True
print('z' in word)  # False

print(4 not in numbers)  # False
print(6 not in numbers)  # True
```

### 2) 시퀀스형 연산자
---
  - \+ 와 * 는 시퀀스 간 연산에서 산술 연산자일때와 다른 역할을 가짐
#### 시퀀스형 연산자 예시
``` python
# 시퀀스형 연산자
print('Gildong' + ' Hong')  # Gildong Hong

print('hi' * 5)  # hihihihihi

print([1, 2] + ['a', 'b'])  # [1, 2, 'a', 'b']

print([1, 2] * 2)  # [1, 2, 1, 2]
```

### 3) 연산자 우선순위 정리
  - 표그리기