-- 코드를 작성해주세요

SELECT COUNT(INFO.FISH_TYPE) AS FISH_COUNT
FROM FISH_INFO AS INFO
INNER JOIN FISH_NAME_INFO AS NAME
ON INFO.FISH_TYPE = NAME.FISH_TYPE
WHERE NAME.FISH_NAME IN ('BASS', 'SNAPPER');