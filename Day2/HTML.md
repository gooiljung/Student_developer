# HTML
***HTML*** 은 웹페이지를 기술하기 위한 마크업 언어로써 웹페이지의 내용과 구조를 담당하는 언어로써 HTML 태그를 통해 정보를 구조화하는 것이다.

**HTML구성**

1. < !DOCTYPE html >으로 시작하여 문서 형식을 html5로 지정한다.
2. 실제적인 HTML document는 2행부터 시작되는데 < html > 과 < /html > 사이에 기술한다.
3. < head > 와 < /head > 사이에는 document title, 외부파일의 참조, metadata의 설정 등이 위치하고 이 정보들은 브라우저에 표시되지 않는다.
4. 웹 브라우저에 출력되는 모든 요소는 < body > 와 < /body > 사이에 위치한다.
5. HTML document 는 .html 확장자를 갖는 순수한 텍스트 파일이고 메모장으로도 편집할 수 있으나 editor를 사용한다.

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>안녕하세요! HTML5</p>
  </body>
</html>
```

# HTML5 의 기본 문법
**-요소-**

1. HTML 요소는 시작태그 < p >  와 종료태그 < /p > 사이에 위치한 content로 구성. ex) < p >Hello< /p >
2. 요소는 중접될 수 있다. 즉 요소는 다른 요소를 포함할 수 있다. 이때 부자관계가 성립. h1,p요소 이게 중첩 관계(부자 관계)
3. ***빈요소는*** content를 가질 수 없는 요소로써 Attribute만을 가질 수 있다.ex)br,hr,img,input,link,meta


**Attribute**

속성이란 요소의 성질 특징을 정의하는 명세이다. 요소는 어트리뷰트를 가질 수 있고 어트리뷰트는 요소에 추가적 정보(이미지 파일의 경로,크기)를 제공한다. 어트리뷰트는 시작태그에 위치해야 하며 이름과 값의 쌍을 이룬다.

```
< p > < img src="html.jpg" width="104" height="142" > < /p >
```
**Global Attribute**- 모든 HTML 요소가 공통으로 사용할 수 있는 어트리뷰트.


Attribute | 설명
------|------
id|유일한 식별자(id)를 요소에 지정한다. 중복지정 불가
class| 스타일시트에 정의된 class를 요소에 지정한다. 중복지정이 가능하다.
hidden| css의 hidden과는 다르게 의미상으로도 브라우저에 노출되지 않게 된다.
lang| 지정된 요소의 언어를 지정한다. 검색엔진의 크롤링시 웹페이지의 언어를 인식할 수 있게 한다.
style| 요소에 인라인 스타일을 지정한다.
tabindex| 사용자가 키보드로 페이지를 네비게이션시 이동 순서를 지정한다.
title|요소에 관한 제목을 지정한다.

***주석*** < !--주석은 화면에표시되지 않는다-- >

# 시멘틱 웹

**검색엔진** 은 로봇이라는 프로그램을 이용해 매일 전세계의 웹사이트 정보를 수집한다. 이를 **크롤링**이라 한다. 그리고 검색 사이트 이용자가 검색할 만한 키워드를 미리 예상하여 검색 키워드에 대응하는 인덱스를 만들어 둔다. 이것을 **인덱싱** 이라 하고 검색엔진의 인덱서가 이를 수행한다. 인덱스를 생성할 때 사용되는 정보도 로봇이 수집한 정보인데 결국 HTML코드 이다. 즉 검색 엔진은 HTML 코드 만으로 그 의미를 인지하여야 하는데 이때 **시맨틱 요소(Semantic element)**를 해석하게 된다. 검색엔진은 대체로 h1 요소 내의 콘텐츠를 웹문서의 중요한 제목으로 인식하고 인덱스에 포함시킬 확률이 높다. 또한 사람도 h1 요소 내의 콘텐츠가 제목임을 인식할 수 있다. 시맨틱 요소로 구성되어 있는 웹페이지는 검색엔진에 보다 의미론적으로 문서 정보를 전달할 수 있고 검색엔진 또한 시맨틱 요소를 이용하여 보다 효과적인 크롤링과 인덱싱이 가능하게 되었다. 즉, **시맨틱 태그란** 브라우저, 검색엔진, 개발자 모두에게 콘텐츠의 의미를 명확히 설명하는 역할을 한다. 시맨틱 태그에 의해 컴퓨터가 HTML 요소의 의미를 보다 명확히 해석하고 그 데이터를 활용할 수 있는 시맨틱 웹이 실현될 수 있다.

**시맨틱 웹이란** 웹에 존재하는 수많은 웹페이지들에 메타데이터(Metadata)를 부여하여, 기존의 잡다한 데이터 집합이었던 웹페이지를 ‘의미’와 ‘관련성’을 가지는 거대한 데이터베이스로 구축하고자 하는 발상이다.


```
<font size="6"><b>Hello</b></font>
<h1>Hello</h1>
```
의미는 폰트 사이즈 6의 bold체를 사용하고 < h1 > 은 첫째줄같은 의미의 태그다 라는 의미,header(제목) 중 가장 상위 레벨이라는 의미를 내포

**HTML 요소**

1. non-semantic 요소: div,span 등이 있으며 이들 태그는 content에 대하여 어떤 설명도 하지 않는다.
2. semantic 요소: form,table,img 등이 있으며 이들 태그는 content의 의미를 명확히 설명한다.

**시맨틱 태그**

tag	|Description
----|------
header	|헤더를 의미한다
nav	|내비게이션을 의미한다
aside	|사이드에 위치하는 공간을 의미한다
section	|본문의 여러 내용(article)을 포함하는 공간을 의미한다
article	|분문의 주내용이 들어가는 공간을 의미한다
footer|	푸터를 의미한다


# Form

***form*** 태그는 사용자가 입력한 데이터를 수집하기 위해 사용되며 input, textarea, button, select, checkbox, radio button, submit button 등의 입력 양식 태그를 포함할 수 있다.

```
<form>
...
form elements (input, checkbox, radio button, submit button...)
...
</form>
```

attribute	|Value|	Description
---|----|----
action	|URL|	입력 데이터(form data)가 전송될 URL 지정
method	|get / post|	입력 데이터(form data) 전달 방식 지정

get 과 post는 HTTP 프로토콜을 이용해서 사용자 입력 데이터를 서번에 전달하는 방식을 나타내며 HTTP request method라 한다.

# GET

1. GET 방식은 전송 URL에 입력 데이터를 쿼리스트링으로 보내는 방식이다.
2. ex)http://jsonplaceholder.typicode.com/posts?userId=1&id=1
3. 전송 URL 바로 뒤에 ‘?’를 통해 데이터의 시작을 알려주고, key-value형태의 데이터를 추가한다. 1개 이상의 전송 데이터는 ‘&’로 구분한다.
4. URL에 전송 데이터가 모두 노출되기 때문에 보안에 문제가 있으며 전송할 수 있는 데이터의 한계가 있다. (최대 255자).
5. REST API에서 GET 메소드는 모든 또는 특정 리소스의 조회를 요청한다

```
<!DOCTYPE html>
<html>
  <body>
    <form action="http://jsonplaceholder.typicode.com/users" method="get">
      ID: <input type="text" name="id" value="1"><br>
      username: <input type="text" name="username" value="Bret"><br>
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
```


# POST

1. POST 방식은 Request Body에 담아 보내는 방식이다.
2. ex) http://jsonplaceholder.typicode.com/posts
3. URL에 전송 데이터가 모두 노출되지 않지만 GET에 비해 속도가 느리다.
4. REST API에서 POST 메소드는 특정 리소스의 생성을 요청한다.


# input 
너무 많아서 홈페이지 참조하기 http://poiemaweb.com/html5-tag-forms

# Select
복수 개의 리스트에서 복수개의 아이템을 선택할 때 사용한다. 서버에 전송되는 데이터는 select 요소의 name 어트리뷰트를 키로, option 요소의 value 어트리뷰트를 값으로하여 key=value의 형태로 전송된다.

tag	|Description
---|----
select	|select form 생성
option	|option 생성
optgroup|	option을 그룹화한다

```
<!DOCTYPE html>
<html>
  <body>
    <select name="cars1">
      <option value="volvo" selected>Volvo</option>
      <option value="saab" disabled>Saab</option>
      <option value="fiat">Fiat</option>
      <option value="audi">Audi</option>
   </select>
  </body>
