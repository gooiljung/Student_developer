# CSS
**css**는 HTML 요소의 **Style**을 표현한다.
# 셀렉터(selector,선택자)
-스타일을 적용하고자 하는 HTML 요소를 선택하는 것이다.

```
h1 {color:red;font-size:12px;}
```
이와 같은 Rule set의 집합을 스타일시트라 한다.

**Rule set**

1. h1:셀렉터 
2. { }: 선언 블록 
3. color,font-size: 프로퍼티(property)
4. red,12px: 값(property value)

**HTML은 CSS를 포함할 수 있다. css를 가지고 있지 않은 HTML은 브라우저에서 기본으로 적용하는 css에 의해 렌더링된다.**

# CSS 와 HTML의 연동(Link Style)

**HTML**

```
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="css/style.css">
  </head>
  <body>
    <h1>Hello World</h1>
    <p>This is a web page.</p>
  </body>
</html>
```

**CSS**

```
h1 { color: red; }
p  { background: blue; }
```


# Embedding Style

HTML 내부에 CSS 를 포함시키는 방식. 위의 Link Style이 더 좋다.

```
<!DOCTYPE html>
<html>
  <head>
    <style>
      h1 { color: red; }
      p  { background: aqua; }
    </style>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>This is a web page.</p>
  </body>
</html>
```

# Inline Style

HTML 요소의 style 프로퍼티에 CSS를 기술하는 방식이다. Link Style이 더 좋다.

```
<!DOCTYPE html>
<html>
  <body>
    <h1 style="color: red">Hello World</h1>
    <p style="background: aqua">This is a web page.</p>
  </body>
</html>
```

# Reset CSS 사용하기

Reset CSS는 기본적인 HTML 요소의 CSS를 초기화하는 용도로 사용된다. 즉 브라우저 별로 제각각인 디폴트 스타일을 하나의 스타일로 통일시켜 주는 역할을 한다.
***즉*** 크롬 파이어폭스 등등의 브라우저들에 reset css 를 하지 않으면 지멋대로 되는대 이것을 reset 으로 맞춰준다.

# 전체 셀렉터(Universal Selector)

패턴|	Description
---|----
*|	HTML 문서 내의 모든 요소를 선택한다. html 요소를 포함한 모든 요소가 선택된다. (head 요소도 포함된다)

```
<!DOCTYPE html>
<html>
<head>
  <style>
    /* 모든 요소를 선택 */
    * { color: red; }
  </style>
</head>
<body>
  <h1>Heading</h1>
  <div>
    <p>paragraph 1</p>
    <p>paragraph 2</p>
  </div>
  <p>paragraph 3</p>
</body>
</html>
```

# 태그 셀렉터(Type Selector)
이전에 계속 나온 방식

```
<style>
	p{color:red}
</style>
```

# ID 셀렉터(ID Selector)

패턴	|Description
---|----
 #id 어트리뷰트 값	|id 어트리뷰트 값을 지정하여 일치하는 요소를 선택한다. id 어트리뷰트 값은 중복될 수 없는 유일한 값이다.

```
<!DOCTYPE html>
<html>
<head>
  <style>
    /* id 어트리뷰트 값이 p1인 요소를 선택 */
    #p1 { color: red; }
  </style>
</head>
<body>
  <h1>Heading</h1>
  <div class="container">
    <p id="p1">paragraph 1</p>
    <p id="p2">paragraph 2</p>
  </div>
  <p>paragraph 3</p>
</body>
</html>
```
이러면 id=p1 인 부분만 색 바뀐다.

# 클래스 셀렉터(Class Selctor)

패턴	|Description
---|---
.class 어트리뷰트 값|	class 어트리뷰트 값을 지정하여 일치하는 요소를 선택한다. class 어트리뷰트 값은 중복될 수 있다. class 한번에 여러개 설정 가능.

```
<!DOCTYPE html>
<html>
<head>
  <style>
    /* class 어트리뷰트 값이 container인 모든 요소를 선택 */
    /* color 어트리뷰트는 자식 요소에 상속된다. */
    .container { color: red; }
    /* not supported in IE */
    #p2 { color: initial; }
  </style>
</head>
<body>
  <h1>Heading</h1>
  <div class="container">
    <p id="p1">paragraph 1</p>
    <p id="p2">paragraph 2</p>
  </div>
  <p>paragraph 3</p>
</body>
</html>
```

class ="container" 쪽에 p1,p2가 바뀌어야하는데 #p2로 initial 로 지정해서 p1만 바뀜

# 어트리뷰트 셀렉터(Attribute Selector)

