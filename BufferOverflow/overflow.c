#include <stdio.h>
void hacker()
{
    printf("No, I'm a hacker!\n");
}
void hacker2()
{
    printf("No, I'm a hacker!\n");
}
void nonSecure()
{
    char name[16];
    printf("What's your name?\n");
    gets(name);            
    printf("Hey %s, you're good guys, aren't you?\n", name);
}
int main()
{   
    nonSecure();
    //printf("Press Any Key to Exit\n");  
    //getchar();   
    return 0;
}