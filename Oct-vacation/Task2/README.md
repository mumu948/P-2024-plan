# Task 2
现学了个冒泡循环（小白哭泣）

#include<stdio.h>
int main()
{
	int a,b,c,d,e,f,g,h,i,j;
	scanf("%d,%d,%d,%d,%d,%d,%d,%d,%d,%d",&a,&b,&c,&d,&e,&f,&g,&h,&i,&j);
	int num[10]={a,b,c,d,e,f,g,h,i,j};
	int m=0,n=0;
	for (m=0;m<9;m++)
	{
		for(n=0;n<10-1-m;n++)
		{
			if(num[n]>num[n+1])
			{
				int x=num[n];
				num[n]=num[n+1];
				num[n+1]=x;
			}
		}
	}
	for(m=0;m<10;m++)
	{
		printf("%d\t",num[m]);
	}
	return 0;
}

@Author:  朱雯杰
@Email:3391030015@qq.com