패턴	|Description
---|---
셀렉터[어트리뷰트]|	지정된 어트리뷰트를 갖는 모든 요소를 선택한다.
셀렉터[어트리뷰트=”값”]|	지정된 어트리뷰트를 가지며 지정된 값과 어트리뷰트의 값이 일치하는 모든 요소를 선택한다.
셀렉터[어트리뷰트~=”값”]|	지정된 어트리뷰트의 값이 지정된 값을 (공백으로 분리된) 단어로 포함하는 요소를 선택한다.
셀렉터[어트리뷰트(이부분에 표 지정자랑 같은거라서 생략해놓음)=”값”] |	지정된 어트리뷰트의 값과 일치하거나 지정 어트리뷰트 값 뒤 연이은 하이픈(“값-“)으로 시작하는 요소를 선택한다
셀렉터[어트리뷰트^=”값”]|	지정된 어트리뷰트 값으로 시작하는 요소를 선택한다.
셀렉터[어트리뷰트$=”값”]|	지정된 어트리뷰트 값으로 끝나는 요소를 선택한다.
셀렉터[어트리뷰트*=”값”]|	지정된 어트리뷰트 값을 포함하는 요소를 선택한다.



```
<!DOCTYPE html>
<html>
<head>
  <style>
    /* a 요소 중에 href 어트리뷰트를 갖는 모든 요소 */
    a[href] { color: red; }
  </style>
</head>
<body>
  <a href="http://www.poiemaweb.com">poiemaweb.com</a><br>
  <a href="http://www.google.com" target="_blank">google.com</a><br>
  <a href="http://www.naver.com" target="_top">naver.com</a>
</body>
</html>
```

# 복합 셀렉터(Combinator)

**후손 셀렉터-**자신의 1 level 상위에 속하는 요소를 부모 요소, 1 level 하위에 속하는 요소를 자손 요소(자식 요소)라한다.

자신보다 n level 하위에 속하는 요소는 후손 요소(하위 요소)라 한다.

후손 셀렉터는 셀렉터A의 모든 후손(하위) 요소 중 셀렉터B와 일치하는 요소를 선택한다.
```
셀렉터 A 셀렉터 B
```


```
<!DOCTYPE html>
<html>
<head>
  <style>
    /* div 요소의 후손요소 중 p 요소 */
    div p { color: red; }
  </style>
</head>
<body>
  <h1>Heading</h1>
  <div>
    <p>paragraph 1</p>
    <p>paragraph 2</p>
    <span><p>paragraph 3</p></span>
  </div>
  <p>paragraph 4</p>
</body>
</html>
```

**자식 셀렉터-** 자손 셀렉터는 셀렉터 A의 모든 자식 요소중 셀렉터 B와 일치하는 요소를 선택한다.

```
셀렉터 A > 셀렉터 B
```

```
<!DOCTYPE html>
<html>
<head>
  <style>
    /* div 요소의 자식요소 중 p 요소 */
    div > p { color: red; }
  </style>
</head>
<body>
  <h1>Heading</h1>
  <div>
    <p>paragraph 1</p>
    <p>paragraph 2</p>
    <span><p>paragraph 3</p></span>
  </div>
  <p>paragraph 4</p>
</body>
</html>
```


# 형제(동위) 셀렉터 

**인접 형제 셀렉터-**셀렉터A의 형제 요소 중 셀렉터A 바로 뒤에 위치하는 셀렉터B 요소를 선택한다. A와 B 사이에 다른 요소가 존재하면 선택되지 않는다.

```
셀렉터 A + 셀렉터 B
```

A 요소의 형제 요소 중에  p 요소 바로 뒤에 위치하는 ul 요소 선택.

```
  <p>The first paragraph.</p>
  <ul>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
  </ul>
```

**일반 형제 셀렉터-**셀렉터A의 형제 요소 중 셀렉터A 뒤에 위치하는 셀렉터B 요소를 모두 선택한다.

```
셀렉터A ~ 셀렉터B
```

A 요소의 형제 요소 중에  A요소 뒤에 위치하는 ul 요소를 모두 선택한다.

```
<p>The first paragraph.</p>
  <ul>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
  </ul>

  <h2>Another list</h2>
  <ul>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
  </ul>
```

# 가상 클래스 셀렉터(Pseudo-Class selector)

가상 클래스는 요소의 특정 상태에 따라 스타일을 정의할 때 사용된다. 특정 상태란 예를 들어 다음과 같다.

1. 마우스가 올라와 있을때
2. 링크를 방문했을 때와 아직 방문하지 않았을 때
3. 포커스가 들어와 있을 때

