-- 코드를 입력하세요
SELECT *  # 모두 선택
FROM PLACES  # PLACES 라는 table에서  
WHERE HOST_ID IN ( #IN 조건을 만족하는 HOST_ID들 출력
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID #그룹바이로 묶어줘야 HOST_ID 를 출력할 수 있음, 그룹으로 묶은 col만 불러올 수 있음
    HAVING count(HOST_ID)>=2 # having은 group화 된 group에 조건을 줌 / where가 헷갈리지 말것 
)
ORDER BY ID # 근데 이미 아이디 순이라 안 해줘도 되는?

"""
PLACES 테이블은 공간 임대 서비스에 등록된 공간의 정보를 담은 테이블입니다. PLACES 테이블의 구조는 다음과 같으며 ID, NAME, HOST_ID는 각각 공간의 아이디, 이름, 공간을 소유한 유저의 아이디를 나타냅니다. ID는 기본키입니다.

NAME	TYPE
-------------
ID	    INT
NAME	VARCHAR
HOST_ID	INT

이 서비스에서는 공간을 둘 이상 등록한 사람을 '헤비 유저'라고 부릅니다. 
헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회하는 SQL문을 작성해주세요.
"""