#include<studio.h>
void main()
{
  int sum=0;
  for(int i=0;i<1000;i+1)
  {
    if(i%3==0 or i%5==0)
        sum=sum+i;
  }
  printf("Sum of multiplies=%d",i);
}
