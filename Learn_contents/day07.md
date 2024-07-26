# 객체 지향 프로그래밍
## 1. 절차 지향 프로그래밍
  - 프로그램을 '데이터'와 '절차'로 구성하는 방식의 프로그래밍 패러다임
### 절차 지향 프로그래밍 특징
---
  - "데이터"와 해당 데이터를 처리하는 "함수(절차)"가 분리되어 있으며, 함수 호출의 흐름이 중요
  - 코드의 순차적인 흐름과 함수 호출에 의해 프로그램이 진행
  - 실제로 실행되는 내용이 무엇인가가 중요
  - 데이터를 다시 재사용하거나 하기보다는 처음부터 끝까지 실행되는 결과물이 중요한 방식
### 소프트웨어 위기
---
  - 하드웨어의 발전으로 컴퓨터 계산용량과 문제의 복잡성이 급격히 증가함에 따라 소프트웨어에 발생한 충격
## 2. 객체 지향 프로그래밍
  - 데이터와 해당 데이터를 조작하는 메서드를 하나의 객체로 묶어 관리하는 방식의 프로그래밍 패러다임
### 절차 지향 vs 객체 지향
---
|절차 지향|객체 지향|
|:---:|:---:|
|데이터와 해당 데이터를 처리하는 함수(절차)가 분리|데이터와 해당 데이터를 처리하는 메서드(메시지)를 하나의 객체(클래스)로 묶음|
|함수 호출의 흐름이 중요|객체 간 상호작용과 메시지 전달이 중요|

### 클래스
---
  - 파이썬에서 타입을 표현하는 방법
  - 객체를 생성하기 위한 설계도
  - 데이터와 기능을 함께 묶는 방법을 제공
### 객체
---
  - 클래스에 정의한 것을 토대로 메모리에 할당된 것
  - '속성'과 '행동'으로 구성된 모든 것
#### 객체 예시
---
|속성(정보)|행동(동작)|
|:---:|:---:|
|직업 : 가수|랩()|
|생년월일 : XX.XX.XX|댄스()|
|국적 : 대한민국|소몰이()|
### 클래스와 객체
---
  - 클래스로 만든 객체를 **인스턴스** 라 부른다.
  - 아이유는 객체다(O)
  - 아이유는 인스턴스다(X)
  - 아이유는 가수의 인스턴스다(O)
#### 인스턴스
---
  - 클래스의 속성과 행동을 기반으로 생성된 개별 객체
#### 클래스와 객체
---
  - 변수 name의 타입은 str 클래스다.
  - 변수 name은 str클래스의 인스턴스이다.
  - 우리가 사용해왔던 데이터 타입은 사실 모두 클래스였다.
``` python
name = 'Alice'

print(type(name)) # <class 'str'>
```

#### 하나의 객체는 특정 타입의 인스턴스이다.
---
### 객체 정리
---
  - 타입(type) : 어떤 연산자와 조작이 가능한가?
  - 속성(attribute) : 어떤 상태(데이터)를 가지는가?
  - 조작법(method) : 어떤 행위(함수)를 할 수 있는가?
## 3. 클래스
  - 파이썬에서 타입을 표현하는 방법
  - 객체를 생성하기 위한 설계도
  - 데이터와 기능을 함께 묶는 방법을 제공
### 클래스 정의
---
  - class 키워드
  - 클래스 이름은 파스칼 케이스(Pascal Case)방식으로 작성
``` python
class MyClass:
  pass
```
#### 인스턴스 생성 및 활용
``` python
class Person:
  iu = Person()
  iu.메서드()
  iu.attribute()
```
#### 클래스 구조
---
  - 생성자 메서드
    - 객체를 생성할 때 자동으로 호출되는 특별한 메서드
    - __init__ 이라는 이름의 메서드로 정의되며, 객체의 초기화를 담당
    - 생성자 함수를 통해 인스턴스를 생성하고 필요한 초기값을 설정
  - 인스턴스 변수
    - 인스턴스(객체)마다 별도로 유지되는 변수
    - 인스턴스마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화됨
  - 클래스 변수
    - 클래스 내부에 선언된 변수
    - 클래스로 생성된 모든 인스턴스들이 공유하는 변수
  - 인스턴스 메서드
    - 각각의 인스턴스에서 호출할 수 있는 메서드
    - 인스턴스 변수에 접근하고 수정하는 등의 작업을 수행