즉 원래 클래스가 존재하지 않지만 가상 클래스를 임의로 지정하여 선택한다. 가상 클래스는 마침표(.) 대신해서 콜론(:)을 사용한다.

**CSS**

```
selector:pseudo-class{
  property:value;
 }
```

**HTML** 

1. :hover 마우스가 올라와 있을 때 
2. :link  방문하지 않은 링크를 선택
3. :visited  방문한 링크를 선택
4. input:focus  포커스를 가질 때 즉 input 박스에 포커스를 둘 때
5. :active  셀렉터가 클릭된 상태일 때
6. :checked  셀렉터가 체크 상태일 때
7. :enabled  셀렉터가 사용 가능한 상태일 때
8. :disabled  셀렉터가 사용 불가능한 상태일때
9. :first-child  셀렉터에 해당하는 모든 요소 중 첫번째 자식인 요소를 선택한다.
10. :last-child  셀렉터에 해당하는 모든 요소 중 마지막 자식인 요소를 선택한다.
11. :nth-child(n)  셀렉터에 해당하는 모든 요소 중 앞에서 n번째 자식인 요소를 선택한다.
12. :nth-last-child(n) 셀렉터에 해당하는 모든 요소 중 뒤에서 n번째 자식인 요소를 선택한다.
13. :first-of-type	셀렉터에 해당하는 요소의 부모 요소의 자식 요소 중 첫번째 등장하는 요소를 선택한다.
14. :last-of-type	셀렉터에 해당하는 요소의 부모 요소의 자식 요소 중 마지막에 등장하는 요소를 선택한다.
15. :nth-of-type(n)	셀렉터에 해당하는 요소의 부모 요소의 자식 요소 중 앞에서 n번째에 등장하는 요소를 선택한다.
16. :nth-last-of-type(n)	셀렉터에 해당하는 요소의 부모 요소의 자식 요소 중 뒤에서 n번째에 등장하는 요소를 선택한다.
17. :not 셀렉터에 해당하지 않는 모든 요소를 선택한다.

```
<!DOCTYPE html>
<html>
<head>
  <style>
    /* a 요소가 hover 상태일 때 */
    a:hover { color: red; }
    /* input 요소가 focus 상태일 때 */
    input:focus { background-color: yellow; }
  </style>
</head>
<body>
  <a href="#">Hover me</a><br><br>
  <input type="text" placeholder="focus me">
</body>
</html>
``` 

# 가상 요소 셀렉터(Pseudo-Element Selector)

가상 요소는 요소의 특정 부분에 스타일을 적용하기 위하여 사용된다. 특정 부분이란 예를 들어 다음과 같다.

1. 요소 콘텐츠의 첫글자 또는 첫줄
2. 요소 콘텐츠의 앞 또는 뒤

가상 요소에는 두개의 콜론(::)을 사용한다. 

**CSS**

```
selector::pseudo-element{
  property:value;
}
```

**HTML**

1. ::first-letter	콘텐츠의 첫글자를 선택한다.
2. ::first-line	콘텐츠의 첫줄을 선택한다. 블록 요소에만 적용할 수 있다.
3. ::after	콘텐츠의 뒤에 위치하는 공간을 선택한다. 일반적으로 content 어트리뷰트와 함께 사용된다.
4. ::before	콘텐츠의 앞에 위치하는 공간을 선택한다. 일반적으로 content 어트리뷰트와 함께 사용된다.
5. ::selection	드래그한 콘텐츠를 선택한다. iOS Safari 등 일부 브라우저에서 동작 않는다.

```
<!DOCTYPE html>
<html>
<head>
  <style>
    /* p 요소 콘텐츠의 첫글자를 선택 */
    p::first-letter { font-size: 3em; }
    /* p 요소 콘텐츠의 첫줄을 선택 */
    p::first-line   { color: red; }

    /* h1 요소 콘텐츠의 앞 공간에 content 어트리뷰트 값을 삽입한다 */
    h1::before {
      content: " HTML!!! ";
      color: blue;
    }
    /* h1 요소 콘텐츠의 뒷 공간에 content 어트리뷰트 값을 삽입한다 */
    h1::after {
      content: " CSS3!!!";
      color: red;
    }

    /* 드래그한 콘텐츠를 선택한다 */
    ::selection {
      color: red;
      background: yellow;
    }
  </style>
</head>
<body>
  <h1>This is a heading</h1>
  <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Explicabo illum sunt distinctio sed, tempore, repellat rerum et ea laborum voluptatum! Quisquam error fugiat debitis maiores officiis, tenetur ullam amet in!</p>
</body>
</html>
```














 