</html>
```

# textarea
textarea 태그는 여러 줄의 글자를 입력할 때 사용한다.

```
<!DOCTYPE html>
<html>
  <body>
    <textarea name="message" rows="10" cols="30">Write something here</textarea>
  </body>
</html>
```

# button
button 태그는 클릭할 수 있는 버튼을 생성한다. <input type="button">과 유사하지만 input 태그는 빈 태그인 반면 button 태그는 그렇지 않다. 따라서 button 요소에는 텍스트나 이미지 같은 콘텐츠를 사용할 수 있다.

type 어트리뷰트는 반드시 지정하는 것이 바람직하며 어트리뷰트값으로 button, reset, submit를 지정할 수 있다.

```
<!DOCTYPE html>
<html>
  <body>
    <button type="button" onclick="alert('Hello World!')">Click Me!</button>

    <input type="button" value="Click Me!" onclick="alert('Hello world!')">
  </body>
</html>
```

# filedset/legend
fieldset 태그는 관련된 입력 양식들을 그룹화할 때 사용한다. legend 태그는 filedset 태그 내에서 사용되야 하며 그룹화된 filedset의 제목을 정의한다.

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
  </head>
  <body>
      <fieldset>
        <legend>Login</legend>
        Username <input type="text" name="username">
        Password <input type="text" name="password">
      </fieldset>
  </body>
</html>
```



