``` python
class Person:
    blood_color = 'red'

    def __init__(self, name): # 
        self.name = name
    
    def singing(self):
        return f'{self.name}가 노래합니다.'

# 인스턴스 생성
singer1 = Person('iu')

# (인스턴스) 메서드 호출
print(singer1.singing()) # iu가 노래합니다.

# 속성(변수) 접근
print(singer1.blood_color) # red

# 인스턴스 속성(변수)
print(singer1.name) # iu
```

#### 클래스 변수 활용
---
  - 가수가 몇 명인지 확인하고 싶다면?
    - 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정할 수 있다.
  - class.class_variable로 클래스 변수 참조하기
``` python
class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

c1 = Circle(5)
c2 = Circle(10)

print(c1.r) # 5
print(c2.r) # 10

# c1의 인스턴스 변수 pi를 생성
c1.pi = 100

print(Circle.pi) # 3.14
print(c1.pi) # 100
print(c2.pi) # 3.14
```

## 4. 메서드
### 메서드 종류
---
  - 인스턴스 메서드
  - 클래스 메서드
  - 정적 메서드
### 인스턴스 메서드
---
  - 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
  - 인스턴스의 상태를 조작하거나 동작을 수행
#### 인스턴스 메서드 구조
---
  - 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
    - 인스턴스의 상태를 조작하거나 동작을 수행
  - 반드시 첫 번째 매개변수로 인스턴스 자신(self)을 전달받음
``` python
class MyClass:

  def instance_method(self, arg1, ...):
    pass
```
#### self 동작 원리
---
  - upper 메서드를 사용해 문자열 'hello'를 대문자로 변경하기
``` python
'hello'.upper()
```
  - 하지만 실제 파이썬 내부 동작은 다음과 같이 진행됨
``` python
str.upper('hello')
```
  - str클래스가 upper 메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것
  - 인스턴스 메서드의 첫번째 매개변수가 반드시 인스턴스 자기 자신인 이유
  - 객체 지향 방식의 메서드로 호출하는 표현(단축형 호출)
  - 'hello'라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자로 활용되는 것이 아닌 객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적인 표현인 것

### 생성자 메서드
---
  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
  - 인스턴스 변수들의 초기값을 설정
``` python
class Person:
  def __init__(self):
    pass
```
#### 생성자 메서드 예시
``` python
class Person:
    def __init__(self, name):
        # 좌변의 name : 인스턴스 변수 name
        # 우변의 name : 생성자 메서드의 매개변수이름
        self.name = name
        print('인스턴스가 생성되었습니다.')

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')

person1 = Person('지민') # 인스턴스가 생성되었습니다.
person1.greeting() # 안녕하세요 지민입니다.
Person.greeting(person1) # 안녕하세요 지민입니다.
```
### 클래스 메서드
---
  - 클래스가 호출하는 메서드
  - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
### 클래스 메서드 구조 및 예시
---
  - @classmethod 데코레이터를 사용하여 정의
  - 호출 시, 첫번째 인자로 해당 메서드를 호출하는 클래스(cls)가 전달됨
> 클래스 메서드 예시
``` python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def number_of_population(cls):
        # 단일 클래스일때는 (상속이 없을 때 즉 하위 클래스가 없을 때)
        # cls.count는 Person.count와 동일하다.
        print(f"인구수는 {cls.count}입니다.")


person1 = Person('iu')
person2 = Person('BTS')

Person.number_of_population()
```
### 스태틱(정적) 메서드
---
  - 클래스와 인스턴스와 상관없이 독립적으로 동작하는 메서드
  - 주로 클래스와 관련이 있지만 인스턴스와 상호작용이 필요하지 않은 경우에 사용
### 스태틱 메서드 구조 및 예시
---
  - @staticmethod 데코레이터를 사용하여 정의
  - 호출 시 필수적으로 작성해야 할 매개변수가 없음
    - 즉, 객체 상태나 클래스 상태를 수정할 수 없으며 단지 기능(행동)만을 위한 메서드로 사용
