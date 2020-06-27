# -*- coding: utf-8 -*-

import numpy as np
import seaborn as sns

"""비추정"""
###데이터 입력
x = np.array([  ])
y = np.array([  ])

###산점도 그리기
sns.regplot(x=x, y=y)

###x,y 평균
bx = sum(x)/10
by = sum(y)/10
print(bx, by)

###비추정 e=Y-X
be = by-bx
print(be)

###비추정 잔차
ei = x-y

###비추정 Se^2 값
se = sum((ei-be)**2)/9
print(se)


"""회귀추정"""
###데이터 입력
x = np.array([  ])
y = np.array([  ])

###산점도 그리기
sns.regplot(x=x, y=y)

###x,y 평균
bx = sum(x)/10
by = sum(y)/10
print(bx, by)

###회귀추정 계수
xx = x-bx
yy = y-by
b = sum(xx*yy)/sum(xx**2)
a = by-b*bx
print(a, b)

##회귀추정 Se^2 값
se = sum((yy-b*xx)**2)/9
print(se)


