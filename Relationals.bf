[ Operation safe Comment
implements basic relationals
gt : >
lt : <
ge : >=
le : <=
eq : ==
ne : !=
] Comment end

OP: differ
[ OP SAFE COMMENT

Compacted form:
+[>+<<-[>>-<<[->>>+<<<]]>>>[-<<<+>>>]<[-<->]+<<<-[>>>-<<<[->>>>+<<<<]]>>>>[-<<<<+>>>>]<[-<[-]>]<]

] COMMENT END


[ OP SAFE COMMENT

With Comments:
+> 1       ::  new flag1 = 1
<[> while  ::  while (flag1){
+> 1       ::  new flag2 = 1
<<<-ldec_3 ::  y~=1
[>>-<<[->>>+<<<]]>>>[-<<<+>>>]
           ::  if(y!=0){flag2=0}
<[-<->]>   ::  if(flag2!=0){flag1=0}
           ::  //last 2 lines just act like if(y==0){flag1=0}
<          ::  del flag2

+> 1       ::  new flag2 = 1
<<<<-ldec_4::  x~=1
[>>>-<<<[->>>>+<<<<]]>>>>[-<<<<+>>>>]
           ::  if(x!=0){flag2=0}
<[-<[-]>]> ::  if(flag2!=0){flag1=0}
           ::  //last 2 lines just act like if(x==0){flag1=0}
<          ::  del flag2
<]> loop   ::  }
<          ::  del flag1

] COMMENT END



Code start
++++++> 3       ::  new x = 3
+++++> 5     ::  new y = 5

+[>+<<-[>>-<<[->>>+<<<]]>>>[-<<<+>>>]<[-<->]+<<<-[>>>-<<<[->>>>+<<<<]]>>>>[-<<<<+>>>>]<[-<[-]>]<]
  differ     :: x~=min(x&y);y~=min(x&y)

LT:
[<[[-]>+<]<[[-]>>[-]<<]>>[-<<+>>]<]

GT:
[<<[[-]>>+<<]>[[-]>[-]<]>[-<<+>>]<]

EQ:
[+<[[-]>[-]<]<[[-]>>[-]<<]>>[-<<+>>]<]

NE:
[<[[-]>+<]<[[-]>>+<<]>>[[-]<<+>>]<]

LE:
[+<[-]<[[-]>>-<<]>>[-<<+>>]<]

GE:
[+<[[-]>-<]<<[-]>>[-<<+>>]<]
