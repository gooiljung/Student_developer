**Python이란?**

1. 동적 형 변환 지원(변수에 다양한 객체를 자유롭게 할당)
2. 객체 지향 인터프리터 언어(모든 데이터는 객체)
3. 범용 프로그래밍 언어

**기본 자료형**

1. NULL 대신해서 Python에서는 NONE 쓴다.
2. a="abcd" -> 문자열
3. a=['a','b','c'] -> 리스트
4. a=('a','b','c') -> 튜플

# **문자열**

작은 따옴표 큰 따옴표 상관없이 시작과 끝만 맞추고 여러줄은 따옴표 세 개를 이용한다.

*<메소드>*

1. replace() ->대체 str1.replace('t','a')
2. strip() ->공백제거 str2.strip()
3. join() ->문자열 합치기 "".join(str2)
4. split() ->문자열 쪼개기 str3.split('t)

**출력은 string+string 은 print(str1+str2) 이렇게 해도 돌아가는데 int+string 이런거는 java와 다르다.**
```a=3
   b=4
   print("{},{}".format(a,b))```

이렇게 하면 3,4 가 출력

*[sequence slicing]*

[start:end:step] start 를 명시하지 않으면 0 end 는 마지막 인덱스 step은 어떻게 이동할 것인지를 명시

문자열을 거꾸로 출력하려면?```a[::-1]```

#**리스트와 튜플**
리스트|튜플
---------|------
순서를 갖는 다양한 객체들의 시퀀스|상수 리스트
변경 가능한 객체|변경 불가능한 객체
[] 또는 list()로 생성|() 또는 tuple()로 생성
튜플이 더적은 메모리를 사용한다.

#Packing/Unpacking
**Packing**:여러 항목을 리스트 튜플에 넣는 것

**UnPacking**:리스트나 튜플에 있는 항목을 변수들로 풀어헤쳐 담는 것
#매핑-사전형(Dictionary)
1. key 와 value 형태로 짝지어진 사전 자료형
2. 순서열과 달리 사전형은 순서를 보장하지 않음
3. 중괄호로 생성 키랑 값을 콜론으로 (:)으로 구분
4. 변경 가능한 객체
5. 중괄호로 생성{} or dict()
6. .get(key) ->해당 value 값 가져오기
7. .items() ->key:value 가져오기
8. .keys() -> key 다 가져오기
9. .values() -> 값 다 가져오기
``` 
	d=dict();
	d['key']='value';
	d={'key':'value'}
	```

#if 조건문
``` 
    if a==b and a>0:
	     pass
	 elif:
        pass
    else:
        pass
```
들여쓰기는 스페이스 4번, *pass* (아무일도 하지 않는것)
#반복문
*-for문*: iterable 한 객체를 사용한다 (sequence or iterator or generator)

for 요소 in 반복가능한 객체:

*-while문*: while 조건: 조건식이 true일때 계속 돔

*for문 활용*

```
def prac():
    for i in range(1,50):
        if i<40:
            continue
        elif i==51:
            break
        else:
            print(i)
    else:
        print('못찾음')
prac()
```
*while문 활용*

```
def fortowhile():
    i=1
    while i<50:
        if i<40:
            pass
        elif i==51:
            break
        else:
            print(i)
        i+=1
        
    else:
        print('못찾음')
fortowhile()
```
#컴프리헨션
반복문과 조건문을 결합하여 간단하게 코드를 만들 수 있다.
**0~50 까지 숫자 중 3의 배수만 포함하는 리스트 컴프리헨션을 만들자**
```
list2 =[x for x in range(1,51) if x%3==0];
list2
```
**[(1,1),(2,3)...(10,100)] 해당하는 리스트 컴프리 헨션을 만들자**
```
list=[(x,x*x) for x in range(1,11)];
list
```
#함수

1. 자바의 클래스처럼 반복 사용할것은 def()로 만들자.
2. Python에서 함수는 1급 객체
 
*함수의 인자로 1)인자 2)위치인자 3)키워드인자*

1. 인자는 그냥 변수명 아무거나 써놓으면 되는듯
2. *위치인자* 함수의 매개변수를 튜플로 묶기위에 * 사용한다. def prac(*args):
3. *키워드 인자* 함수의 매개변수를 딕셔너리로 묶기위해 ** 사용한다. def prac(**args):

#모듈과 패키지
*모듈*-> 파이썬 파일

import [모듈],import [모듈] as [다른이름], from [모듈] import [필요한 부분]

*패키지*->파일 디렉토리

**구구단 함수 만들기**

```
def gugudan(n):
    for i in range(1,10):
        print('{}*{}={}'.format(n,i,i*n))
gugudan(5)
```

#객체와 클래스
***객체***

1. 데이터와 데이터에 관련되는 동작을 모두 포함할 수 있는 개념적 존재
2. 클래스를 실체화 한것이며 instance라고 한다.
3. 데이터 와 코드 를 모드 포함(변수,함수)

***클래스***

1. 파이썬은 모든 자료형이 객체
2. 객체는 자료형으로부터 만든다.
3. 클래스는 새로운 객체 자료형을 정의하는 자료형

**클래스 생성**

자바와 비슷하게 하면 된다.

```	
class prac(상속하고싶은 클래스):
	def __init__(self,study_name,num):
	    self.study_name=study_name
	    self.num=num
```
생성자를 쓰고 싶은 경우에는 init으로 생성자를 만든다.


#Decorator
데코레이터는 쉽게 말해서 함수를 꾸며주는 함수로써 기존 함수에 기능을 추가하거나 새로운 함수를 만드는 역할을 하며 어떤 동작을 함수의 전/후에 수행해야 하거나 공통적으로 사용하는 코드를 쉽게 관리하기 위해 사용한다.

***문제***

시간을 측정하는 decorator함수 작성[시간 측정] import time    t1 = time.time()프로그램 실행 t2 = time.time()time = t2-t1

```
import time
def count():
    t1,t2
    def wrapper(*args,**kwargs):
        t1=time.time()
        t2=time.time()
        return t2-t1
    return wrapper
k=count()
k()
//wrapper 를 오브젝트로 넘겼기에 그거를 함수호출로 
오브젝트를 받고 k()하면 함수형식으로 받는다
```

#Iterator
1. iterator는 반복가능한 iterable 의 객체 중 하나
2. next() 메소드가 있다.(자바의 iterator 랑 동일)
3. next()의 마지막은 stopiteration 예외 발생

***iterator 연습***

```
def prac():
    a=['a','b','c','d','e']
    it=iter(a)
    while True:
        try :
            print(next(it))
        except StopIteration:
               break; 
prac()
```

#Generator

1. yield문이 있으면 모두 Generator
2. 순환할 때마다 필요한 값을 만들어 값을 발생시킴
3. lazy facotry(값 생산을 연기함 필요할 때마다 발생시켜서)
4. StopIteration 을 일으키며 종료

***yield?***

 generator 함수가 실행 중 yield 를 만날 경우, 해당 함수는 그 상태로 정지 되며, 반환 값을 next() 를 호출한 쪽으로 전달 하게 된다. 이후 해당 함수는 일반적인 경우 처럼 종료되는 것이 아니라 그 상태로 유지되게 된다. 즉, 함수에서 사용된 local 변수나 instruction pointer 등과 같은 함수 내부에서 사용된 데이터들이 메모리에 그대로 유지되는 것이다. 

***generator 연습***

```
def fib():
   prev, curr = 0, 1
   while True:
       yield curr
       prev, curr = curr, prev + curr
a=fib()
for i in a:
    print(i)
```