> 스태틱 메서드 예시
  - 단순히 문자열을 조작하는 기능을 제공하는 메서드 예시
``` python
class StringUtils:
    def __init__(self): # 작성하지 않으면 파이썬에서 알아서 실행해준다.
        pass            # 하지만 권장하지 않으므로 꼭 작성해주자.

    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def capitalize_string(string):
        return string.capitalize()

text = 'hello, world'

result1 = StringUtils.reverse_string(text)
print(result1) # dlrow ,olleh
result2 = StringUtils.capitalize_string(text)
print(result2) # Hello, world
```
### 메서드 정리
---
  - 인스턴스 메서드
    - 인스턴스의 상태를 변경하거나, 해당 인스턴스의 특정 동작을 수행
  
  - 클래스 메서드
    - 인스턴스의 상태에 의존하지 않는 기능을 정의
    - 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
  
  - 스태틱 메서드
    - 클래스 및 인스턴스와 관련이 없는 일반적인 기능을 수행
### 누가 어떤 메서드를 사용해야 할까
---
  - 클래스가 사용해야 할 것
    - 클래스 메서드
    - 스태틱 메서드
  - 인스턴스가 사용해야 할 것
    - 인스턴스 메서드
#### 클래스가 할 수 있는 것
---
  - 클래스는 모든 메서드를 호출 할 수 있음
  - 하지만 클래스는 클래스 메서드와 스태틱 메서드만 사용하도록 한다.
``` python
instance = MyClass()
# 클래스가 할 수 있는 것
print(MyClass.instance_method(instance)) # ('instance method', <__main__.MyClass object at 0x000001EF3D3AEE20>)
print(MyClass.class_method()) # ('class method', <class '__main__.MyClass'>)
print(MyClass.static_method()) # static method
```
#### 인스턴스가 할 수 있는 것
---
  - 인스턴스는 모든 메서드를 호출 할 수 있음
  - 하지만 인스턴스는 인스턴스 메서드만 사용하도록 한다
``` python
instance = MyClass()

# 인스턴스가 할 수 있는 것
print(instance.instance_method()) # ('instance method', <__main__.MyClass object at 0x000001EF3D3AEE20>)
print(instance.class_method()) # ('class method', <class '__main__.MyClass'>)
print(instance.static_method()) # static method
```
## 할 수 있다 != 써도 된다
  - 각자의 메서드는 OOP 패러다임에 따라 명확한 목적에 따라 설계된 것이기 때문에
  - 클래스와 인스턴스 각각 올바른 메서드만 사용한다.
## 5. 참고
### 인스턴스와 클래스 간 이름 공간
---
  - 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
  - 인스턴스를 만들면, 인스턴스 객체가 생성되고 독립적인 이름 공간 생성
  - 인스턴스에서 특정 속성에 접근하면, 인스턴스 -> 클래스 순으로 탐색
``` python
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()  # unknown

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown
p2.name = 'Kim'
p2.talk()  # Kim

print(Person.name)  # unknown
print(p1.name)  # unknown
print(p2.name)  # Kim
```
#### 독립적인 이름공간을 가지는 이점
---
  - ㅇ
### 매직 메서드
---
  - 인스턴스 메서드
  - 특정 상황에 자동으로 호출되는 메서드
  - Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
  - 스페셜 메서드 혹은 매직 메서드라고 불림
  - 예시
### 데코레이터(Decorator)
---
  - 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

## 절차 지향과 객체 지향은 대조되는 개념이 아니다
  - 객체 지향은 기존 절차 지향을 기반으로 두고 보완하기 위해 객체라는 개념을 도입해 상속, 코드 재사용성, 유지보수성 등의 이점을 가지는 패러다임

``` python

class test:
  # instance variable : name, age

  __ssafy__(self, name, age):
    self.name = name
    self.age = age
    print('__ssafy__')


  def setdata(selt, name, age):
    self.name = name

  def __str__:
    return 'self.name'

_varable : 
__variable : 
```

@classMethod(func)
@staticMethod

- 포함관계인가? -> 선언된 Decorator 함수들 중에 하나,